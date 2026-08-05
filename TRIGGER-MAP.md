# 觸發對照表：使用者說什麼 → 觸發哪個 Skill → 它負責什麼

這份文件是給「人」查的速查表，目的是讓你一眼看出「我這句話應該會叫出哪個技能」。分類方式跟 [`README.md`](README.md) 一致；每個技能實際的觸發判斷仍以各自 `SKILL.md` 的 `description` 為準，這裡只列典型範例。

---

## 🛠️ 開發流程與品質保證

| 使用者可能說的話 | 觸發技能 | 它負責什麼 |
|---|---|---|
| 「幫我做一個新功能」「這個 bug 怎麼修比較好」（對話剛開始） | `using-superpowers` | 先判斷這次任務該用哪個技能，包含要問你的釐清問題 |
| （長串雜亂、口語/語音口述式的碎念，還沒整理成一句話的需求） | `thinking-out-loud` | 先產出 echo 摘要（含推論/猜測標註區）讓你確認，才動手做任何事；確認後若是要做功能設計，銜接到 `brainstorming` |
| 「我想加一個 XX 功能，先幫我想想怎麼設計」 | `brainstorming` | 動手寫程式前，先探索你的意圖與需求 |
| 「需求都確定了，幫我寫個實作計畫」 | `writing-plans` | 把需求轉成有步驟的實作計畫 |
| 「開始做這個功能前，先開一個獨立工作區」 | `using-git-worktrees` | 用 git worktree 建立隔離的開發環境 |
| 「照著這份計畫在新的 session 執行」 | `executing-plans` | 在獨立 session 執行已寫好的計畫，設檢查點 |
| 「照著計畫在這個對話裡，一個任務一個任務做完」 | `subagent-driven-development` | 序列派 subagent 執行計畫裡的任務，不平行派 implementer |
| 「這 3 個 bug 互不相關，可以同時查嗎」 | `dispatching-parallel-agents` | 派平行 agent 處理互不依賴的獨立任務（⚠️ 與上一項的分工目前不夠明確，見 `SKILL-AUDIT.md`） |
| 「功能做完了，測試也過了，接下來怎麼合併」 | `finishing-a-development-branch` | 決定分支要 merge / PR / rebase 的方式 |
| 「幫我逼問一下這個計畫的細節」 | `grilling`／`grill-me` | 一次一題的相關人審問式訪談（`--batch` 可切換整批問）；跟 `brainstorming` 互補，不是取代 |
| 「幫我邊訪談邊更新專案的領域詞彙文件」 | `grill-with-docs` | 逼問訪談 + 同步更新 `CONTEXT.md`/ADR |
| 「『帳號』這個詞在專案裡到底指什麼」 | `domain-modeling` | 挑戰模糊詞彙、解決一詞多義、記錄不可逆決策為 ADR |
| 「把這個對話整理成一份 spec」 | `to-spec` | 合成 spec 並發布到 issue tracker |
| 「把這份 spec 拆成一張一張的票」 | `to-tickets` | 拆成宣告依賴關係的 tracer-bullet 票 |
| 「這個專案大到一個 session 裝不下，不知道怎麼下手」 | `wayfinder` | 用決策票地圖逐步解開超大型灰地專案 |
| 「幫我把這個重構請求拆成可逐步提交的步驟」 | `request-refactor-plan` | 訪談 + 拆解成最小可提交步驟 |
| 「幫我做個拋棄式原型測一下這個設計」 | `prototype` | 跑完即刪的原型驗證 |
| 「這個專案要開始用逼問式規劃工具了，先幫我設定」 | `setup-matt-pocock-skills` | 一次性設定 issue tracker、triage 標籤等 |
| 「把這個對話交接給下一個 session」 | `handoff` | 壓縮對話成交接文件，CLI 支援就直接 launch 背景 agent，否則存檔 |
| 「解決一下這個 merge conflict」 | `resolving-merge-conflicts` | 逐 hunk 解決衝突，禁止 `--abort` |
| 「幫我裝一個攔截危險 git 指令的 hook」 | `git-guardrails-claude-code` | 攔截 `push --force`、`reset --hard` 等 |
| 「不確定該用逼問訪談還是哪個規劃工具」 | `ask-matt` | 這批工具自己的流程路由圖 |
| 「寫/改程式碼前，提醒我一下不要過度設計、只動手術刀式修改」 | `karpathy-guidelines` | 4 條濃縮行為守則：動手前先想清楚、精簡優先、手術刀式修改、目標導向可驗證；與 `brainstorming`／TDD/驗證／code review 精神相通但不是同一套流程 |
| 「開始寫這個功能前先寫測試」 | `test-driven-development` | Red-Green-Refactor：先寫定義成功的測試（已融合 mattpocock 原 `tdd` 的 Seams/反模式/Mocking 內容） |
| 「我測試過了，應該修好了」 | `verification-before-completion` | 要求你先跑驗證指令、讀懂輸出，才能宣稱完成 |
| 「用 Playwright 幫我測一下這個網頁」 | `webapp-testing` | 對本地網頁做互動測試、截圖、console log 除錯 |
| 「不要幫我省略程式碼」「這個檔案要完整寫完，不要放 TODO」「回應被截斷了，繼續」 | `output-skill` | 禁止輸出截斷/佔位符，數清楚要交付幾項再動筆，token 上限時用固定格式暫停/續寫 |
| 「開 PR 前先看一下這個改動有沒有超出範圍」「這個 diff 是不是改太多了」 | `scope-creep-detector` | 比對 git diff 跟宣稱的意圖，抓範圍蔓延/新依賴/API 改名，給 keep/split/justify 建議；純範圍分流，不做品質/安全審查 |
| 「幫我審查一下這次改動」 | `code-review-expert` | 資深工程師視角審查 git 變更，抓 SOLID 違規與安全風險 |
| 「幫我寫個 Semgrep 規則抓這種寫法」 | `semgrep` | 靜態分析工具，含自訂規則撰寫 |
| 這段程式碼碰到輸入、驗證、檔案、DB、網路、加密、infra 設定 | `code-security`（🔁必用，不用你開口） | 主動檢查安全風險 |
| 「我在做一個 AI/RAG 應用，這樣安全嗎」 | `llm-security` | LLM/RAG 應用的 OWASP Top 10 安全檢查 |
| 「幫我加個 xxx 套件」「這個檔案寫完了，附一下授權/相依套件的檢查結果」「這是要商用/開源釋出的專案，先確認一下授權沒問題」 | `ip-guard` | 新增外部相依套件前做授權相容性+遞移相依安全掃描（OSV+隔離套件狀態），每完成一個檔案/artifact 附加 provenance block；觸發粒度是「每次新增依賴」與「每完成一個檔案」，不是每次回應都觸發，也未列入全域必用（與 `code-security`／`llm-security` 的 supply-chain 章節是不同軸線，互不重疊） |
| 「重要功能做完了，我該怎麼發起 code review」 | `requesting-code-review` | 教你怎麼「提出」審查請求 |
| 「審查意見回來了，我該怎麼回應」 | `receiving-code-review` | 教你怎麼嚴謹評估、回應審查意見 |
| 「這個 bug 到底為什麼會發生」 | `systematic-debugging` | 先找根因、影響範圍，再提修法（已融合 mattpocock 原 `diagnosing-bugs` 的「先建可靠紅色訊號迴圈」方法論） |
| 「這段程式碼到底為什麼會這樣寫」「重構前先幫我查一下這裡的歷史」 | `commit-archaeologist` | 用本地 git 歷史（非僅 blame）重建程式碼存在的原因：起源 commit、後續變更、常一起改的檔案、意圖線索 |
| 「這些外部回報的 bug/需求幫我分類處理」 | `triage` | 用狀態機把湧入的原始回報整理成 agent 可接手的 issue |
| 「我口頭描述一個 bug，幫我拆成 issue」 | `qa` | 背景探索程式碼理解領域語言，拆解建成 GitHub issue |
| 這個專案本來就用 OpenSpec 慣例管理變更 | `openspec-workflow`（含 explore/propose/apply/sync/archive 5 個階段） | 走 OpenSpec 的完整變更生命週期，取代 `brainstorming`→`writing-plans` |
| 「幫我掃一下這個 codebase 有沒有架構能改善的地方」 | `improve-codebase-architecture` | 掃描深模組化機會，產出視覺化 HTML 報告 |
| 「這個模組的介面該怎麼設計」 | `codebase-design` | 深模組設計詞彙（interface/depth/seam/adapter） |
| 「幫我審查一下這次的 diff，照 Standards 跟 Spec 兩個軸」 | `code-review` | 雙軸審查+Fowler smell 基準（跟 `code-review-expert` 二選一，不要同時觸發） |
| 「用 dependency-cruiser 幫我強制模組邊界」 | `setup-ts-deep-modules` | TS 套件只能透過入口檔案被外部引用 |
| 「幫我設定 pre-commit hook」 | `setup-pre-commit` | Husky+lint-staged+Prettier |
| 「這個技能該怎麼規劃架構」 | `skill-forge` | 架構設計階段：workflow checklist、資源規劃 |
| 「幫我測試/優化這個技能的觸發率」 | `skill-creator` | eval/benchmark 迭代階段：跑測試、比對輸出、優化 description |
| 「這個技能上線前幫我把關一下」 | `writing-skills` | 上線前驗證：TDD 式壓力測試、SDO 描述規則 |
| 「幫我審查一下這個現成技能」 | `skill-review` | 純審查，不編輯 |
| 「技能的 description 該怎麼寫比較好」 | `writing-great-skills` | 撰寫技能的詞彙/原則參考，隨時可查（跟 `writing-skills` 的差異：參考 vs 上線前測試關卡） |

## 🚀 部署與維運

| 使用者可能說的話 | 觸發技能 | 它負責什麼 |
|---|---|---|
| 「幫我把這個部署到 Vercel」「push this live」 | `deploy-to-vercel` | 互動式部署（檢查 git remote / .vercel link / CLI 登入） |
| 「用 CI token 部署，不要互動登入」 | `vercel-cli-with-tokens` | 用 access token 非互動部署，適合 CI |
| 「為什麼這個 Vercel 專案這麼貴/這麼慢」 | `vercel-optimize`（`data-analysis` 底下） | 用真實用量數據（Function Invocations、Build Minutes、Core Web Vitals）找優化點 |
| 「幫我做一個互動式的設定/遷移引導腳本」 | `wizard`（`infrastructure-ops` 底下） | 產生互動式 bash 精靈，帶人跑完一次性設定/遷移 |
| 日常伺服器/資料庫維運、防止破壞性指令需求 | `infrastructure-ops` | **仍未涵蓋**——`wizard` 只處理一次性、需要人在場的設定流程，不是持續性維運工具，這個缺口還在 |

## 🌐 瀏覽器自動化與研究

| 使用者可能說的話 | 觸發技能 | 它負責什麼 |
|---|---|---|
| 「幫我去這個網站幫我點一下、填個表單」 | `browser` | 自然語言 CLI 操控真實瀏覽器 |
| 「只要抓這個網址的 HTML/JSON 就好，不用開瀏覽器」 | `fetch` | 純 HTTP 取內容，無 JS 渲染 |
| 「幫我搜尋一下網路上有沒有相關資料」 | `search` | 不開瀏覽器的輕量網路搜尋，回結構化標題/URL |
| 「這個網站要先登入才能看，幫我同步 cookie」 | `cookie-sync` | 把本機 Chrome cookie 同步進 Browserbase |
| 「幫我測一下這次 UI 改動有沒有壞掉」 | `ui-test` | 對 git diff 有變更的部分做對抗式 UI 測試 |
| 「這次自動化跑失敗了，幫我看看哪裡卡住」 | `browser-trace` | 擷取 DevTools trace 除錯 |
| 「把這個瀏覽器任務變成排程/webhook」 | `functions` | 部署成 Browserbase 無伺服器函式 |
| 「這個任務老是失敗，幫我訓練到穩定」 | `autobrowse` | 反覆執行、讀 trace、優化策略直到穩定 |
| 「這段流量幫我轉成 API 文件」 | `browser-to-api` | 把 HTTP 流量轉成 OpenAPI 3.1 規格 |
| 「幫我找這家公司的潛在客戶名單」 | `company-research` | 依 ICP 條件研究目標公司 |
| 「幫我看看我們的競爭對手在做什麼」（還不知道有誰） | `competitor-analysis` | 自動探索競品、產出互動 HTML 報告與戰卡 |
| 「幫我研究這幾個競品網址的 SEO/流量表現」（已有 URL 清單） | `competitor-profiling` | 用 Firecrawl/DataForSEO 挖 SEO/流量/評論情報，產出 Markdown |
| 「這場研討會的講者名單，幫我篩出潛在客戶」 | `event-prospecting` | 從會議 speaker 頁抽人、按 ICP 過濾 |
| 「幫我研究一下 XX 這個主題，給我結構化報告」（中文、非銷售場景） | `deep-research`（research→research-deep→research-report） | 通用主題研究 pipeline，⚠️ 跟上面的 `company-research` 命名容易撞車，「研究一家公司」這句話兩邊都可能觸發 |
| 「幫我查一下這個問題，寫成一份筆記」（單一問題，不需要比較表） | `background-research`（`deep-research` 底下） | 背景 agent 單次查證，產出一份帶引用的筆記——不是 pipeline 的一部分，沒有 outline/多 agent 結構 |

## 🎨 內容、文件與設計

| 使用者可能說的話 | 觸發技能 | 它負責什麼 |
|---|---|---|
| 「幫我大量產生 SEO 頁面」 | `programmatic-seo` | 資料驅動產生 SEO 頁面樣板 |
| 「幫我做一整套品牌識別+Logo+Banner+簡報」（跨多種產出、或不確定要哪個） | `design` | 全包版：內建 Logo/CIP/Banner/Icon/Slides/社群圖生成 |
| 「只要幫我定義品牌語氣」／「只要一張 Banner」／「只要簡報」／「只要 token 規格」 | `brand`／`banner-design`／`slides`／`design-system` | 同一供應商的精簡單功能版，只做一件事、載入更少 context |
| 「幫我建一套 design token 系統」 | `design-system` | 三層 token（primitive→semantic→component）+ 元件規格 |
| 「幫我用 shadcn/Tailwind 刻這個 UI」 | `ui-styling` | UI 樣式實作規範 |
| 「有沒有現成的配色/字體/風格可以參考」 | `ui-ux-pro-max` | 可搜尋的 UI/UX 資料庫（67 風格/161 配色等） |
| 「這個 UI 看起來很有 AI 感，幫我改得有個性一點」 | `frontend-design` | 反樣板感的視覺方向判斷 |
| 「幫我做一張海報」 | `canvas-design` | 靜態視覺藝術（PNG/PDF） |
| 「幫我用 p5.js 生成一些演算法藝術」 | `algorithmic-art` | 種子隨機數生成藝術 |
| 「幫這份文件/簡報套個主題」 | `theme-factory` | 套用內建 10 組預設主題 |
| 「幫我做一個有狀態管理的複雜 claude.ai 頁面」 | `web-artifacts-builder` | React/Tailwind/shadcn 打造複雜 artifact |
| 「幫我審查一下這個 UI 符不符合無障礙規範」 | `web-design-guidelines` | 依 Web Interface Guidelines 審查 UI 程式碼 |
| 「幫我審查一下這份文件的語氣」 | `writing-guidelines` | 依 Writing Guidelines 審查文案語氣 |
| 「幫我做一份簡報」 | `slides` | 用 Chart.js + design token 做策略性 HTML 簡報 |
| 「幫我做一個落地頁/portfolio，不要看起來像 AI 生成的」 | `taste-skill`（或 `hallmark`，二選一、別混用） | 兩套機制不同、規則會互相打架（例如禁用字體清單互相矛盾）：要接官方設計系統(Fluent/Material/Carbon等)或單次輕量建置 → `taste-skill`；同專案要做多頁且不能重複、或要用 audit(只評分不改)/study(從URL/截圖萃取風格) → `hallmark` |
| 「幫我把這個網站改版升級一下，不要動到原本的框架」 | `redesign-skill`（或 `hallmark redesign`） | 稽核既有專案的樣板感問題，原地修正不重寫 |
| 「幫我從這個 URL/截圖抓設計風格套用到我的內容」 | `hallmark`（`study` 動詞） | 從 URL 或截圖萃取設計 DNA（巨觀結構、字體配對、色彩），不是像素級複製 |
| 「幫我做一套品牌識別板/Logo 系統的圖」 | `brandkit` | 品牌識別板、Logo 系統的圖片生成（文字型品牌語氣文件用 `brand`） |
| 「幫我做一個工業風/軍事終端風格的儀表板」 | `brutalist-skill` | Swiss 印刷+軍事終端融合的工業感 UI |
| 「幫我做一個 Awwwards 等級、GSAP 動態很強的網站」 | `gpt-tasteskill` | GSAP 動態工程+AIDA 結構+偽隨機排版變化 |
| 「先幫我生成設計圖，再照圖寫程式碼」（Codex 情境） | `image-to-code-skill` | 圖片優先工作流：先生成設計參考圖、深入分析後再寫程式碼 |
| 「幫我生成幾張手機 App 畫面的概念圖，不用寫程式碼」 | `imagegen-frontend-mobile` | 純圖片生成的 App 畫面概念，含裝置外框 mockup |
| 「幫我生成這個落地頁每個區塊的參考圖，不用寫程式碼」 | `imagegen-frontend-web` | 純圖片生成，一個區塊一張參考圖 |
| 「幫我做一個極簡編輯風的介面，暖色調、無漸層」 | `minimalist-skill` | 暖色調極簡編輯風 UI |
| 「幫我做一個看起來很貴、代理商級的視覺設計」 | `soft-skill` | 「$150k 代理商級」視覺規格+雙層卡片架構+出貨前檢查清單 |
| 「幫我做一份 Google Stitch 用的 DESIGN.md」 | `stitch-skill` | 產生 Stitch 專用的語義化設計規格檔 |
| 「幫我讀寫這份 Word/Excel/PPT/PDF」 | `docx`／`xlsx`／`pptx`／`pdf` | 對應檔案格式的建立、編輯、讀取 |
| 「幫我做一個 MCP 伺服器」 | `mcp-builder` | 建置高品質 MCP 伺服器 |
| 「這個 React/Next.js 專案效能怎麼優化」 | `vercel-react-best-practices` | 通用 React/Next.js 效能準則 |
| 「這是 React Native/Expo 專案，效能怎麼優化」 | `vercel-react-native-skills` | 僅限行動端的效能規則 |
| 「幫我加個 View Transition 動畫」 | `vercel-react-view-transitions` | View Transitions API 應用 |
| 「這個元件架構怎麼設計比較好」 | `vercel-composition-patterns` | React 組合模式 |
| 「幫我一起寫一份提案/技術規格」 | `doc-coauthoring` | 結構化共寫文件流程 |
| 「幫我照公司格式寫一份狀態報告/電子報」 | `internal-comms` | 套用公司慣用的內部溝通格式 |
| 「幫我把這些寫作靈感先記下來，還沒想好怎麼組織」 | `writing-fragments` | 純探索，挖掘素材片段，不急著定結構 |
| 「幫我把這堆素材寫成一篇文章」／「幫我改一下這篇文章草稿」 | `writing-shape` | 塑形成文章（含敘事 beat 模式）或編輯既有草稿 |
| 「這幾個問題我答不出來，幫我整理成問卷發給知情人」 | `to-questionnaire` | 把答不出來的問題整理成問卷，非同步填寫或會議上討論 |

## 📈 行銷

| 使用者可能說的話 | 觸發技能 | 它負責什麼 |
|---|---|---|
| 「幫我寫一則廣告文案/投放策略」 | `ads`／`ad-creative` | 付費廣告策略與素材 |
| 「幫我做 App Store 上架優化稽核」 | `aso` | ASO 稽核 |
| 「怎麼讓 ChatGPT/Perplexity 這類 AI 搜尋引擎推薦我」 | `ai-seo` | 針對 AI 搜尋引擎的 SEO |
| 「幫我做網站 SEO 健檢」 | `seo-audit` | 傳統技術/內容 SEO 健檢（跟 `ai-seo` 已互斥） |
| 「幫我寫一篇部落格文章/文案」 | `copywriting`／`copy-editing` | 文案撰寫與潤稿 |
| 「幫我規劃內容策略/網站架構」 | `content-strategy`／`site-architecture` | 內容與架構規劃 |
| 「幫我優化註冊/導入流程/轉換率」 | `signup`／`onboarding`／`cro` | 各階段轉換優化 |
| 「幫我設計定價/付費牆/優惠方案」 | `pricing`／`paywalls`／`offers` | 商業模式設計 |
| 「使用者一直流失，幫我想辦法留住」 | `churn-prevention` | 流失防範 |
| 「幫我寫 Email/簡訊行銷內容」 | `emails`／`sms`／`cold-email` | 對應管道的行銷內容 |
| 「幫我設計推薦計畫/找網紅合作/做社群經營」 | `referrals`／`influencer-marketing`／`community-marketing` | 成長與夥伴關係 |
| 「幫我規劃產品發布」 | `launch` | 產品發布計畫 |
| 「幫我了解目標客群/建立潛在客戶名單」 | `customer-research`／`prospecting` | 客戶研究與名單開發（兩者觸發詞部分重疊） |
| 「幫我做一份行銷計畫/找點子/多角度顧問建議」 | `marketing-plan`／`marketing-ideas`／`marketing-council` | 策略發想（三者觸發詞部分重疊） |
| 「幫我設計 A/B 測試/歸因模型/看數據」 | `ab-testing`／`attribution`／`analytics` | 數據相關（已用明確邊界說明區分） |
| 「幫我做競品比較頁/alternative 頁」 | `competitors` | 只做「成品頁面」，不做背後的競品研究（研究見 `browser-automation`） |
| 其餘（`schema`／`social`／`video`／`image`／`popups`／`co-marketing`／`free-tools`／`lead-magnets`／`marketing-loops`／`marketing-psychology`／`product-marketing`／`public-relations`／`revops`／`sales-enablement`／`directory-submissions`） | 對應同名子技能 | 各自對應該行銷細分領域，觸發詞清楚，未發現重疊或模糊問題 |

## 📖 學習與任務管理

| 使用者可能說的話 | 觸發技能 | 它負責什麼 |
|---|---|---|
| 「我想系統性地讀完這本書」 | `book-study` | 間隔重複 + 精熟度測驗的讀書教練 |
| 「幫我把這些筆記整理進知識庫」 | `wiki-ingest` | 彙整文章/筆記成結構化 wiki |
| 「教我 XX 這個主題，用問答的方式」 | `sigma` | 蘇格拉底式 AI 家教（與 book-study 底層機制重疊，見 `SKILL-AUDIT.md`） |
| 「我想長期建立一個學這個主題的工作區」 | `teach` | 長期課程資產建構（跟 `sigma` 的差異：無嚴格掌握度評分） |
| 「這個任務很長，幫我把進度存到硬碟上」 | `business-automation`（`planning-with-files` 系列） | 跨 session 保留 task_plan/findings/progress，語言變體視你的對話語言而定 |
| 「我生活/工作裡有個重複的模式，幫我整理成可執行的 workflow」 | `loop-me`（`business-automation` 底下） | 用逼問訪談把重複模式整理成 workflow 規格文件 |
| 「我電腦裡一堆做到一半就放棄的專案，幫我看看該救哪個」「為什麼我老是沒把專案做完」 | `project-graveyard`（`business-automation` 底下） | 掃描機器上被放棄的側專案，從 git 歷史解剖死因、找出失敗模式，挑一個最值得復活的並協助動手 |

## 🧠 Agent / 上下文工程（進階研究向）

只有在你自己打造/優化 agent 系統、multi-agent 架構、context 管理策略時才會用到，一般任務幾乎不會觸發：

| 使用者可能說的話 | 觸發技能 |
|---|---|
| 「這個 agent 為什麼中段就忘記指令了」 | `context-degradation` |
| 「長對話怎麼做上下文壓縮/交接摘要」 | `context-compression` |
| 「token 預算怎麼優化，要不要用 KV cache」 | `context-optimization` |
| 「怎麼用檔案系統做持久化 scratchpad」 | `filesystem-context` |
| 「怎麼設計跨 session 的記憶系統」 | `memory-systems` |
| 「多 agent 系統的架構怎麼設計」 | `multi-agent-patterns` |
| 「怎麼給 LLM 設計好用的工具」 | `tool-design` |
| 「這個 agent 專案的開發流程怎麼走」 | `project-development` |
| 「怎麼評估 agent 系統的表現」 | `evaluation`／`advanced-evaluation`（後者專做 LLM-as-judge、pairwise 比較） |
| 其餘（`context-fundamentals`／`bdi-mental-states`／`hosted-agents`／`harness-engineering`／`self-improvement-loops`／`long-horizon-prompting`） | 更底層/更學術的子場景，觸發頻率極低（`latent-briefing` 已於 2026-07-31 移除，見 `SKILL-AUDIT.md`；`bdi-mental-states` 經確認後保留） |

---

> 2026-07-31 匯入的第三方 `mattpocock-skills`（Matt Pocock，MIT 授權，見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）已依主題分散進上面各分類，不再獨立成一個分類——`ask-matt`／`grilling`／`grill-me`／`grill-with-docs`／`domain-modeling`／`to-spec`／`to-tickets`／`wayfinder`／`request-refactor-plan`／`prototype`／`setup-matt-pocock-skills`／`handoff`／`resolving-merge-conflicts`／`git-guardrails-claude-code` 在「開發流程與品質保證」；`triage`／`qa`／`improve-codebase-architecture`／`codebase-design`／`code-review`／`design-an-interface`／`setup-ts-deep-modules`／`setup-pre-commit` 同樣在那個分類；`background-research` 在「瀏覽器自動化與研究」；`writing-fragments`／`writing-shape`／`to-questionnaire` 在「內容、文件與設計」；`teach`／`loop-me` 在「學習與任務管理」；`wizard` 在「部署與維運」。原始的 `tdd`／`diagnosing-bugs` 已經**不存在**了——內容已實體併入 `test-driven-development`／`systematic-debugging`，說「幫我寫測試」「幫我診斷這個 bug」還是會照常觸發，只是觸發到的是合併後的版本。

如果實際使用時發現「我說了這句話，結果沒觸發到我以為的那個技能」，代表對應的 `description` 需要調整——回報給我，我可以直接幫你改寫該技能的 frontmatter。
