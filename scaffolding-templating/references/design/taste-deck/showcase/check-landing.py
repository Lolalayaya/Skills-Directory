# -*- coding: utf-8 -*-
"""
Landing page 静态 QA 检查器（check-landing.py）
==========================================
对 landing page / portfolio HTML 做静态可自动化的 Pre-Flight 检查。
不依赖浏览器，纯 regex + stdlib HTMLParser。

用法：
  python showcase/check-landing.py path/to/landing.html
  python showcase/check-landing.py path/to/landing.html --json
  python showcase/check-landing.py path/to/landing.html --strict
  python showcase/check-landing.py path/to/landing.html --skip em-dash,h-screen
  python showcase/check-landing.py path/to/landing.html --verbose

退出码：0 = 全部通过，1 = 存在 FAIL
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

# === Constants & Word Lists ===

EM_DASHES = ["\u2014", "\u2013"]

GENERIC_NAMES = [
    "John Doe", "Jane Doe", "Sarah Chan", "Mike Johnson",
    "John Smith", "Jane Smith", "Alex Chen", "Sam Lee",
    "David Kim", "Lisa Wang", "Tom Brown", "Amy Davis",
]

GENERIC_BRANDS = [
    "Acme", "Nexus", "SmartFlow", "TechFlow", "InnovateTech",
    "CloudSync", "DataFlow", "NextGen", "FutureTech", "SmartSolutions",
    "TechSolutions", "ProSolutions", "GlobalTech", "ApexSolutions",
]

FILLER_VERBS = [
    "Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionize",
    "Transformative", "Empower", "Supercharge", "Game-changing",
    "Cutting-edge", "World-class", "Best-in-class", "Industry-leading",
]

SCROLL_CUE_RE = re.compile(
    r"scroll\s*(?:to\s*(?:explore|learn|discover|see)|down|for more)|"
    r"\u2193\s*scroll|mouse.?wheel|scroll cue",
    re.IGNORECASE,
)

VERSION_LABEL_RE = re.compile(
    r"(?:^|[\s>\"'(])"
    r"(?:[Vv]\d+\.\d+(?:\.\d+)?(?:-\w+)?|"
    r"BETA\b|ALPHA\b|EARLY\s+ACCESS|INVITE[- ]ONLY|"
    r"Build\s+\d{3,}|v\d+\.\d+\.\d+|"
    r"Version\s+\d+\.\d+)"
    r"(?=$|[\s<\"')\.,;:!?])",
)

SECTION_NUMBER_RE = re.compile(
    r"(?:^|>)\s*0\d\s*(?:/|\u00b7|\|)\s*\w+|"
    r"0\d\s*\u00b7\s*\w+|"
    r"(?:0\d)\s*/\s*(?:INDEX|CAPABILITIES|FEATURES|ABOUT)",
    re.IGNORECASE,
)

BANNED_SERIFS = ["Fraunces", "Instrument_Serif", "Instrument Serif"]

ALLOWED_ICON_LIBS = [
    "@phosphor-icons", "phosphor-icons", "hugeicons",
    "@radix-ui/react-icons", "@tabler/icons", "tabler-icons",
]

DISCOURAGED_ICON_LIBS = ["lucide"]

AI_PURPLE_VALUES = {"#6366f1", "#8b5cf6", "#7c3aed", "#6d28d9", "#5b21b6"}
PURE_BLACK_RE = re.compile(r"#000000\b")
PURE_WHITE_RE = re.compile(r"#ffffff\b")

PREMIUM_DEFAULT_PALETTE = [
    "#d4c5a9", "#c4a882", "#b8860b", "#8b4513", "#654321",
    "#800020", "#d2b48c", "#deb887", "#bc8f8f", "#cd853f",
]

FAKE_PRECISE_RE = re.compile(
    r"\b(?:99\.99%|99\.9%|100%|1000%|"
    r"\d+\.\d+x\s*(?:faster|better|more)|"
    r"\d+(?:,\d{3})+\s*(?:users|customers|downloads))\b",
    re.IGNORECASE,
)

CTA_INTENT_GROUPS = {
    "contact": ["get in touch", "contact us", "let's talk", "lets talk",
                "reach out", "start a project", "get in contact", "contact"],
    "signup": ["sign up", "get started", "start free", "try free",
               "request demo", "book a demo", "create account",
               "start your free", "join now", "register"],
    "download": ["download now", "get the app", "download", "install"],
    "learn-more": ["learn more", "read more", "discover", "explore more", "see more"],
    "subscribe": ["subscribe", "join newsletter", "stay updated", "sign up for updates"],
    "purchase": ["buy now", "purchase", "add to cart", "get it now", "order now"],
}

HSCREEN_RE = re.compile(r'class="[^"]*\bh-screen\b[^"]*"')
SCROLL_LISTENER_RE = re.compile(r"window\.addEventListener\s*\(\s*[\"']scroll[\"']")
GRADIENT_TEXT_RE = re.compile(
    r"(?:bg-clip-text|background-clip:\s*text).*?text-transparent|"
    r"text-transparent.*?(?:bg-clip-text|background-clip:\s*text)"
)
CUSTOM_CURSOR_RE = re.compile(r"cursor\s*:\s*(?:none|url\s*\()")
WILL_CHANGE_RE = re.compile(r"will-change\s*:", re.IGNORECASE)
ANIMATE_DIMENSION_RE = re.compile(r"transition\s*:[^;{}]*(?:width|height|top|left)\b")
EYEBROW_RE = re.compile(r"uppercase\s+tracking[-\w]*|tracking[-\w]*\s+uppercase")
GRID_COLS_3_RE = re.compile(r"grid-cols-3")
MARQUEE_ANIMATION_RE = re.compile(
    r"@keyframes\s+\w*(?:marquee|scroll|slide)\w*.*?(?:translateX|translate)\s*\("
    r"|animation\s*:[^;]*(?:marquee|scroll-x|infinite.*translate)",
    re.DOTALL | re.IGNORECASE,
)

# === LandingParser ===

class LandingParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.raw_html = ""
        self.visible_text_parts: list[str] = []
        self.css_text = ""
        self.script_text = ""
        self.all_class_attrs: list[str] = []
        self.sections: list[dict] = []
        self.images: list[dict] = []
        self.background_images: list[str] = []
        self.tables: list[dict] = []
        self.lists: list[dict] = []
        self.nav_info: dict | None = None
        self.hero_info: dict | None = None
        self.cta_texts: list[str] = []
        self.inline_svg_count = 0
        self.dark_mode_signals = 0
        self.reduced_motion_signals = 0
        self.grid_cols_3_sections: list[dict] = []
        self._in_style = False
        self._in_script = False
        self._in_svg = False
        self._current_tag = ""
        self._section_stack: list[dict] = []
        self._list_stack: list[dict] = []
        self._table_row_count = 0
        self._in_table = False
        self._hero_found = False
        self._depth = 0

    def set_html(self, html: str):
        self.raw_html = html

    def handle_starttag(self, tag, attrs):
        attr_map = {k: (v or "") for k, v in attrs}
        classes = attr_map.get("class", "")
        self._depth += 1
        self._current_tag = tag

        if tag == "style": self._in_style = True
        elif tag == "script": self._in_script = True
        elif tag == "svg": self._in_svg = True; self.inline_svg_count += 1

        if classes:
            self.all_class_attrs.append(classes)
            if "dark:" in classes: self.dark_mode_signals += 1
            if "motion-reduce" in classes or "motion-safe" in classes: self.reduced_motion_signals += 1

        if "grid-cols-3" in classes:
            self.grid_cols_3_sections.append({"tag": tag, "classes": classes, "children": 0, "depth": self._depth})

        if tag in ("section", "header", "main", "footer", "nav"):
            section = {
                "tag": tag, "classes": classes, "depth": self._depth,
                "text_parts": [], "children": 0,
                "is_hero": not self._hero_found and ("hero" in classes.lower() or (tag == "header" and self._depth <= 3)),
                "is_nav": "nav" in classes.lower() or tag == "nav",
            }
            if section["is_hero"]: self._hero_found = True; self.hero_info = section
            if section["is_nav"] or tag == "nav": self.nav_info = section
            self.sections.append(section)
            self._section_stack.append(section)

        if tag == "img":
            self.images.append({"src": attr_map.get("src", ""), "alt": attr_map.get("alt", ""), "classes": classes})

        style_attr = attr_map.get("style", "")
        if "background-image" in style_attr or "bg-[url" in classes:
            self.background_images.append(style_attr or classes)

        if tag == "table":
            self._in_table = True; self._table_row_count = 0
        elif tag == "tr" and self._in_table:
            self._table_row_count += 1

        if tag in ("ul", "ol"):
            self._list_stack.append({"tag": tag, "classes": classes, "items": 0})
        elif tag == "li" and self._list_stack:
            self._list_stack[-1]["items"] += 1

        if tag in ("button", "a"):
            text_hint = attr_map.get("aria-label", "") or attr_map.get("title", "")
            if text_hint: self.cta_texts.append(text_hint)

    def handle_endtag(self, tag):
        self._depth = max(0, self._depth - 1)
        if tag == "style": self._in_style = False
        elif tag == "script": self._in_script = False
        elif tag == "svg": self._in_svg = False
        elif tag == "table":
            self._in_table = False; self.tables.append({"rows": self._table_row_count})
        if tag in ("ul", "ol") and self._list_stack:
            self.lists.append(self._list_stack.pop())
        if tag in ("section", "header", "main", "footer", "nav") and self._section_stack:
            self._section_stack.pop()

    def handle_data(self, data):
        stripped = data.strip()
        if not stripped: return
        if self._in_style: self.css_text += data
        elif self._in_script: self.script_text += data
        elif not self._in_svg:
            self.visible_text_parts.append(stripped)
            if self._section_stack:
                self._section_stack[-1]["text_parts"].append(stripped)
                self._section_stack[-1]["children"] += 1
            if self._current_tag in ("button", "a"):
                self.cta_texts.append(stripped)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def get_visible_text(self) -> str: return " ".join(self.visible_text_parts)
    def get_all_classes(self) -> str: return " ".join(self.all_class_attrs)

# === Check Functions ===

def check_em_dash(p): 
    issues=[]; text=p.get_visible_text()
    for ch in EM_DASHES:
        if ch in text: issues.append(f"Em-dash '{ch}' found ({text.count(ch)} occurrence(s))")
    return issues

def check_h_screen(p):
    if HSCREEN_RE.search(p.raw_html): return ["h-screen found - use min-h-[100dvh] instead"]
    return []

def check_scroll_listener(p):
    if SCROLL_LISTENER_RE.search(p.raw_html): return ["window.addEventListener('scroll') found"]
    return []

def check_inter_default(p):
    issues=[]
    for decl in re.findall(r'font-family\s*:\s*([^;"}]+)', p.raw_html):
        if re.search(r'\bInter\b', decl):
            first=decl.split(",")[0].strip().strip("'\"").lower()
            if first in ("inter","inter, sans-serif"):
                issues.append(f"Inter as primary font: '{decl.strip()}'")
    return issues

def check_pure_black(p):
    m=PURE_BLACK_RE.findall(p.raw_html)
    return [f"Pure black #000000 found ({len(m)}x) - use off-black"] if m else []

def check_pure_white(p):
    m=PURE_WHITE_RE.findall(p.raw_html)
    return [f"Pure white #ffffff found ({len(m)}x) - use off-white"] if m else []

def check_generic_names(p):
    text=p.get_visible_text()
    return [f"Generic name '{n}' found" for n in GENERIC_NAMES if n in text]

def check_generic_brands(p):
    text=p.get_visible_text()
    return [f"Generic brand '{b}' found" for b in GENERIC_BRANDS if b in text]

def check_filler_verbs(p):
    text=p.get_visible_text()
    return [f"Filler verb '{v}' found" for v in FILLER_VERBS if re.search(rf'\b{v}\b',text,re.I)]

def check_scroll_cues(p):
    text=p.get_visible_text()
    return ["Scroll cue text found"] if SCROLL_CUE_RE.search(text) else []

def check_version_labels(p):
    m=VERSION_LABEL_RE.findall(p.get_visible_text())
    return [f"Version label(s): {m}"] if m else []

def check_section_numbering(p):
    m=SECTION_NUMBER_RE.findall(p.get_visible_text())
    return [f"Section numbering: {m}"] if m else []

def check_serif_discipline(p):
    return [f"Banned serif '{s}' found" for s in BANNED_SERIFS if s in p.raw_html]

def check_ai_purple(p):
    return [f"AI-purple {c} found" for c in AI_PURPLE_VALUES if c.lower() in p.raw_html.lower()]

def check_gradient_text(p):
    if GRADIENT_TEXT_RE.search(p.get_all_classes()) or re.search(r"background-clip:.s*text", p.css_text or ""): return ["Gradient text detected"]
    return []

def check_custom_cursor(p):
    if CUSTOM_CURSOR_RE.search(p.css_text or p.raw_html): return ["Custom cursor CSS found"]
    return []

def check_fake_precise_numbers(p):
    m=FAKE_PRECISE_RE.findall(p.get_visible_text())
    return [f"Suspiciously precise numbers: {m}"] if m else []

def check_eyebrow_count(p):
    ec=len(EYEBROW_RE.findall(p.get_all_classes())); sc=max(len(p.sections),1)
    mx=math.ceil(sc/3)
    if ec>mx: return [f"Eyebrow count {ec} > max {mx} ({sc} sections)"]
    return []

def check_marquee_count(p):
    css=p.css_text or ""; classes=p.get_all_classes()
    total=len(MARQUEE_ANIMATION_RE.findall(css))+css.lower().count('marquee')+len(re.findall(r'\bmarquee\b|\bscroll-x\b',classes,re.I))
    if total>1: return [f"Multiple marquee patterns ({total}) - max 1 per page"]
    return []

def check_duplicate_cta(p):
    issues=[]; seen={}
    for cta in [c.lower().strip() for c in p.cta_texts if c.strip()]:
        for intent,labels in CTA_INTENT_GROUPS.items():
            for label in labels:
                if label in cta or cta==label:
                    seen.setdefault(intent,set()).add(cta)
    for intent,labels in seen.items():
        if len(labels)>1: issues.append(f"Duplicate CTA intent '{intent}': {sorted(labels)}")
    return issues

def check_real_images(p):
    total=len(p.images)+len(p.background_images)
    if total<2: return [f"Only {total} image(s) - landing needs >=2-3"]
    return []

def check_long_lists(p):
    issues=[]
    for lst in p.lists:
        if lst["items"]>5 and "divide-y" in lst.get("classes",""):
            issues.append(f"<{lst['tag']}> {lst['items']} items + divide-y - use different component")
        elif lst["items"]>10:
            issues.append(f"<{lst['tag']}> {lst['items']} items - too long")
    return issues

def check_progress_bars(p):
    pat=re.compile(r'class="[^"]*rounded-full[^"]*"[^>]*>.*?class="[^"]*(?:bg-\w+-\d+|w-\[\d+%\])[^"]*"',re.DOTALL)
    has_tw = pat.search(p.raw_html)
    has_css = re.search(r"border-radius\s*:\s*(?:9999px|50%)", p.css_text or "") and re.search(r"width\s*:\s*\d+[%]", p.css_text or "")
    if has_tw or has_css: return ["Progress bar with filled track detected"]
    return []

def check_locale_strips(p):
    pat=re.compile(r"\d{1,2}:\d{2}\s*(?:[AP]M)?\s*[\u00b7|]\s*\d+\u00b0[CF]")
    if pat.search(p.get_visible_text()): return ["Locale/time/weather strip detected"]
    return []

def check_icon_library(p):
    issues=[]; html=p.raw_html.lower()
    has_allowed=any(l in html for l in ALLOWED_ICON_LIBS)
    if "lucide" in html and not has_allowed:
        issues.append("Lucide icons (discouraged) - prefer Phosphor/HugeIcons/Tabler")
    if p.inline_svg_count>5:
        issues.append(f"{p.inline_svg_count} inline SVGs - use icon library")
    return issues

def check_dark_mode_tokens(p):
    html=p.raw_html; css=p.css_text or ""
    if not any(["dark:" in html, "prefers-color-scheme" in css, "data-theme" in html]):
        return ["No dark mode signals - design for both modes"]
    return []

def check_reduced_motion(p):
    html=p.raw_html; css=p.css_text or ""
    has_motion=any(["animate-" in html,"keyframes" in css,"gsap" in html.lower()])
    has_reduced=any(["prefers-reduced-motion" in css,"motion-reduce" in html,"motion-safe" in html])
    if has_motion and not has_reduced: return ["Motion but no prefers-reduced-motion"]
    return []

def check_design_system_mix(p):
    html=p.raw_html.lower(); ds=[]
    if "@material/web" in html or "material-components" in html or "@mui/material" in html: ds.append("Material")
    if "shadcn" in html: ds.append("shadcn/ui")
    if "@carbon/react" in html: ds.append("Carbon")
    if "@fluentui" in html: ds.append("Fluent")
    if len(ds)>1: return [f"Multiple design systems: {ds} - use ONE"]
    return []

def check_premium_palette(p):
    hexes=set(h.lower() for h in re.findall(r"#[0-9a-fA-F]{6}\b",p.raw_html))
    matched=hexes&{c.lower() for c in PREMIUM_DEFAULT_PALETTE}
    if len(matched)>=3: return [f"AI-default premium palette: {sorted(matched)}"]
    return []

def check_will_change(p):
    c=len(WILL_CHANGE_RE.findall(p.css_text or ""))
    if c>5: return [f"will-change used {c}x - use sparingly"]
    return []

def check_animate_dimension(p):
    if ANIMATE_DIMENSION_RE.search(p.css_text or ""): return ["Transition on width/height/top/left - animate transform/opacity only"]
    return []

def check_lucide_import(p):
    if "lucide" in p.raw_html.lower(): return ["Lucide icons found - only on explicit request"]
    return []

def check_broken_unsplash(p):
    m=re.findall(r'unsplash\.com/photo-',p.raw_html)
    if m: return [f"Unsplash direct links ({len(m)}) - use picsum.photos/seed/"]
    return []

def check_emoji_policy(p):
    emoji_re=re.compile(r"[\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F300-\U0001F5FF\U00002700-\U000027BF\U0001F900-\U0001F9FF]")
    m=emoji_re.findall(p.get_visible_text())
    if len(m)>3: return [f"{len(m)} emojis - use icon library glyphs"]
    return []

def check_z_index_spam(p):
    zc=Counter(re.findall(r'\bz-\d+\b',p.get_all_classes()))
    high={z:c for z,c in zc.items() if int(z.split("-")[1])>=40 and c>3}
    if high: return [f"High z-index overuse: {high}"]
    return []

def check_animate_scroll_y(p):
    code=p.script_text or p.raw_html
    issues=[]
    if re.search(r'window\.scrollY',code): issues.append("window.scrollY used - use useScroll()")
    if re.search(r'requestAnimationFrame.*(?:setState|useState)',code,re.DOTALL): issues.append("rAF touching state - use motion values")
    return issues

def check_hero_stack(p):
    if p.hero_info and p.hero_info.get("children",0)>6:
        return [f"Hero has {p.hero_info['children']} children - max 4 text elements"]
    return []

def check_hero_padding(p):
    if p.hero_info:
        cls=p.hero_info.get("classes","")
        m=re.search(r'\bpt-(\d+)\b',cls)
        if m and int(m.group(1))>24: return [f"Hero padding pt-{m.group(1)} exceeds max pt-24"]
        ma=re.search(r'\bpt-\[(\d+)(px|rem)\]',cls)
        if ma:
            v,unit=int(ma.group(1)),ma.group(2)
            mx=96 if unit=="px" else 6
            if v>mx: return [f"Hero padding pt-[{v}{unit}] exceeds max ~{mx}{unit}"]
    return []

def check_nav_height(p):
    if p.nav_info:
        m=re.search(r'\bh-(\d+)\b',p.nav_info.get("classes",""))
        if m and int(m.group(1))>20: return [f"Nav height h-{m.group(1)} exceeds max h-20 (80px)"]
    return []

def check_table_density(p):
    issues=[]
    for tbl in p.tables:
        if tbl["rows"]>20: issues.append(f"Table {tbl['rows']} rows - show top 3-5 + link")
        elif tbl["rows"]>10: issues.append(f"Table {tbl['rows']} rows - consider grouping")
    return issues

def check_bento_diversity(p):
    for s in p.sections:
        cls=s.get("classes","")
        if "grid" in cls and "gap-" in cls and s.get("children",0)>2:
            has_bg=bool(re.search(r'bg-\w+-\d{2,3}|gradient|from-|to-',cls))
            has_img=len(p.images)>0
            if not has_bg and not has_img:
                return ["Grid section with no visual variation - add images/gradients"]
    return []

def check_three_equal_cards(p):
    if p.grid_cols_3_sections:
        return ["grid-cols-3 detected - verify not 'three equal feature cards'"]
    return []

# === Check Registry ===

CHECKS = [
    ("em-dash-ban", check_em_dash, "S9.G", 1),
    ("h-screen-ban", check_h_screen, "S3.E", 1),
    ("scroll-listener", check_scroll_listener, "S5.D", 1),
    ("inter-default", check_inter_default, "S9.B", 1),
    ("pure-black", check_pure_black, "S9.A", 1),
    ("pure-white", check_pure_white, "S9.A", 1),
    ("generic-names", check_generic_names, "S9.D", 1),
    ("generic-brands", check_generic_brands, "S9.D", 1),
    ("filler-verbs", check_filler_verbs, "S9.D", 1),
    ("scroll-cues", check_scroll_cues, "S9.F", 1),
    ("version-labels", check_version_labels, "S9.F", 1),
    ("section-numbering", check_section_numbering, "S9.F", 1),
    ("serif-discipline", check_serif_discipline, "S4.1", 1),
    ("ai-purple", check_ai_purple, "S9.A", 1),
    ("gradient-text", check_gradient_text, "S9.A", 1),
    ("custom-cursor", check_custom_cursor, "S9.A", 1),
    ("fake-precise-numbers", check_fake_precise_numbers, "S4.9", 1),
    ("eyebrow-count", check_eyebrow_count, "S4.7", 2),
    ("marquee-count", check_marquee_count, "S5", 2),
    ("duplicate-cta", check_duplicate_cta, "S4.5", 2),
    ("real-images", check_real_images, "S4.8", 2),
    ("long-lists", check_long_lists, "S4.9", 2),
    ("progress-bars", check_progress_bars, "S9.F", 2),
    ("locale-strips", check_locale_strips, "S9.F", 2),
    ("icon-library", check_icon_library, "S3.C", 2),
    ("dark-mode-tokens", check_dark_mode_tokens, "S6.C", 2),
    ("reduced-motion", check_reduced_motion, "S6.B", 2),
    ("design-system-mix", check_design_system_mix, "S2.A", 2),
    ("premium-palette", check_premium_palette, "S4.2", 2),
    ("will-change", check_will_change, "S6.A", 2),
    ("animate-dimension", check_animate_dimension, "S6.A", 2),
    ("lucide-import", check_lucide_import, "S3.C", 2),
    ("broken-unsplash", check_broken_unsplash, "S9.E", 2),
    ("emoji-policy", check_emoji_policy, "S3.D", 2),
    ("z-index-spam", check_z_index_spam, "S6.F", 2),
    ("animate-scroll-y", check_animate_scroll_y, "S5.D", 2),
    ("hero-stack", check_hero_stack, "S4.7", 3),
    ("hero-padding", check_hero_padding, "S4.7", 3),
    ("nav-height", check_nav_height, "S4.7", 3),
    ("table-density", check_table_density, "S4.9", 3),
    ("bento-diversity", check_bento_diversity, "S4.7", 3),
    ("three-equal-cards", check_three_equal_cards, "S9.C", 3),
]

# === Main ===

def resolve_html_path(arg):
    p=Path(arg)
    if p.is_file() and p.suffix==".html": return p.resolve()
    if p.is_dir() and (p/"index.html").exists(): return (p/"index.html").resolve()
    raise SystemExit(f"[!!] Cannot find HTML: {arg}")

def run_checks(html_path, skip, verbose):
    html=html_path.read_text(encoding="utf-8",errors="ignore")
    p=LandingParser(); p.set_html(html)
    try: p.feed(html); p.close()
    except: pass
    results=[]
    for name,fn,ref,tier in CHECKS:
        if name in skip:
            results.append({"check":name,"tier":tier,"ref":ref,"status":"skip","issues":[]})
            continue
        try:
            issues=fn(p); status="fail" if issues else "pass"
        except Exception as e:
            issues=[f"check error: {e}"]; status="error"
        results.append({"check":name,"tier":tier,"ref":ref,"status":status,"issues":issues})
    return results

def print_human(results, verbose):
    fails=[r for r in results if r["status"]=="fail"]
    errors=[r for r in results if r["status"]=="error"]
    passes=[r for r in results if r["status"]=="pass"]
    skips=[r for r in results if r["status"]=="skip"]
    if verbose:
        for r in results:
            icon={"pass":"[ok]","fail":"[!!]","error":"[ERR]","skip":"[skip]"}[r["status"]]
            print(f"{icon} {r['check']:<24} (tier {r['tier']}, {r['ref']})")
            for issue in r["issues"]: print(f"     -> {issue}")
    else:
        for r in fails+errors:
            print(f"[!!] {r['check']:<24} (tier {r['tier']}, {r['ref']})")
            for issue in r["issues"]: print(f"     -> {issue}")
    total=len(results)
    if not fails and not errors:
        print(f"\n[ok] {len(passes)}/{total} checks passed ({len(skips)} skipped)")
    else:
        print(f"\n[!!] {len(fails)} failed, {len(errors)} errors / {total} checks")

def main():
    if hasattr(sys.stdout,"reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
    ap=argparse.ArgumentParser(description="Landing page static QA checker")
    ap.add_argument("html_path",help="HTML file or dir with index.html")
    ap.add_argument("--json",action="store_true",dest="as_json")
    ap.add_argument("--strict",action="store_true")
    ap.add_argument("--skip",default="",help="Comma-separated check names to skip")
    ap.add_argument("--verbose","-v",action="store_true")
    args=ap.parse_args()
    skip=set(s.strip() for s in args.skip.split(",") if s.strip())
    html_path=resolve_html_path(args.html_path)
    results=run_checks(html_path,skip,args.verbose)
    if args.as_json:
        print(json.dumps({"file":str(html_path),"results":results},ensure_ascii=False,indent=2))
    else:
        print(f"=== check-landing: {html_path.name} ===")
        print_human(results,args.verbose)
    sys.exit(1 if any(r["status"] in ("fail","error") for r in results) else 0)

if __name__=="__main__":
    main()

