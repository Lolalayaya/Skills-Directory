# Skills Directory 健檢報告

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
