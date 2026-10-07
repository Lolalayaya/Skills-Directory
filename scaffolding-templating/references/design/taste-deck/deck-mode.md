# Deck Mode + Style Contract —— SKILL.md §15-16 外置参考

> 触发时机：0.E 路由判定为 Deck / slide brief 时，**生成前完整读取本文档**。
> §15 锁定骨架（page plan / stage / motion / QA / CONFIG）；§16 定义风格合约（must-respect vs free-to-play）。
> 两者共同构成 deck 输出合约：§15 是边界，§16 是创意自由的范围。
## 15. DECK MODE (Fixed-Stage Slides) - Incremental Rules

Applied when the brief is a presentation deck or a fixed set of slides (see 0.E). DECK MODE rules override the core rules in SKILL.md and their reference files wherever they conflict. Output is a single-file standalone HTML (no build step), 1920x1080 stage, 8 slides by default, fit-scaled to any viewport.

### 15.1 Default Page Plan (8 slides)
1. Cover (brand wordmark + hero statement + primary CTA)
2. Agenda / principles
3-5. Feature / capability pages (2-3 pages, flow layout)
6. Data or quote page (stats, tables, testimonial)
7. Product / example page (console, UI mock, case)
8. Closing CTA (repeat wordmark + final action)
Adjust page count to the brief, but every slide must satisfy 15.3-15.6.

### 15.2 Deterministic Stage (non-negotiable)
- Fixed stage 1920x1080. One `<section class="slide">` per page: `position:absolute; inset:0; width:1920px; height:1080px; overflow:hidden`.
- Fit to viewport with ONE JS helper: `factor = min(vw/1920, vh/1080)`, center via `transform: translate(x,y) scale(factor)` on a stage wrapper. Never size the stage in vw/vh units.
- Slide switching: toggle `.active` / `.visible` classes (visibility + opacity + pointer-events), NEVER `display:none`.
- Navigation: `?slide=N` deep link, keys ← → Space Home End, touch swipe, `prefers-reduced-motion`, `@media print` renders all slides.
- Speaker notes (presenter mode, recommended): slides may carry a `data-note` per slide; pressing `N` toggles an overlay showing the current slide's note (time + page + note). Optional presenter-sync via `postMessage`/`StorageEvent` for a second window. Keep the notes OUT of the visible slide composition (they are chrome-layer, not content).
- Deck chrome: brand wordmark inside each slide at top 56px / left 120px; bottom-center clickable dot-progress navigation wrapped in a pill capsule (one dot per slide; active dot solid + slightly enlarged), NO on-screen keyboard hint text. Rules for the capsule:
  - Width is content-driven (`fit-content`): it grows automatically as slide count changes.
  - Color adapts to the slide background: capsule background = theme's main body-text color at ~8% alpha + same-color hairline border; dots inherit that color. Light background -> dark navigation; dark / saturated background -> light navigation. Source of truth is the theme's body/primary text variable, never a hardcoded hex.
  - `.nav-dot` is a `<button>`: it MUST set `color: inherit`, otherwise `currentColor` resolves to the UA default black and breaks contrast on dark themes.
  - Inject the theme body-text color explicitly on the pill container (`color: var(--color-...)`): do NOT rely on inheriting from the chrome bar's own color, which is a muted gray that washes the capsule out on light backgrounds.
  - Treat the capsule as a three-token surface, not a single `currentColor` effect: expose `--nav-pill-fg`, `--nav-pill-bg`, and `--nav-pill-border`, plus dark-tone fallbacks `--nav-pill-fg-dark`, `--nav-pill-bg-dark`, and `--nav-pill-border-dark`. Provide an `rgba()` fallback before the `color-mix()` enhancement; do not assume `color-mix()` support.
  - For a deck whose slides switch between light, dark, saturated, gradient, or image-led backgrounds, mark the affected slide with `data-nav-tone="dark"`. The controller must mirror that state to `.dot-nav[data-tone="dark"]`, so the capsule remains readable while preserving the series palette. Do not infer a single tone from the first slide and reuse it for the whole deck. If a deck uses only one tone, it still must declare the semantic tokens explicitly rather than relying on UA defaults.
  - Add a restrained `backdrop-filter` and shadow only as legibility aids. Under `prefers-reduced-transparency: reduce`, disable blur and use an opaque theme surface. The capsule must remain compact chrome, not become a card or a second content panel.
  - Class must be namespaced (`.nav-dot`) to avoid clashing with in-page decorative dots.
  - **CAPSULE RENDERING HARD RULE (2026-08-21, 30 套全量踩坑)**：胶囊背景/描边用 `color-mix(in srgb, currentColor calc(var(--nav-pill-alpha) * 100%), transparent)`。**color-mix 的混合比例必须是百分比**——直接写 `var(--nav-pill-alpha)`（值 `0.08`，无单位数字）或裸数字，整条声明会 invalid-at-computed-value，背景/描边退回全透明，胶囊视觉消失（只剩裸圆点）。`rgba()` 里的 0-1 数字合法，不受此限。`check-decks.py` 已含对应断言（每页 `.dot-nav` 背景 alpha>0.01 且描边 ≥1px）。
- 以上舞台结构（stage/缩放/切页/导航胶囊/print/reduced-motion）的事实骨架参考：`showcase/_skeleton.html`（373 行可运行骨架，新 deck 从它起步改造，勿凭记忆重写舞台机械）。

### 15.3 Value-Layer Fidelity Boundary (highest-leverage rule)
- `tokens.json` is the ONLY numeric source. `variables.css` / `theme.css` are implementation references. `DESIGN.md` is the fact source. Never design from screenshots or intuition.
- Palette, radii, font names: use EXACTLY the source tokens, 1:1. Typography sizes and spacing: multiply by 2 (web design → stage). Line-height: use the source `--leading-body` UNMODIFIED, applied to EVERY body-like class (`.body`, `.body-muted`, `.body-on-color`, `.card-body`, ...). Fixing only the main `.body` class is a known regression.
- Fonts: load the DESIGN.md substitute via Google Fonts with the fallbacks listed in the source; on load failure fall back to those substitutes, never to the default sans.
- 素材模式生成的 deck 必须在 `<head>` 写来源标记 `<meta name="design-source" content="<style-slug>">`：包外目录 deck 靠它被 check-decks.py 用素材权威行高校验（缺标记时降级为 deck 自身声明自洽检查）。
- **Boundary vs freedom**: this section only guards the fidelity of the TOKENS (what the palette / type / radii ARE). HOW to compose colors, assign type roles, and land the visual voice is the model's creative call under Section 16 - do not freeze it here.

### 15.4 Layout Hard Rules
- Flow layout inside slides. NO absolute-positioned content (known canvas overflow bug).
- Height budget: content must not cross y=900. Bottom 160px is a safety zone reserved for chrome.
- Absolute decorations (bubbles, triangles, shapes) must be checked for geometric overlap with the content block.
- Radii, shadows, button-corner direction follow the DESIGN.md signature literally.
- Remember line-height increases push card bottoms down, re-verify 15.6.2 after any line-height change.
- Budget the height IN THE FIRST DRAFT: display-scale headlines (e.g. 90px source x2 = 180px) spanning two lines, and dense multi-card/multi-table grids, are the highest-frequency overflow points. Compress margins and paddings up front, leave margin before the QA pass.

### 15.5 Story-Reveal Motion (v5 editorial expo - reference-deck-verified)
Transition-driven, driven by `.slide.visible` (NOT CSS `animation` + JS re-trigger):
- No slide-level translate or transition: the slide appears instantly, then its elements tell the story one by one.
- Reveal base state: `opacity:0; transform: translateY(28px)`. `.slide.visible .reveal` → `opacity:1; transform: translateY(0)`. Transition: `opacity/transform 0.7s cubic-bezier(0.16, 1, 0.3, 1)` (ease-out expo). Defined once as CSS tokens `--ease-out-expo` / `--duration-normal` in `:root`.
- Stagger via `transition-delay` on `.slide.visible .reveal.dN`: d1 0.12s / d2 0.24s / d3 0.36s / d4 0.48s (0.12s steps). Sequence matters: hero title → subhead → CTA; list items top-to-bottom; card grids left-to-right; all via d1-d4 (or finer by theme).
- Leaving a slide simply removes `.visible` — the reverse transition (elements slide down 28px and fade out) IS the exit animation. No extra code, no JS re-trigger needed in showSlide beyond toggling `.active` / `.visible`.
- Data-viz on entry: SVG line charts draw left-to-right (`.chart-line` with `pathLength="1"`, `stroke-dasharray:1` / `stroke-dashoffset:1 → 0` on `.visible`, ~1.4s delay 0.5s); ring charts fill clockwise.
- Interaction (hover on buttons / cards / link-arrow) must override the reveal transition to snappy timing (`.slide.visible [class*="btn"], .slide.visible .artifact, .slide.visible .link-arrow { transition: ... 0.2s ease }`).
- FORBIDDEN: large-delay chunked stagger ("block by block"), CSS `animation`-based reveals (forces JS re-trigger hacks), scroll-driven reveals.
- Banners / marquees: static large centered text only. NEVER scrolling marquees (unreadable at any speed).
- `prefers-reduced-motion`: collapse all animations/transitions to instant.

### 15.6 Mandatory QA Gates (run all four; none may be skipped)
1. **Value-layer check**: every color used in the HTML must be inside the source palette (tokens.json colors). This catches the biggest failure mode (inventing palettes). Reference implementation: `python showcase/check-values.py <slug 或 deck 目录>`（静态扫描，无需浏览器；包外 deck 需 `--style <slug>` 或 `design-source` 标记定素材基准，无自洽降级）. In **自由发挥模式** this gate downgrades to "declared-token self-consistency" - every color/font used must be inside the `freeplay-declaration.md` ②③ declared token sets (no stray colors/fonts beyond what you declared; the deck must match its own declaration).
2. **Automated deck check**: reference implementation `showcase/check-decks.py <slug 或 deck 目录>`（file:// 直读，无需起 HTTP 服务；需 playwright + Chrome）. It asserts per slide: every body-like computed line-height == the leading baseline (±0.02), visible content bottom <= 900, and nav-pill visibility/contrast. It excludes decor elements (hero-art / glow-* / bar-* / marquee) and fixed chrome. 行高基准解析：showcase 套（slug）取素材 `variables.css` 的 `--leading-body`（权威，不变）；包外用户 deck 依次取 `--style <slug>` → deck `<head>` 的 `<meta name="design-source">` 标记（15.3 契约）→ deck 自身 `:root --leading-body`（自洽降级，输出注明）。In **自由发挥模式** there is no source `--leading-body`; the line-height target is the declaration's own body line-height, and the safety-zone y<=900 check still runs — pass `--freeplay`（声明文件优先读 deck 旁 `freeplay-declaration.md`，回退包内模板）for this mode.
3. **Visual QA (capability-adaptive)**: Chrome headless `?slide=N` screenshots at 1920x1080 (工具 `python showcase/shot-all-slides.py <slug 或 deck 目录>`，file:// 直读无需起服务；showcase 套截到 `showcase/<slug>/screenshots/`，包外 deck 截到 deck 旁 `screenshots/`), then an inspection by whoever CAN see images: a native multimodal main model inspects directly; a text-only main model must delegate to a vision-capable sub-agent (e.g. a vision-reader). Never skip the visual pass just because the main model can't see. Covers palette adherence, signature moves, overflow below y=900, crop / overlap, and the bottom capsule on at least one light slide, one dark/saturated slide, and one gradient/photo-led slide. Confirm that the capsule has a visible surface boundary, that inactive dots remain legible, and that the active dot is distinguishable without overpowering the material style.
Arbitration (applies to ANY vision source - multimodal model or sub-agent): color / corner-radius / line-spacing judgments are UNRELIABLE (bone-white vs white confusion, 8px radius misread, 1.0 line-height reported as "comfortable"). Confirm via CSS computed values + pixel measurement before changing code.
4. **Structure anti-convergence**: run `python showcase/check-structure.py [<slug 或 deck 目录>]`（静态分析；包外 deck 需 `--style <slug>` 或 `design-source` 标记定契约基准）. It inspects middle slides 2-6 and requires at least two distinct, style-specific DOM/CSS signals; generic `card`, `quote`, `stat`, `frame`, and wordmark scaffolding does not count. The allowed middle-expression families are: data = real data cards/charts; newspaper = multi-column layout; illustration = full illustration plus side notes; product = product entity/UI artifact; playful = stickers, annotations, hand-drawn arrows; industrial = numbering, spec tables, engineering callouts. A single quote or breathing-space slide may be a deliberate rhythm change; the check warns only when more than half of the middle slides lose identifiable signals.

### 15.7 Deck-Specific Tells (banned in DECK MODE)
- Invented palette colors outside tokens.json (the #1 rework cause)
- Content crossing y=900 or overflowing the 1920x1080 canvas
- Decorative shapes overlapping text
- Body line-height drifting from the source `--leading-body` (including sibling classes)
- Scrolling banners, chunked stagger reveals

### 15.8 Customization Contract (clone-friendly CONFIG block)
Every generated deck MUST expose its adjustable parameters as named CSS custom properties, grouped in ONE clearly-marked `/* ════ CONFIG ... ════ */` block at the top of the `<style>` (right after the value-layer `:root`), each line carrying a short Chinese comment that names the parameter and gives the common range. Cloners edit ONLY that block and refresh - no build step.

Fixed token contract (names identical across all decks; defaults = the verified reference feeling):
- **Motion**: `--motion-ease` (default `cubic-bezier(0.16,1,0.3,1)`), `--motion-duration` (0.7s), `--motion-distance` (28px), `--motion-stagger-step` (0.12s)
- **Nav pill**: `--nav-dot-size` (14px), `--nav-dot-gap` (18px), `--nav-pill-pad-y` (14px), `--nav-pill-pad-x` (28px), `--nav-pill-alpha` (0.08), `--nav-pill-border-alpha` (0.28), `--nav-pill-shadow-alpha` (0.12), `--nav-pill-blur` (10px), `--nav-active-scale` (1.15), `--nav-hover-scale` (1.35). The semantic surface tokens (`--nav-pill-*`) must remain in the same CONFIG block when a deck needs brand-specific tuning.
- **Layout**: `--safety-bottom` (160px), `--frame-pad-top` (112px), `--frame-pad-x` (120px)
- **Data-viz**: `--chart-draw-duration` (1.4s)

Value-layer tokens from tokens.json stay 1:1 and do NOT go into CONFIG (they are the material contract; editing them breaks source fidelity). `.reveal`, `.slide`, and `.nav-dot` rule bodies must reference the CONFIG variables (`var(--motion-*)`, `var(--nav-*)`, `var(--safety-bottom)` ...), not hardcoded numbers.

### 15.9 Share & Export (P2 — deck delivery, reference implementation in showcase/)
Deck delivery happens in three dialects; pick by audience:

1. **本地导出 PDF** — `python showcase/export-pdf.py <slug 或 deck 目录>` → `.pdf`。showcase 样品按 slug（产物在 `showcase/exports/`）；**用户自己的 deck** 传包外任意含 index.html 的目录路径，产物落在 deck 旁边。deck 经 file:// 直读，无需起服务；`../fonts` 相对引用按目录解析（字体库从 `showcase/fonts/` 拷到 deck 同级，与部署暂存同结构）。8 页 16:9 落版（骨架 `@media print` 每 slide 一页，脚本注入 `@page size` 保证不缩放不裁切）。适合打印、评审、存档。
2. **本地导出 PPTX** — `python showcase/export-pptx.py <slug 或 deck 目录>` → `.pptx`，输出位置规则同上。逐页截 1920×1080 全幅图嵌 16:9 幻灯片，与浏览器所见 1:1。适合发给不改代码的同事继续编辑。
3. **公开 URL 分享** — 动手前**先完整读取 `deploy-guide.md`**（部署规范/AI 代理执行手册，本节仅要点摘要）：环境自备自检、Vercel / 飞书妙搭两条出口的完整流程、字体改造与失败处理都在该文档。要点：
   - **Vercel**：默认部署**用户自己的 deck**（暂存 `<deck>/ + fonts/` 保持 `../fonts` 相对结构后 `vercel deploy --prod --yes`）；样品整站在 `showcase/` 内部署（`.vercelignore` 排除 exports/本地截图；根落地页 `showcase/index.html` 自动跳图廊）。
   - **飞书妙搭**：单 deck 创意模式应用（`+create --app-type html` → `+init` → push `sprint/default` → `+release-create` / `+release-get` 轮询 → `/page/<meta_token>` 链接，开发态=发布态）。**字体必须先换官方镜像** `https://miaoda.feishu.cn/fonts/css2`（平台资源不进 git；样品查 `deck-font-map.json`、用户 deck 自动探测字族并与 fonts.css 求交；斜体族用 `ital,wght` 双轴；未知字族不进查询，否则 css2 整条 400 全字体失败）。`+html-publish` 为旧链路勿用；重部署复用应用不重复 `+create`。
   - 登录授权（`vercel login` / `lark-cli auth login --domain apps`）属用户操作；部署前 deck 必须已过 15.6 QA。

**字体自托管（强制，2026-08-19 起）**：deck 字体一律用本地共享字体库，禁止 Google Fonts 外链。原因：外链依赖观看者网络能否到达 `fonts.googleapis.com`/`fonts.gstatic.com`，国内/飞书生态观看者会回退系统字体，视觉掉档。实现：
- 共享库 `showcase/fonts/`：62 个 latin 子集 `.woff2` + `fonts.css`（62 个 `@font-face`，只取 latin，内容为英文省体积）。覆盖 30 套实际用到的全部 23 个字族（Inter/JetBrains Mono/Archivo/Archivo Black/Anton/Bebas Neue/Fraunces/Source Serif 4/EB Garamond/Caveat/DM Sans/Alfa Slab One/Manrope/Bowlby One SC/Open Sans/Roboto Condensed/Nunito/Raleway/Space Grotesk/Noto Sans/Press Start 2P/VT323/Literata）。
- 每个 deck 的 `<head>` 用 `<link rel="stylesheet" href="../fonts/fonts.css">` 引用（相对路径，`file://` 和 Vercel/妙搭都可用）。字体选择仍每套各异的品牌替代字体（素材 DESIGN.md 的 substitute 规则），只是文件不再依赖 Google。
- 重建工具：`python showcase/fonts_download.py`（重新下载/增量）+ `python showcase/fonts_rewrite.py`（改写 deck 外链为本地引用）。
- 改字体后必须重跑 QA：`check-values.py` + `check-decks.py` + `gallery-shots.py`（重截 gallery 封面）+ build-index.py（图廊回填）。截图用 `document.fonts.ready` 等待加载完成。

---

## 16. STYLE CONTRACT (creative freedom - where the model decides)

Section 15 locks the skeleton: page plan, stage, navigation, motion, layout safety, QA, CONFIG. The STYLE CONTRACT is NOT another rulebook. It is the agreement on what the model MUST respect while playing and where it has true freedom. Sections 15 and 16 together define a deck's output contract.

### 16.1 What the model MUST respect (binding, from the material)
- Style source of truth = the material `DESIGN.md` (facts) + `tokens.json` (only numeric source). Never screenshots, never echoing another style, never the model's own generic default. Anticipate the expected output is a deck that READS as that exact brand, not "a nice deck".
- Palette, type, radii, shadows come EXACTLY from the source tokens (1:1; sizes/spacing x2). Zero invented colors or fonts.
- 氛围与装饰手法可对照真实品牌官网的表现学习（`brand-style-reference.md` 的沉淀规则：官网是"表现标杆"、DESIGN.md 是"事实源"，学手法不照搬布局；背景纹理是 30 套普遍缺失项，优先从该报告找补）。
- The material's USAGE constraints are the style's voice and are binding, not suggestions. Extract them from DESIGN.md Do's/Don'ts and obey. Examples that shipped: IKEA link-blue only for links / yellow only for activation; Steep sienna only on peach surfaces and chart strokes, max one peach card per page; Flying Papers serif 400-only with isolated italic phrases, accent card one per row; Raycast deep monitor system with a single signature pop color.

### 16.2 Where the model is FREE TO PLAY (do NOT over-specify)
- **Color composition**: how to use the palette inside its rules - emphasis order, surface hierarchy, where the one accent lands, contrast layering. Skill never dictating which accent on which page.
- **Typographic voice**: role split of the substitute fonts (headline / body / micro-label), letter-spacing feel, editorial vs technical tone - decided from reading DESIGN.md.
- **Page composition & "signature moves"**: italics placement, card geometry, data-viz style for that brand, layout personality - the model's judgment from the material.
- **Copywriting / content voice** inside the 8-page plan: tone, microstructure, what each section says.

### 16.3 Keeping freedom disciplined
- Before code, write a 3-line "Style Read": palette voice / typographic voice / signature moves, each traceable to a DESIGN.md line (mirrors 0.B for the material).
- In **自由发挥模式** the Style Read IS the `freeplay-declaration.md` (0.E) - no external DESIGN.md to trace to, so the declaration's own ②③④ sections are the trace anchor.
- Every decorative decision must trace to source basis. If a decoration has no source line, drop it - restraint is the move (most brands here are restrained for reasons).
- If a visual call cannot be sourced or justified, prefer the source's default restraint.

### 16.4 Anti-slop guard (style layer)
The deck must NOT converge to a generic AI look: no AI-purple, no default glassmorphism, no invented palette, no "three equal cards" if the source does not say so, no interpolation between styles. Enforcement = 15.6 gate 1 (value-layer ⊆ tokens) + the source usage constraints + 16.3 traceability.
Anti-convergence warning (Zara-style self-reminder): when generating a BATCH of styles (e.g. the whole library), models tend to converge toward one comfortable look across generations. This is the core risk of a style library - every deck must stay distinguishable. Before each deck, re-read 16.3 Style Read and confirm the palette voice / typographic voice / signature moves genuinely differ from the previous deck's. If two adjacent decks read as "the same design," redo the stylistic calls.
Structural anti-convergence: each style must declare at least two distinct middle-slide signals in `metadata/structure-contracts.json`, and the implementation must express its declared family rather than falling back to a shared card/grid recipe. Different families intentionally use different middle expressions: data cards/charts, newspaper columns, illustration with side notes, product/UI artifacts, playful stickers and annotations, or industrial numbered specifications and engineering callouts.

### 16.5 CJK / Chinese Fallback Contract
English-first decks work as-is. When deck content is Chinese or mixed CJK, apply a fallback system so the material's typographic voice survives the script change:
- **Font mapping (per role)**: map each substitute font to a CJK-capable pairing drawn from the material's voice - display serif/sans → 思源宋体/思源黑体 (Noto Serif SC / Noto Sans SC) or a brand-appropriate display face (e.g. 站酷小薇体 for warm/editorial); body sans → 思源黑体 (Noto Sans SC); mono → keep the Latin mono for digits/latin + a CJK fallback (most monos lack CJK). Weights must match the material's weight budget (e.g. Steep serif 400-only → Noto Serif SC 400).
- **Metric adjustments**: line-height bumps for CJK (~1.75-1.85 vs the Latin 1.35-1.5); letter-spacing returns to 0 (no negative tracking on CJK); NO `text-transform: uppercase` on CJK text; NO italic emphasis on CJK (use weight or color instead - mirrors Zara's rule).
- **Spacing convention**: 盘古之白 - insert a space between CJK and Latin/digits (`使用 Claude`, not `使用Claude`).
- **Loading**: add the CJK font to the Google Fonts `<link>` with `display=swap`, keeping the Latin substitute as primary so Latin glyphs render from the branded face and CJK auto-falls to the SC font.
- **Re-verify**: after switching language, re-run 15.6 gates - the CJK line-height bump moves card bottoms and can push content past y=900.

---


