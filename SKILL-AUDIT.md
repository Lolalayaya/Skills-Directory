# Skills Directory 檢查與更新紀錄

審查方法：把 18 個頂層技能 + 137 個子技能拆成 6 組，分別實際讀取每份 `SKILL.md` 的 frontmatter 與內文，核對觸發條件是否清楚、彼此是否重疊，再由人工彙整判斷（而非只看 README 摘要）。日期：2026-07-31。

> **執行進度**：下方分類與建議是健檢當時的判斷結論，**保留原始內容作為完整記錄**。實際處理結果見文件最後的「✅ 執行紀錄」——已完成的項目不會反過來修改上面的敘述，避免這份報告失去「當時為什麼這樣判斷」的脈絡。

---

## 步驟一：五類分類

### 分類 1｜核心常用

**頂層（11）**：`agentic-dev-workflow`、`product-verification`、`code-quality-review`、`incident-runbooks`、`cicd-deployment`、`browser-automation`、`deep-research`、`scaffolding-templating`、`library-api-reference`、`personal-learning`、`business-automation`

**子技能**：
- 開發流程：`brainstorming`、`writing-plans`、`subagent-driven-development`、`finishing-a-development-branch`、`test-driven-development`、`verification-before-completion`、`code-review-expert`、`code-security`、`systematic-debugging`
- 部署：`deploy-to-vercel`
- 瀏覽器/研究：`browser`、`ui-test`、`fetch`、`search`、`research`、`research-deep`、`research-report`
- 設計/文件：`ui-ux-pro-max`、`vercel-react-best-practices`
- 任務管理：`planning-with-files`（英文版）
- 行銷（21）：`copywriting`、`copy-editing`、`content-strategy`、`seo-audit`、`social`、`cro`、`onboarding`、`signup`、`pricing`、`emails`、`ads`、`ad-creative`、`analytics`、`customer-research`、`product-marketing`、`marketing-ideas`、`sales-enablement`、`popups`、`churn-prevention`、`paywalls`、`competitors`

### 分類 2｜偶爾需要

**頂層（4）**：`openspec-workflow`、`skill-authoring`、`data-analysis`、`internal-writing-comms`

**子技能**：
- 開發流程：`using-git-worktrees`、`executing-plans`、`semgrep`、`llm-security`、`requesting-code-review`、`receiving-code-review`、`webapp-testing`、`skill-review`、`openspec-explore/propose/apply-change/sync-specs/archive-change`（5個）
- 部署：`vercel-cli-with-tokens`、`vercel-optimize`
- 瀏覽器/研究：`cookie-sync`、`browser-trace`、`functions`、`autobrowse`、`browser-to-api`、`webmcp-gen`、`research-add-fields`、`research-add-items`
- 設計/文件：`ui-styling`、`frontend-design`、`brand`、`canvas-design`、`algorithmic-art`、`theme-factory`、`web-artifacts-builder`、`web-design-guidelines`、`writing-guidelines`、`programmatic-seo`、`docx`、`xlsx`、`pptx`、`pdf`、`mcp-builder`、`vercel-react-native-skills`、`vercel-react-view-transitions`、`vercel-composition-patterns`、`doc-coauthoring`、`internal-comms`
- 學習：`book-study`、`wiki-ingest`、`sigma`
- 上下文工程（進階但描述清楚，非「不確定」）：`context-fundamentals`、`context-degradation`、`context-compression`、`context-optimization`、`filesystem-context`、`memory-systems`、`tool-design`、`project-development`、`evaluation`
- 行銷（26）：`schema`、`site-architecture`、`image`、`video`、`sms`、`cold-email`、`offers`、`aso`、`ai-seo`、`directory-submissions`、`co-marketing`、`community-marketing`、`free-tools`、`influencer-marketing`、`launch`、`lead-magnets`、`marketing-loops`、`referrals`、`ab-testing`、`attribution`、`marketing-council`、`marketing-plan`、`marketing-psychology`、`prospecting`、`public-relations`、`revops`

> `context-engineering-collection`（頂層）本身也歸這類——描述清楚，只是使用者角色窄（打造 agent 系統時才用），不算「不確定用途」。

### 分類 3｜功能重疊

| 重疊組 | 說明 |
|---|---|
| `using-superpowers` ↔ 根目錄 `skills-directory` | 兩者都宣稱「對話開始時先讀我」，職責高度重疊 |
| `skill-creator` / `skill-forge` / `writing-skills` | 三者都覆蓋「建立新技能／編輯既有技能」，觸發詞幾乎相同，只有方法論不同（見步驟二） |
| `competitor-analysis` ↔ `competitor-profiling` | 都是「深研競品產出結構化報告」，只是有無自動發現階段不同，且用完全不同工具鏈 |
| `company-research` ↔ `event-prospecting` | 後者是前者的「會議場景」特化版，共用同一套 ICP 格式與規則 |
| `research`（deep-research）↔ `company-research`（browser-automation） | 命名層級撞名，使用者說「研究一家公司」時兩邊都可能被觸發 |
| `design` / `design-system` / `brand` / `banner-design` / `slides` | 品牌語氣、Banner、投影片邏輯在多份文件裡重複出現，觸發詞也重疊 |
| `customer-research` ↔ `prospecting`（行銷） | 都用「ICP research」當觸發詞，但已有部分互斥說明 |
| `marketing-plan` ↔ `marketing-ideas` | 都涉及「策略發想」，已有部分互斥說明 |
| `attribution` / `analytics` / `ab-testing` | 都跟數據相關，但已用明確的 Boundaries 段落解決，風險低 |

### 分類 4｜不確定用途（描述模糊或彼此矛盾）

| 技能 | 問題 |
|---|---|
| `dispatching-parallel-agents` | 與 `subagent-driven-development` 的指引**直接矛盾**：一份文件建議計畫執行完後接續平行派工，另一份明文禁止平行派 implementer。這是本次審查裡最明確的「觸發條件需要你補定義」案例 |
| `agent-experience` | 描述本身清楚（產品/SDK/文件的 DX 審計），但放在 `browser-automation` 底下主題不符，容易讓人以為跟瀏覽器操作有關 |
| `slack-gif-creator` | 用途極窄（做 Slack 動畫 GIF），使用頻率存疑，接近「可能可以刪」的邊界 |

### 分類 5｜可能可以刪

| 技能 | 理由 |
|---|---|
| `infrastructure-ops`（頂層） | 確認為完全空白的佔位資料夾，只有一份「目前無內容」的自陳文件 |
| `browser-use-to-stagehand` | 一次性遷移工具，遷完即用不到，需要時再重裝即可 |
| `safe-browser` | 範例硬編碼在 Hacker News demo，通用性低，近乎教學腳手架而非可重用技能 |
| `anthropic-brand-guidelines` | 只在製作 Anthropic 官方品牌 artifact 時有用，通用性極低 |
| `latent-briefing` | 需要直接操作 worker 的 KV cache，文件自己都說「多數情況是研究構想，非可部署技術」 |
| `bdi-mental-states` | 用 RDF/BDI 本體建模 agent 心智狀態，極學術向，日常任務幾乎不會觸發 |
| `planning-with-files-ar`／`-de`／`-es` | 核心邏輯與英文版完全相同，只是語言不同；除非你會用阿拉伯文/德文/西班牙文跟 AI 對話，否則永遠不會觸發 |

---

## 步驟二：建議

### 建議合併

| 合併對象 | 建議新名稱 | 合併後負責什麼 |
|---|---|---|
| `skill-creator` + `skill-forge` + `writing-skills` | 保留 `writing-skills`（最完整） | 技能撰寫全流程：TDD 式壓力測試（writing-skills）+ 架構 checklist（skill-forge）+ eval/benchmark 量化迴圈（skill-creator）+ SDO 描述優化規則，三份方法論疊在一起，不再各自獨立成三個名字。`skill-review` **維持獨立**，只做「審查既有技能、不編輯」——這是四者中唯一觸發條件乾淨的 |
| `competitor-analysis` + `competitor-profiling` | `competitor-analysis`（保留現名，淘汰 profiling） | 不論是「自動探索競品」還是「給定 URL 清單」，統一走同一套工具鏈，輸出矩陣＋戰卡；淘汰 profiling 額外引入的 Firecrawl/DataForSEO 路徑 |
| `design` + `brand` + `banner-design` | 新名 `brand-assets` | 品牌語氣、視覺識別、Logo/Banner/Icon/社群圖生成，一次收斂 |
| `design-system`／`slides` 內重複的簡報產生邏輯 | 不新增名稱，做法是「刪除重複」 | 只保留獨立的 `slides` 技能當唯一的簡報產生器，`design`／`design-system` 裡的簡報章節整段移除，改成一句「產生簡報請用 `slides`」 |

**可以不合併、但建議加互斥說明的（風險較低，先補句子即可）**：
- `company-research` ↔ `event-prospecting`：在 `event-prospecting` 開頭加一句「本質是 company-research 的會議場景特化版」
- `customer-research` ↔ `prospecting`（行銷）：互相加一句「For 建名單見 prospecting／For 理解客戶心理見 customer-research」

### 觸發條件不清楚，需要你補定義

1. **`dispatching-parallel-agents` vs `subagent-driven-development`**：需要你明確拍板一條規則，例如「平行派工只用在無共享狀態的獨立研究/除錯任務；計畫內的 implementer 任務永遠序列執行」，再把這句話寫回兩份技能的 description。
2. **`using-superpowers` 的失效引用**：文件內用 `superpowers:xxx` 前綴引用其他技能，但本倉庫實際技能名稱沒有這個前綴，引用會失效。需要你決定：修正這些引用，還是直接讓這個技能跟根目錄 `skills-directory` 二選一保留（目前兩者職責幾乎重複）。
3. **`deep-research` 提到的 `web-research-prospecting`**：description 裡寫「不用於 sales/prospecting，見 `web-research-prospecting`」，但倉庫裡沒有這個名字的技能（應該是指 `browser-automation`），這是一個失效連結，需要修正。
4. **`agent-experience` 的歸類位置**：內容其實是「產品/SDK/文件的 DX 審計」，跟瀏覽器操作無關，需要你決定要不要搬到別的分類（例如併入 `skill-authoring`），或保留現狀。

### 建議直接移除

- `infrastructure-ops`（頂層空殼，若近期不會補內容）
- `browser-use-to-stagehand`
- `safe-browser`
- `anthropic-brand-guidelines`
- `latent-briefing`
- `bdi-mental-states`
- `planning-with-files-ar` / `-de` / `-es`（`-zh` 視你是否會用簡體中文對話決定去留）
- `slack-gif-creator`（如果你從未真的用它做過 GIF）

> 以上是健檢當時的原始建議，保留不動。實際處理結果見下方「✅ 執行紀錄」。

---

## ✅ 執行紀錄（2026-07-31）

### 已修正的 bug（步驟二「觸發條件不清楚」）

- `dispatching-parallel-agents` ↔ `subagent-driven-development` 的矛盾指引：已在 `agentic-dev-workflow/SKILL.md` 的路由步驟、`dispatching-parallel-agents/SKILL.md` 的「When NOT to Use」都補上明確規則——平行派工只用在計畫外、無共享狀態的獨立任務，計畫內的 implementer 任務永遠序列執行。
- `using-superpowers` 及另外 5 份文件（`writing-plans`、`writing-skills`、`subagent-driven-development`、`executing-plans`、`systematic-debugging`）裡失效的 `superpowers:xxx` 前綴引用，已全部修正為本倉庫實際使用的技能名稱（去掉前綴）。
- `deep-research` 引用不存在的 `web-research-prospecting`，已修正為正確指向 `browser-automation` 的 `company-research`/`competitor-analysis`/`event-prospecting`，並在 `company-research` 加回互斥說明。

### 已補上的互斥說明句

- `company-research` ↔ `event-prospecting`
- `customer-research` ↔ `prospecting`
- `deep-research` ↔ `company-research`（命名易混淆問題）

### 已刪除（7 個）

`browser-use-to-stagehand`、`safe-browser`、`slack-gif-creator`、`planning-with-files-ar`、`planning-with-files-de`、`planning-with-files-es`、`latent-briefing`。全部用 `git rm -r` 刪除（保留在 git 歷史裡，需要可還原），並同步更新了 `README.md`、`SKILL.md`（含子技能數量與稽核註記）、`context-engineering-collection/SKILL.md` 的索引。

**例外：`context-engineering-collection` 內部的研究資料（`researcher/corpus/index.json`、`mechanisms/registry.jsonl`、`claims/index.jsonl`、benchmarks、`.claude-plugin/marketplace.json`、`.plugin/plugin.json` 等）沒有跟著更新** ——這些是第三方 MIT 授權集合自己的內部驗證/研究資料，需要跑它自己的 Python 驗證腳本（`validate_repo.py --strict`、`skill_health.py`、`run_benchmarks.py`、`check_activation_cases.py` 等）才能正確同步，手動改動風險比效益高，因此只更新了它自己的 `SKILL.md` 索引。

**實際影響範圍**：
- 日常透過 Claude Code 呼叫技能完全不受影響——`latent-briefing` 單純從可觸發的技能清單消失，其他 16 個子技能正常運作。
- 已額外修掉一個真實會遇到的坑：`context-optimization`、`multi-agent-patterns` 這兩個仍在使用的技能，內文原本各有一句「KV-cache 共享請見 `latent-briefing`」，會讓 Claude 在對應情境下指向一個已不存在的技能——已從兩份文件移除這句話。
- 唯一還留著、且刻意不處理的落差：上面列的內部研究/驗證資料。只有在**未來有人主動維護這個第三方集合本身、去跑它自己的測試套件**時才會顯現（驗證腳本會報「找不到 `latent-briefing` 對應資料」之類的錯誤），一般使用情境不會碰到。

### 使用者決定保留（不刪除）

- `infrastructure-ops`（空佔位，先留著）
- `anthropic-brand-guidelines`（保留，當作產出網站時的 UI 參考）
- `bdi-mental-states`（先暫時留存）

### 3 組「合併建議」實際處理結果：改為澄清，不做實體合併

深入讀完三組的完整內容後，發現原始建議的「合併」判斷有誤——這三組看起來重疊，實際上都是**各自獨立、內建真正可執行工具（腳本/agent/reference）的完整技能**，強行合併等於要拆解多套不同來源的程式碼，風險遠高於效益。三組都改為「不動資料夾，只把 description／路由文件裡的分工講清楚」：

1. **`skill-creator` + `skill-forge` + `writing-skills`**：三者分別帶著完全不同的工具鏈（官方 eval-viewer/benchmark 腳本、獨立的 architecture-first checklist+腳本、TDD 測試方法論），已在三份 description 加上明確的「階段標籤」（架構設計 → eval 迭代 → 上線前驗證），並更新 `skill-authoring/SKILL.md` 路由說明「這是循序的不同階段，不是重複」。
2. **`competitor-analysis` + `competitor-profiling`**：分別用完全不同的資料來源與工具（Browserbase browse CLI 自動探索 + HTML 互動報告 vs Firecrawl/DataForSEO 針對已知 URL 清單做 SEO/流量情報），已在兩份 description 互相加上「你有沒有現成 URL 清單」「要 HTML 報告還是 Markdown 檔案」的判斷依據。
3. **`design` + `brand`/`design-system`/`banner-design`/`slides`**：確認全部標記 `author: claudekit`，是同一供應商刻意設計的「全包版 vs 精簡單功能版」雙軌架構（`design` 內建自己的 Logo/CIP/Banner/Icon/Slides 生成邏輯，故意不假手其他技能），並非意外重複。已在 `design` 的 description 與 `scaffolding-templating/SKILL.md` 路由裡加上這個「全包 vs 精簡」的判斷依據，不合併、不視任何一方為過時。

**這帶出一個值得記住的教訓**：光看 `description` 判斷「兩個技能很像」不可靠——本次三組候選合併，三組都在讀完整份 SKILL.md 及其綁定的 scripts/references 後被推翻。之後若再懷疑技能重疊，應先完整讀過雙方內容，而非只比對 description 文字。

---

## 附錄：`mattpocock-skills` 匯入健檢（2026-07-31，同一天進行）

在完成上述 18 個頂層技能的健檢後，使用者要求把第三方技能包 `mattpocock-skills`（作者 Matt Pocock，[aihero.dev](https://www.aihero.dev/s/skills-newsletter)，MIT 授權）整套匯入本倉庫，並套用同一套五類分類法篩選。方法：先把原始 41 個資料夾（22 個作者正式對外宣告、19 個在 deprecated/in-progress/misc/personal 分類但未正式宣告）整套複製進倉庫，再拆成 3 組分別實際讀完全文（含對照本倉庫既有的 5 組疑似重疊技能），才下分類判斷——延續上面「不能只看 description」的教訓。

### 分類結果

**核心常用**：`domain-modeling`、`to-spec`、`to-tickets`、`grill-with-docs`、`grilling`/`grill-me`、`setup-pre-commit`
**偶爾需要**：`improve-codebase-architecture`、`codebase-design`、`prototype`、`wayfinder`、`triage`、`setup-matt-pocock-skills`、`resolving-merge-conflicts`、`ask-matt`、`research`、`handoff`、`git-guardrails-claude-code`、`setup-ts-deep-modules`、`to-questionnaire`、`wizard`、`writing-fragments`、`loop-me`
**功能重疊（需決策）**：`tdd`↔`test-driven-development`、`diagnosing-bugs`↔`systematic-debugging`（真重疊）；`code-review`↔`code-review-expert`、`teach`↔`sigma`、`writing-great-skills`↔`writing-skills`、`research`↔`deep-research`（表面像，實際不同）；`batch-grill-me`/`claude-handoff`/`writing-beats`/`edit-article`（同手法的競爭版本）
**不確定用途**：無——41 個裡沒有真正「看不出怎麼用」的半成品，這點本身出乎意料（原本預期 in-progress 資料夾會有明顯半成品）
**可能可以刪**：`obsidian-vault`、`scaffold-exercises`、`migrate-to-shoehorn`、`implement`、`ubiquitous-language`（高信心）；`design-an-interface`、`qa`、`request-refactor-plan`（deprecated，信心不一）

### 使用者決策與實際處理

1. **真重疊兩對，指示「實體整合兩邊精華」**：
   - `tdd` 併入 `test-driven-development`：貢獻 Seams（測試邊界共識）、三個具名反模式（implementation-coupled/tautological/horizontal-slicing）、Mocking 章節（系統邊界才 mock、依賴注入）。原本的紅綠重構鐵律、話術攔截表、驗證清單維持不變。
   - `diagnosing-bugs` 併入 `systematic-debugging`：貢獻「先建可靠的紅色訊號迴圈」方法論（10 種構造手法、非決定性 bug 處理、`building-a-feedback-loop.md`）、Phase 3 從單一假設升級成 3-5 個排序假設、Phase 4 加入 debug tag 慣例與「正確 seam」判斷、結尾清理清單。原本的四階段架構、rationalization 對照表、「3 次修不好=架構問題」鐵律維持不變。

2. **同手法競爭版本，指示「交叉比對後合併」**：
   - `batch-grill-me` 併入 `grilling`/`grill-me`，變成 `--batch` 模式（整批問 vs 預設一次一題）
   - `claude-handoff` 併入 `handoff`，變成背景 agent 交付路徑（有 `claude --bg` 就直接launch，否則存檔）
   - `writing-beats` + `edit-article` 併入 `writing-shape`：`writing-beats` 貢獻敘事節奏的 beat 模式（含「預覽這個 beat 會解鎖什麼」技巧）；`edit-article`（只有 8 行的早期草稿）貢獻「編輯既有草稿」這個獨立場景（依賴關係排序 + 逐節重寫），但重寫時套用 `writing-shape` 原有的品質標準，捨棄 `edit-article` 那條「每段最多 240 字」的武斷規則

3. **高信心可刪 5 個全刪；3 個信心不一的 deprecated 先保留**：
   - 已刪除：`obsidian-vault`、`scaffold-exercises`、`migrate-to-shoehorn`、`implement`、`ubiquitous-language`
   - 保留觀察：`design-an-interface`、`qa`、`request-refactor-plan`
   - `ubiquitous-language` 刪除後，`qa` 技能裡引用其產出檔案 `UBIQUITOUS_LANGUAGE.md` 的地方，已改指向 `domain-modeling` 產出的 `CONTEXT.md`

4. **4 組「表面像、實際不同」維持不合併**：`code-review`↔`code-review-expert`、`teach`↔`sigma`、`writing-great-skills`↔`writing-skills`、`research`↔`deep-research`——在四份既有技能的 description 都補上反向的互斥說明句。

### 內部一致性修復

匯入+刪除+合併後，逐一檢查 mattpocock-skills 內部的交叉引用是否失效：
- `ask-matt/SKILL.md`（整套技能的流程路由文件）大量引用了 `/implement`、`/tdd`、`/diagnosing-bugs`，已全部改指向本倉庫對應的替代技能（`subagent-driven-development`、`test-driven-development`、`systematic-debugging`），並在文件開頭加註說明
- `engineering/README.md`、`writing-great-skills/GLOSSARY.md` 裡的同類引用一併修正
- 移除了原始廠商的 `plugin.json`（宣告的技能清單已跟實際內容不符，且本倉庫不是以 plugin 形式安裝）

### 第一輪結果（後被第 5 點的決定取代）

41 個資料夾 → 30 個（14 engineering + 7 productivity + 3 deprecated + 4 in-progress + 2 misc，其中 `writing-shape` 是兩次合併的匯集點，但它本身原本就是這 30 個之一，合併進來的內容不額外增加資料夾數）。當時的做法是新建一個第 19 個頂層技能 `mattpocock-skills` 收納這 30 個，並移除了廠商原本每個分類底下、內容已跟實際狀態不符的 6 份 README.md。

### 5. 使用者要求：不另立第 19 個分類，直接融入既有 18 個分類

使用者接著要求撤銷「獨立第 19 個頂層技能」的做法，改成把這 30 個依主題直接分散進本倉庫既有的 18 個分類裡，理由是這樣才符合原本的分類邏輯，而不是把第三方來源當成特殊待遇。實際處理：

1. **確認可安全搬移**：先確認 mattpocock-skills 內部沒有任何跨資料夾的相對路徑引用（都是用 `/skill-name` 這種與位置無關的技能名稱互相引用），搬移資料夾不會弄斷內部連結。
2. **依主題分配到 9 個既有頂層技能**：
   - `agentic-dev-workflow`（+14）：`ask-matt`、`grill-with-docs`、`domain-modeling`、`to-spec`、`to-tickets`、`wayfinder`、`resolving-merge-conflicts`、`prototype`、`setup-matt-pocock-skills`、`grilling`、`grill-me`、`handoff`、`request-refactor-plan`、`git-guardrails-claude-code`
   - `code-quality-review`（+6）：`improve-codebase-architecture`、`codebase-design`、`code-review`、`design-an-interface`、`setup-ts-deep-modules`、`setup-pre-commit`
   - `incident-runbooks`（+2）：`triage`、`qa`
   - `deep-research`（+1）：`research`（發現跟 `deep-research` 自己既有的 `research` 子技能撞名，改名並改 frontmatter `name:` 為 `background-research`，詳見下方「發現的命名衝突」）
   - `personal-learning`（+1）：`teach`
   - `internal-writing-comms`（+3）：`writing-fragments`、`writing-shape`、`to-questionnaire`
   - `skill-authoring`（+1）：`writing-great-skills`
   - `business-automation`（+1）：`loop-me`
   - `infrastructure-ops`（+1）：`wizard`（讓這個原本空白的佔位技能第一次有真實內容，但明確標註「仍不涵蓋日常維運」，不誇大範疇）
3. **發現的命名衝突**：`mv` 移動 `research` 到 `deep-research/references/research` 時，因為目的地已經存在同名資料夾（`deep-research` 自己 pipeline 第一階段的 `research`），`mv` 沒有覆蓋也沒有報錯，而是把來源資料夾**嵌套進**已存在的資料夾裡（變成 `deep-research/references/research/research/`）——這是操作過程中才發現的真實 bug，不是模擬。修正方式：把嵌套的資料夾拉出來重新命名為 `background-research`，並同步修改 SKILL.md 內的 `name:` frontmatter 欄位（不只資料夾名要改，技能實際的識別名稱也要改，否則兩個技能還是同名）。這之後補做了一次全倉庫 `name:` 欄位查重，確認沒有其他衝突。
4. **建立集中授權文件**：因為內容分散到 9 個不同資料夾，不再適合放一份 `LICENSE` 檔案在單一資料夾裡，改成在倉庫根目錄新建 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)，列出完整授權全文、逐項技能對應到哪個目的地資料夾、以及 `test-driven-development`／`systematic-debugging` 這兩個「內容被吸收但檔名不變」的特殊案例。
5. **更新 9 個目的地頂層技能自己的 `SKILL.md`**：每個都新增對應的子技能列表、調整 description 涵蓋新增能力、補上跟既有子技能的分工說明（例如 `agentic-dev-workflow` 把新增的 14 個依功能分成「逼問式規劃工具」與「Session／git 機制」兩個子分類，避免單一表格塞 22 列失去可讀性）。
6. **移除第 19 個頂層技能**：刪除 `mattpocock-skills/` 整個資料夾（原本的 `plugin.json` 已於第一輪移除，`LICENSE` 內容併入 `THIRD-PARTY-LICENSES.md`），改回 18 個頂層技能。
7. **確認「全域必用」問題**：搜尋這 30 個技能全文裡的 `MUST use`／`before any`／`ALWAYS use` 等字樣，找到的幾處都是技能**自己流程內部**的步驟用語（例如「claim a ticket **before any work**」是 `wayfinder`/`triage` 自己流程的一步），不是「這個技能本身必須在任何回應前使用」的宣告——確認這 30 個裡沒有一個夠資格列進 `SKILL.md` 開頭的「🔁 Universal」清單。

### 最終結果

18 個頂層技能維持不變，子技能數從健檢前的 130 個變成 **160 個**（130 + 30，`context-engineering-collection` 自己的 16 個維持獨立計算）。完整的最終落點、合併細節、命名衝突處理，都同步寫進了根目錄 `SKILL.md` 的 `THIRD-PARTY IMPORT` 註解區塊、`README.md` 對應的 9 個小節，以及 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)。

---

## 2026-08-01：匯入第三方技能包 `andrej-karpathy-skills`（forrestchang，MIT）

使用者提供來源：`https://github.com/multica-ai/andrej-karpathy-skills.git`（forrestchang 原倉庫 `github.com/forrestchang/andrej-karpathy-skills` 的鏡像）。要求依照標準流程（階段 A-D）評估、決定分類、整併、更新文件，並同步安裝到本機 `~/.claude/skills/`。

**內容**：clone 後確認整個倉庫只含 **1 個技能**——`skills/karpathy-guidelines/SKILL.md`，濃縮成 4 條行為準則（Think Before Coding／Simplicity First／Surgical Changes／Goal-Driven Execution），衍生自 Andrej Karpathy 對 LLM coding 常見毛病的觀察。倉庫其餘檔案（`README.md`、`README.zh.md`、`CLAUDE.md`、`CURSOR.md`、`EXAMPLES.md`、`.claude-plugin/`、`.cursor/`）都是廠商自己的安裝/plugin 腳手架，不是額外的技能內容，未複製進本倉庫。沒有獨立 `LICENSE` 檔，MIT 授權宣告在 `SKILL.md` frontmatter 與 `README.md` 裡；作者資訊取自 `.claude-plugin/plugin.json`（`forrestchang`）。

**階段 A（評估）**：完整讀完這唯一一個技能的全文，並比對 3 個表面主題相近的既有技能全文：
- `agentic-dev-workflow/brainstorming`（Think Before Coding 的「先釐清假設」精神相近，但 brainstorming 是一套結構化、多步驟、產出 spec 文件並要求使用者核准的流程，karpathy-guidelines 只是一段隨時可查的行為守則，機制完全不同）
- `product-verification` 的 `test-driven-development` + `verification-before-completion`（Goal-Driven Execution 精神相近，但兩者是具體的紅綠重構鐵律與「宣稱完成前必須真的跑驗證指令」協議，karpathy-guidelines 只是一句「define success criteria」的提醒）
- `code-quality-review`（Simplicity First／Surgical Changes 精神相近，但 code-quality-review 是事後審查協議與靜態分析工具，karpathy-guidelines 是事前/當下的編碼守則）

結論：三邊都不構成「真重疊」（核心邏輯不同、無共用機制），依標準流程第 4 點，**不物理合併**，維持獨立檔案，只在目的地技能的 `SKILL.md` 裡加註跟這三者的關係說明。

**階段 B（分類與落點）**：套用五類分類法——判定為「偶爾需要」（不是核心常用，但情境明確：撰寫/審查/重構程式碼時可查）。依主題（而非來源）併入既有 18 分類中最相關的 `agentic-dev-workflow`（軟體開發生命週期總成），因為這 4 條準則橫跨「動手前想清楚」到「目標導向驗證」的整個開發生命週期，比單獨塞進 `code-quality-review` 或 `product-verification` 其中一邊更貼切。沒有另立第 19 個分類。

**階段 C（執行）**：
1. 命名衝突查核：`karpathy-guidelines` 資料夾名稱與 frontmatter `name:` 皆與本倉庫現有技能查重，無衝突。
2. 內部交叉引用：`SKILL.md` 本身不含指向其他檔案的相對路徑引用，搬移後無需修正。
3. 未搬入廠商自己的分類索引檔（`README.md` 等）——這些本來就只是廠商的安裝文件，非技能索引，直接略過不搬。
4. 授權歸屬：因為只併入單一目的地分類（不像 mattpocock-skills 分散到 9 個分類），理論上可以只放一份 `LICENSE`，但因為是併入既有資料夾而非獨立資料夾，比照 mattpocock-skills 的做法，改在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增一節記錄全文與出處，保持全站授權文件單一入口。
5. 全域必用資格查核：搜尋 `SKILL.md` 全文的 `MUST use`／`before any`／`ALWAYS use` 等字樣——`description` 寫的是「Use when writing, reviewing, or refactoring code」，屬於情境觸發用語，不是「必須在任何回應前使用」的宣告，不列入 `SKILL.md` 的「🔁 Universal」清單。

**階段 D（文件更新）**：`agentic-dev-workflow/SKILL.md`（新增 domain 列＋簡介段落註明來源）、`README.md`（該小節新增條目、子技能數 22→23、頂部總數 160→161、版權聲明段落）、根目錄 `SKILL.md`（Quick lookup 摘要調整、Full skill list 子技能數、稽核區塊新增 `THIRD-PARTY IMPORT` 段落）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增一節）。`TRIGGER-MAP.md` 同步新增觸發範例，見該檔案。

**額外備註（非標準流程項目，但值得記錄）**：這 4 條準則跟 Claude Code 系統層級提示本身既有的行為規範（例如「不引入超出需求的抽象」「預設不寫註解」「宣稱完成前要跑驗證」）高度重疊——這不影響是否要收錄這個技能（使用者明確要求安裝），但代表這個技能的邊際效益主要在於「把已隱含的規範明文化、方便查閱／分享給其他工具（Cursor 等沒有這層系統提示的環境）」，而不是引入全新規則。

**本機安裝**：確認 `~/.claude/skills/agentic-dev-workflow`（Windows：`C:\Users\user\.claude\skills\agentic-dev-workflow`）是本倉庫同名資料夾的完整複製（非 symlink），修改完倉庫版本後，把整個資料夾重新複製過去覆蓋，讓全域安裝同步含有 `karpathy-guidelines`。

**最終結果**：18 個頂層技能維持不變，`agentic-dev-workflow` 子技能數 22→23，全倉庫子技能總數 160→161。

## 2026-08-01：匯入第三方倉庫 `awesome-llm-apps` 的 `agent_skills/` 資料夾（Shubham Saboo / Matt Van Horn，Apache-2.0）

使用者提供來源：`https://github.com/Shubhamsaboo/awesome-llm-apps.git`，要求（1）新增這個 skill 到專案中、（2）評估合併、（3）重新安裝到本機。依標準流程（階段 A-D）執行。

**內容**：clone 後發現這是一個以「LLM 應用範例集」為主體的大型倉庫（`advanced_ai_agents/`、`rag_tutorials/`、`starter_ai_agents/` 等，數百個不相關的範例 app），**不是**一個單一技能。真正符合 `SKILL.md` 格式的技能，只在 `agent_skills/` 子資料夾裡，共 5 個：`advisor-orchestrator-worker`、`commit-archaeologist`、`project-graveyard`、`scope-creep-detector`、`thinking-out-loud`。同資料夾下另有 `evals/`（每個技能的測試案例，未匯入）與 `self-improving-agent-skills/`（Next.js+Python 的完整 demo 網頁 app，不是技能，未匯入）。倉庫整體採 Apache-2.0 授權（根目錄 `LICENSE`），各技能 `SKILL.md` frontmatter 的 `metadata.author` 分別標註實際作者（Shubham Saboo 或 Matt Van Horn）。

因為使用者訊息只給了倉庫網址、沒有指定要哪個技能，先向使用者說明「這其實是 5 個技能＋大量不相關範例」，並逐一列出 5 個技能的用途讓使用者確認要哪些。

**階段 A（評估）**：完整讀完 5 個技能的全文（含 frontmatter、bundled `scripts/`、`references/`）：
- `advisor-orchestrator-worker`：三層模型團隊編排（advisor 審計畫、worker 平行執行），依賴外部 CLI（`agy`/`claude`）與 API key、大量 bash。判定與此環境**內建的多代理 `Workflow` 工具**功能重疊，建議不匯入。使用者確認同意排除。
- `commit-archaeologist`：純本地 Python script，走 git 歷史重建「這段程式碼為什麼存在」。
- `project-graveyard`：純本地 Python script，掃描機器上的廢棄側專案並解剖死因。
- `scope-creep-detector`：純本地 Python script，比對 git diff 與宣稱意圖，抓範圍蔓延。
- `thinking-out-loud`：處理雜亂語音輸入的 echo 確認機制，無 script，純 prompt 流程。

比對表面主題相近的既有技能全文（委派 Explore agent 執行，讀取完整內容而非只看描述）：
- `thinking-out-loud` vs `agentic-dev-workflow/brainstorming`：`brainstorming` 的 checklist 假設輸入已經「可提問」（從"Explore project context"、"Ask clarifying questions"開始），完全沒有處理雜亂/語音輸入的階段；`thinking-out-loud` 是輸入前的「聽懂了什麼」稽核機制，兩者機制不同、無共用邏輯。結論：不合併，互相加交叉引用，`thinking-out-loud` 產出的核准摘要若涉及功能設計則銜接到 `brainstorming`。
- `scope-creep-detector` vs `code-quality-review/receiving-code-review` + `code-review-expert`：`receiving-code-review` 談的是「收到意見後怎麼回應」的態度協議，`code-review-expert` 是 SOLID/安全性審查，`scope-creep-detector` 明確自稱「pre-PR 範圍分流，不是完整審查（正確性/安全性/測試品質故意排除在外）」——三邊軸線完全不同，皆無真重疊。結論：三個都保留，互相加交叉引用。

**階段 B（分類與落點）**：4 個保留技能都屬於「偶爾需要」（情境明確：git 歷史調查、廢棄專案盤點、PR 範圍檢查、雜亂輸入處理）。依主題（非來源）分散融入 4 個既有頂層分類，未另立新分類：
- `commit-archaeologist` → `incident-runbooks`（跟 `systematic-debugging` 同屬「動手前先系統性調查」模式）
- `project-graveyard` → `business-automation`（屬於專案優先順序/該不該繼續的規劃決策）
- `scope-creep-detector` → `code-quality-review`（跟既有 code review 工具同主題、互補）
- `thinking-out-loud` → `agentic-dev-workflow`（自然銜接既有的 `brainstorming` 流程）

**階段 C（執行）**：
1. 命名衝突查核：4 個資料夾名稱與 frontmatter `name:` 皆與本倉庫現有技能全文查重，無衝突。
2. 內部交叉引用：各技能的 `SKILL.md` 只引用自己資料夾內的 `references/*.md`／`scripts/*.py`，搬移後路徑仍相對於自身資料夾，全部正常解析，無需修正。
3. 各技能自帶的 `README.md`（來源倉庫自己的行銷文案、`npx skills add` 安裝指令、外部託管 demo GIF）全數未搬入——比照本倉庫既有慣例，`SKILL.md` 是唯一索引。
4. 授權歸屬：4 個技能分散到 4 個不同頂層分類（非單一獨立資料夾），比照 mattpocock-skills／andrej-karpathy-skills 的做法，在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增一節記錄 Apache-2.0 全文、出處與逐檔歸屬（含個別作者）。
5. 全域必用資格查核：4 個技能的 `description` 都沒有「MUST use before any response」這類宣告，均為情境觸發（雜亂輸入、PR 前、廢棄專案提問、動手改動前的歷史提問），未列入 `SKILL.md` 的「🔁 Universal」清單。

**階段 D（文件更新）**：`incident-runbooks/SKILL.md`／`business-automation/SKILL.md`／`code-quality-review/SKILL.md`／`agentic-dev-workflow/SKILL.md`（新增 domain 列＋交叉引用）、`README.md`（4 個小節新增條目與子技能數：`incident-runbooks` 3→4、`business-automation` 4→5、`code-quality-review` 12→13、`agentic-dev-workflow` 23→24；頂部總數 161→165；版權聲明段落）、根目錄 `SKILL.md`（Full skill list 子技能數、稽核區塊新增 `THIRD-PARTY IMPORT` 段落）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增一節）。`TRIGGER-MAP.md` 同步新增觸發範例。

**本機安裝**：把修改後的 `incident-runbooks`、`business-automation`、`code-quality-review`、`agentic-dev-workflow` 四個資料夾整份複製覆蓋到 `C:\Users\user\.claude\skills\` 對應同名資料夾，讓全域安裝同步含有這 4 個新子技能。

**最終結果**：18 個頂層技能維持不變，`incident-runbooks` 3→4、`business-automation` 4→5、`code-quality-review` 12→13、`agentic-dev-workflow` 23→24，全倉庫子技能總數 161→165。`advisor-orchestrator-worker` 確認不匯入（與內建 `Workflow` 工具重疊）。
