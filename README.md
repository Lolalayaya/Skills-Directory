# Skills Directory 技能總覽

本資料夾是一套給 Claude Code 使用的自訂技能（Skills）集合，目前共 **18 個頂層技能**，內部再細分為 **136 個子技能**（另加 `context-engineering-collection` 自帶、未拆分的 17 個子技能），總計對應最初安裝的 **137 個技能**。

> 完整的索引與觸發規則請見根目錄的 [`SKILL.md`](SKILL.md)（給 Claude 讀取的機器可讀版本）；本 README 是給「人」看的導覽版本，說明每個分類的用途與內含的所有子技能。

## 📁 資料夾結構

```
Skills-Directory/
├── SKILL.md                      ← 主索引（Claude 會優先讀這份）
├── README.md                     ← 本文件
└── <18 個技能資料夾>/
    ├── SKILL.md                  ← 該技能的進入點 / 總覽
    └── references/<子技能>/SKILL.md  ← 細分的子技能，各自獨立可觸發
```

每個頂層技能資料夾底下的 `references/`（或 `context-engineering-collection` 的 `skills/`）都收納了數個更細的子技能，各自有自己的 `SKILL.md`，可視為「同一主題下的不同工具/場景」。

---

## 🔁 全域必用技能（Universal — 不用等使用者開口）

以下 5 個子技能帶有「always / MUST / before any」等強制語氣，理論上**每次符合情境就該主動套用**，不需要使用者明確要求：

| 觸發時機 | 子技能 | 所屬技能 | 為什麼是必用 |
|---|---|---|---|
| 任何對話開始時 | `using-superpowers` | `agentic-dev-workflow` | 在回應前先確認該用哪個技能，包含要問使用者的釐清問題 |
| 任何創意/功能開發前 | `brainstorming` | `agentic-dev-workflow` | 動手設計前先釐清使用者意圖與需求 |
| 實作任何功能/修 bug 前 | `test-driven-development` | `product-verification` | 先寫出定義「成功」的測試，再寫實作 |
| 宣稱「修好了」「測試通過」「完成了」之前 | `verification-before-completion` | `product-verification` | 要有證據（實際跑過驗證指令並讀懂輸出），不能只是宣稱 |
| 撰寫/審查涉及輸入、驗證、檔案、資料庫、網路、加密或基礎設施設定的程式碼 | `code-security` | `code-quality-review` | 即使使用者沒提「安全性」也要主動檢查 |

---

## 📚 技能分類地圖

為了方便理解，把 18 個頂層技能依用途歸成 7 大類：

| 分類 | 包含技能 |
|---|---|
| 🛠️ 開發流程與品質保證 | `agentic-dev-workflow`、`product-verification`、`code-quality-review`、`incident-runbooks`、`openspec-workflow`、`skill-authoring` |
| 🚀 部署與維運 | `cicd-deployment`、`data-analysis`、`infrastructure-ops` |
| 🌐 瀏覽器自動化與研究 | `browser-automation`、`deep-research` |
| 🎨 內容、文件與設計 | `scaffolding-templating`、`library-api-reference`、`internal-writing-comms` |
| 📈 行銷 | `marketing` |
| 📖 學習與任務管理 | `personal-learning`、`business-automation` |
| 🧠 Agent / 上下文工程（進階研究向） | `context-engineering-collection` |

---

## 🛠️ 開發流程與品質保證

### 1. `agentic-dev-workflow` — 軟體開發生命週期總成
從探索意圖到收尾分支，涵蓋完整的 agentic 開發流程。包含 **8 個子技能**：

- **`using-superpowers`**（🔁必用）— 對話一開始就先判斷該用哪個技能
- **`brainstorming`**（🔁必用）— 任何創意/功能開發前，先探索使用者意圖與需求、釐清設計
- **`writing-plans`** — 拿到需求/規格後，動手寫程式前先產出實作計畫
- **`using-git-worktrees`** — 開始功能開發前，用 git worktree（或原生工具）建立隔離工作區
- **`executing-plans`** — 在獨立 session 中執行已寫好的實作計畫，中途設檢查點
- **`subagent-driven-development`** — 在目前 session 中執行含獨立任務的實作計畫
- **`dispatching-parallel-agents`** — 遇到 2 個以上互不依賴、可平行處理的任務時派發並行 agent
- **`finishing-a-development-branch`** — 實作完成、測試都過了之後，決定怎麼把分支合併/送出

### 2. `product-verification` — 讓「完成」有憑有據
證明修好的功能/bug 真的可行，而不是憑感覺宣稱完成。包含 **3 個子技能**：

- **`test-driven-development`**（🔁必用）— 實作任何功能/修 bug 前，先寫測試（red-green-refactor）
- **`verification-before-completion`**（🔁必用）— 宣稱完成前，必須實際跑驗證指令並讀懂輸出
- **`webapp-testing`** — 用 Playwright 對本地網頁應用做互動測試，含截圖、console log、UI 除錯

### 3. `code-quality-review` — 程式碼審查與安全性
標準化「程式碼怎麼被審查與掃描」。包含 **6 個子技能**：

- **`code-review-expert`** — 以資深工程師視角審查目前 git 變更，抓 SOLID 違規與安全風險
- **`semgrep`** — 靜態分析工具，含撰寫自訂 Semgrep 規則
- **`code-security`**（🔁必用）— 涉及輸入/驗證/檔案/DB/網路/加密/基礎設施設定的程式碼安全守則
- **`llm-security`** — LLM/RAG 應用程式的安全性（OWASP Top 10 for LLM）
- **`requesting-code-review`** — 完成任務、實作重要功能或合併前，如何「提出」程式碼審查請求
- **`receiving-code-review`** — 收到審查意見後如何嚴謹回應、驗證，而非照單全收或表面敷衍

### 4. `incident-runbooks` — 系統化除錯方法論
包含 **1 個子技能**：

- **`systematic-debugging`** — 遇到任何 bug、測試失敗或異常行為時，在提出修法前先找出根因、影響範圍，並記錄成可重用的診斷紀錄

### 5. `openspec-workflow` — OpenSpec 變更生命週期
包含 **5 個子技能**：

- **`openspec-explore`** — 進入探索模式，動手前先思考問題、釐清需求
- **`openspec-propose`** — 一次生成完整提案（含設計、規格、任務清單）
- **`openspec-apply-change`** — 實作 OpenSpec 變更中的任務
- **`openspec-sync-specs`** — 把 delta spec 的變更同步回主要規格文件（不歸檔）
- **`openspec-archive-change`** — 實作完成後歸檔並定案該變更

### 6. `skill-authoring` — 打造/優化技能本身
包含 **4 個子技能**：

- **`skill-creator`** — 從零建立新技能、修改既有技能、跑評測衡量表現
- **`skill-forge`** — 技能鍛造/優化工具
- **`skill-review`** — 上線前依最佳實踐審查技能
- **`writing-skills`** — 撰寫新技能、編輯既有技能、部署前驗證是否可用

---

## 🚀 部署與維運

### 7. `cicd-deployment` — 部署到 Vercel
包含 **2 個子技能**：

- **`deploy-to-vercel`** — 互動式部署應用程式/網站到 Vercel（"deploy my app"、"push this live"）
- **`vercel-cli-with-tokens`** — 用 access token（非互動登入）方式部署與管理 Vercel 專案，適合 CI 場景

### 8. `data-analysis` — 用真實數據找優化點
包含 **1 個子技能**（目前僅涵蓋 Vercel，之後可擴充其他平台）：

- **`vercel-optimize`** — 分析 Vercel 專案的 Function Invocations、Build Minutes、Fast Data Transfer、Core Web Vitals、快取狀況等，找出真正值得優化、且有數據佐證的成本/效能問題

### 9. `infrastructure-ops` — 佔位技能（尚無內容）
目前是**空的佔位資料夾**，預留給未來的日常維運（伺服器管理、資料庫/佇列維運、防止破壞性指令的防呆機制）技能，目前無任何實質內容，不應被當作權威來源使用。

---

## 🌐 瀏覽器自動化與研究

### 10. `browser-automation` — Browserbase 全套瀏覽器工具箱
只要任務牽涉「瀏覽網站」「自動化瀏覽器操作」「用真實瀏覽器測試網頁」「除錯失敗的自動化流程」「同步登入狀態」或「研究公司/競品/活動」都算。包含 **17 個子技能**：

- **`browser`** — 用自然語言 CLI 指令自動化瀏覽器操作（瀏覽、擷取資料、截圖、填表單、點按鈕）
- **`autobrowse`** — 自我改進的瀏覽器自動化：反覆執行任務、讀 trace、優化導覽策略直到穩定
- **`safe-browser`** — 建立有網域白名單限制的安全瀏覽器 agent，避免超出授權範圍存取
- **`ui-test`** — AI 驅動的對抗式 UI 測試，可只測 git diff 有變更的部分，涵蓋功能正確性、無障礙、RWD、UX 慣例
- **`cookie-sync`** — 把本機 Chrome 的 cookie 同步到 Browserbase，讓 CLI 能存取需要登入的網站
- **`browser-trace`** — 擷取完整 DevTools protocol trace（CDP、截圖、DOM dump），並拆分成可搜尋的分頁區塊，用於除錯
- **`browser-to-api`** — 把觀察到的 HTTP 流量（透過 browser-trace）轉換成 OpenAPI 3.1 規格文件
- **`browser-use-to-stagehand`** — 把 Python 的 browser-use 腳本遷移成 TypeScript 的 Stagehand v3（Browserbase）
- **`webmcp-gen`** — 針對目標網站產生、編譯、驗證 WebMCP 初始化腳本
- **`functions`** — 把瀏覽器自動化部署成 Browserbase 的無伺服器雲端函式（排程、webhook）
- **`fetch`** — 不開瀏覽器、直接抓取 URL 的 HTML/JSON、檢查狀態碼與 header，適合簡單爬蟲
- **`search`** — 不開瀏覽器、直接做網路搜尋，回傳結構化的標題/URL/作者/日期
- **`agent-experience`** — 讓網站對「AI agent 存取」更友善的相關指引
- **`company-research`** — 針對特定公司的研究
- **`competitor-analysis`** — 競品分析
- **`competitor-profiling`** — 競品側寫（更完整的競品畫像）
- **`event-prospecting`** — 活動/研討會開發潛在客戶

### 11. `deep-research` — 通用主題研究流程（中文）
先產生研究大綱，再擴充欄位/研究對象，接著為每個項目派出獨立的深度研究 agent，最後彙整成一份 Markdown 報告。適合學術研究、技術/產品比較、或任何「幫我研究這個主題並給結構化報告」的需求。包含 **5 個子技能**：

- **`research`** — 對目標主題做初步調研，產生調研大綱
- **`research-add-fields`** — 向既有大綱補充欄位定義
- **`research-add-items`** — 向既有大綱補充研究對象（items）
- **`research-deep`** — 讀取大綱，為每個 item 各自啟動獨立 agent 做深度調研
- **`research-report`** — 把深度調研結果彙整成涵蓋所有欄位的 Markdown 報告

---

## 🎨 內容、文件與設計

### 12. `scaffolding-templating` — 樣板、腳手架與完整設計系統
把最佳實踐轉換成可直接套用的樣板、腳手架、色彩/字體系統與參考資料庫。包含 **17 個子技能**：

- **`programmatic-seo`** — 用資料驅動的方式大量產生 SEO 頁面樣板
- **`design`** — 一般性設計指引
- **`design-system`** — 三層設計 token（primitive→semantic→component）、元件規格、投影片產生
- **`ui-styling`** — shadcn/Tailwind 為主的 UI 樣式規範
- **`ui-ux-pro-max`** — 可搜尋的本地 UI/UX 資料庫（67 種風格、161 組配色、57 組字體搭配、25 種圖表、21 種技術棧）
- **`banner-design`** — 橫幅/Banner 設計
- **`brand`** — 品牌語氣、視覺識別、訊息框架、資產管理與一致性
- **`anthropic-brand-guidelines`** — 套用 Anthropic 官方品牌色彩與字體規範
- **`canvas-design`** — 產出海報等靜態視覺藝術（PNG/PDF）
- **`algorithmic-art`** — 用 p5.js 搭配種子隨機數產生演算法藝術（flow field、粒子系統等）
- **`theme-factory`** — 為 artifact（投影片、文件、報表、HTML 頁面等）套用/產生主題（內建 10 組預設主題）
- **`frontend-design`** — 打造有個性、非樣板感的 UI 視覺方向、字體排印
- **`web-artifacts-builder`** — 用 React、Tailwind、shadcn/ui 打造複雜、需要狀態管理/路由的 claude.ai HTML artifact
- **`web-design-guidelines`** — 依 Web Interface Guidelines 審查 UI 程式碼（無障礙、UX）
- **`writing-guidelines`** — 依 Writing Guidelines 審查文件/文案語氣風格
- **`slides`** — 用 Chart.js、design token、文案公式打造策略性 HTML 簡報
- **`slack-gif-creator`** — 製作適合 Slack 的動態 GIF

### 13. `library-api-reference` — 第三方函式庫/檔案格式參考
在動手寫程式呼叫這些函式庫前，先查這裡的參考片段、版本差異與常見錯誤。包含 **9 個子技能**：

- **`docx`** — 讀寫、建立、編輯 Word（.docx）文件
- **`xlsx`** — 讀寫、建立、編輯 Excel（.xlsx）試算表
- **`pptx`** — 讀寫、建立、編輯 PowerPoint（.pptx）簡報
- **`pdf`** — PDF 的讀取/擷取文字表格、合併、拆分、旋轉、浮水印、建立、表單填寫、加解密、OCR
- **`mcp-builder`** — 打造高品質 MCP（Model Context Protocol）伺服器（Python FastMCP 或 Node/TS MCP SDK）
- **`vercel-react-best-practices`** — Vercel 工程團隊的 React/Next.js 效能優化準則
- **`vercel-react-native-skills`** — React Native 相關技巧
- **`vercel-react-view-transitions`** — React View Transitions API 應用
- **`vercel-composition-patterns`** — Vercel/React 組合模式（composition patterns）

### 14. `internal-writing-comms` — 文件協作與內部溝通
包含 **2 個子技能**：

- **`doc-coauthoring`** — 結構化流程協助共同撰寫文件（提案、技術規格、決策文件），透過反覆迭代確認內容對讀者有效
- **`internal-comms`** — 依公司慣用格式撰寫內部溝通（狀態報告、主管更新、公司電子報、FAQ、事故報告、專案更新等）

---

## 📈 行銷

### 15. `marketing` — 全漏斗行銷手冊
只要問題牽涉廣告、SEO、文案、轉換率、定價、Onboarding、流失、Email/SMS、推薦計畫、影響者/社群行銷、產品發布、行銷策略、歸因分析、A/B 測試、業務銷售素材或競品定位——即使使用者沒講出具體的行銷術語也算。內部再分 **5 大子群，共 47 個子技能**：

**🎯 付費取得與 ASO（`paid-acquisition`，5 個）**
- `ads` — 付費廣告投放策略
- `ad-creative` — 廣告素材設計
- `aso` — App Store / Google Play 上架優化稽核
- `ai-seo` — 針對 AI 搜尋引擎的 SEO
- `directory-submissions` — 目錄型網站提交/收錄

**📝 內容與 SEO（`content-seo`，9 個）**
- `seo-audit` — SEO 健檢
- `content-strategy` — 內容策略規劃
- `copywriting` — 文案撰寫
- `copy-editing` — 文案潤稿/校對
- `schema` —結構化資料（Schema.org）標記
- `site-architecture` — 網站架構規劃
- `social` — 社群內容
- `video` — 影音內容策略
- `image` — 圖片內容/優化

**💰 轉換與生命週期（`conversion-lifecycle`，10 個）**
- `cro` — 轉換率優化
- `signup` — 註冊流程優化
- `onboarding` — 使用者導入流程
- `paywalls` — 付費牆設計
- `popups` — 彈窗策略
- `pricing` — 定價策略
- `churn-prevention` — 流失防範
- `offers` — 優惠/方案設計
- `emails` — Email 行銷
- `sms` — 簡訊行銷
- `cold-email` — 陌生開發信

**🚀 成長與夥伴關係（`growth-partnerships`，8 個）**
- `referrals` — 推薦計畫
- `co-marketing` — 聯合行銷/合作夥伴
- `influencer-marketing` — 網紅行銷
- `community-marketing` — 社群經營
- `marketing-loops` — 成長循環設計
- `launch` — 產品發布計畫
- `free-tools` — 免費工具型獲客
- `lead-magnets` — 名單磁鐵設計

**🔍 研究與策略（`research-strategy`，14 個）**
- `customer-research` — 顧客研究
- `marketing-plan` — 行銷計畫制定
- `marketing-psychology` — 行銷心理學
- `marketing-ideas` — 行銷點子發想
- `marketing-council` — 多角度行銷顧問視角
- `attribution` — 行銷歸因分析
- `analytics` — 數據分析
- `ab-testing` — A/B 測試
- `product-marketing` — 產品行銷
- `prospecting` — 潛在客戶開發
- `public-relations` — 公關
- `revops` — 營收維運（RevOps）
- `sales-enablement` — 業務賦能素材
- `competitors` — 競品分析

---

## 📖 學習與任務管理

### 16. `personal-learning` — 個人知識學習工具
包含 **3 個子技能**：

- **`book-study`** — 系統化讀書教練，含間隔重複與精熟度測驗
- **`wiki-ingest`** — 把文章/文件/筆記彙整進結構化的 wiki 知識庫
- **`sigma`** — 一對一蘇格拉底式 AI 家教，適應式引導學習任何主題

### 17. `business-automation` — 跨 session 的檔案化任務規劃
把 `task_plan.md`、`findings.md`、`progress.md` 寫在硬碟上，讓長任務的規劃/進度在 `/clear` 或 context 重置後依然存在。核心邏輯 **1 種，附 5 種語言版本**：

- **`planning-with-files`** — 英文版（Manus 風格檔案化規劃系統）
- **`planning-with-files-zh`** — 簡體中文版
- **`planning-with-files-zht`** — 繁體中文版
- **`planning-with-files-ar`** — 阿拉伯文版
- **`planning-with-files-de`** — 德文版
- **`planning-with-files-es`** — 西班牙文版

---

## 🧠 Agent / 上下文工程（進階研究向）

### 18. `context-engineering-collection` — 上下文工程技能全集
唯一一個**保持原樣、未被拆分**的技能（原本就是一個涵蓋 17 個子技能的完整集合，拆開沒有額外價值）。用於打造/優化/評估/除錯需要有效上下文管理與可靠運作迴圈的 agent 系統。包含 `skills/` 底下 **17 個子技能**：

- **`context-fundamentals`** — 上下文工程基礎概念
- **`context-compression`** — 長任務的上下文壓縮、結構化摘要、交接摘要
- **`context-degradation`** — 診斷/緩解 lost-in-middle、context poisoning、context clash 等退化問題
- **`context-optimization`** — 上下文效率優化：token 預算、prefix/KV-cache 策略、檢索範圍縮減
- **`filesystem-context`** — 用檔案系統支撐持久化的 scratchpad、工具輸出卸載、跨 agent 交接檔
- **`memory-systems`** — 跨 session 的持久語意記憶：實體追蹤、時效性、圖/向量檢索
- **`multi-agent-patterns`** — 多 agent 系統設計：上下文隔離、supervisor/swarm 協調、平行執行
- **`latent-briefing`** — 多 agent 間共享記憶、KV cache compaction、降低 worker token 消耗
- **`long-horizon-prompting`** — 長時間跨度任務的提示設計
- **`bdi-mental-states`** — 用 BDI（信念-慾望-意圖）概念建模 agent 心智狀態
- **`hosted-agents`** — 託管/背景 agent 基礎設施：沙箱執行、warm pool、session 持久化
- **`harness-engineering`** — 自主 agent 運作框架設計：研究迴圈、評估腳手架、可回滾機制
- **`self-improvement-loops`** — Agent 自我改進迴圈設計
- **`tool-design`** — 給 LLM 用的工具設計原則
- **`project-development`** — Agent 系統的專案開發流程
- **`evaluation`** — Agent 評估系統：確定性檢查、回歸測試、多維度評分
- **`advanced-evaluation`** — 進階評估：LLM-as-judge、成對比較、評分者偏誤緩解

另外還附帶 `examples/`（`book-sft-pipeline`、`digital-brain-skill`、`interleaved-thinking` 等示範技能）與 `template/`（撰寫新技能用的範本），供延伸擴充參考。

---

## 🔎 如何使用這份索引

1. 先看「技能分類地圖」判斷任務屬於哪個大類。
2. 打開對應頂層技能的 `SKILL.md`，裡面會指向更細的子技能。
3. 若任務橫跨多個技能（例如任何要出貨的程式碼，通常會依序用到 `agentic-dev-workflow` → `product-verification` → `code-quality-review` → `cicd-deployment`），依序套用而非只選一個。
4. 之後若安裝新技能，記得在根目錄 `SKILL.md` 與本 README 都補上一筆，避免索引過時。
