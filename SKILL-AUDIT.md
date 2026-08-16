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

---

## 2026-08-02：匯入第三方技能 `claude-skill-ip-guard`（Mugdha Vairagade，Apache-2.0）

使用者提供來源：`https://github.com/mugdhav/claude-skill-ip-guard.git`，要求（1）新增這個 skill 到專案中、（2）評估合併、（3）重新安裝到本機。依標準流程（階段 A-D）執行。

**內容**：clone 後確認這是單一技能的獨立倉庫，只有一個技能 `ip-guard/SKILL.md`，附 `references/license-compatibility.md`（12+ 種授權相容矩陣）、`references/dependency-security.md`（掃描結果判讀、修復劇本、`.pth` 持久化偵測）、`scripts/license_audit.sh`（呼叫 license-checker/pip-licenses/cargo-license/go-licenses）、`scripts/dependency_security_scan.sh`（解析遞移相依樹並對照 OSV 資料庫與隔離套件狀態）。倉庫根目錄另有 `README.md`／`CHANGELOG.md`／`CONTRIBUTING.md`／`LICENSE`（Apache-2.0）／`user-reports/`（兩份使用者回饋範例），皆為廠商自己的行銷/流程文件，非技能內容本身。

**技能做什麼**：三階段 IP/授權合規防護——(1) 產生程式碼/內容前先確立專案授權目標、列出計畫使用的相依套件並做授權相容性檢查、解析完整遞移相依樹並對照 OSV 弱點資料庫與套件隔離狀態（❌ 發現會阻擋繼續生成）；(2) 生成過程中即時標記 GPL/AGPL 不相容、超過 10 行的逐字重製、疑似專利演算法、來源不明的資產；(3) 每個產出的檔案/文件/UI 元件都附加一段 provenance block（記錄用了哪些相依套件、授權相容性、掃描結果、需要人工複查的項目）。另有 Fast Mode（"fast mode"/"prototype" 等關鍵字觸發）跳過階段一、二的檢查，只留精簡版 provenance block。

**階段 A（評估）**：完整讀完 `ip-guard/SKILL.md`、兩份 `references/*.md`、兩支 `scripts/*.sh`（逐行確認腳本只呼叫標準弱點/授權掃描工具如 pip-audit、npm audit、cargo-audit、license-checker 等，掃描對象限於目前專案自己的 manifest/lockfile，無外洩、無破壞性操作）。比對主題相近的既有技能全文：
- vs `code-quality-review/code-security`：後者是一般安全編碼守則（注入、驗證、檔案操作、加密、基礎設施設定），完全沒有授權/IP 內容，無重疊。
- vs `code-quality-review/llm-security` 的 supply-chain 章節：該章節談的是 **LLM/模型供應鏈**（未驗證的模型下載、惡意 pickle 檔、LoRA adapter），不是一般 npm/pip/cargo 套件的授權或遞移弱點掃描，軸線不同，無重疊。

結論：無真重疊，`ip-guard` 保留為獨立子技能，三邊互相加交叉引用說明分工。

**階段 B（分類與落點）**：分類為「偶爾需要」（情境明確：要出貨的程式碼/內容、商業專案、開源釋出時才需要）。依主題併入既有的 `code-quality-review`（跟既有的程式碼審查/安全掃描工具同屬「出貨前把關」的範疇），未另立新分類。

**階段 C（執行）**：
1. 命名衝突查核：`ip-guard` 資料夾名稱與 frontmatter `name:` 與本倉庫現有技能全文查重，無衝突。
2. 內部交叉引用：`SKILL.md` 只引用自己資料夾內的 `references/license-compatibility.md`、`references/dependency-security.md`、`scripts/*.sh`，搬移後路徑仍相對於自身資料夾，全部正常解析，無需修正。
3. 廠商自帶的 `README.md`／`CHANGELOG.md`／`CONTRIBUTING.md`／`user-reports/` 全數未搬入——比照本倉庫既有慣例，`SKILL.md` 是唯一索引。
4. 授權歸屬：單一技能併入既有分類（非獨立頂層資料夾），比照 andrej-karpathy-skills 的做法，在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增一節記錄 Apache-2.0 全文與出處。
5. **全域必用資格查核（本次唯一需要使用者拍板的判斷）**：`ip-guard` 自己的 `description` 寫的是「Activates automatically whenever Claude is about to generate code... even if the user doesn't mention copyright」——語氣比現有 5 個「全域必用」條目都更廣（那 5 個只在觸碰輸入/驗證/DB/加密等**特定敏感面向**時觸發；這個讀起來像是「任何」程式碼/內容產出都要觸發）。因為列入全域必用會讓「之後所有專案的每一次程式碼產出」都多出授權宣告與 provenance block 的開銷，屬於影響範圍遠超過一般技能安裝的決策，因此依標準流程階段 C 第 9 點的精神，主動提出來讓使用者決定，而不是單方面判斷。

   使用者的決定：**不列入「全域必用」清單**；觸發粒度確認為 (a) 每次新增外部相依套件時觸發一次授權/安全檢查（對應技能原本的 Stage 1b/2 設計）、(b) 每完成一個檔案/artifact 時觸發一次 provenance block（對應原本的 Stage 3 設計）——不是每次回應/每個段落都觸發。這剛好符合 `ip-guard` 原作者自己的設計粒度，因此不需要改寫 `ip-guard/SKILL.md` 本身的邏輯，只需要：(i) 不把它加進 `SKILL.md` 的「🔁 Universal」表格、(ii) 在 `code-quality-review/SKILL.md` 與本檔案明確記錄這個決策與理由，避免未來的 session 誤以為它應該被升級為全域必用。

**階段 D（文件更新）**：`code-quality-review/SKILL.md`（新增 domain 列＋description 補充＋「How to use」新增一點）、`README.md`（`code-quality-review` 小節新增條目與子技能數 13→14、頂部版權聲明段落新增一條、Universal 表格前言補充本次判斷）、根目錄 `SKILL.md`（Quick lookup、Full skill list 子技能數 13→14、Universal 表格前言補充、稽核區塊新增 `THIRD-PARTY IMPORT` 段落、Total 165→166）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增一節）、`TRIGGER-MAP.md`（同步新增觸發範例，併入既有的 `code-quality-review` 小節）。

**本機安裝**：把更新後的 `code-quality-review` 資料夾整份複製覆蓋到 `C:\Users\user\.claude\skills\code-quality-review\`，讓全域安裝同步含有 `ip-guard` 這個新子技能。

**最終結果**：18 個頂層技能維持不變，`code-quality-review` 13→14，全倉庫子技能總數 165→166。`ip-guard` **未**列入「全域必用」清單（使用者明確決策），觸發粒度限定在「每次新增外部相依套件」與「每完成一個檔案/artifact」。

---

## 2026-08-05：匯入第三方技能包 `taste-skill`（Leonxlnx，MIT）

使用者提供來源：`https://github.com/Leonxlnx/taste-skill.git`，要求（1）新增這個 skill 到專案中、（2）評估合併、（3）重新安裝到本機——與 `hallmark`（見下一節）同一個請求一起處理。依標準流程（階段 A-D）執行。

**內容**：clone 後發現這不是單一技能，而是一個 Claude Code plugin（`.claude-plugin/marketplace.json` + `plugin.json`），底下 `skills/` 資料夾裝了 12 個獨立技能：`taste-skill`（現行版，frontmatter name `design-taste-frontend`）、`taste-skill-v1`（作者自己標註是「v2 重寫前的舊版，僅為需要精確舊行為的專案保留」）、`brandkit`（品牌識別板/Logo 系統的**圖片生成**技能）、`brutalist-skill`（Swiss 印刷+軍事終端融合的工業感 UI）、`gpt-tasteskill`（GSAP 動態工程+AIDA 頁面結構+Python 偽隨機排版變化）、`image-to-code-skill`（先生成設計圖再依圖寫程式碼的 Codex 工作流）、`imagegen-frontend-mobile`／`imagegen-frontend-web`（純圖片生成，不寫程式碼，分別對應手機 App 畫面與網頁分區塊參考圖）、`minimalist-skill`（暖色調極簡編輯風 UI）、`output-skill`（禁止 LLM 輸出截斷/佔位符的完整輸出紀律——注意這個**不是設計技能**）、`redesign-skill`（既有專案的稽核式升級改版）、`soft-skill`（「$150k 代理商級」視覺規格）、`stitch-skill`（產生給 Google Stitch 用的語義化 `DESIGN.md`，附帶一份 `DESIGN.md` 範例檔）。廠商根目錄的 `README.md`／`CHANGELOG.md`／`.github/copilot-instructions.md`／`research/`（一份跟任何單一技能無關的「LLM 為什麼會偷懶」研究文件）都是廠商自己的行銷/研究文件，非技能內容本身，未搬入。

**階段 A（評估）**：12 個技能的 `SKILL.md` 全部讀完整篇（不是只看 frontmatter description），逐一跟現有 `scaffolding-templating` 底下的設計類技能（`frontend-design`、`brand`、`design`、`ui-styling`、`ui-ux-pro-max`）以及彼此互相比對：
- 11 個是前端視覺設計「品味」規格，範圍各不相同（完整反樣板產線 vs. 具名美學風格 vs. 純圖片方向 vs. Codex 專用的圖片優先工作流 vs. Google Stitch 專用的 DESIGN.md 產生器），沒有任何一組是真重複——每個都有自己一套具體、且彼此大多互斥的規則（不同的禁用字體清單、不同的數值化「旋鈕」系統、不同的程式碼骨架、不同的輸出型態：程式碼 vs. 純圖片 vs. Markdown 規格檔）。全部保留為獨立檔案。
- 第 12 個 `output-skill`（frontmatter name `full-output-enforcement`）讀完後確認**根本不是設計技能**——它管的是「LLM 輸出不要截斷/不要用佔位符」的紀律（禁止 `// rest of code`、`// TODO`、「為了簡潔省略」之類的文字，並定義一套遇到 token 上限時的暫停/恢復格式）。跟 `product-verification/verification-before-completion` 比對：兩者是相鄰但不同的軸線——`verification-before-completion` 管「宣稱完成前有沒有真的驗證過」，`output-skill` 管「這次產出本身有沒有被悄悄截斷/省略」。沒有重複，改放進 `product-verification`。

**階段 B（分類與落點）**：11 個設計技能歸類為「偶爾需要」（情境明確：要出一個看起來不像 AI 樣板的前端頁面時），依主題併入既有的 `scaffolding-templating`（跟現有的 design/brand/frontend-design 同屬視覺設計範疇），未另立新分類；並在該技能自己的 `SKILL.md` 新增一個獨立的「Anti-AI-slop frontend taste systems」小節與挑選指南（見階段 D）。`output-skill` 歸類同樣是「偶爾需要」，依主題併入既有的 `product-verification`。

**階段 C（執行）**：
1. 命名衝突查核：12 個技能的資料夾名稱與 frontmatter `name:`（`design-taste-frontend`、`design-taste-frontend-v1`、`brandkit`、`industrial-brutalist-ui`、`gpt-taste`、`image-to-code`、`imagegen-frontend-mobile`、`imagegen-frontend-web`、`minimalist-ui`、`full-output-enforcement`、`redesign-existing-projects`、`high-end-visual-design`、`stitch-design-taste`）與本倉庫現有技能全文查重，無衝突。
2. 內部交叉引用：12 個技能都是自我完備的單一 `SKILL.md`（`stitch-skill` 額外帶一份同資料夾內的 `DESIGN.md`），彼此之間、對外都沒有相對路徑引用，搬移後無需修正任何連結。
3. 廠商自帶的 `README.md`／`CHANGELOG.md`／`.github/copilot-instructions.md`／`research/` 全數未搬入——比照本倉庫既有慣例，各技能自己的 `SKILL.md` 是唯一索引。
4. 授權歸屬：12 個技能分散併入 2 個既有分類（非獨立頂層資料夾），在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增一節記錄 MIT 全文與出處。
5. 全域必用資格查核：12 個技能的 description 都是明確場景觸發（「設計落地頁時」「要升級既有專案時」等），沒有一個帶「invoke before any response」語氣，均不列入「全域必用」清單。

**階段 D（文件更新）**：`scaffolding-templating/SKILL.md`（新增「Anti-AI-slop frontend taste systems」表格 11 列＋description 補充＋「How to use」新增第 7、8 點挑選指南）、`product-verification/SKILL.md`（新增 `output-skill` 一列＋description 補充＋「How to use」新增第 4 點）、`README.md`（兩個技能小節新增條目與子技能數、頂部版權聲明段落新增一條）、根目錄 `SKILL.md`（Quick lookup 兩處微調、Full skill list 子技能數 `scaffolding-templating` 16→28、`product-verification` 3→4、稽核區塊新增 `THIRD-PARTY IMPORT` 段落、Total 166→178，待下一節 `hallmark` 匯入後再 178→179）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增一節）、`TRIGGER-MAP.md`（同步新增觸發範例，併入既有的兩個小節）。

**本機安裝**：把更新後的 `scaffolding-templating`、`product-verification` 兩個資料夾整份複製覆蓋到 `C:\Users\user\.claude\skills\` 對應同名資料夾，讓全域安裝同步含有這 12 個新子技能。

**最終結果**：18 個頂層技能維持不變，`scaffolding-templating` 16→28，`product-verification` 3→4，全倉庫子技能總數 166→178。無一列入「全域必用」清單。

---

## 2026-08-05：匯入第三方技能 `hallmark`（Nutlope，MIT）

使用者提供來源：`https://github.com/Nutlope/hallmark.git`，與上一節的 `taste-skill` 同一個請求一起處理（新增／合併／重新安裝）。依標準流程（階段 A-D）執行。

**內容**：clone 後發現這是一個完整的 npm 套件（CLI + `site/` 底下的 demo 站、`docs/`、`package.json`、`ROADMAP.md`），但真正的 agent 技能內容只有 `skills/hallmark/SKILL.md` 加上它自己的 `references/` 樹（105 個檔案：`anti-patterns.md`、`color.md`、`typography.md`、`layout-and-space.md`、`motion.md`、`copy.md`、`macrostructures.md`（21 種具名頁面結構的索引）+ `macrostructures/` 逐一檔案、`component-cookbook.md`（50 種 nav/hero/section/CTA/testimonial/footer 元件原型）+ `components/` 逐一檔案、`genres/`（editorial／modern-minimal／atmospheric／playful）、`verbs/audit.md`＋`verbs/redesign.md`、`study.md`（URL/截圖 DNA 萃取）、`custom-theme.md`、`slop-test.md`（58 條出貨前檢查關卡）等）。`site/`、`docs/`、`package.json`、`ROADMAP.md`、根目錄 README 都是廠商自己的產品/demo/建置工具，非技能內容，未搬入——只搬入 `skills/hallmark/` 整份（含 `references/`，因為跟 `taste-skill` 那 12 個單檔技能不同，hallmark 自己的 SKILL.md 明確要求「依需要才載入對應的 references 檔案」，是設計上就要保留的目錄結構，不能只搬 SKILL.md）。

**階段 A（評估）**：完整讀完 `SKILL.md`（558 行）以及 `references/` 的代表性樣本（`macrostructures.md` 索引、`anti-patterns.md`、`genres/` 四份、`verbs/` 兩份）後再下判斷。跟同一天匯入的 `taste-skill` 以及既有的 `frontend-design` 比對：確實有主題重疊——`taste-skill` 跟 `hallmark` 都是「完整反樣板前端產線」，都有「先問清楚需求」的步驟、都有一套風格選擇機制、都有硬性排版規則、都有出貨前自我檢查——但機制上處處不同，不是真重複：`hallmark` 有強制的三問（受眾/用途/語氣）情境門，`taste-skill` 是一句話推斷的「design read」；`hallmark` 是具名的 20 主題目錄 + 客製 OKLCH 分支，`taste-skill` 是數值化的 3 旋鈕系統；`hallmark` 有自己的 `audit`／`redesign`／`study`（含 URL/截圖 DNA 萃取）動詞，`taste-skill` 沒有對應機制；`hallmark` 有跨 session 持久化的 `.hallmark/log.json` 多樣性紀錄，強制這次的巨觀結構/主題/nav/footer 都要跟前幾次不同，`taste-skill` 沒有對應機制。因此不合併進 `taste-skill` 或 `frontend-design`，保留為獨立檔案，改在 `scaffolding-templating/SKILL.md` 新增交叉引用/挑選指南（見階段 D）——依「主題重疊不等於該合併」的既有原則。

**階段 B（分類與落點）**：歸類為「偶爾需要」，依主題併入既有的 `scaffolding-templating`（跟 `taste-skill`、`frontend-design` 同屬視覺設計範疇），未另立新分類。

**階段 C（執行）**：
1. 命名衝突查核：`hallmark` 資料夾名稱與 frontmatter `name: hallmark` 與本倉庫現有技能全文查重，無衝突。
2. 內部交叉引用：搬入的 `references/` 樹內部全部是相對於自己資料夾的路徑（`references/<file>.md`、`references/components/<code>.md` 等），搬移後全部正常解析，無需修正。
3. 廠商自己的 `site/`／`docs/`／`package.json`／`ROADMAP.md`／根目錄 README 全數未搬入——比照本倉庫既有慣例，`SKILL.md` 是唯一索引。SKILL.md 內文裡的「Powered by Together AI」歸屬說明保留原樣（那是 hallmark 自己圖片生成分層用到的服務歸屬，不是本倉庫背書該服務）。
4. 授權歸屬：單一技能併入既有分類（非獨立頂層資料夾），在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增一節記錄 MIT 全文與出處。
5. 全域必用資格查核：`hallmark` 自己的 description 是「設計/稽核/改版/風格萃取時使用」的場景觸發，沒有「invoke before any response」語氣，不列入「全域必用」清單。

**階段 D（文件更新）**：`scaffolding-templating/SKILL.md`（「Anti-AI-slop frontend taste systems」表格新增 `hallmark` 一列）、`README.md`（`scaffolding-templating` 小節子技能數更新）、根目錄 `SKILL.md`（Full skill list `scaffolding-templating` 28（taste-skill 匯入後）已含 hallmark、稽核區塊新增 `THIRD-PARTY IMPORT` 段落、Total 178→179）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增一節）、`TRIGGER-MAP.md`（同步新增觸發範例）。

**本機安裝**：把更新後的 `scaffolding-templating` 資料夾整份複製覆蓋到 `C:\Users\user\.claude\skills\scaffolding-templating\`，讓全域安裝同步含有 `hallmark` 這個新子技能。

**最終結果**：18 個頂層技能維持不變，`scaffolding-templating` 27→28（含本節與上一節 taste-skill 的合計 16→28），全倉庫子技能總數 178→179。未列入「全域必用」清單。

---

## 2026-08-07：匯入第三方技能 `anysearch`（AnySearch Team，Apache-2.0）

使用者提供來源：`https://github.com/anysearch-ai/anysearch-skill.git`，要求（1）新增這個 skill 到專案中、（2）評估合併（要求所有文件都更新）、（3）重新安裝到本機。依標準流程（階段 A-D）執行。

**內容**：clone 後確認這是單一技能的獨立倉庫，只有一個技能 `SKILL.md`，附一套跨平台的多執行環境 CLI（`scripts/anysearch_cli.py`／`.js`／`.ps1`／`.sh`，外加 `scripts/generate.py` 與 `scripts/shared/constants.json`＋`doc_spec.md` 作為四份 CLI 的共用真實來源）、`runtime.conf.example`、`.env.example`。倉庫根目錄另有 `README.md`／`README_zh.md`／`SECURITY.md`／`LICENSE`（Apache-2.0）／`NOTICE`，皆為廠商自己的行銷/安裝/漏洞回報文件，非技能內容本身，比照 `claude-skill-ip-guard` 的先例未搬入（授權全文集中記錄在 `THIRD-PARTY-LICENSES.md`，不額外複製 `LICENSE` 檔案到資料夹內）。

**技能做什麼**：統一即時搜尋服務——(1) 一般網路搜尋；(2) 垂直領域搜尋（finance/academic/travel/health/code/legal/gaming/film/business/security/ip/energy/environment/agriculture/resource/social_media 共 16 個具名領域，透過 `get_sub_domains` 查出正確 `sub_domain` 與必填參數）；(3) `batch_search` 平行批次查詢；(4) `extract` 全頁內容擷取（輸出已是 Markdown）。單一 JSON-RPC 2.0 endpoint（`https://api.anysearch.com/mcp`），免安裝 MCP server，四種執行環境自動偵測（Python > Node.js > PowerShell/Bash），偵測結果寫入 `runtime.conf` 供之後快速呼叫。API Key 可選（匿名存取但限額較低），技能本身要求 agent 能在使用者提供真實 email 後自動呼叫註冊 API 取得金鑰，且**必須先取得使用者明確同意才能把金鑰寫入 `.env`**。

**階段 A（評估）**：完整讀完 `SKILL.md`，並逐行檢查全部 4 支 CLI 腳本（551＋486＋460＋622 行）：確認四者都只呼叫同一個 hardcode 的 endpoint `https://api.anysearch.com/mcp`，全文搜尋 `eval(`／`exec(`／`subprocess`／`os.system`／`child_process`／`Invoke-Expression`／`base64` 等可疑模式，無一命中（唯一一處字串命中是註解文字，非實際呼叫），確認沒有偷偷對外送資料或執行任意指令。跟主題最相近的既有子技能 `browser-automation/search`（Browserbase 的輕量 curl 搜尋 API）全文比對：`search` 只有單一 endpoint、不需 CLI、無垂直領域、無批次模式；`anysearch` 是完全不同的第三方服務，有自己的四執行環境 CLI、16 個具名垂直領域結構化搜尋、平行批次查詢、獨立的 `extract` 命令——機制上處處不同，非真重複。

**階段 B（分類與落點）**：歸類為「偶爾需要」（情境明確：需要即時資料查證、跨領域結構化搜尋、或批次/平行查詢時才用）。依主題併入既有的 `browser-automation`（跟既有的 `search` 同屬「不開瀏覽器的搜尋」範疇），未另立新分類，兩邊互相加交叉引用/選用指南（見 `browser-automation/SKILL.md` 新增的「Note on `search` vs `anysearch`」）。

**階段 C（執行）**：
1. 命名衝突查核：`anysearch` 資料夾名稱與 frontmatter `name: anysearch` 與本倉庫現有技能全文查重，無衝突。
2. 內部交叉引用：`SKILL.md` 只引用自己資料夾內的 `<skill_dir>/scripts/*`、`<skill_dir>/runtime.conf`、`<skill_dir>/.env`，搬移後路徑仍相對於自身資料夾，全部正常解析，無需修正。
3. 廠商自帶的 `README.md`／`README_zh.md`／`SECURITY.md`／`LICENSE`／`NOTICE` 全數未搬入——比照本倉庫既有慣例，`SKILL.md` 是唯一索引。
4. 授權歸屬：單一技能併入既有分類（非獨立頂層資料夾），比照 `claude-skill-ip-guard` 的做法，在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增一節記錄 Apache-2.0 全文與出處。
5. 全域必用資格查核：`anysearch` 自己的 description 是「需要資訊檢索/事實查證/網頁瀏覽/垂直領域查詢/多意圖平行查詢時」的場景觸發語氣，沒有「invoke before any response」語氣，不列入「全域必用」清單。
6. 憑證/對外連線風險備註（非落點阻礙，但記錄供未來 session 參考）：這個技能會把搜尋關鍵字、擷取的 URL、以及（若設定）API Key 送到第三方 `https://api.anysearch.com`；技能本身要求 agent 在取得使用者真實 email 後可自動呼叫註冊 API，並在收到新金鑰後**必須先徵得使用者明確同意才能寫入 `.env`**——這跟本倉庫其他對外連線技能（如 `search`）既有的「visible before persist」原則一致，未修改技能本身邏輯。

**階段 D（文件更新）**：`browser-automation/SKILL.md`（description 補充＋新增 domain 列＋「How to pick a domain」新增一點＋新增「Note on `search` vs `anysearch`」小節）、`README.md`（`browser-automation` 小節子技能數 15→16、新增條目、頂部版權聲明段落新增一條、簡介段落更新匯入鏈）、根目錄 `SKILL.md`（Quick lookup、Full skill list 子技能數 15→16、Total 179→180、稽核區塊 browser-automation 列表新增 `anysearch`、新增 `THIRD-PARTY IMPORT` 段落）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增一節）、`TRIGGER-MAP.md`（同步新增觸發範例，併入既有的「瀏覽器自動化與研究」小節）、`skills-search.html`（`DATA` 陣列同步新增一列）。

**本機安裝**：把更新後的 `browser-automation` 資料夾整份複製覆蓋到 `C:\Users\user\.claude\skills\browser-automation\`，讓全域安裝同步含有 `anysearch` 這個新子技能。

**最終結果**：18 個頂層技能維持不變，`browser-automation` 15→16，全倉庫子技能總數 179→180。`anysearch` 未列入「全域必用」清單。使用者若要實際使用這個技能，仍需自行決定是否註冊 API Key（技能本身支援匿名存取，較低限額）。

---

## 2026-08-09：匯入第三方技能包 `emilkowalski/skills`（Emil Kowalski，MIT）

使用者提供來源：`https://github.com/emilkowalski/skills.git`，要求（1）新增這個 skill 到專案中、（2）評估合併（要求所有文件都更新）、（3）重新安裝到本機。依標準流程（階段 A-D）執行。

**內容**：clone 後確認這是一個技能包，`skills/` 底下有 9 個技能：`emil-design-eng`（674 行，主要技能，Emil Kowalski 整體審美/打磨哲學）、`animate`（+`RECIPES.md`，從零建構動畫）、`animation-vocabulary`（動畫效果反查詞彙表）、`apple-design`（Apple WWDC 設計/流體動作原則）、`find-animation-opportunities`（唯讀，掃描 UI 找出值得加動畫的地方，並明確列出不該加的）、`improve-animations`（+`AUDIT.md`+`PLAN-TEMPLATE.md`，唯讀，對整個 codebase 做動畫稽核並產生執行計畫）、`pick-ui-library`（依任務挑選推薦的前端函式庫）、`prototype`（+`PICKER.md`，建構同一個 UI 元件的多個版本，用視覺選擇器即時比較）、`review-animations`（+`STANDARDS.md`，嚴格審查動畫/動作程式碼）。倉庫根目錄的 `README.md`／`LICENSE`（MIT）為廠商自己的行銷/安裝/授權文件，非技能內容，未搬入（授權全文集中記錄在 `THIRD-PARTY-LICENSES.md`）。全部 9 個技能都是純 Markdown（`SKILL.md` + 附帶的參考文件），沒有任何 `scripts/`，因此不需要程式碼執行風險審查。

**技能做什麼**：一套完整的「介面動作工程」技能群——不是視覺語言（顏色/排版/字體/具名美學），而是動作機制本身：正確的 easing curve/duration/spring 設定值、手勢速度交接與慣性投射公式（源自 Apple WWDC *Designing Fluid Interfaces*）、可中斷性、GPU-only 屬性、無障礙（reduced-motion）。四個技能構成一條唸法互補的 pipeline：`find-animation-opportunities`（找機會）→ `improve-animations plan`（規劃修法）→ 任意 executor 執行 → `review-animations`（嚴格審查，預設打回，核准需靠證據）。另外兩個是同一個包裡的相鄰 UI 決策工具：`pick-ui-library`（不是函式庫 API 參考，是「該用哪個函式庫」的品味化推薦清單）與 `prototype`（多版本 UI 並排比較，非本倉庫既有 `prototype` 的「單一次性驗證」邏輯）。

**階段 A（評估）**：完整讀完全部 9 份 `SKILL.md`（合計約 1840 行）以及代表性參考檔案（`PICKER.md` 全文，確認只是自包含的 HTML/CSS/JS harness，沒有對外連線或可疑程式碼）。比對主題相近的既有技能全文：
- vs `scaffolding-templating` 的「Anti-AI-slop frontend taste systems」整組（`taste-skill`、`hallmark` 等）與 `frontend-design`：那組談的是視覺語言，這個包談的是動作機制——`hallmark` 自己的 `references/motion.md`（109 行）雖然也有 easing/duration 的概念，但只是它龐大 pipeline 裡的一個小分支，且具體數值不同（`cubic-bezier(0.16,1,0.3,1)` vs 本包的 `cubic-bezier(0.23,1,0.32,1)`）——各自獨立撰寫，非真重複，不合併，兩邊互相加交叉引用。
- vs `code-quality-review`（`code-review-expert`、`code-review`、`receiving-code-review`、`scope-creep-detector`）：軸線完全不同——一般程式碼正確性/SOLID/安全/範疇控管，不是動畫手感，無重疊。
- vs `library-api-reference`（`docx`／`xlsx`／`pptx`／`pdf`／`mcp-builder`／`vercel-*`）：那些是特定函式庫/檔案格式的**用法**參考；`pick-ui-library` 是「該選哪個函式庫」的**決策**工具，沒有任何 API 用法文件，軸線不同，且來自同一個包，改併入 `scaffolding-templating`（跟其他設計決策型技能同類）而非 `library-api-reference`。

**命名衝突查核與處理**：來源倉庫的 `prototype`（資料夾名稱與 frontmatter `name: prototype`）跟本倉庫既有的 `agentic-dev-workflow/references/prototype`（2026-07-31 從 mattpocock-skills 匯入）撞名。兩邊全文讀完比對：既有的 `prototype` 是通用的「一次性驗證程式碼」紀律——單一產物、單一設計問題（state/logic 或 UI 二選一），驗證完就存進分支後丟棄；新匯入的 `prototype` 範圍更窄但機制更完整——永遠是 UI，永遠是**多個**（3–5 個）方向真正不同的版本，放在同一個具體規格（`PICKER.md`：鍵盤導覽、URL 參數持久化、重播鍵）的視覺選擇器背後即時比較，選定後才整合進正式程式碼。兩邊都有獨立深度，非真重複，保留為兩個獨立檔案，不合併。把新匯入的一份改名為 `prototype-variants`（資料夾名稱與 frontmatter `name:` 都改），解決撞名——依標準流程階段 C 第 5 點處理。並在三處加上交叉引用：`agentic-dev-workflow/references/prototype/SKILL.md` 自己的 description、`agentic-dev-workflow/SKILL.md` 的 domain 表格、`scaffolding-templating/SKILL.md` 新增的 domain 表格條目。

**階段 B（分類與落點）**：歸類為「偶爾需要」（情境明確：出現動畫/動作/UI 函式庫選擇/多版本比較需求時才用）。全部 9 個依主題併入既有的 `scaffolding-templating`（設計/視覺樣板叢集），新增一個獨立的「Animation, motion & UI-decision tools」表格區塊，未另立新分類。

**階段 C（執行）**：
1. 命名衝突查核：`emil-design-eng`、`animate`、`animation-vocabulary`、`apple-design`、`find-animation-opportunities`、`improve-animations`、`pick-ui-library`、`review-animations` 八個對資料夾名稱與 frontmatter `name:` 全文查重，均無衝突；第 9 個 `prototype` 撞名，處理見上。
2. 內部交叉引用：`SKILL.md` → `RECIPES.md`／`AUDIT.md`／`PLAN-TEMPLATE.md`／`STANDARDS.md`／`PICKER.md` 全部是相對於自己資料夾的路徑，搬移後全部正常解析，無需修正。
3. 廠商自帶的 `README.md`／`LICENSE` 全數未搬入——比照本倉庫既有慣例，`SKILL.md` 是唯一索引，授權全文改記錄在 `THIRD-PARTY-LICENSES.md`。
4. 授權歸屬：技能包併入既有分類（非獨立頂層資料夾），在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增一節記錄 MIT 全文與出處。
5. 全域必用資格查核：9 個技能的 description 都是「明確的動畫/函式庫選擇/多版本比較請求」場景觸發語氣，沒有「invoke before any response」語氣，不列入「全域必用」清單。其中 `review-animations`／`pick-ui-library` 兩個自帶 `disable-model-invocation: true`（廠商自己的設計：只在明確呼叫時執行），原樣保留，未覆寫。

**階段 D（文件更新）**：`scaffolding-templating/SKILL.md`（description 補充＋新增「Animation, motion & UI-decision tools」表格區塊與挑選指南＋「How to use this skill」新增第 9 點）、`agentic-dev-workflow/references/prototype/SKILL.md`（description 補充交叉引用）、`agentic-dev-workflow/SKILL.md`（domain 表格新增一行交叉引用）、根目錄 `SKILL.md`（Quick lookup、Full skill list `scaffolding-templating` 28→37、Total 180→189、稽核區塊 scaffolding-templating 列表新增 9 個技能、新增 `THIRD-PARTY IMPORT` 段落）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增一節）、`README.md`（簡介段落、版權聲明、`scaffolding-templating` 小節）、`TRIGGER-MAP.md`（同步新增觸發範例，併入既有的內容/設計小節）、`skills-search.html`（`DATA` 陣列同步新增）。

**本機安裝**：把更新後的 `scaffolding-templating` 與 `agentic-dev-workflow` 資料夾整份複製覆蓋到 `C:\Users\user\.claude\skills\scaffolding-templating\` 與 `C:\Users\user\.claude\skills\agentic-dev-workflow\`，讓全域安裝同步含有這 9 個新子技能與 `prototype` 的交叉引用更新。

**最終結果**：18 個頂層技能維持不變，`scaffolding-templating` 28→37，全倉庫子技能總數 180→189。全部 9 個技能未列入「全域必用」清單。`prototype`（原名衝突）已改名為 `prototype-variants`，與既有的 `agentic-dev-workflow/prototype` 並存，兩邊互相加了交叉引用。

---

## 2026-08-16：一次匯入 5 個來源（4 個接受、1 個拒絕）

使用者一次提供 5 個來源，要求（1）新增到專案中、（2）評估合併（要求所有文件都更新）、（3）重新安裝到本機：
`kevintsai1202/Humanizer-zh-TW`、`firecrawl/firecrawl`、`Master-cai/Research-Paper-Writing-Skills`、`ultimatile/arxiv-skills`、`guillaumemeyer/watermarks-remover`。依標準流程（階段 A-D）逐一評估，其中一個拒絕收錄。

### `firecrawl/firecrawl` → 實際匯入 `firecrawl/cli` + `firecrawl/skills`（Firecrawl 官方，ISC）

Clone 使用者給的 `firecrawl.git` 後發現這是 Firecrawl 公司自己的完整產品原始碼（Node/Rust monorepo：`apps/api/`、`native/` 等），全倉庫沒有任何 `SKILL.md`。倉庫內有兩份指標性 README（`firecrawl-cli-skills/README.md`、`firecrawl-skills/README.md`）指向真正的技能來源：`github.com/firecrawl/skills`（應用程式整合技能）與 `github.com/firecrawl/cli`（內建於 CLI 自己倉庫裡的即時網頁工具技能）。判斷不應該從使用者連結的「非技能」monorepo 硬生出技能內容，改為直接 clone 這兩個官方倉庫並完整評估。

**內容**：`firecrawl/skills` 有 7 個技能——`firecrawl-build`（總覽）、`firecrawl-build-scrape`、`firecrawl-build-search`、`firecrawl-build-interact`、`firecrawl-build-onboarding`（皆為「把 Firecrawl 接進應用程式原始碼」的整合指引，附語言別 SDK 用法連結）、`firecrawl-developer-index`（從 GitHub issue/PR/README/文件回答開發問題，回傳實際命中段落）、`firecrawl-research-index`（Firecrawl 自己的論文摘要語料庫語意搜尋，約 4300 萬筆，以 PubMed/bioRxiv/medRxiv 為主+arXiv）。`firecrawl/cli` 有 10 個技能——`firecrawl-cli`（總覽，frontmatter `name: firecrawl`，維持原樣、與現有技能全文查無衝突）、`firecrawl-scrape`、`firecrawl-search`、`firecrawl-map`、`firecrawl-crawl`、`firecrawl-monitor`、`firecrawl-interact`、`firecrawl-download`、`firecrawl-agent`、`firecrawl-parse`（後兩者的 `rules/install.md`＋`rules/security.md` 各自帶 frontmatter，作為附屬參考檔保留，不升級為獨立頂層條目）。全部 17 份 `SKILL.md` 完整讀完。兩個倉庫根目錄的 `README.md`／`CLAUDE.md`／`AGENTS.md`／`CONTRIBUTING.md`／marketplace/plugin 清單／`.mcp.json` 皆為安裝/行銷/外掛腳手架，非技能內容，未搬入。

**落點依「工作性質」而非「來源倉庫」拆分**：`firecrawl-build*` 5 個技能是「把 Firecrawl 寫進應用程式自己的原始碼」——併入 `library-api-reference`，跟既有的「如何正確呼叫這個 API/函式庫」系列同類。`firecrawl/cli` 的 10 個技能加上 2 個索引技能，是「這次 session 裡的即時、一次性網頁工作」——併入 `browser-automation`，跟既有的 `browser`／`fetch`／`search`／`anysearch` 同類。這正好對應原始專案自己的說法（`firecrawl-build` 自己的 SKILL.md：「這是給『把網頁資料能力建進應用程式』用的，不是『現在把 Firecrawl 當終端機工具用』」）。

**全文比對既有技能**：
- vs `browser-automation` 的 `search`＋`anysearch`：三個不同廠商都做搜尋。非真重複——Firecrawl 範圍最廣（多了 crawl/map/monitor/interact/parse/agent 結構化擷取/開發者索引/論文索引，另外兩個都沒有）。在 `browser-automation/SKILL.md` 新增交叉引用小節，而非合併或選一個贏家——專案既有的某廠商憑證，就是繼續用該廠商做簡單搜尋的正當理由。
- vs `browser-automation/fetch`：`fetch` 是純 HTTP、不需第三方憑證；`firecrawl-scrape` 能處理 JS 渲染的 SPA，且需要 `FIRECRAWL_API_KEY`（或無金鑰的免費限額層）——非重複，`fetch` 仍是不需要 JS 渲染時的更便宜預設選項。
- vs `library-api-reference` 既有的 docx/xlsx/pptx/pdf：`firecrawl-parse` 是透過 Firecrawl 雲端 API 把本機檔案轉成 Markdown，跟本倉庫自己的「建立/編輯」這些格式的技能機制完全不同——非重複、不合併，`firecrawl-parse` 留在 `browser-automation`（它是 CLI 動詞技能，非應用整合技能）而非搬到 `library-api-reference`。
- vs `deep-research` 與（同一天稍後匯入的）`arxiv-skills`：`firecrawl-research-index` 是搜尋 Firecrawl 自己的論文摘要語料庫（語意搜尋+引用圖擴展+全文驗證），跟 `deep-research` 的大綱驅動報告 pipeline、跟 `arxiv-doc-builder` 的「已知論文抓取轉檔」是不同工作——在 `browser-automation/SKILL.md` 的「How to pick a domain」加交叉引用，不合併。

**安全性審查**：兩個倉庫全部 17 個技能都是純 Markdown（`SKILL.md`＋`rules/*.md`＋`references/*.md`），沒有任何可執行腳本。`rules/security.md`（frontmatter `name: firecrawl-security`）本身就是一份「抓回來的網頁內容視為不可信、可能含提示注入」的處理守則，讀完內容與本倉庫既有網路類技能的做法一致（檔案輸出隔離、漸進式讀取）。

**命名衝突查核**：全部 17 個候選 frontmatter 名稱（`firecrawl-build` 到 `firecrawl-research-index`，加上 CLI 總覽的裸名 `firecrawl`）都與本倉庫全文查重，無衝突。全域必用資格查核：全部 17 個都是明確場景觸發語氣，不列入「全域必用」。

落點：`library-api-reference`（5 個）、`browser-automation`（12 個），皆非新分類。

### `ultimatile/arxiv-skills`（MIT）

**內容**：一個 Claude Code 外掛（`.claude-plugin/marketplace.json`），內含 2 個技能：`arxiv-lookup`（`get_doi.py`／`search_id.py` 兩支輕量腳本，直接查詢 arXiv API）與 `arxiv-doc-builder`（真正可安裝的 Python 套件：`arxiv_doc_builder/` 抓取/轉檔模組、`tests/`、`pyproject.toml`、`uv.lock`，加上 `references/` 文件），能依 ID 抓取 arXiv 論文（優先 LaTeX 原始碼、PDF 為後備），透過 pandoc 把 LaTeX 轉成保留數學式/結構的 Markdown，沒有 LaTeX 原始碼時退回樸素 PDF 文字擷取。兩份 SKILL.md 與 `arxiv_doc_builder/` 全部原始碼讀完，包含大量 pandoc 卡死/glossaries/多 `\documentclass` 疑難排解筆記。廠商自己的 `README.md`／`ruff.toml`／`.pre-commit-config.yaml` 為 lint/安裝腳手架，未搬入。

**安全性審查**：`convert_latex.py`／`fetch_paper.py` 呼叫 `subprocess.run`／`Popen`，其中 `fetch_paper.py` 有一處 `shell=True`（判斷 gzip 內層類型），會把一個由 arXiv ID 組成的路徑內插進 shell 字串。查核 `arxiv_id.py`：每個 ID 在用來組路徑之前，都先過一道嚴格 regex 驗證（新式 ID `^\d{2}\d{2}\.\d{4,5}(v\d+)?$`，舊式 ID 也是類似窄格式），代表不可能有任何 shell 特殊字元存活進內插字串——無指令注入風險。所有網路請求都只打 `arxiv.org`／`export.arxiv.org`。沒有其他可疑模式（`eval`、未驗證輸入的 `os.system`）。

**比對既有技能**：跟 `deep-research` 與（同一天匯入的）Firecrawl 的 `firecrawl-research-index` 比對：現有技能都不做「把一篇已知特定論文抓取並轉成實作參考用 Markdown」這件事——`deep-research` 是大綱驅動的多來源報告產出，`firecrawl-research-index` 是搜尋語料庫「找」論文。把工作性質（搜尋 vs. 抓取轉檔）講清楚後就沒有重疊，互相加交叉引用而非合併。

**落點**：併入既有的 `library-api-reference`（非新分類），歸類在既有的 docx/xlsx/pptx/pdf「把這個格式轉成能用的東西」同一群組，並對非 arXiv 的 PDF 加了指回 `pdf` 技能的交叉引用。命名無衝突（`arxiv-lookup`、`arxiv-doc-builder` 皆已全文查重）。全域必用查核：兩者皆為明確場景觸發，不列入。

### `Master-cai/Research-Paper-Writing-Skills`（MIT）

**內容**：單一技能 `research-paper-writing/SKILL.md`，附龐大的 `references/` 樹（Abstract/Introduction/Related Work/Method/Experiments/Conclusion/Paper Review 各章節指引、段落流暢度自我檢查、以及大量帶標註的範例論文段落 before/after）。另附 `agents/openai.yaml`——讀完內容，這是 OpenAI 平台 Agent Builder 的顯示中繼資料（display name、簡短描述、預設 prompt），不是給 Claude Code 用的 agent-facing 技能內容，比照本倉庫每次匯入對廠商平台腳手架的處理慣例，未搬入。根目錄 `README.md`／`README_zh.md` 同樣未搬入。

**比對既有技能**：跟 `internal-writing-comms/doc-coauthoring` 比對——`doc-coauthoring` 是通用的結構化文件共寫**流程**（脈絡轉移→草稿→修訂→對讀者驗證），適用任何提案/規格/決策文件；`research-paper-writing` 是學術論文專用，有固定的章節分類法（Abstract/Introduction/Method 等）、強制的「主張—證據」對齊檢查（對照實驗結果）、以及投稿前的五維度對抗式自我審查——非真重複，併入為同層級的姊妹技能，兩邊互相加交叉引用而非合併。

**落點**：併入既有的 `internal-writing-comms`（非新分類），路徑為 `references/research-paper-writing/SKILL.md`（含其 `references/` 樹，不含 `agents/`）。命名無衝突（`research-paper-writing` 已全文查重）。內部交叉引用皆為相對於自己資料夾的路徑，無需修正。全域必用查核：明確場景觸發（起草/修訂論文），不列入。

### `kevintsai1202/Humanizer-zh-TW`（MIT）

**內容**：單一技能，只有一份 `SKILL.md`（無附帶 references/scripts）。技能自己的中繼資料記錄了傳承脈絡：翻譯自 op7418/humanizer-zh 的正體中文分支，op7418 又翻譯自 blader/humanizer，並參考 hardikpandya/stop-slop。讀完全文：這是一份基於維基百科「Signs of AI writing」頁面（由 WikiProject AI Cleanup 維護）的文字編輯模式目錄——誇大意義的宣傳性措辭、模糊歸因、破折號過度使用、三段式法則、填充短語、諂媚語氣、通用積極結論等——附 before/after 改寫範例與 5 維度 50 分品質評分表，全文為正體中文。

**明確與「規避偵測」劃清界線**：這個技能自己聲明的任務是「寫作品質改善」（去除罐頭式/機械感的 LLM 文字模式、加入作者聲音）——它完全沒有聲稱能騙過 AI 內容偵測工具，也完全不觸碰浮水印、C2PA/來源中繼資料、或任何統計/加密標記。這個區別正是同一天另一個來源（`guillaumemeyer/watermarks-remover`，其自身宣稱的用途包含「anti-detect clean AI output」與剝除廠商來源標記）被拒絕收錄、而這個被接受的原因——詳見下方的拒絕收錄記錄。

**比對既有技能**：跟 `internal-writing-comms/writing-shape` 比對——`writing-shape` 是把素材塑形成文章結構、或對既有草稿逐段重整；這個技能是在完稿草稿上做句子/措辭層級的 LLM 痕跡去除——相鄰但不同層次的處理，非重複，兩邊互相加交叉引用。

**落點**：併入既有的 `internal-writing-comms`（非新分類），路徑為 `references/humanizer-zh-tw/SKILL.md`。命名無衝突（`humanizer-zh-tw` 資料夾名稱與 frontmatter `name:` 皆已全文查重）。全域必用查核：明確場景觸發（編輯/審閱文字），不列入。

### 拒絕收錄：`guillaumemeyer/watermarks-remover`

**內容**：單一技能 `skills/remove-ai-marks/SKILL.md`，背後由一個獨立 HTTP 服務（`service/`）支撐，掛載了 CtrlRegen、MarkDiffusion、MarkLLM、SynthID 評分器等重型後端，用途是剝除 AI 來源標記：不可見 Unicode 標記、統計式 token 取樣浮水印（透過 LLM 改寫/回譯/人性化重寫通過）、以及跨 PNG/JPEG/WebP/SVG/PDF/DOCX/ODT/HTML/MD 的 C2PA/EXIF/XMP/容器中繼資料。技能本身的 `SKILL.md` 與 `references/ethics.md` 全文讀完後才下判斷。

技能自己的觸發語氣就很明確：frontmatter description 裡把「anti-detect clean AI output」列為第一線用途之一，且它的工作流程**永遠會主動提議**一段改寫，目的就是要打敗統計式/浮水印式的 AI 內容偵測。`ethics.md` 確實把「學術造假」「規避法定透明度或平台揭露規則」列為「不適當」用途，並指示 agent 在這些情境下要「警告」（但不是拒絕），同時「仍然只執行使用者擁有內容的技術清理」——換句話說，這個免責聲明只是轉移責任，並沒有真的限制技術能力本身。C2PA Content Credentials 與 Google 的 SynthID 存在的目的就是內容來源/透明度機制；一個核心功能就是「從任意內容剝除這些標記」、且被設計成隨時可用的通用技能，本質上就是一個規避偵測的工具，不因為附加了一段倫理聲明就改變這個事實。

**決定**：依本環境「拒絕為惡意目的規避偵測」的既有原則不予收錄，因為免責聲明並不會改變這個工具實際做的事——它仍然被設計成可以對使用者交付的任何內容剝除 AI 來源標記，包括使用者有動機想把內容偽裝成人類撰寫的情況。這跟同一天收錄的 `Humanizer-zh-TW`（見上）不同——後者的工作是文字品質編輯，完全不涉及浮水印/中繼資料/來源標記。未合併進任何既有技能，未另立新分類，來源倉庫的任何內容都沒有搬入。使用者在同一輪對話中被直接告知拒絕的理由。

### 本機安裝

把更新後的 `library-api-reference`、`browser-automation`、`internal-writing-comms` 三個資料夾整份複製覆蓋到 `C:\Users\user\.claude\skills\` 對應目錄下，讓全域安裝同步含有這 21 個新子技能。

### 最終結果

18 個頂層技能維持不變。`library-api-reference` 9→16、`browser-automation` 16→28、`internal-writing-comms` 5→7，全倉庫子技能總數 189→210。5 個來源中 4 個收錄（21 個子技能）、1 個拒絕（`watermarks-remover`，理由見上）。全部新增技能未列入「全域必用」清單。

---

## 2026-08-16（續）：比對四個 UI/UX 相關來源並選擇性匯入

同一天稍晚，使用者一次提供 4 個第三方來源的本機 clone：`AccessLint/skills`、bencium.io 的 marketplace（`bencium-marketplace`）、`NousResearch/hermes-agent`、`vercel-labs/agent-skills`（後者已在 2026-08-09 匯入 `emilkowalski/skills` 時一併 clone 過，這次是拿來對照既有的 `vercel-react-view-transitions` 是否過時，而非新技能來源）。

**本次流程與前面每一節「整批匯入」不同**：這次不是「clone 一個來源、通篇評估、決定收不收」，而是使用者以三選一（AskUserQuestion 形式）框架詢問後，明確選擇「只安裝新內容＋補齊未重疊的落差，不要整批照搬」——也就是說，Stage A 的評估工作（哪些跟既有技能重複、哪些是真正的新內容）已經在前一輪對話完成，本節記錄的是依照該決策執行的 Stage B–D，而非重新評估要不要裝。

### Stage A（評估結論摘要，非本節重新做的評估）

四個來源逐一比對本倉庫既有技能全文後，分成「新內容，匯入」與「重疊/多餘，不匯入」兩組：

**判定為新內容，匯入（見下方各小節）**：
- `AccessLint/skills` 全部 5 個技能（WCAG 2.2 稽核/掃描/檢測/差異比對/修復管線）——本倉庫先前沒有任何無障礙（a11y）相關技能，非重疊。
- bencium.io 的 `typography`（排版正確性強制規則）與 `relationship-design`（agentic UX 關係設計）——兩者的具體機制（LLM 常犯的排版錯誤清單、記憶/信任演化為核心的 UX 策略）在既有的 `ui-ux-pro-max`／`brand`／`frontend-design` 裡都找不到對應內容。
- `NousResearch/hermes-agent` 的 `popular-web-designs`（54 個真實網站設計系統目錄）、`design-md`（Google 開放 `DESIGN.md` 規格的作者/驗證/匯出工具）、`baoyu-infographic`（21 版面×21 風格資訊圖產生器）——分別是具體真實站點目錄、正式規格檔案格式、資訊圖生成，本倉庫既有技能都沒有對應機制。

**判定為與既有技能重疊/多餘，不匯入**（逐一比對後的一行理由）：
- `bencium-controlled-ux-designer`／`bencium-innovative-ux-designer`／`bencium-impact-designer`（bencium 的 3 個「UI/UX 設計師」技能）：都是「避免通用 AI 美學、產出獨特前端介面」的同款包裝，跟既有的 `frontend-design`／`taste-skill`／`hallmark` 反樣板管線在同一個問題空間，未帶來既有管線沒有的機制，不匯入。
- `human-architect-mindset`：系統性架構思維／領域建模／問題拆解，跟既有 `agentic-dev-workflow` 的 `domain-modeling`／`brainstorming` 及 `code-quality-review` 的 `codebase-design` 重疊，不是設計/UI 技能，不匯入。
- `design-audit`：UI/UX 稽核並產出分階段改版計畫，跟既有 `hallmark` 的 `audit`/`redesign` 動詞與獨立的 `redesign-skill`（審計優先的既有專案升級路徑）重疊，不匯入。
- `bencium-aeo`：AI 搜尋引擎優化（Answer Engine Optimization）內容產生，屬於 `marketing` 分類既有的 `ai-seo` 範疇，不是設計/UI 技能，不匯入。
- `insurgent-campaign`：草根行銷戰役策略，屬於 `marketing` 分類既有的 `marketing-plan`／`marketing-ideas`／`co-marketing` 範疇，不是設計/UI 技能，不匯入。
- `negentropy-lens`：用熵/負熵透鏡評估系統與架構決策的決策支援框架，跟既有 `code-quality-review` 的 `codebase-design` 及 `agentic-dev-workflow` 的判斷型工具重疊，不是設計/UI 技能，不匯入。
- `renaissance-architecture`：軟體架構＋UI/UX 第一性原理思維，同時跟既有的架構決策工具（`codebase-design` 等）與反樣板設計叢集（"創造而非複述" 訴求與 `taste-skill`/`hallmark` 重疊）兩邊都重疊，不匯入。
- `claude-design`（hermes-agent）：一次性 HTML artifact（落地頁/簡報/原型）設計流程，跟既有的 `web-artifacts-builder`／`frontend-design` 重疊，不匯入。
- `p5js`（hermes-agent）：p5.js 生成藝術/著色器/互動/3D 草圖，跟既有的 `algorithmic-art`（同樣是 p5.js 生成藝術）直接重疊，不匯入。
- `sketch`（hermes-agent）：一次性 HTML mockup，產生 2-3 個版本供比較，跟既有的 `prototype-variants`（多版本 UI 在視覺選擇器背後即時比較）機制上幾乎一致，不匯入。

`vercel-labs/agent-skills` 這個來源沒有「匯入/不匯入」的問題——比對後發現它就是已安裝的 `vercel-react-view-transitions` 的同一個上游來源，只是版本較新，處理方式是同步落差（見下方「同日重新同步」小節），不是新增授權項目。

### Stage B（分類與落點）

6 個新增子技能全部判定為「偶爾需要」（情境明確：無障礙稽核、排版規則、agentic UX 設計、依真實網站風格建頁、正式 `DESIGN.md` 規格檔、資訊圖生成）。依主題（而非來源）全部併入既有的 `scaffolding-templating`（設計/視覺樣板叢集），未另立新分類——`AccessLint` 的 5 個技能落在新的「Accessibility auditing」表格區塊，bencium.io 的 2 個技能落在新的「Typography & agentic UX philosophy」表格區塊，hermes-agent 的 3 個技能落在新的「Design reference catalogs & spec generators」表格區塊。

### Stage C（執行）

1. **命名衝突查核**：
   - AccessLint 的 5 個 frontmatter 名稱（`accessibility-audit`／`accessibility-scan`／`accessibility-inspect`／`accessibility-diff`／`accessibility-fix`）與本倉庫全文查重，無衝突。
   - `typography`（bencium.io）：來源自己的 frontmatter 已經是 `name: ui-typography`（跟資料夾名稱 `typography` 不同），本倉庫全文查重 `typography`／`ui-typography` 兩種寫法皆無衝突——但為了讓資料夾名稱與 frontmatter `name:` 欄位保持一致（沿用 2026-08-09 `prototype-variants` 那次建立的慣例），資料夾統一命名為 `ui-typography`，而不是照搬來源的資料夾名稱 `typography`。
   - `relationship-design`：資料夾名稱與本倉庫查重無衝突；其 frontmatter `name:` 欄位是一個非慣用格式的字串（`Agentic UX Design - Relationship-Centric Interfaces`，含空格與大小寫），因為不構成實際衝突，依本倉庫「不擅自修正廠商格式」的慣例原樣保留，只在本節記錄這個觀察供未來留意。
   - `popular-web-designs`／`design-md`／`baoyu-infographic`：三者的資料夾名稱與 frontmatter `name:` 皆與本倉庫全文查重，無衝突。其中 `design-md` 特別檢查了跟已安裝的 `stitch-skill` 是否為同名——確認不是（`stitch-skill` 的 frontmatter `name:` 是 `stitch-design-taste`），只是概念上容易混淆（見下方 Stage D 的排歧義說明）。
2. **內部交叉引用驗證**：AccessLint 的 5 個 SKILL.md 都用 `../shared/methodology.md` 相對路徑指回同一個 `shared/` 資料夾，`accessibility-inspect` 另外指向自己的 `references/checkpoints.md`——複製整個 `skills/` 子樹（5 個技能資料夾＋`shared/` 皆為同層手足）之後，兩者都驗證存在且路徑正確。bencium.io 與 hermes-agent 的檔案/資料夾（`css-templates.md`／`html-entities.md`／`CHECKLIST.md`／`EXAMPLES.md`／`REFERENCE.md`／`templates/starter.md`／`templates/` 54 檔／`references/` 樹）全部是相對於自己資料夾的路徑，搬移後不需修正。
3. **未搬入廠商自己的索引/腳手架檔案**：AccessLint 的 `.claude-plugin/plugin.json`（讀取但未搬入，用於取得作者/版本資訊）、`README.md`／`CHANGELOG.md`／`docs/`／`benchmark/`；bencium.io 每個技能各自的 `.claude-plugin/plugin.json`；hermes-agent 的根目錄 `README.md`／`CLAUDE.md`／`AGENTS.md`。**例外**：AccessLint 的 `.mcp.json` 雖然也是安裝設定檔、沒有直接搬入資料夾，但因為它宣告的 MCP server（`accesslint`，透過 `npx -y @accesslint/mcp@latest`）是 `accessibility-audit`／`accessibility-fix` 實際運作所需的相依，屬於「操作上必要的資訊」而非單純廠商行銷文件，已在 `scaffolding-templating/SKILL.md` 新增的表格區塊裡明確記錄這個需求，而不是像一般廠商 README 一樣直接略過。hermes-agent 的 `baoyu-infographic/PORT_NOTES.md` 例外保留（不同於一般 README/CHANGELOG，這份記錄的是移植者自己對這個技能的調整決策，屬於技能內容的一部分）。
4. **授權歸屬**：3 個來源分散併入同一個既有分類（`scaffolding-templating`），比照多來源匯入的慣例，在根目錄 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md) 新增三節：AccessLint（MIT，作者 AccessLint／support@accesslint.com——來源倉庫本身沒有附帶明確著作權年份/持有人字串，用 `plugin.json`／`marketplace.json` 記載的作者身份代入標準 MIT 範本）、bencium.io（MIT，著作權行取自同一個 marketplace 裡 `eu-ai-act-reviewer` 技能自帶的 `LICENSE` 檔案——`typography`／`relationship-design` 兩個技能自己的資料夾都沒有個別附 `LICENSE`）、NousResearch/hermes-agent（MIT，Copyright (c) 2025 Nous Research，並在同一節內額外具名 credit `baoyu-infographic` 的原作者 宝玉/JimLiu 與 `popular-web-designs` 的資料來源 Teknium/VoltAgent，比照先前 Shubham Saboo／Matt Van Horn 那次「一批內多位作者」的記錄方式）。
5. **全域必用資格查核**：AccessLint 的 5 個、hermes-agent 的 3 個都是明確場景觸發語氣（「稽核我的網站無障礙」「這個變更有沒有破壞無障礙」「產生資訊圖」等），未列入「全域必用」清單。`relationship-design` 自己的 frontmatter 更進一步明講「ONLY use when specifically asked, not for general UI/UX tasks」，同樣不列入。**`ui-typography` 是本次唯一需要比照 `ip-guard` 先例、主動說明而非單方面判斷的案例**：它自己的 description 寫著「auto-apply every rule in this skill silently…even if the user doesn't mention typography…whenever generating UI output」——這句話的廣度已經超過 `SKILL.md`「🔁 Universal」表格裡現有任何一條（那 5 條都只在觸碰特定敏感面向時觸發，這句讀起來像是「任何會產出 UI 的回合」都要觸發）。比照 `ip-guard` 那次的決策邏輯，本次預設**不**把它加進 Universal 表格——因為升級成全域必用，會讓「這台機器上所有專案往後每一次 HTML/CSS/React 產出」都多一層排版規則檢查的開銷，是遠超過一般技能安裝的影響範圍決策。已在 `scaffolding-templating/SKILL.md` 的新表格區塊與根目錄 `SKILL.md` 的 Universal 表格前言都記錄了這個判斷與理由，若未來要調整為全域必用，應該重新確認這個理由而非直接改動。

### Stage D（文件更新）

`scaffolding-templating/SKILL.md`（description 補充、新增「Accessibility auditing」「Typography & agentic UX philosophy」「Design reference catalogs & spec generators」三個表格區塊、「How to use this skill」新增第 10、11 點）、`library-api-reference/SKILL.md`（`vercel-react-view-transitions` 那一列的描述補上 `router.push(href, { transitionTypes })` 與 shared-element readiness/prefetching，無新增授權項目）、根目錄 `SKILL.md`（description 210→220、Quick lookup、Full skill list `scaffolding-templating` 37→47、Total 210→220、Universal 表格前言新增 `ui-typography` 的說明、稽核區塊新增 3 個 `THIRD-PARTY IMPORT` 段落＋1 個「SAME-DAY RESYNC」段落）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（新增 3 節）、`README.md`（簡介段落、版權聲明、`scaffolding-templating` 小節）、`TRIGGER-MAP.md`（同步新增觸發範例，併入既有的內容/設計小節）、`skills-search.html`（`DATA` 陣列同步新增 10 筆）。

### 同日重新同步（非新匯入）：`vercel-react-view-transitions`

已安裝的 `library-api-reference/references/vercel-react-view-transitions/` 來自 2026-08-09 匯入的 `emilkowalski/skills` 那次一併帶入的 `vercel-labs/agent-skills` 來源（已在 `THIRD-PARTY-LICENSES.md` 記錄過授權）。本次逐檔比對同一個上游倉庫目前的 `skills/react-view-transitions/`，發現 `README.md`、`SKILL.md`、`references/nextjs.md` 三個檔案有落差（上游新增了 `router.push(href, { transitionTypes })` API 文件、一個「When Content Must Be Ready」的預先擷取/快取小節、以及 `SKILL.md` 裡的「Shared Element Readiness」小節），其餘 `AGENTS.md`／`metadata.json`／`references/css-recipes.md`／`references/implementation.md`／`references/patterns.md` 逐位元組相同，無需更動。已用上游版本覆蓋這 3 個落差檔案，並重新逐檔 diff 確認完全一致。**這不是新的授權項目**——`THIRD-PARTY-LICENSES.md` 不需要新增章節，只在本節記錄這是同一天的內容重新同步，而非新匯入。

### 最終結果

18 個頂層技能維持不變，`scaffolding-templating` 37→47，全倉庫子技能總數 210→220。4 個 clone 來源中：3 個（AccessLint、bencium.io、NousResearch/hermes-agent）貢獻新內容共 10 個子技能全部收錄；第 4 個（`vercel-labs/agent-skills`）確認只是既有 `vercel-react-view-transitions` 的同源更新，已同步落差，不算新匯入。bencium.io／hermes-agent 兩個來源裡另有 10 個技能（3 個 UX 設計師技能＋`human-architect-mindset`＋`design-audit`＋`bencium-aeo`＋`insurgent-campaign`＋`negentropy-lens`＋`renaissance-architecture`＋`claude-design`＋`p5js`＋`sketch`）因與既有技能重疊或超出設計範疇，確認不匯入。`ui-typography` 未列入「全域必用」清單（比照 `ip-guard` 先例的判斷，理由見上）。

## 2026-08-16（三）：使用者指定的 9 項精準抽取／整包安裝

同一天第三次處理同一批來源（`bencium-marketplace`、`hermes-agent`）。前一節（續）已經把兩個來源整體評估過一輪，結論是「10 個子技能匯入、10 個不匯入」。這一次不是重新評估，而是使用者親自看過其他 agent 做的詳細比對報告後，**明確指定 9 項非常精準的動作**——大多數不是「整包安裝」，而是「只抽這一個機制、折進某個既有檔案」。本節記錄這 9 項的執行結果，逐項寫清楚抽了什麼、捨棄了什麼、為什麼。

### 執行前提

- 來源本機 clone 路徑不變：`external_repos/bencium-marketplace`、`external_repos/hermes-agent`。
- 每一項抽取前都先讀來源檔案原文取得精確文字，不用記憶或猜測措辭。
- 每一個新資料夾／檔名，先對全倉庫 grep 查重，才建立。
- 折進既有檔案的每個片段都在該檔案裡留一句話的來源標註（技能名＋來源 repo＋授權），不寫大段引言方塊。

### 逐項紀錄

**1. `frontend-design` 新增「Surface-First」步驟（來源：hermes-agent `claude-design`）**
從 `claude-design/SKILL.md` 抽出「先講清楚這是哪一種介面，再動手設計」的機制——7 個具名 archetype（Monitor / Operate / Compare / Configure / Decide-Learn / Explore / Command-Inspect），以及「用一句話陳述是哪一種 surface，再設計」的規則。折進 `scaffolding-templating/references/design/frontend-design/SKILL.md`，位置在既有「Process」流程小節之前，作為新的前置步驟。`claude-design` 其餘內容（十分制 slop 診斷評分、hosted-tool 對應表、deck/prototype 細則）**不**安裝——這些跟既有 `web-artifacts-builder`／本檔案自己的內容重疊，前一節（續）已經評估過整包不匯入，這次只精準抽這一個機制。

**2. 整包安裝 `p5js`（來源：hermes-agent）**
完整複製 `SKILL.md` ＋ 完整 `references/`（10 個檔案：core-api、shapes-and-geometry、visual-effects、animation、typography、color-systems、webgl-and-3d、interaction、export-pipeline、troubleshooting）＋ `templates/viewer.html` ＋ `scripts/`（setup.sh、serve.sh、render.sh、export-frames.js，四個腳本都讀過全文，是標準 Puppeteer headless 擷取 + ffmpeg 編碼流程，沒有可疑的網路外連或混淆手法）。目標路徑：`scaffolding-templating/references/design/p5js/`，跟既有 `algorithmic-art` 平行放置。來源自己的 `README.md` 只是重複 `SKILL.md` 的表格內容，依慣例不搬入。前一節（續）評估過「`p5js` 跟既有 `algorithmic-art` 重疊，不匯入」——這次使用者重新檢視後改變主意，明確要求整包安裝，並在 `scaffolding-templating/SKILL.md` 新增雙向交叉引用釐清兩者差異：`algorithmic-art` 是窄一點的「哲學優先」p5.js 工具；`p5js` 是更廣的技巧庫（curl noise、boid flocking、L-system、圓形堆疊、Voronoi、reaction-diffusion、pixel sorting）加上真正能用的匯出管線（Puppeteer headless、ffmpeg MP4、SVG、CCapture.js）。

**3. 整包安裝 `sketch`（來源：hermes-agent）**
來源只有單一 `SKILL.md`，沒有 `references/`／`templates/` 子樹（已核對過來源目錄）。複製到 `scaffolding-templating/references/design/sketch/SKILL.md`。同樣是前一節（續）評估過「跟既有 `prototype-variants` 機制幾乎一致，不匯入」的項目，這次使用者要求整包安裝，並在 `scaffolding-templating/SKILL.md` 新增交叉引用區分兩者：`sketch` 是每個變體各自獨立資料夾＋各自 README（`sketches/NNN-stance-name/index.html` + `README.md`），最後用比較表呈現；`prototype-variants` 是多個變體共享同一個即時視覺選擇器，在同一個產物裡切換，不是分開的檔案。額外發現：`sketch` 自己的「Attribution」小節記載它改編自 GSD（Get Shit Done）專案的 `/gsd-sketch` 工作流程——MIT © 2025 Lex Christopherson（上游 repo 現已封存/無人維護）——因此 `THIRD-PARTY-LICENSES.md` 的 hermes-agent 段落同時具名credit hermes-agent 與 Lex Christopherson 兩位作者，比照先前 baoyu-infographic／popular-web-designs 的雙作者記錄模式。

**4a. 從 `bencium-innovative-ux-designer` 抽出玻璃擬態禁令（來源：bencium.io）**
讀取來源 `SKILL.md` 找到兩處明確禁令：`## Foundational Design Principles` 底下「NEVER Use These AI-Generated Aesthetics」列出「Effects: Glass morphism, Apple design mimicry, liquid/blob backgrounds」；以及 `Bold Visual Expression` 小節明確寫「NO glass morphism effects (this is the one banned technique)」，緊接著解釋陰影／漸層允許使用，玻璃擬態是唯一被明文禁止的技巧。

**4b. 翻轉既有 `redesign-skill` 裡衝突的建議**
`scaffolding-templating/references/design/redesign-skill/SKILL.md` 的「Surface Upgrades」小節原本把「True glassmorphism」列為推薦的升級技巧（`backdrop-filter: blur` + 1px 內邊框 + 內陰影模擬邊緣折射）。找到這條規則後，依使用者決定**整條翻轉成禁令**，並在原地留一句話說明：這是使用者決定，起因是發現跟 bencium.io 的 `bencium-innovative-ux-designer` 衝突，並引用該來源的具體文字。**刻意沒有動 `hallmark`**——前一輪比對也發現 `hallmark` 自己的素材把玻璃擬態視為「Apple 系品牌時情境合理」，這個矛盾使用者只要求處理 `redesign-skill`，`hallmark` 保持原樣。這個未處理的張力已經在 `scaffolding-templating/SKILL.md`「How to use this skill」第 13 點明確標註「flagged, not resolved」，讓未來的閱讀者看得到但不強迫現在解決。

**5. 從 `bencium-impact-designer` 抽出「Creative Reframing Prompts」（來源：bencium.io）**
讀取來源找到完整清單，共三組共 15 個提示，比先前比對報告舉的兩個例子（Sagmeister、protest poster）多得多：Designer lens（Sagmeister／Neville Brody／Studio Dumbar／Dieter Rams／David Carson）、Context shift（magazine spread／museum exhibit／street signage／vinyl record cover／protest poster）、Era lens（1960s Swiss International／1990s Emigre-Ray Gun／1920s Bauhaus／2000s Flash era／Cyberpunk 2077）。折進 `scaffolding-templating/references/design/taste-skill/SKILL.md` 的 Section 0（Brief Inference）底下，新增 §0.E，明確標示為「optional lateral-thinking nudge」，不是強制規則。來源的 40 個美學工作室名稱目錄與骰子擲點式的「Force Variety」機制**不**安裝——跟 `taste-skill` 自己的三軸數值撥盤系統重疊。

**6. 從 `design-audit` 抽出「先讀專案文件＋分階段核准」工作流程（來源：bencium.io）**
讀取來源找到兩塊：`## Before You Start` 要求在形成任何意見前先讀 `DESIGN_SYSTEM.md`／`FRONTEND_GUIDELINES.md`／`APP_FLOW.md`／`PRD.md`／`TECH_STACK.md`／`LESSONS.md`（以及 progress、live app）；以及 `### Step 4: Wait for Approval`——呈現計畫、不動手實作、逐階段取得核准才能進下一階段。折進既有 `hallmark` 的 `audit` 動詞（`scaffolding-templating/references/design/hallmark/references/verbs/audit.md`），新增「Alternate mode: doc-grounded, phased audit」小節，**只在專案真的有這些具名文件時觸發**，明確標註是同一個 `audit` 動詞的「另一種、更嚴格」模式，不取代預設的扁平嚴重度清單行為。來源的 14 維度稽核檢查表**不**安裝——跟 `audit.md` 檔案裡自己既有的維度表完全重複。

**7. 從 `human-architect-mindset` 抽出「Loyalty」哲學框架（來源：bencium.io）**
讀取來源 `SKILL.md` 找到 Foundation 小節（The AI Perfection Trap、The Human Moat、Loyalty in Architecture 的四類作法、The Loyalty Question）；接著發現 `REFERENCE.md` 裡還有更完整的 `The Loyalty Decision Matrix`（5 列情境對照表）與 5 個具名反樣式（The Endless Pivot、The Greenfield Fallacy、The Trend Chase、The Premature Abstraction、The Shiny Object Syndrome），以及 `CHECKLIST.md` 的 `Phase 0: Loyalty Audit`（Betrayal Test 四問）。判斷 `agentic-dev-workflow/SKILL.md` 本身是密集的路由表格結構、沒有適合塞進長篇哲學論述的位置（跟 `karpathy-guidelines` 當初被獨立成檔的理由一樣），因此**新增一個獨立參考檔** `agentic-dev-workflow/references/loyalty-mindset/SKILL.md`，並在主檔案的表格裡加一列、intro 段落加一句來源說明。來源的 Domain Modeling／Systems Thinking／Constraint Navigation／AI-Aware Decomposition 四大支柱與 Spec-Driven-Development 延伸章節**不**安裝——跟既有 `domain-modeling`／`brainstorming`／`code-quality-review` 的 `codebase-design` 重複。

**8. 從 `bencium-aeo` 抽出「Authority Level Determines Strategy」表格（來源：bencium.io）**
讀取來源找到完整表格（Challenger vs. Established 兩列，含「Rank-5 sites gained 115% visibility... Rank-1 sites that over-optimized lost 30%」的 Princeton 研究數據點）。折進既有 `marketing/references/paid-acquisition/ai-seo/SKILL.md`，緊接在既有 Pillar 2（Princeton GEO 9 法排名表）之後新增一個補充小節，明確標註是「additive to」而非取代既有的新鮮度／引用／查詢測試指引。

**9. 整包安裝 `insurgent-campaign`（來源：bencium.io）**
完整複製 `SKILL.md` ＋ 完整 `references/`（7 個檔案：asymmetry-audit-table、authenticity-playbook、campaign-archetypes、channel-tier-stack、hungarian-case-study、lift-test-templates、sector-riders）。這是行銷策略內容，不是設計內容，因此讀 `marketing/SKILL.md` 找它既有的 `references/<sub-domain>/<leaf-skill>/SKILL.md` 慣例（兩層巢狀，例如 `references/research-strategy/attribution/`），放到 `marketing/references/research-strategy/insurgent-campaign/`，跟既有的 `attribution`、`marketing-plan` 同層。在 `marketing/SKILL.md` 新增一個小節交叉引用 `attribution`：兩者共用同一套增量／lift-test 測量研究基礎（Lewis & Rao 2015 QJE），但 `insurgent-campaign` 多了一整套分階段（intake → ideation → asymmetry audit → MMF gate → channel stack → shape 選擇 → 30 天計畫）的弱勢方策略工作流程，`attribution` 沒有這個。前一節（續）評估過整包不匯入（理由是跟既有 `marketing-plan`／`marketing-ideas`／`co-marketing` 重疊），這次使用者重新檢視後改變主意，明確要求整包安裝。

### 命名查重與授權整理

- 新資料夾／檔名 `p5js`、`sketch`、`insurgent-campaign`（資料夾名稱與 frontmatter `name:` 兩種寫法）都先對全倉庫 grep 查重，均無衝突（`sketch` 一詞在別處只以一般文字出現，例如觸發語句範例，從未作為技能資料夾或 frontmatter 名稱）。
- `THIRD-PARTY-LICENSES.md` 沒有新增任何一節——兩個來源（bencium.io、NousResearch/hermes-agent）都已經在同一天稍早的匯入裡建過節，這次只**延伸既有段落**：hermes-agent 段落的標題與清單新增 `p5js`／`sketch`（含 `sketch` 的雙作者 GSD/Lex Christopherson 具名credit），並補一句話說明 `claude-design` 的 Surface-First 只抽了片段；bencium.io 段落的標題與清單新增 `insurgent-campaign`（整包）與另外 5 個只抽片段的來源技能清單（`bencium-innovative-ux-designer`／`bencium-impact-designer`／`design-audit`／`human-architect-mindset`／`bencium-aeo`），並註明這 5 個都用同一份既有的 MIT 授權區塊，不需要各自附完整授權全文。

### 文件更新範圍

`scaffolding-templating/SKILL.md`（新增「Generative art & disposable UI sketching」表格區塊收納 `p5js`／`sketch`＋雙向交叉引用、「How to use this skill」新增第 12、13 點）、`agentic-dev-workflow/SKILL.md`（新增 `loyalty-mindset` 表格列、intro 段落補一句來源說明）、`marketing/SKILL.md`（研究策略列補上 `insurgent-campaign`、新增交叉引用小節）、根目錄 `SKILL.md`（`scaffolding-templating` 47→50、`marketing` 47→48、`agentic-dev-workflow` 24→25、全倉庫子技能總數 220→225、稽核區塊新增一整段 THIRD-PARTY IMPORT 紀錄＋逐一核對過的手算算式）、本檔案（本節）、`THIRD-PARTY-LICENSES.md`（延伸既有兩節，見上）、`README.md`／`TRIGGER-MAP.md`／`skills-search.html`（新增 `p5js`／`sketch`／`insurgent-campaign` 三個整包安裝項目的條目；5 個折進既有檔案的片段判斷不需要各自獨立的搜尋/觸發條目，因為它們是既有技能既有觸發語境下的補充內容，不是新的觸發場景——已在各自被折入的既有條目描述裡補一句話帶到）。

**arithmetic 附註**：`scaffolding-templating` 從 47 到 50 是 +3，不是預期的 +2（只裝了 `p5js`／`sketch` 兩個新檔案）——逐檔重新點過 `scaffolding-templating/references/` 底下所有 `SKILL.md` 後發現，前一節（續）陳述的 47 這個數字本身就少算了一個（本次批次前的實際檔案數是 48，不是 47）。這是前一輪 session 的一次性算術誤差，不是本次新增的問題；已在根目錄 `SKILL.md` 的稽核區塊留一段說明修正到哪一步、為什麼沒有往回追溯更早的每一次異動，往後的總數以本節修正後的 225 為準。

### 最終結果

18 個頂層技能維持不變。9 項動作中：4 項是新的獨立 `SKILL.md` 檔案（`p5js`、`sketch` 進 `scaffolding-templating`；`insurgent-campaign` 進 `marketing`；`loyalty-mindset` 進 `agentic-dev-workflow`，這個不是整包安裝而是新建的精簡參考檔），5 項是折進既有檔案的片段抽取（不算新增子技能檔案）。`scaffolding-templating` 實際 48→50（見上方 arithmetic 附註：前一輪陳述的 47 本身少算一個），`marketing` 47→48，`agentic-dev-workflow` 24→25，全倉庫子技能總數 220→225（`context-engineering-collection` 自己的 16 個維持不變、未觸碰）。`redesign-skill` 的玻璃擬態建議已翻轉成禁令；`hallmark` 刻意保持原樣未動，張力已記錄但不在本次範圍內處理。

### 補記：`ui-typography` 語言範疇修正（同一天，9 項動作之後）

使用者檢視當天稍早匯入的 `ui-typography`（bencium.io）後，指出它原本的「只要產生 UI 就默默自動套用全部規則」語氣，對這個工作區大量使用繁體中文的實際情況是有問題的——它的規則（彎引號、en/em dash 區分、斷字、全大寫字母加字距、以字元數計算的行長）全部是拉丁字母排版特有的慣例，對中文完全不適用，若不分語言就自動套用，可能對中文 UI 文案產生實際錯誤的排版建議，而不只是「多此一舉」。

**處理**：直接修改 `scaffolding-templating/references/design/ui-typography/SKILL.md`——frontmatter description 加上明確的語言範疇限定(僅英文可見文字自動套用；中文/CJK 文字退回一般觸發模式，只有使用者明確要求排版/校對時才用)，並新增一段「Language Scope — English/Latin-script only」章節，列出彎引號、斷字、字距、行長規則為何不適用於中文。同步更新 `scaffolding-templating/SKILL.md` 的 `ui-typography` 表格列說明與「Universal-tier judgment call」段落，補一段「2026-08-16 refinement」註記——強調這是對既有判斷的**細化**，不是推翻：即使限定在英文範疇，這個技能依然刻意不列入全域必用清單（維持 8 月 16 日稍早的判斷）。未觸碰 `THIRD-PARTY-LICENSES.md`（沒有新增授權內容，只是修改既有已授權內容的範疇限定文字）。本機安裝：單檔覆蓋複製 `ui-typography/SKILL.md` 到 `C:\Users\user\.claude\skills\`，已驗證。子技能檔案數無變化(未新增/刪除檔案，純內容修正)。

## 2026-08-16（四）：四個外部 UI 參考的深度整合（react-bits／React Aria／shadcn/ui／Magic UI）

使用者貼了四個連結（`github.com/DavidHDev/react-bits`、`react-aria.adobe.com`、`github.com/shadcn-ui/ui`、`github.com/magicuidesign/magicui`）問能不能整合進本倉庫。不同於本檔案前幾節的「整包安裝或不裝」二選一，這次先經過完整討論才動手，過程分三輪：

### 第一輪：初步調查與方案

讀了 `pick-ui-library`（已有 base-ui 推薦）、`ui-styling`（shadcn 覆蓋但可能過時）、`animate`／`animation-vocabulary`（動畫決策/命名，非元件庫）確認現有覆蓋範圍後，回報四個庫都能整合、且大多數不重疊：shadcn/ui 已有深度覆蓋（`ui-styling`）、React Aria 全空缺、react-bits 與 magicui 屬同一類（動畫特效元件庫）需要區分。使用者要求先討論整合方式再動手。

### 第二輪：確認整合深度、範圍、重疊處理

用 AskUserQuestion 問了三題（整合深度／這次要處理哪些庫／react-bits 跟 magicui 重疊怎麼處理），使用者選擇：**深度整合**（比照 `library-api-reference/references/vercel-react-view-transitions` 的模式：SKILL.md + README.md + 按主題拆分的 references/*.md）、**全部四庫都要**（shadcn/ui 只需更新，不必重裝）、**react-bits 跟 magicui 兩邊各自獨立並交叉引用**。

補充研究時發現兩個原本沒預期的關鍵事實：
1. **shadcn/ui 官方自己就有兩份完整的 Claude skill**（`skills/shadcn/`、`skills/migrate-radix-to-base/`），內容比本倉庫既有的 `ui-styling` 新且完整（registry 系統、MCP server、CLI、styling/forms/composition/icons/chat 規則、完整的 Radix→Base UI 遷移引擎）。
2. **Magic UI 官方也有一份完整的 Claude skill**（`skills/magic-ui/`），但只涵蓋 CLI 安裝流程與元件分類，不含實際原始碼。
3. **react-bits 的授權不是純 MIT**，而是「MIT + Commons Clause License Condition v1.0」——明文禁止「重新散布元件本身（單獨、打包或改版皆算）」，這直接排除了把它的元件原始碼複製進本倉庫參考文件的可能性（本倉庫本身會被打包/複製到 `~/.claude/skills/`，等同重新散布）。

把這個授權限制解釋給使用者聽（差別在於：magicui/shadcn 可以在我們自己的參考文件裡靜態存一份程式碼副本，react-bits 不行，只能存指引，程式碼永遠即時從官方 CLI 現抓）後，使用者確認理解並在第三輪給出最終指示。

### 第三輪：最終指示與執行

使用者的最終指示：**除了 react-bits 之外都要放入原始碼並深度整合**；**react-bits 要比較所有內容並寫清楚使用時機、跟 magicui 的具體差異**；三個動作——新增這幾個 skill 到專案（1）、合併進專案且所有文件都要更新（2）、重新安裝到這台電腦（3）。

**執行方式**：先做研究確認每個來源的實際檔案結構（GitHub API 列目錄、逐檔 curl 讀取 README/LICENSE），確認 React Aria 官方文件網站在本環境連線失敗（多次 ECONNRESET/SSL handshake 錯誤，`curl -4` 強制 IPv4 後 GitHub raw 內容才抓得到，文件網站本身仍抓不到），改用 `adobe/react-spectrum` 原始碼建置。接著派出 4 個背景 agent 平行處理：

1. **shadcn 官方 skill 整包搬入**（`shadcn-official`＋`migrate-radix-to-base`，共 21 個檔案，逐位元組原樣搬入）——成功完成。
2. **magicui 深度整合**（官方 3 個檔案逐位元組搬入＋本倉庫自撰、內嵌 20 個真實元件原始碼的 `source-catalog.md`）——成功完成。
3. **react-bits 純比較文件**（零內嵌原始碼，跟 magicui／`animate`／`animation-vocabulary`／`pick-ui-library` 的比較表，161 個真實元件名稱經 GitHub API 目錄列表核實）——成功完成。
4. **React Aria 深度整合**——**執行到一半失敗**：達到帳號 session 用量上限（"session limit · resets 5:20am"），中斷於正在寫 `hooks.md` 的當下。檢查 agent 留下的檔案發現 `SKILL.md`／`hooks.md`／`components.md` 三份其實都已完整寫完（agent 在被中斷前就已經完成，只差最後一份 `patterns.md` 沒開始），因此由主線程直接接手，額外抓取 `Field.tsx`／`Popover.tsx` 兩個官方 Tailwind starter 原始檔補完 `patterns.md`（表單組合、collection 共用 API、overlay 疊層/dismissal、hook vs. 元件的取捨），並自行完成名稱撞名檢查（無衝突）。

**最終落點與檔案數**：
- `scaffolding-templating/references/design/shadcn-official/`（11 檔，vendored）
- `scaffolding-templating/references/design/migrate-radix-to-base/`（10 檔，vendored）
- `scaffolding-templating/references/design/magicui/`（SKILL.md＋2 份 vendored reference＋1 份自撰 source-catalog.md，內嵌 20 個真實元件）
- `scaffolding-templating/references/design/react-bits/`（1 檔，純比較文件，零原始碼）
- `library-api-reference/references/react-aria/`（SKILL.md＋3 份 reference，內嵌 ~14 個真實元件＋3 個真實 hook 範例，全部來自 `adobe/react-spectrum` 官方 Tailwind starter kit 與套件 README，非憑記憶杜撰）

**文件更新範圍**：`scaffolding-templating/references/design/pick-ui-library/SKILL.md`（新增 React Aria 列與 base-ui 並列比較、新增「Animated component galleries」小節收 magicui／react-bits、新增 migrate-radix-to-base 交叉引用）、`scaffolding-templating/references/design/ui-styling/SKILL.md`（新增指向 `shadcn-official` 的交叉引用註記）、`scaffolding-templating/SKILL.md`（新增 4 個表格列、description 補充、「Picking within this cluster」段落新增交叉引用句）、`library-api-reference/SKILL.md`（新增 `react-aria` 表格列、description 補充、新增一條 cross-domain gotcha）、`THIRD-PARTY-LICENSES.md`（新增 4 節：shadcn／magicui／react-bits（含授權限制專門說明）／Adobe react-aria，Apache-2.0 全文複用 Shubham Saboo 節已有的版本不重複貼）、根目錄 `SKILL.md`（`scaffolding-templating` 50→54、`library-api-reference` 16→17、全倉庫子技能總數 225→230，全 skill list 表格與 HTML 註解區塊的逐倉庫清單同步新增 5 個名稱）、`README.md`（intro 段落延伸算式、版權聲明新增 4 條、`scaffolding-templating`／`library-api-reference` 兩節新增條目與計數）、本檔案（本節）、`TRIGGER-MAP.md`／`skills-search.html`（新增 5 個新技能的觸發範例/搜尋條目）。

**名稱撞名檢查**：`shadcn`、`migrate-radix-to-base`、`magic-ui`、`react-bits`、`react-aria` 五個 frontmatter `name:` 皆已逐一 grep 全倉庫確認無衝突，未發生任何重新命名。

### 最終結果

18 個頂層技能維持不變。5 個新增子技能檔案（`shadcn-official`／`migrate-radix-to-base`／`magicui`／`react-bits` 進 `scaffolding-templating`；`react-aria` 進 `library-api-reference`），皆為整包搬入或本倉庫自撰的獨立新檔案，非既有檔案的片段抽取。`scaffolding-templating` 50→54，`library-api-reference` 16→17，全倉庫子技能總數 225→230。react-bits 因授權限制刻意不內嵌原始碼——這是本倉庫第一次因為第三方授權條款而主動限縮某個技能的內容深度，而非因為內容重疊或範疇不符；這個先例（Commons Clause 禁止重新散布）未來遇到類似授權的來源時應該直接比照辦理，不需要重新討論。
