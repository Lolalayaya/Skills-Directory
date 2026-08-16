# Skills Directory 技能總覽

本資料夾是一套給 Claude Code 使用的自訂技能（Skills）集合，目前共 **18 個頂層技能**，內部再細分為 **225 個子技能**（另加 `context-engineering-collection` 自帶、未拆分的 16 個子技能）。原始 137 個技能經 2026-07-31 的健檢移除 7 個確認不會用到的子技能；同一天又匯入了 Matt Pocock 的第三方技能包（原 41 個資料夾，健檢後留 30 個），並依主題**直接融入既有的 18 個分類**，而不是另立門戶——例如逼問式訪談/spec/tickets 併入 `agentic-dev-workflow`，兩軸審查/架構掃描併入 `code-quality-review`，其中 `tdd`／`diagnosing-bugs` 兩個技能的獨特內容則直接合併進本倉庫既有的 `test-driven-development`／`systematic-debugging`。2026-08-01 再匯入 forrestchang 的第三方技能包 `andrej-karpathy-skills`（僅 1 個技能 `karpathy-guidelines`），同樣依主題併入既有的 `agentic-dev-workflow`。同日再從 Shubham Saboo 的 `awesome-llm-apps` 倉庫的 `agent_skills/` 資料夾匯入 4 個技能（`commit-archaeologist`、`project-graveyard`、`scope-creep-detector`、`thinking-out-loud`），分散融入 `incident-runbooks`／`business-automation`／`code-quality-review`／`agentic-dev-workflow`；同資料夾內的第 5 個技能 `advisor-orchestrator-worker` 因與此環境內建的多代理 `Workflow` 工具功能重疊而未匯入。2026-08-02 匯入 Mugdha Vairagade 的 `claude-skill-ip-guard`（1 個技能 `ip-guard`），併入既有的 `code-quality-review`。2026-08-05 同時匯入 Leonxlnx 的 `taste-skill` 技能包（12 個技能，11 個依主題併入 `scaffolding-templating`、1 個 `output-skill` 併入 `product-verification`）與 Nutlope 的 `hallmark`（1 個技能，併入 `scaffolding-templating`）。2026-08-07 匯入 AnySearch Team 的 `anysearch-skill`（1 個技能 `anysearch`，統一即時搜尋 API，併入既有的 `browser-automation`）。2026-08-09 匯入 Emil Kowalski 的 `emilkowalski/skills` 技能包（9 個技能：動畫/動作工程 7 個＋UI 決策工具 2 個，全部併入既有的 `scaffolding-templating`，其中 `prototype` 因撞名改名為 `prototype-variants`）。2026-08-16 一次評估 5 個來源，收錄 4 個：Firecrawl 官方的 `firecrawl/cli`＋`firecrawl/skills`（17 個技能，5 個併入 `library-api-reference`、12 個併入 `browser-automation`）、`arxiv-skills`（2 個技能，併入 `library-api-reference`）、`Research-Paper-Writing-Skills`（1 個技能，併入 `internal-writing-comms`）、`Humanizer-zh-TW`（1 個技能，併入 `internal-writing-comms`）；第 5 個來源 `watermarks-remover` 因其核心功能是剝除 AI 內容來源標記（規避偵測），予以拒絕收錄，未匯入任何內容。同一天稍晚，再依使用者指定的「比對既有技能、只裝新內容＋補落差」流程，評估 4 個 UI/UX 相關來源，收錄 3 個共 10 個子技能，全數併入 `scaffolding-templating`：AccessLint 的 5 個無障礙（WCAG 2.2）稽核/掃描/檢測/差異比對/修復技能、bencium.io 的 `ui-typography`（排版規則）與 `relationship-design`（agentic UX）、NousResearch/hermes-agent 的 `popular-web-designs`（54 站設計系統目錄）／`design-md`（Google `DESIGN.md` 規格工具）／`baoyu-infographic`（資訊圖產生器）；第 4 個來源 `vercel-labs/agent-skills` 確認只是已安裝 `vercel-react-view-transitions` 的同源更新，用來同步 3 個過時檔案，不算新匯入。同一天第三次處理，使用者親自指定 9 項精準動作（4 項整包安裝：`p5js`／`sketch`（hermes-agent）併入 `scaffolding-templating`、`insurgent-campaign`（bencium.io）併入 `marketing`、`loyalty-mindset`（抽自 bencium.io 的 `human-architect-mindset`）新建進 `agentic-dev-workflow`；5 項只抽單一機制折進既有檔案，不新增子技能檔案），全倉庫子技能總數 220→224；驗證過程中另外發現 `scaffolding-templating` 前一輪陳述的 47 其實少算一個（實際檔案數是 48），順手修正為 224→225。同一天稍晚，使用者提出將四個外部 UI 參考（react-bits、React Aria、shadcn/ui、Magic UI）整合進本倉庫的請求，經討論確認整合深度、範圍與授權限制後執行：shadcn/ui 官方的兩個技能（`shadcn-official`／`migrate-radix-to-base`）與 Magic UI 官方技能逐位元組原樣搬入（皆 MIT），Magic UI 另外新增本倉庫自撰、內嵌 20 個真實元件原始碼的目錄；React Aria（Apache-2.0）官方文件網站在本環境連線失敗，改由 `adobe/react-spectrum` 原始碼（套件 README、`AGENTS.md` 分層說明、官方 Tailwind starter kit）建置；react-bits 因授權為「MIT + Commons Clause」明文禁止重新散布元件本身，改為只做分類目錄與跟 `magicui` 的比較文件，刻意不內嵌任何原始碼。`scaffolding-templating` 50→54（+4：`shadcn-official`／`migrate-radix-to-base`／`magicui`／`react-bits`），`library-api-reference` 16→17（+1：`react-aria`），全倉庫子技能總數 225→230。完整過程與每個子技能的最終落點詳見 [`SKILL-AUDIT.md`](SKILL-AUDIT.md)。

> 完整的索引與觸發規則請見根目錄的 [`SKILL.md`](SKILL.md)（給 Claude 讀取的機器可讀版本）；本 README 是給「人」看的導覽版本，說明每個分類的用途與內含的所有子技能。

## ⚠️ 版權與內容來源聲明

**這個倉庫是「整理／彙整」，不是「原創」。**

本倉庫底下 18 個頂層資料夾裡的技能內容，絕大多數是從各個開源技能專案、AI 廠商官方範例、社群發布的技能包蒐集、彙整、分類而來，**原始文字內容的著作權屬於各自的原作者／專案**，並非本倉庫維護者所寫。舉例來說（僅為協助辨識來源，不代表完整清單）：

- `library-api-reference` 底下的 `docx`／`xlsx`／`pptx`／`pdf`／`mcp-builder` 等，來自 AI 廠商官方發布的範例技能
- `browser-automation` 的多數子技能，來自 Browserbase 相關的開源工具鏈
- `agentic-dev-workflow` 裡 `using-superpowers`／`brainstorming`／`test-driven-development` 等，來自社群流通的開源技能框架
- `context-engineering-collection` 是完整保留、未拆分的第三方開源集合，本身附有獨立的 [`LICENSE`](context-engineering-collection/LICENSE)（MIT License），版權標註為原作者所有
Matt Pocock（[aihero.dev](https://www.aihero.dev/s/skills-newsletter)）發布的第三方開源技能包 `mattpocock-skills`（MIT 授權）於 2026-07-31 匯入並依主題分散融入本倉庫既有的 9 個頂層技能（`agentic-dev-workflow`、`code-quality-review`、`incident-runbooks`、`deep-research`、`personal-learning`、`internal-writing-comms`、`skill-authoring`、`business-automation`、`infrastructure-ops`），完整清單與授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)；原始文字內容的著作權仍屬於原作者
- forrestchang 發布的第三方開源技能包 `andrej-karpathy-skills`（[github.com/forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)，MIT 授權）於 2026-08-01 匯入，內含單一技能 `karpathy-guidelines`，依主題併入既有的 `agentic-dev-workflow`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Shubham Saboo 發布的第三方開源專案 `awesome-llm-apps`（[github.com/Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)，Apache-2.0 授權，其中個別技能由 Shubham Saboo 或 Matt Van Horn 撰寫）的 `agent_skills/` 資料夾於 2026-08-01 匯入 4 個技能（`commit-archaeologist`、`project-graveyard`、`scope-creep-detector`、`thinking-out-loud`），依主題分散融入本倉庫既有的 4 個頂層技能（`incident-runbooks`、`business-automation`、`code-quality-review`、`agentic-dev-workflow`），完整清單與授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)；原始文字內容的著作權仍屬於原作者
- Mugdha Vairagade 發布的第三方開源技能 `claude-skill-ip-guard`（[github.com/mugdhav/claude-skill-ip-guard](https://github.com/mugdhav/claude-skill-ip-guard)，Apache-2.0 授權）於 2026-08-02 匯入，內含單一技能 `ip-guard`（程式碼/內容產出的 IP 與授權合規防護、相依套件安全掃描），依主題併入既有的 `code-quality-review`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Leonxlnx 發布的第三方開源技能包 `taste-skill`（[github.com/Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)，MIT 授權）於 2026-08-05 匯入，內含 12 個前端設計/反 AI 樣板技能，其中 11 個依主題併入既有的 `scaffolding-templating`，第 12 個 `output-skill`（非設計技能，完整輸出紀律）併入既有的 `product-verification`，完整清單與授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Nutlope 發布的第三方開源技能 `hallmark`（[github.com/Nutlope/hallmark](https://github.com/Nutlope/hallmark)，MIT 授權）於 2026-08-05 匯入，內含單一技能 `hallmark`（反 AI 樣板前端設計系統，含 audit/redesign/study 動詞），依主題併入既有的 `scaffolding-templating`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- AnySearch Team 發布的第三方開源技能 `anysearch-skill`（[github.com/anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill)，Apache-2.0 授權）於 2026-08-07 匯入，內含單一技能 `anysearch`（統一即時搜尋服務：一般網路搜尋、16 個垂直領域結構化搜尋、平行批次查詢、URL 內容擷取，附跨平台多執行環境 CLI），依主題併入既有的 `browser-automation`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Emil Kowalski 發布的第三方開源技能包 `emilkowalski/skills`（[github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)，MIT 授權）於 2026-08-09 匯入，內含 9 個技能（介面動作工程：`emil-design-eng`／`animate`／`review-animations`／`improve-animations`／`find-animation-opportunities`／`animation-vocabulary`／`apple-design`，外加 UI 決策工具 `pick-ui-library` 與 `prototype`），依主題全部併入既有的 `scaffolding-templating`；其中 `prototype` 因與本倉庫既有的 `agentic-dev-workflow/prototype` 撞名，改名為 `prototype-variants`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Firecrawl 發布的官方開源技能倉庫 `firecrawl/cli` 與 `firecrawl/skills`（[github.com/firecrawl/cli](https://github.com/firecrawl/cli)、[github.com/firecrawl/skills](https://github.com/firecrawl/skills)，ISC 授權）於 2026-08-16 匯入，共 17 個技能——`firecrawl/skills` 的 5 個應用整合技能併入 `library-api-reference`，`firecrawl/cli` 的 10 個即時網頁工具技能加上 `firecrawl/skills` 的 2 個索引技能併入 `browser-automation`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- ultimatile 發布的第三方開源技能包 `arxiv-skills`（[github.com/ultimatile/arxiv-skills](https://github.com/ultimatile/arxiv-skills)，MIT 授權）於 2026-08-16 匯入，內含 2 個技能（`arxiv-lookup`、`arxiv-doc-builder`），依主題併入既有的 `library-api-reference`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Master-cai 發布的第三方開源技能 `Research-Paper-Writing-Skills`（[github.com/Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)，MIT 授權）於 2026-08-16 匯入，內含單一技能 `research-paper-writing`，依主題併入既有的 `internal-writing-comms`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- kevintsai1202 發布的第三方開源技能 `Humanizer-zh-TW`（[github.com/kevintsai1202/Humanizer-zh-TW](https://github.com/kevintsai1202/Humanizer-zh-TW)，MIT 授權）於 2026-08-16 匯入，內含單一技能 `humanizer-zh-tw`，依主題併入既有的 `internal-writing-comms`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- AccessLint 發布的第三方開源技能包 `skills`（[github.com/AccessLint/skills](https://github.com/AccessLint/skills)，MIT 授權）於 2026-08-16 匯入，內含 5 個技能（`accessibility-audit`／`accessibility-scan`／`accessibility-inspect`／`accessibility-diff`／`accessibility-fix`，WCAG 2.2 稽核/掃描/檢測/差異比對/修復管線），依主題併入既有的 `scaffolding-templating`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- bencium.io 發布的第三方開源技能包（MIT 授權）於 2026-08-16 匯入 2 個技能：`typography`（frontmatter 命名為 `ui-typography`，UI 排版正確性強制規則）與 `relationship-design`（agentic/關係中心 UX 設計），依主題併入既有的 `scaffolding-templating`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)。同一天稍晚，同一個 marketplace 又整包安裝了 `insurgent-campaign`（併入 `marketing`），並從另外 5 個未整包安裝的技能（`bencium-innovative-ux-designer`／`bencium-impact-designer`／`design-audit`／`human-architect-mindset`／`bencium-aeo`）各抽出一個機制折進既有檔案——完整清單見 `THIRD-PARTY-LICENSES.md` 的 bencium.io 段落
- Nous Research 發布的第三方開源專案 `hermes-agent`（[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)，MIT 授權）的 `skills/creative/` 資料夾於 2026-08-16 匯入 3 個技能：`popular-web-designs`（54 個真實網站設計系統目錄，另credit Teknium/VoltAgent 為資料來源）、`design-md`（Google 開放 `DESIGN.md` 規格的作者/驗證/匯出工具）、`baoyu-infographic`（21 版面×21 風格資訊圖產生器，原作者為 宝玉/JimLiu，經 hermes-agent 改編），依主題併入既有的 `scaffolding-templating`，完整授權全文與逐項作者歸屬見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)。同一天稍晚，同一個來源又整包安裝了 `p5js`與`sketch`（`sketch` 另具名 credit GSD 專案原作者 Lex Christopherson），並從 `claude-design` 抽出「Surface-First」機制折進既有的 `frontend-design`
- shadcn/ui 發布的官方開源技能倉庫（[github.com/shadcn-ui/ui](https://github.com/shadcn-ui/ui)，MIT 授權）於 2026-08-16 匯入 2 個技能：`shadcn`（frontmatter 命名，資料夾為 `shadcn-official`，最新 CLI/registry/MCP server 工作流程與 styling/forms/composition/icons/chat 規則）與 `migrate-radix-to-base`（shadcn 官方的 Radix→Base UI 遷移引擎），皆整包逐位元組原樣搬入，依主題併入既有的 `scaffolding-templating`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Magic UI Design 發布的官方開源技能倉庫 `magicui`（[github.com/magicuidesign/magicui](https://github.com/magicuidesign/magicui)，MIT 授權）於 2026-08-16 匯入，內含官方 skill（`SKILL.md`／`references/components.md`／`references/recipes.md`，逐位元組原樣搬入）外加本倉庫自行撰寫、內嵌 20 個真實元件原始碼的 `references/source-catalog.md`（授權允許嵌入原始碼，這點與下面的 react-bits 不同），依主題併入既有的 `scaffolding-templating`，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- David Haz 發布的第三方開源專案 `react-bits`（[github.com/DavidHDev/react-bits](https://github.com/DavidHDev/react-bits)，**MIT + Commons Clause 授權，非標準 MIT**）於 2026-08-16 匯入，內含單一技能 `react-bits`，依主題併入既有的 `scaffolding-templating`；因授權明文禁止「重新散布元件本身」，本技能**刻意不內嵌任何原始碼**，只有分類目錄、比較文件與官方 CLI 安裝指令，完整授權全文與限制說明見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)
- Adobe 發布的官方開源專案 `react-spectrum`（[github.com/adobe/react-spectrum](https://github.com/adobe/react-spectrum)，Apache-2.0 授權）於 2026-08-16 匯入，內含單一技能 `react-aria`（無樣式、高無障礙覆蓋率、深度國際化的 headless React 元件庫），依主題併入既有的 `library-api-reference`；官方文件網站在本環境連線失敗，內容改由倉庫本身的套件 README、`AGENTS.md` 分層說明與官方 Tailwind starter kit 的真實原始碼建置而成，完整授權全文見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)

**本倉庫真正屬於維護者自己的部分，只有：**
- 這份 [`README.md`](README.md) 與 [`SKILL.md`](SKILL.md) 這兩份「索引/分類文件」本身的撰寫、分類方式、安裝說明與常見錯誤排解
- 把原本 137 個零散技能重新分類、合併成 18 個頂層資料夾的組織方式

**使用與再分發前請注意：**
1. 若某技能資料夾內附有自己的 `LICENSE`／`README`／作者署名，該檔案的授權條款優先適用，請自行查閱並遵守。
2. 若資料夾內沒有附授權說明，並不代表沒有著作權——請自行查證原始出處，勿直接用於商業散布。
3. 本倉庫僅供個人學習、研究與技術參考用途；若你是某技能的原作者，認為收錄方式有侵權疑慮，歡迎透過 Issue 聯繫，會立即移除或補上正確署名。
4. 本倉庫不對任何技能內容的正確性、授權狀態做擔保。

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

## 🔧 安裝方式

Skill 本質上就是一個「內含 `SKILL.md`（YAML frontmatter + Markdown）的資料夾」，不需要編譯、不需要伺服器，只要放到 AI 工具會掃描的路徑就能生效。以下依工具分別說明。

**前置步驟：先把這個倉庫 clone 下來**

```bash
git clone https://github.com/Lolalayaya/Skills-Directory.git
cd Skills-Directory
```

之後範例裡的 `<path-to-repo>` 都是指你 clone 下來的這個資料夾的完整路徑。

### Claude Code

Claude Code 會掃描兩個層級的 `skills/` 目錄，兩者可以並存：

| 層級 | 路徑 | 生效範圍 | 適合放 |
|---|---|---|---|
| **專案級** | `<你的專案>/.claude/skills/<skill-name>/` | 只在該專案生效，會進版控 | 跟該專案高度相關、要與團隊共享的技能 |
| **使用者級（全域）** | `~/.claude/skills/<skill-name>/`（Windows 為 `C:\Users\<user>\.claude\skills\<skill-name>\`） | 所有專案都能用 | 通用技能，例如本倉庫這 18 個 |

**安裝步驟（以本倉庫任一技能資料夾為例，例如 `agentic-dev-workflow`）：**

1. **直接複製**（最簡單、最穩定）：
   ```bash
   # macOS/Linux
   cp -r agentic-dev-workflow ~/.claude/skills/

   # Windows PowerShell（先 git clone 這個倉庫，再把 <path-to-repo> 換成你實際 clone 到的路徑）
   Copy-Item -Recurse "<path-to-repo>\agentic-dev-workflow" "$HOME\.claude\skills\"
   ```
2. **或建立 symlink**（方便之後 `git pull` 這個倉庫就能同步更新，但 Windows 需要額外權限，見下方常見錯誤）：
   ```bash
   # macOS/Linux
   ln -s /path/to/Skills-Directory/agentic-dev-workflow ~/.claude/skills/agentic-dev-workflow

   # Windows（需以系統管理員身分執行 PowerShell，或先開啟「開發人員模式」；<path-to-repo> 換成你實際 clone 到的路徑）
   New-Item -ItemType SymbolicLink -Path "$HOME\.claude\skills\agentic-dev-workflow" -Target "<path-to-repo>\agentic-dev-workflow"
   ```
3. 重新開啟 Claude Code（或新開一個對話），輸入 `/skills` 確認技能已被列出。
4. 若技能有巢狀的 `references/<子技能>/SKILL.md`，不需要額外處理——Claude Code 會依你的任務描述自動判斷要不要深入讀取子技能，不用整包都放進頂層。

> 想一次裝全部 18 個技能？直接把整個 `Skills-Directory` 底下的 18 個資料夾都複製或 symlink 進 `~/.claude/skills/` 即可（`README.md`、`SKILL.md` 這兩份索引檔留在原倉庫，不用複製）。

### 其他支援 Skill 的 AI CLI（Codex、GitHub Copilot CLI、Gemini CLI）

這幾個工具都額外認得 `~/.agents/skills/` 這個「跨工具共用路徑」（cross-runtime alias），把技能放這裡，Claude Code 與上述工具可以共用同一份，不用複製多份：

```bash
mkdir -p ~/.agents/skills
cp -r agentic-dev-workflow ~/.agents/skills/
```

### 沒有原生 Skill 機制的 AI 工具（Cursor、Windsurf、一般 Chat 介面等）

因為 `SKILL.md` 就是純 Markdown，即使工具沒有「skill」這個概念，也可以手動搬過去：

- **Cursor**：把 `SKILL.md` 內容貼進 `.cursor/rules/<skill-name>.mdc`，或整份放進 `.cursorrules`。
- **通用做法**：把 `SKILL.md`（連同它引用的 `references/*.md`）當成一份「系統提示片段」，貼進該工具的 system prompt / custom instructions 欄位，或是專案根目錄的 `AGENTS.md` / `CLAUDE.md`（多數新一代 CLI 工具都會自動讀取專案根目錄的這類檔案）。
- 若技能內容太長，優先貼 frontmatter 的 `description` 與 Overview／Quick Reference 段落，`references/` 底下的細節留給工具需要時再貼。

---

## 🔁 全域必用技能（Universal — 不用等使用者開口）

以下 5 個子技能帶有「always / MUST / before any」等強制語氣，理論上**每次符合情境就該主動套用**，不需要使用者明確要求。（2026-08-02 匯入 `ip-guard` 時也套用了同一套判斷標準：它自己的說明文字寫得像「任何程式碼/內容產出前都要自動觸發」，範圍比下表這 5 個更廣，但經與使用者確認後，決定不列入此表——維持一般子技能、觸發粒度限定在「每個完成的檔案/artifact」與「每次新增外部相依套件」，理由與完整討論見 `SKILL-AUDIT.md`。2026-08-16 匯入 `ui-typography`（`scaffolding-templating`）時同樣遇到這個情況：它的說明文字寫「任何 UI 產出都要靜默自動套用」，比照 `ip-guard` 的先例，預設同樣不列入此表，理由見 `SKILL-AUDIT.md`。）

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

> `agentic-dev-workflow`、`code-quality-review`、`incident-runbooks`、`deep-research`、`skill-authoring`、`personal-learning`、`internal-writing-comms`、`business-automation`、`infrastructure-ops` 這 9 個底下都含有 2026-07-31 匯入的第三方 `mattpocock-skills`（Matt Pocock，MIT）內容，各自的小節裡有標註，完整清單見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)。

---

## 🛠️ 開發流程與品質保證

### 1. `agentic-dev-workflow` — 軟體開發生命週期總成
從探索意圖到收尾分支，涵蓋完整的 agentic 開發流程。包含 **25 個子技能**（其中 14 個來自 2026-07-31 匯入的第三方 `mattpocock-skills`，MIT 授權；1 個來自 2026-08-01 匯入的第三方 `andrej-karpathy-skills`，MIT 授權；1 個來自同日匯入的第三方 `awesome-llm-apps`，Apache-2.0 授權；1 個是 2026-08-16 從 bencium.io 的 `human-architect-mindset` 抽出的片段（MIT 授權）；見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

**核心生命週期（8）**：
- **`using-superpowers`**（🔁必用）— 對話一開始就先判斷該用哪個技能
- **`brainstorming`**（🔁必用）— 任何創意/功能開發前，先探索使用者意圖與需求、釐清設計
- **`writing-plans`** — 拿到需求/規格後，動手寫程式前先產出實作計畫
- **`using-git-worktrees`** — 開始功能開發前，用 git worktree（或原生工具）建立隔離工作區
- **`executing-plans`** — 在獨立 session 中執行已寫好的實作計畫，中途設檢查點
- **`subagent-driven-development`** — 在目前 session 中執行含獨立任務的實作計畫
- **`dispatching-parallel-agents`** — 遇到 2 個以上互不依賴、可平行處理的任務時派發並行 agent
- **`finishing-a-development-branch`** — 實作完成、測試都過了之後，決定怎麼把分支合併/送出

**輕量行為守則（2，1 個來自第三方 `andrej-karpathy-skills`、1 個是 2026-08-16 從 bencium.io 抽出的片段）**：
- **`karpathy-guidelines`** — 撰寫/審查/重構程式碼時的 4 條行為準則濃縮版（動手前先想清楚、精簡優先、只動手術刀式的必要修改、目標導向可驗證的成功條件），是隨時可查的守則而非流程步驟，與 `brainstorming`／`product-verification` 的 TDD/驗證／`code-quality-review` 精神相通但不重複其細節流程
- **`loyalty-mindset`**（抽自第三方 bencium.io 的 `human-architect-mindset`）— 「忠誠度」哲學框架：為什麼堅持既有架構承諾、不追逐每個新框架，是 AI 結構性做不到的人類能力；附 Loyalty Decision Matrix 與 5 個具名反樣式（Endless Pivot、Greenfield Fallacy 等）。評估是否該遷移/重寫/放棄既有架構承諾時查閱

**雜亂輸入前處理（1，來自第三方 `awesome-llm-apps`）**：
- **`thinking-out-loud`** — 收到一長串雜亂、語音口述式的碎念輸入時，先產出「echo 摘要」（含推論/猜測的標註區）讓使用者確認，才動手做任何事；確認後若內容是要做功能設計，銜接到 `brainstorming` 繼續

**逼問式規劃工具（10，與上面的 brainstorming/writing-plans 互補，不是取代）**：
- **`ask-matt`** — 這批工具自己的流程路由，不確定該用哪個先問這個
- **`grilling`**／**`grill-me`** — 逼問式訪談逼出計畫裡的隱藏假設，預設一次一題、`--batch` 可整批問
- **`grill-with-docs`** — 同樣的逼問訪談，但邊做邊更新專案的 `CONTEXT.md`/ADR（有 codebase 時用）
- **`domain-modeling`** — 挑戰模糊詞彙、解決一詞多義、把不可逆決策記成 ADR
- **`to-spec`** — 把對話合成一份 spec 並發布到 issue tracker
- **`to-tickets`** — 把計畫/spec 拆成宣告依賴關係的 tracer-bullet 票
- **`wayfinder`** — 處理超出單一 session 能扛的超大型灰地專案，用決策票地圖逐步解開
- **`request-refactor-plan`** — 把重構請求拆成最小可逐步提交的步驟
- **`prototype`** — 拋棄式原型驗證單一設計問題，驗完即刪（若要「同一個 UI 元件的多個版本並排比較」，是 `scaffolding-templating` 底下的 `prototype-variants`，不是這個）
- **`setup-matt-pocock-skills`** — 上面這批工具的一次性專案設定（issue tracker、triage 標籤等）

**Session／git 機制（4）**：
- **`handoff`** — 把對話壓縮成交接文件，CLI 支援背景 agent 就直接 launch，否則存檔給下一個 session
- **`resolving-merge-conflicts`** — 逐個 hunk 解決進行中的 merge/rebase 衝突，禁止 `--abort`
- **`git-guardrails-claude-code`** — 攔截危險 git 指令（`push --force`、`reset --hard` 等）的 hook

### 2. `product-verification` — 讓「完成」有憑有據
證明修好的功能/bug 真的可行，而不是憑感覺宣稱完成。包含 **4 個子技能**（其中 1 個來自第三方 `taste-skill`，MIT 授權；見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`test-driven-development`**（🔁必用）— 實作任何功能/修 bug 前，先寫測試（red-green-refactor）
- **`verification-before-completion`**（🔁必用）— 宣稱完成前，必須實際跑驗證指令並讀懂輸出
- **`webapp-testing`** — 用 Playwright 對本地網頁應用做互動測試，含截圖、console log、UI 除錯
- **`output-skill`**（來自第三方 `taste-skill`）— 禁止 LLM 輸出截斷/佔位符（`// rest of code`、「為簡潔省略」等），逼你先數清楚要交付幾項再動筆，並定義 token 上限時的暫停/續寫格式；跟 `verification-before-completion` 是相鄰但不同的軸線——那個管「宣稱完成前有沒有驗證」，這個管「這次產出有沒有被悄悄截斷」

### 3. `code-quality-review` — 程式碼審查與安全性
標準化「程式碼怎麼被審查與掃描」。包含 **14 個子技能**（其中 6 個來自第三方 `mattpocock-skills`，MIT 授權；1 個來自第三方 `awesome-llm-apps`，Apache-2.0 授權；1 個來自第三方 `claude-skill-ip-guard`，Apache-2.0 授權；見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`ip-guard`**（來自第三方 `claude-skill-ip-guard`）— 產生程式碼/內容前先宣告專案授權目標，新增外部相依套件時做授權相容性檢查與遞移相依套件安全掃描（OSV 資料庫、隔離套件狀態），每完成一個檔案/artifact 就附加一份 provenance block；觸發粒度是「每個完成的檔案」與「每次新增外部相依套件」，不是每次回應都觸發，也未列入本倉庫的「全域必用」清單（理由見 `SKILL-AUDIT.md`）；跟 `code-security`（一般資安）、`llm-security` 的 supply-chain 章節（LLM/模型供應鏈，不是一般 npm/pip/cargo 套件授權）是不同軸線，不重疊
- **`scope-creep-detector`**（來自第三方 `awesome-llm-apps`）— 開 PR 前，比對 git diff 跟原本宣稱的意圖，抓範圍蔓延/新依賴/API 改名/設定檔異動，給出 keep/split/justify 建議；純範圍分流，不做品質/安全審查（見 `code-review-expert`）
- **`code-review-expert`** — 以資深工程師視角審查目前 git 變更，抓 SOLID 違規與安全風險
- **`semgrep`** — 靜態分析工具，含撰寫自訂 Semgrep 規則
- **`code-security`**（🔁必用）— 涉及輸入/驗證/檔案/DB/網路/加密/基礎設施設定的程式碼安全守則
- **`llm-security`** — LLM/RAG 應用程式的安全性（OWASP Top 10 for LLM）
- **`requesting-code-review`** — 完成任務、實作重要功能或合併前，如何「提出」程式碼審查請求
- **`receiving-code-review`** — 收到審查意見後如何嚴謹回應、驗證，而非照單全收或表面敷衍
- **`code-review`** — 另一套審查框架：Standards+Spec 雙軸審查、Fowler smell 基準（跟 `code-review-expert` 二選一，不要同一次審查兩邊都用）
- **`improve-codebase-architecture`** — 掃描 codebase 找深模組化機會，產出視覺化 HTML 報告
- **`codebase-design`** — 深模組設計詞彙（module/interface/depth/seam/adapter/leverage/locality）
- **`design-an-interface`** — 多個子代理各自產生不同限制條件下的模組介面設計，再比較取捨（作者已棄用，健檢信心不一，先保留觀察）
- **`setup-ts-deep-modules`** — 用 dependency-cruiser 強制 TS 套件只能透過入口檔案被外部引用
- **`setup-pre-commit`** — 設定 Husky+lint-staged+Prettier 的 pre-commit hook

### 4. `incident-runbooks` — 系統化除錯方法論
包含 **4 個子技能**（其中 2 個來自第三方 `mattpocock-skills`，MIT 授權；1 個來自第三方 `awesome-llm-apps`，Apache-2.0 授權；見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`systematic-debugging`** — 遇到任何 bug、測試失敗或異常行為時，在提出修法前先找出根因、影響範圍，並記錄成可重用的診斷紀錄。已融合 mattpocock 原 `diagnosing-bugs` 的獨特內容：先建可靠紅色訊號迴圈的方法論、多假設排序、debug tag 慣例
- **`commit-archaeologist`**（來自第三方 `awesome-llm-apps`）— 動手重構/改動風險程式碼前，用本地 git 歷史（非僅 blame）重建「這段程式碼為什麼存在」：起源 commit、後續變更、常一起改的檔案、commit 訊息裡的意圖線索
- **`triage`** — 用狀態機處理外部湧入、還沒整理過的 bug 回報/需求，產出 agent 可直接接手的 issue
- **`qa`** — 使用者口語描述 bug 時，背景探索程式碼理解領域語言，拆解建成 GitHub issue

### 5. `openspec-workflow` — OpenSpec 變更生命週期
包含 **5 個子技能**：

- **`openspec-explore`** — 進入探索模式，動手前先思考問題、釐清需求
- **`openspec-propose`** — 一次生成完整提案（含設計、規格、任務清單）
- **`openspec-apply-change`** — 實作 OpenSpec 變更中的任務
- **`openspec-sync-specs`** — 把 delta spec 的變更同步回主要規格文件（不歸檔）
- **`openspec-archive-change`** — 實作完成後歸檔並定案該變更

### 6. `skill-authoring` — 打造/優化技能本身
包含 **5 個子技能**（其中 1 個來自第三方 `mattpocock-skills`，見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`skill-creator`** — 從零建立新技能、修改既有技能、跑評測衡量表現
- **`skill-forge`** — 技能鍛造/優化工具
- **`skill-review`** — 上線前依最佳實踐審查技能
- **`writing-skills`** — 撰寫新技能、編輯既有技能、部署前驗證是否可用
- **`writing-great-skills`** — 撰寫/編輯技能的詞彙與原則參考，隨時可查（跟 `writing-skills` 的差異：前者是參考、後者是上線前的測試關卡）

---

## 🚀 部署與維運

### 7. `cicd-deployment` — 部署到 Vercel
包含 **2 個子技能**：

- **`deploy-to-vercel`** — 互動式部署應用程式/網站到 Vercel（"deploy my app"、"push this live"）
- **`vercel-cli-with-tokens`** — 用 access token（非互動登入）方式部署與管理 Vercel 專案，適合 CI 場景

### 8. `data-analysis` — 用真實數據找優化點
包含 **1 個子技能**（目前僅涵蓋 Vercel，之後可擴充其他平台）：

- **`vercel-optimize`** — 分析 Vercel 專案的 Function Invocations、Build Minutes、Fast Data Transfer、Core Web Vitals、快取狀況等，找出真正值得優化、且有數據佐證的成本/效能問題

### 9. `infrastructure-ops` — 互動式設定精靈（日常維運仍未填補）
包含 **1 個子技能**（來自第三方 `mattpocock-skills`，見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`wizard`** — 產生互動式 bash 引導腳本，帶人一步步跑完一次性第三方設定/遷移（開網址、記錄輸入值、寫入 `.env`）

**仍未涵蓋**：日常維運（伺服器管理、資料庫/佇列維運）、防止破壞性指令的防呆機制——`wizard` 只處理「一次性、需要人在場」的設定流程，不是持續性的維運工具，這個缺口還在，不要把 `wizard` 誤當成涵蓋整個 infra-ops 範疇。

---

## 🌐 瀏覽器自動化與研究

### 10. `browser-automation` — Browserbase 全套瀏覽器工具箱
只要任務牽涉「瀏覽網站」「自動化瀏覽器操作」「用真實瀏覽器測試網頁」「除錯失敗的自動化流程」「同步登入狀態」「研究公司/競品/活動」「即時搜尋/查證資料」或「用 Firecrawl CLI 做一次性的網頁搜尋/爬取/監控」都算。包含 **28 個子技能**（其中 1 個 `anysearch` 來自第三方 `anysearch-skill`、12 個來自 Firecrawl 官方的 `firecrawl/cli`＋`firecrawl/skills`，見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`browser`** — 用自然語言 CLI 指令自動化瀏覽器操作（瀏覽、擷取資料、截圖、填表單、點按鈕）
- **`autobrowse`** — 自我改進的瀏覽器自動化：反覆執行任務、讀 trace、優化導覽策略直到穩定
- **`ui-test`** — AI 驅動的對抗式 UI 測試，可只測 git diff 有變更的部分，涵蓋功能正確性、無障礙、RWD、UX 慣例
- **`cookie-sync`** — 把本機 Chrome 的 cookie 同步到 Browserbase，讓 CLI 能存取需要登入的網站
- **`browser-trace`** — 擷取完整 DevTools protocol trace（CDP、截圖、DOM dump），並拆分成可搜尋的分頁區塊，用於除錯
- **`browser-to-api`** — 把觀察到的 HTTP 流量（透過 browser-trace）轉換成 OpenAPI 3.1 規格文件
- **`webmcp-gen`** — 針對目標網站產生、編譯、驗證 WebMCP 初始化腳本
- **`functions`** — 把瀏覽器自動化部署成 Browserbase 的無伺服器雲端函式（排程、webhook）
- **`fetch`** — 不開瀏覽器、直接抓取 URL 的 HTML/JSON、檢查狀態碼與 header，適合簡單爬蟲
- **`search`** — 不開瀏覽器、直接做網路搜尋，回傳結構化的標題/URL/作者/日期（Browserbase 專用）
- **`anysearch`** — 統一即時搜尋 API（第三方 AnySearch 服務）：一般網路搜尋、16 個垂直領域結構化搜尋（finance/academic/travel/health/code/legal 等）、平行批次查詢、URL 全頁內容擷取，附跨平台 CLI（Python/Node/PowerShell/Bash 自動偵測），API Key 可選（匿名存取限額較低）
- **`agent-experience`** — 讓網站對「AI agent 存取」更友善的相關指引
- **`company-research`** — 針對特定公司的研究
- **`competitor-analysis`** — 競品分析
- **`competitor-profiling`** — 競品側寫（更完整的競品畫像）
- **`event-prospecting`** — 活動/研討會開發潛在客戶

**Firecrawl CLI 叢集**（來自第三方 Firecrawl 官方倉庫，ISC 授權；這次 session 內的即時網頁工作，跟 `library-api-reference` 底下的 `firecrawl-build*` 應用整合技能是不同工作）：

- **`firecrawl-cli`** — 總覽/入口技能，search→scrape→map→crawl→monitor→interact 的升級路徑指引
- **`firecrawl-search`** — 網頁搜尋，可選完整頁面內容，`--categories developer` 走開發者索引
- **`firecrawl-scrape`** — 從已知 URL 擷取乾淨 Markdown，支援 JS 渲染的 SPA、多 URL 平行處理
- **`firecrawl-map`** — 探索/列出網站所有 URL，可用關鍵字過濾
- **`firecrawl-crawl`** — 批次擷取整個網站或區段（例如所有 `/docs/`）
- **`firecrawl-monitor`** — 排程式的變更偵測（頁面或整個網路），內建 AI 雜訊過濾判斷、webhook/email 通知
- **`firecrawl-interact`** — 擷取後的即時瀏覽器互動：點擊、填表單、翻頁、登入、持久化 profile
- **`firecrawl-download`** — 把整個網站批次下載成本機檔案
- **`firecrawl-agent`** — AI 驅動的自動化多頁結構化資料擷取（附 JSON schema）
- **`firecrawl-parse`** — 把本機檔案（PDF/DOCX/DOC/ODT/RTF/XLSX/XLS/HTML）轉成 Markdown，可選 AI 摘要/問答
- **`firecrawl-developer-index`** — 從 GitHub issue/PR/README/文件回答開發問題，回傳實際命中段落
- **`firecrawl-research-index`** — Firecrawl 自己的論文摘要語料庫語意搜尋（PubMed/bioRxiv/medRxiv 為主+arXiv），含引用圖擴展與全文驗證

> `search`／`anysearch`／`firecrawl-*` 三者都能做搜尋但機制不同，完整比較見 `browser-automation/SKILL.md` 的「Note on the Firecrawl CLI cluster vs. `search`/`anysearch`/`fetch`」小節。

### 11. `deep-research` — 通用主題研究流程（中文）
先產生研究大綱，再擴充欄位/研究對象，接著為每個項目派出獨立的深度研究 agent，最後彙整成一份 Markdown 報告。適合學術研究、技術/產品比較、或任何「幫我研究這個主題並給結構化報告」的需求。包含 **6 個子技能**（其中 1 個來自第三方 `mattpocock-skills`，見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`research`** — 對目標主題做初步調研，產生調研大綱
- **`research-add-fields`** — 向既有大綱補充欄位定義
- **`research-add-items`** — 向既有大綱補充研究對象（items）
- **`research-deep`** — 讀取大綱，為每個 item 各自啟動獨立 agent 做深度調研
- **`research-report`** — 把深度調研結果彙整成涵蓋所有欄位的 Markdown 報告
- **`background-research`** — 單一問題的一次性背景查證，產出一份帶引用的筆記（不是這條 pipeline 的一部分，沒有 outline/多 agent 結構）

---

## 🎨 內容、文件與設計

### 12. `scaffolding-templating` — 樣板、腳手架與完整設計系統
把最佳實踐轉換成可直接套用的樣板、腳手架、色彩/字體系統與參考資料庫。包含 **54 個子技能**（其中 12 個來自第三方 `taste-skill`、1 個來自第三方 `hallmark`（皆 MIT）、9 個來自第三方 `emilkowalski/skills`（MIT）、5 個來自第三方 `AccessLint/skills`（MIT）、2 個來自第三方 bencium.io（MIT）、5 個來自第三方 `NousResearch/hermes-agent`（MIT，含 2026-08-16 稍晚整包安裝的 `p5js`／`sketch`）、2 個逐位元組原樣搬入的 shadcn/ui 官方技能（`shadcn-official`／`migrate-radix-to-base`，MIT）、1 個 Magic UI 官方技能＋本倉庫自撰的原始碼目錄（`magicui`，MIT）、1 個純比較文件無內嵌原始碼的第三方技能（`react-bits`，MIT+Commons Clause，2026-08-16）；另有 5 處小片段（Surface-First 步驟、玻璃擬態禁令、Creative Reframing Prompts、分階段稽核模式、Authority 表格）折進既有檔案，不算新增檔案；此數字也修正了前一輪陳述的 47（實際檔案數應為 48）這個一次性的算術誤差，見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`programmatic-seo`** — 用資料驅動的方式大量產生 SEO 頁面樣板
- **`design`** — 一般性設計指引
- **`design-system`** — 三層設計 token（primitive→semantic→component）、元件規格、投影片產生
- **`ui-styling`** — shadcn/Tailwind 為主的 UI 樣式規範；另見下方 `shadcn-official` 取得最新 CLI/registry/MCP 資訊
- **`shadcn-official`**（frontmatter 命名為 `shadcn`，來自 shadcn/ui 官方，MIT）— shadcn/ui 官方自帶的 Claude skill，逐位元組原樣搬入：最新 CLI 指令、registry 發布/命名空間、MCP server 整合、styling/forms/composition/icons/chat 規則
- **`migrate-radix-to-base`**（來自 shadcn/ui 官方，MIT）— shadcn 官方的 Radix→Base UI 遷移引擎，逐元件或整專案遷移，附三方合併保留客製化；跟 `pick-ui-library` 預設推薦 base-ui 的立場互補而非衝突：新專案看 `pick-ui-library`，既有 shadcn+Radix 專案要遷移看這裡
- **`magicui`**（來自 Magic UI 官方，MIT）— 官方 skill（CLI 安裝流程、元件分類）+ 本倉庫自撰、內嵌 20 個真實元件原始碼的目錄；shadcn+Tailwind+Framer Motion 原生的動畫元件庫
- **`react-bits`**（來自第三方 `react-bits`，**MIT+Commons Clause**）— 框架無關的動畫特效元件庫（165+ 元件，另有 Vue/Svelte 版本）；授權禁止重新散布元件本身，本技能刻意**不內嵌任何原始碼**，只有分類目錄、跟 `magicui` 的完整比較表、官方 CLI 安裝指令
- **`ui-ux-pro-max`** — 可搜尋的本地 UI/UX 資料庫（67 種風格、161 組配色、57 組字體搭配、25 種圖表、21 種技術棧）
- **`banner-design`** — 橫幅/Banner 設計
- **`brand`** — 品牌語氣、視覺識別、訊息框架、資產管理與一致性
- **`anthropic-brand-guidelines`** — 套用 Anthropic 官方品牌色彩與字體規範
- **`canvas-design`** — 產出海報等靜態視覺藝術（PNG/PDF）
- **`algorithmic-art`** — 用 p5.js 搭配種子隨機數產生演算法藝術（flow field、粒子系統等）；比 `p5js`（見下方 hermes-agent 小節）窄、哲學優先，`p5js` 是更廣的技巧庫+真正的匯出管線
- **`theme-factory`** — 為 artifact（投影片、文件、報表、HTML 頁面等）套用/產生主題（內建 10 組預設主題）
- **`frontend-design`** — 打造有個性、非樣板感的 UI 視覺方向、字體排印；2026-08-16 新增「Surface-First」前置步驟（抽自第三方 hermes-agent 的 `claude-design`，MIT）：動手設計前先講清楚這是 7 種介面 archetype 中的哪一種
- **`web-artifacts-builder`** — 用 React、Tailwind、shadcn/ui 打造複雜、需要狀態管理/路由的 claude.ai HTML artifact
- **`web-design-guidelines`** — 依 Web Interface Guidelines 審查 UI 程式碼（無障礙、UX）
- **`writing-guidelines`** — 依 Writing Guidelines 審查文件/文案語氣風格
- **`slides`** — 用 Chart.js、design token、文案公式打造策略性 HTML 簡報
- **`taste-skill`**（來自第三方 `taste-skill`）— 落地頁/portfolio/改版的反樣板前端技能：先推斷一句話「design read」，設定 3 個數值旋鈕（variance/motion/density），依 brief 判斷該接官方設計系統（Fluent/Material/Carbon 等）還是原生 CSS 美學，附排版/色彩/圖片/文案硬規則與 GSAP 程式碼骨架；2026-08-16 新增選用的 §0.E「Creative Reframing Prompts」（抽自第三方 bencium.io 的 `bencium-impact-designer`，MIT）——設計師/情境/年代三組聯想提示，非強制
- **`taste-skill-v1`**（來自第三方 `taste-skill`）— 上面 `taste-skill` 改版前的舊版，僅為需要精確舊行為的專案保留
- **`hallmark`**（來自第三方 `hallmark`）— 另一套反樣板前端設計系統，自帶 `audit`／`redesign`／`study`（可從 URL 或截圖萃取設計 DNA）動詞、20 種具名主題目錄+客製 OKLCH 分支、跨 session 持久化的多樣性紀錄（強制這次跟前幾次的巨觀結構/主題/nav/footer 不同）、58 條出貨前檢查關卡；跟 `taste-skill` 主題重疊但機制完全不同，兩者擇一使用、不要同一次建置混用（怎麼選見下方提示）。2026-08-16 `audit` 動詞新增「doc-grounded, phased」替代模式（抽自第三方 bencium.io 的 `design-audit`）：專案有 `DESIGN_SYSTEM.md` 等既有文件時，先讀文件、再分階段取得核准才動手，不取代預設的扁平清單行為。注意：`hallmark` 自己的素材仍把玻璃擬態視為 Apple 系品牌時情境合理，跟上面 `redesign-skill` 的禁令不一致——這個張力刻意保留未處理，見 `SKILL-AUDIT.md`
- **`brandkit`**（來自第三方 `taste-skill`）— 品牌識別板/Logo 系統/識別手冊的**圖片生成**技能（不是文字型品牌語氣文件，那是上面的 `brand`）
- **`brutalist-skill`**（來自第三方 `taste-skill`）— Swiss 印刷+軍事終端融合的工業感 UI，適合數據密集儀表板/portfolio/編輯類站點
- **`gpt-tasteskill`**（來自第三方 `taste-skill`）— GSAP 動態工程+AIDA 頁面結構+模擬 Python 偽隨機排版變化，Awwwards 等級的動態網站
- **`image-to-code-skill`**（來自第三方 `taste-skill`）— 先生成設計參考圖、深入分析後再依圖寫程式碼，寫給 Codex 類型的圖片優先工作流
- **`imagegen-frontend-mobile`**（來自第三方 `taste-skill`）— 純圖片生成（不寫程式碼）的手機 App 畫面概念，含裝置外框 mockup
- **`imagegen-frontend-web`**（來自第三方 `taste-skill`）— 純圖片生成（不寫程式碼）的網頁分區塊參考圖，一個區塊一張圖
- **`minimalist-skill`**（來自第三方 `taste-skill`）— 暖色調極簡編輯風 UI：無漸層、無重陰影、扁平 bento grid
- **`redesign-skill`**（來自第三方 `taste-skill`）— 既有網站/App 的稽核式升級改版，不換框架不破壞功能；2026-08-16 玻璃擬態建議已翻轉成禁令（原因是跟第三方 bencium.io 的 `bencium-innovative-ux-designer` 衝突，見 `SKILL-AUDIT.md`）
- **`soft-skill`**（來自第三方 `taste-skill`）—「$150k 代理商級」視覺規格：禁用字體/圖示/陰影/版型/動態清單、雙層卡片架構、出貨前檢查清單
- **`stitch-skill`**（來自第三方 `taste-skill`）— 產生給 Google Stitch 用的語義化 `DESIGN.md`，把同一套反樣板規則翻譯成 Stitch 的自然語言設計描述格式

> **`taste-skill` vs `hallmark` 怎麼選**（二者機制不同、規則會互相打架，不要同一次建置混用）：
> - 需要接**官方設計系統**（Fluent UI/Material 3/Carbon/govuk-frontend 等），或只是**單次輕量**建置 → `taste-skill`
> - 同一個專案要生成**多頁/多次建置**且要求每次不重複，或需要「**只稽核不改**」「**從 URL/截圖萃取設計風格**」→ `hallmark`
> - 升級既有網站 → `hallmark redesign` 或獨立的 `redesign-skill`，不要用 `taste-skill` 的預設流程（它假設從零開始）
> - 兩者都沒有特別需求的單次全新頁面 → 皆可，`taste-skill` 較輕量（強制詢問較少），`hallmark` 較嚴謹（58 條出貨前檢查），沒有其他線索就預設 `taste-skill`
>
> 完整比較表（含衝突實例）見 `scaffolding-templating/SKILL.md` 的「`taste-skill` vs `hallmark`」小節。`output-skill`（同樣來自第三方 `taste-skill`，但不是設計技能）併入了 `product-verification`，見上方第 2 節。挑選以上其他反樣板前端技能時的判斷指南見 `scaffolding-templating/SKILL.md` 的「How to use this skill」第 7、8 點。

**動畫、動作工程與 UI 決策工具**（來自第三方 `emilkowalski/skills`，MIT 授權，Emil Kowalski——Sonner/Vaul 作者）——跟上面的反樣板技能不同軸線：上面談視覺語言（顏色/排版/具名美學），這裡談動作本身的機制（曲線、彈簧物理、手勢速度、可中斷性、效能）：

- **`emil-design-eng`** — 主要入口技能，Emil Kowalski 整體審美/打磨哲學，涵蓋元件設計與動畫決策
- **`animate`** — 從零建構動畫：該不該動、用什麼工具、什麼曲線/時長/彈簧設定
- **`review-animations`** — 依 10 條硬性標準嚴格審查 diff 裡的動畫/動作程式碼，預設打回、核准需憑證據
- **`improve-animations`** — 唯讀，稽核整個 codebase 的動作程式碼，產出優先順序清單與可執行的修復計畫
- **`find-animation-opportunities`** — 唯讀，掃描 UI 找出值得加動畫的地方，並明確列出刻意不建議的
- **`animation-vocabulary`** — 動畫效果反查詞彙表（把「開合時那個彈一下的效果」轉成正確術語）
- **`apple-design`** — Apple WWDC 系列設計/流體動作原則：彈簧物理、手勢可中斷性、慣性投射、材質/景深、字體排印
- **`pick-ui-library`** — 依任務從一份精選清單推薦前端函式庫（toast/dropdown/圖表/拖曳/狀態管理等），只在明確呼叫時執行
- **`prototype-variants`** — 建構同一個 UI 元件的多個真正不同版本，放在視覺選擇器背後即時比較後再整合；因與既有的 `agentic-dev-workflow` 底下的 `prototype`（單次驗證用）撞名而改名，只在明確呼叫時執行

> 這 9 個技能跟 `hallmark` 自己的 `references/motion.md` 主題相近但深度不同（`hallmark` 那份只是它自己 pipeline 裡的一個小分支，約 109 行；這裡是完整獨立的動作工程系統），並非重複，兩邊已互相加交叉引用。挑選指南與 pipeline 用法見 `scaffolding-templating/SKILL.md` 的「Animation, motion & UI-decision tools」小節與「How to use this skill」第 9 點。

**無障礙（WCAG）稽核、掃描、檢測、差異比對與修復**（來自第三方 `AccessLint/skills`，MIT 授權，2026-08-16 匯入）——本倉庫先前沒有的全新軸線：

- **`accessibility-audit`** — 整站 WCAG 2.2 稽核（WCAG-EM）：定範圍、抽樣頁面/流程、對每個樣本跑下面兩層、彙整一份符合性報告
- **`accessibility-scan`** — 單頁自動化層：透過 CDP 對即時頁面跑規則引擎，回傳含 DOM selector 與 `file:line` 的違規清單；只定位不修
- **`accessibility-inspect`** — 單頁手動層：鍵盤/焦點順序/螢幕報讀器名稱/reflow/減少動態等規則引擎判斷不了的檢查，依證據基礎分級（●已驗證／◐待人工確認／○需人工）
- **`accessibility-diff`** — 迴歸檢查：比對頁面違規與未提交變更（預設）或某個分支，可當 CI gate 用
- **`accessibility-fix`** — 只做修復：對目標或既有的問題清單跑基準→編輯→再驗證迴圈，判斷性修法留 TODO

> **操作性需求（非單純廠商行銷文件，務必留意）**：這組技能的 `.mcp.json`（讀取但未搬入）宣告需要一個 MCP server `accesslint`（`npx -y @accesslint/mcp@latest`），`accessibility-audit`／`accessibility-fix` 直接呼叫它提供的 `list_rules`／`explain_rule`／`audit_html`／`audit_live` 工具；`accessibility-inspect` 另外需要連接一個瀏覽器驅動 MCP（建議 `chrome-devtools`，或 `playwright`／`puppeteer`）才能做鍵盤/焦點/狀態檢查，沒接的話會退回只做靜態檢查、其餘回報為 `○` 人工待辦。`accessibility-scan`／`accessibility-diff` 不需要這兩個 MCP，自帶 `npx @accesslint/chrome`／`@accesslint/cli` 管理自己的 headless Chrome。詳見 `scaffolding-templating/SKILL.md` 的「Accessibility auditing」小節。

**排版正確性與 agentic UX 設計哲學**（來自第三方 bencium.io，MIT 授權，2026-08-16 匯入）：

- **`ui-typography`**（資料夾名稱因與 frontmatter `name:` 保持一致而統一為 `ui-typography`，來源本身是 `typography`）— 依 Matthew Butterick《Practical Typography》整理的排版正確性規則（引號、破折號、間距、階層、字距）；自己的 description 讀起來像「任何 UI 產出都要自動靜默套用」，比照 `ip-guard` 先例**未**列入全域必用清單，判斷理由見 `SKILL-AUDIT.md`
- **`relationship-design`** — agentic/關係中心 UX 設計：圍繞記憶、信任演化、跨 session 協作規劃來設計 AI-first 介面；自己的 frontmatter 明講只在使用者明確要求時使用

**設計參考目錄與規格產生器**（來自第三方 `NousResearch/hermes-agent`，MIT 授權，2026-08-16 匯入，`baoyu-infographic` 另外具名 credit 原作者 宝玉/JimLiu）：

- **`popular-web-designs`** — 54 個真實網站（Stripe、Linear、Vercel 等）的設計系統，現成 HTML/CSS 可套用，適合「做成像某網站」的需求；另 credit Teknium/VoltAgent 的 `awesome-design-md` 為設計系統資料來源
- **`design-md`** — 撰寫/驗證/匯出 Google 開放的 `DESIGN.md` 規格檔（YAML token + 說明文字），透過 `npx @google/design.md` CLI 做 lint（含 WCAG 對比檢查）/diff/匯出 Tailwind 或 DTCG——跟已安裝的 `stitch-skill` 容易被誤認重複，其實不同：`stitch-skill` 是給 Google Stitch 用的自然語言描述、無正式規格無 CLI；`design-md` 是真正可攜、可 lint 的開放規格檔
- **`baoyu-infographic`** — 21 種版面 × 21 種風格自由組合的資訊圖產生器，原作者 宝玉 (JimLiu)，由 hermes-agent 改編

**生成藝術與拋棄式 UI 草稿比較**（同樣來自第三方 `NousResearch/hermes-agent`，MIT 授權，2026-08-16 稍晚整包安裝，屬使用者指定的 9 項精準抽取/整包安裝之一，見 `SKILL-AUDIT.md`）：

- **`p5js`** — 完整 p5.js 生成藝術技巧庫（flow field、curl noise、boid flocking、L-system、圓形堆疊、Voronoi、reaction-diffusion、pixel sorting、WebGL/GLSL shader、audio-reactive）+ 真正的匯出管線（Puppeteer headless 擷取、ffmpeg 轉 MP4、SVG、CCapture.js）；跟上面的 `algorithmic-art` 比較見該條目
- **`sketch`** — 拋棄式 2-3 個 HTML mockup 變體比較：每個變體各自獨立資料夾+各自 README，最後用比較表呈現；跟 `prototype-variants`（同一產物裡即時切換）的差異見該條目。自己的 Attribution 另外具名 credit GSD 專案原作者 Lex Christopherson（MIT © 2025，上游已封存）

### 13. `library-api-reference` — 第三方函式庫/檔案格式參考
在動手寫程式呼叫這些函式庫前，先查這裡的參考片段、版本差異與常見錯誤。包含 **17 個子技能**（其中 5 個來自 Firecrawl 官方的 `firecrawl/skills`（ISC）、2 個來自第三方 `arxiv-skills`（MIT）、1 個來自 Adobe 官方 `react-spectrum`（Apache-2.0），見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`docx`** — 讀寫、建立、編輯 Word（.docx）文件
- **`xlsx`** — 讀寫、建立、編輯 Excel（.xlsx）試算表
- **`pptx`** — 讀寫、建立、編輯 PowerPoint（.pptx）簡報
- **`pdf`** — PDF 的讀取/擷取文字表格、合併、拆分、旋轉、浮水印、建立、表單填寫、加解密、OCR
- **`mcp-builder`** — 打造高品質 MCP（Model Context Protocol）伺服器（Python FastMCP 或 Node/TS MCP SDK）
- **`vercel-react-best-practices`** — Vercel 工程團隊的 React/Next.js 效能優化準則
- **`vercel-react-native-skills`** — React Native 相關技巧
- **`vercel-react-view-transitions`** — React View Transitions API 應用（含 `router.push(href, { transitionTypes })`、Next.js 共享元素的預先擷取/快取時機；2026-08-16 已同步上游最新版，見 `SKILL-AUDIT.md` 的「同日重新同步」小節）
- **`vercel-composition-patterns`** — Vercel/React 組合模式（composition patterns）
- **`react-aria`**（來自 Adobe 官方 `react-spectrum`，Apache-2.0）— 無樣式、高無障礙覆蓋率、深度國際化（RTL、30+ 語系）的 headless React 元件庫（`react-aria-components`）與底層 `@react-aria/*` hooks；官方文件網站本環境連線失敗，內容改由套件 README＋`AGENTS.md` 分層說明＋官方 Tailwind starter kit 真實原始碼建置；該不該選 React Aria（vs. base-ui/Radix）是 `pick-ui-library` 的判斷，這裡只管怎麼用
- **`firecrawl-build`**（來自第三方 `firecrawl/skills`）— 把 Firecrawl 接進應用程式：選新專案/既有專案流程、挑對的 endpoint、裝 SDK、設定 `FIRECRAWL_API_KEY`
- **`firecrawl-build-scrape`**（來自第三方 `firecrawl/skills`）— `/scrape` 整合：已知 URL 的單頁擷取
- **`firecrawl-build-search`**（來自第三方 `firecrawl/skills`）— `/search` 整合：先有查詢字串、還沒有 URL 的探索流程
- **`firecrawl-build-interact`**（來自第三方 `firecrawl/skills`）— `/interact` 整合：擷取後在應用程式碼裡做的瀏覽器動作
- **`firecrawl-build-onboarding`**（來自第三方 `firecrawl/skills`）— 首次把 `FIRECRAWL_API_KEY`／SDK 接進專案、瀏覽器授權流程
- **`arxiv-lookup`**（來自第三方 `arxiv-skills`）— 用 arXiv ID 查期刊 DOI，或用標題/關鍵字查 arXiv ID
- **`arxiv-doc-builder`**（來自第三方 `arxiv-skills`）— 抓取 arXiv 論文（優先 LaTeX 原始碼、PDF 為後備）並轉成結構化 Markdown，供實作參考

> `firecrawl-build*` 跟 `browser-automation` 底下的 `firecrawl-*` CLI 技能是不同工作：這裡是「寫進應用程式原始碼」，那邊是「這次 session 的一次性終端機操作」。

### 14. `internal-writing-comms` — 文件協作與內部溝通
包含 **7 個子技能**（其中 3 個來自第三方 `mattpocock-skills`、1 個來自第三方 `research-paper-writing`、1 個來自第三方 `Humanizer-zh-TW`（皆 MIT），見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`doc-coauthoring`** — 結構化流程協助共同撰寫文件（提案、技術規格、決策文件），透過反覆迭代確認內容對讀者有效
- **`internal-comms`** — 依公司慣用格式撰寫內部溝通（狀態報告、主管更新、公司電子報、FAQ、事故報告、專案更新等）
- **`writing-fragments`** — 純探索階段，挖掘寫作素材片段、不急著定結構
- **`writing-shape`** — 把素材塑形成文章（含敘事節奏的 beat 模式），或編輯既有草稿
- **`to-questionnaire`** — 把答不出來的問題整理成問卷，發給知情人非同步填寫或會議上討論
- **`research-paper-writing`**（來自第三方 `Research-Paper-Writing-Skills`）— 改善 ML/CV/NLP 類學術論文寫作品質：Abstract/Introduction/Method/Experiments/Conclusion 各章節指引、主張—證據對齊檢查、投稿前五維度自我審查
- **`humanizer-zh-tw`**（來自第三方 `Humanizer-zh-TW`）— 依維基百科「Signs of AI writing」去除文字中常見的 AI 寫作痕跡（誇大意義措辭、破折號過度使用、三段式法則等），加入真實聲音；是寫作品質工具，不是規避偵測工具，不觸碰浮水印/來源中繼資料

---

## 📈 行銷

### 15. `marketing` — 全漏斗行銷手冊
只要問題牽涉廣告、SEO、文案、轉換率、定價、Onboarding、流失、Email/SMS、推薦計畫、影響者/社群行銷、產品發布、行銷策略、歸因分析、A/B 測試、業務銷售素材或競品定位——即使使用者沒講出具體的行銷術語也算。內部再分 **5 大子群，共 48 個子技能**（其中 1 個來自第三方 bencium.io 的整包安裝 `insurgent-campaign`，MIT；另有 1 處小片段 Authority 表格折進既有 `ai-seo`，不算新增檔案；見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

**🎯 付費取得與 ASO（`paid-acquisition`，5 個）**
- `ads` — 付費廣告投放策略
- `ad-creative` — 廣告素材設計
- `aso` — App Store / Google Play 上架優化稽核
- `ai-seo` — 針對 AI 搜尋引擎的 SEO；2026-08-16 新增「Authority Level Determines Strategy」補充表格（抽自第三方 bencium.io 的 `bencium-aeo`）——挑戰者站台激進優化、既有權威站台輕觸優化
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

**🔍 研究與策略（`research-strategy`，15 個）**
- `customer-research` — 顧客研究
- `marketing-plan` — 行銷計畫制定
- `marketing-psychology` — 行銷心理學
- `marketing-ideas` — 行銷點子發想
- `marketing-council` — 多角度行銷顧問視角
- `attribution` — 行銷歸因分析；跟下面的 `insurgent-campaign` 共用同一套增量/lift-test 研究基礎，但 `attribution` 是量測方法論，`insurgent-campaign` 是完整策略流程，兩者互補見 `marketing/SKILL.md`
- `analytics` — 數據分析
- `ab-testing` — A/B 測試
- `product-marketing` — 產品行銷
- `prospecting` — 潛在客戶開發
- `public-relations` — 公關
- `revops` — 營收維運（RevOps）
- `sales-enablement` — 業務賦能素材
- `competitors` — 競品分析
- **`insurgent-campaign`**（來自第三方 bencium.io，MIT，2026-08-16 整包安裝）— 弱勢方（新創/NGO/草根運動）對抗財力懸殊對手的分階段草根優先戰役策略：ideation → 財力落差稽核 → message-market-fit 關卡 → 通路分層 70/30 配置 → 3 種戰役形狀擇一 → 30 天行動清單 + lift-test 量測計畫

---

## 📖 學習與任務管理

### 16. `personal-learning` — 個人知識學習工具
包含 **4 個子技能**（其中 1 個來自第三方 `mattpocock-skills`，見 [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)）：

- **`book-study`** — 系統化讀書教練，含間隔重複與精熟度測驗
- **`wiki-ingest`** — 把文章/文件/筆記彙整進結構化的 wiki 知識庫
- **`sigma`** — 一對一蘇格拉底式 AI 家教，適應式引導學習任何主題
- **`teach`** — 把目前目錄當長期教學工作區，圍繞學習動機建課程資產（跟 `sigma` 的差異：這個不做嚴格掌握度追蹤）

### 17. `business-automation` — 跨 session 的檔案化任務規劃
把 `task_plan.md`、`findings.md`、`progress.md` 寫在硬碟上，讓長任務的規劃/進度在 `/clear` 或 context 重置後依然存在。核心邏輯 **1 種，附 2 種語言版本**（阿拉伯文/德文/西班牙文版於 2026-07-31 健檢後移除，因用不到而永遠不會觸發，見 [`SKILL-AUDIT.md`](SKILL-AUDIT.md)），另加 1 個來自第三方 `mattpocock-skills` 的規格設計工具、1 個來自第三方 `awesome-llm-apps`（Apache-2.0 授權）的個人專案盤點工具，共 **5 個子技能**：

- **`planning-with-files`** — 英文版（Manus 風格檔案化規劃系統）
- **`planning-with-files-zh`** — 簡體中文版
- **`planning-with-files-zht`** — 繁體中文版
- **`project-graveyard`**（來自第三方 `awesome-llm-apps`）— 掃描機器上被放棄的側專案，從 git 歷史解剖每個專案的「死因」，找出使用者自己的失敗模式，挑一個最值得復活的並協助動手
- **`loop-me`** — 用逼問訪談把生活/業務裡的重複模式整理成 workflow 規格文件

---

## 🧠 Agent / 上下文工程（進階研究向）

### 18. `context-engineering-collection` — 上下文工程技能全集
唯一一個**保持原樣、未被拆分**的技能（原本就是一個涵蓋 17 個子技能的完整集合，拆開沒有額外價值）。用於打造/優化/評估/除錯需要有效上下文管理與可靠運作迴圈的 agent 系統。包含 `skills/` 底下 **16 個子技能**（`latent-briefing` 於 2026-07-31 健檢後移除，因需要直接操作模型底層 KV cache、幾乎不會被觸發，見 [`SKILL-AUDIT.md`](SKILL-AUDIT.md)；`bdi-mental-states` 經確認後保留）：

- **`context-fundamentals`** — 上下文工程基礎概念
- **`context-compression`** — 長任務的上下文壓縮、結構化摘要、交接摘要
- **`context-degradation`** — 診斷/緩解 lost-in-middle、context poisoning、context clash 等退化問題
- **`context-optimization`** — 上下文效率優化：token 預算、prefix/KV-cache 策略、檢索範圍縮減
- **`filesystem-context`** — 用檔案系統支撐持久化的 scratchpad、工具輸出卸載、跨 agent 交接檔
- **`memory-systems`** — 跨 session 的持久語意記憶：實體追蹤、時效性、圖/向量檢索
- **`multi-agent-patterns`** — 多 agent 系統設計：上下文隔離、supervisor/swarm 協調、平行執行
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
4. 之後若安裝新技能，依下方「新增技能的標準流程」處理，不要只是丟進去就不管，避免索引過時。

---

## ➕ 新增技能的標準流程

2026-07-31 匯入並拆散 `mattpocock-skills` 之後訂出的標準流程（完整實例見 [`SKILL-AUDIT.md`](SKILL-AUDIT.md)）。英文版、給 Claude 讀取的完整版本在根目錄 [`SKILL.md`](SKILL.md) 的「Standard procedure for adding a new skill」。每次有新技能要加入，依序走完以下 4 階段，不要跳著做。

### 階段 A｜評估
1. **確認是否與既有技能重疊或相抵觸**——不能只比對 description 文字。這次同一個 session 裡因為只看 description 就誤判「該合併」，發生了 3 次。務必實際讀完新技能與疑似重疊的既有技能的完整 `SKILL.md`，以及各自綁定的 `scripts/`／`references/`／`agents/`，才能下判斷。

### 階段 B｜決定分類與整併方式
2. **併入現有 18 個分類中最合適的一個**（依主題判斷，不是依來源出處）。真的沒有任何分類合適，才提出來跟使用者討論是否要新增分類——不要自己單方面新增第 19 個分類。（這次就先犯過一次：建立第 19 個頂層技能後，又被要求撤銷改成融入既有分類，融入既有分類才是預設做法，新增分類是需要使用者同意的例外。）
3. **對新內容套用五類分類法**：核心常用／偶爾需要／功能重疊／不確定用途／可能可以刪，作為篩選依據。
4. **遇到「功能重疊」，預設先澄清 description＋互相加註「見 X」的說明，不要預設做實體合併**。只有讀完全文確認雙方是真重疊（核心邏輯相同、沒有各自獨立可用的工具/腳本），且使用者明確要求整合內容，才動手合併。

### 階段 C｜執行搬遷／整合
5. **動手搬移前先查命名衝突**——新技能的資料夾名稱跟 `SKILL.md` 裡的 `name:` frontmatter，都要跟本倉庫現有技能核對一遍（一次全倉庫的 `name:` 查重指令就能做到）。`mv` 到已經存在同名資料夾時**不會報錯、也不會覆蓋**，而是把來源資料夾嵌套進去一層——這是這次實際發生過的 bug，發現衝突就把資料夾名稱跟 frontmatter 的 `name:` 兩個都改掉。
6. **確認內部交叉引用還連得到**——如果新技能包內部靠技能名稱或相對路徑互相引用，搬移/合併/改名後要逐一確認引用還有效（廠商自己的路由文件/README 最容易在這裡出包）。
7. **刪除廠商自帶的分類層級索引檔**——內容分散安置後，這些檔案會立刻跟實際狀態脫節，留著等於兩份會漂移的索引，直接刪除。
8. **處理版權歸屬**：第三方內容整批放單一資料夾，沿用它自己的 LICENSE 即可；分散到多個既有分類，就建立/更新根目錄的 `THIRD-PARTY-LICENSES.md`，並同步更新本 README 的版權聲明段落。
9. **檢查是否夠資格列進「全域必用」**：搜尋新技能全文裡的 `MUST use`／`before any`／`ALWAYS use` 等字樣，但要分清楚「技能自己流程裡的步驟用語」跟「這個技能必須在任何回應前使用」的宣告——多數比對到的都是前者。

### 階段 D｜更新文件
10. **更新每個受影響頂層技能自己的 `SKILL.md`**：新增 Domains 表格列、必要時調整 description、補上跟新鄰居的分工說明。
11. **更新本 README**：受影響分類的小節（新增條目、更新子技能數量、標註第三方來源），以及版權聲明段落。
12. **更新根目錄 `SKILL.md`**：Quick lookup、Full skill list 的子技能數量、審計追蹤註解區塊（新增一筆帶日期的紀錄，不要把舊紀錄改沒了）。
13. **更新 `SKILL-AUDIT.md`**：記下分類結果、安置決策與理由、命名衝突等踩坑細節——這是讓未來的 session 能判斷「這個之前已經考慮過了」而不是重新爭論一次的依據。
14. **更新 `TRIGGER-MAP.md`**：把新子技能的觸發範例併入對應的既有分類小節，不要另立一個獨立區塊（呼應階段 B 第 2 點）。

---

## 🩹 常見錯誤與解決方式

安裝或使用 Skill 時最常遇到的問題，依「安裝期」與「使用期」分類：

### 安裝期

| 錯誤現象 | 原因 | 解決方式 |
|---|---|---|
| `/skills` 列表沒看到新技能 | 資料夾放錯層級，或 `SKILL.md` 沒放在該技能資料夾**最上層** | 確認路徑是 `~/.claude/skills/<name>/SKILL.md`，不是 `~/.claude/skills/SKILL.md` 或多包了一層 |
| 建立 symlink 時出現 `無法建立符號連結，因為用戶端不具備所需的特殊權限`（Windows） | Windows 預設一般使用者不能建立 symlink | 用系統管理員身分開 PowerShell 執行 `New-Item -ItemType SymbolicLink ...`，或到「設定 → 更新與安全性 → 開發人員專用」開啟開發人員模式後即可用一般權限建立；不想處理權限問題就直接用 `Copy-Item -Recurse` 複製即可 |
| YAML frontmatter 解析失敗 / 技能整份被當成純文字忽略 | `description` 裡有沒加引號的冒號（`:`）、或開頭/結尾的 `---` 三個減號寫錯（多了空白、少了換行） | `description` 只要包含冒號就整段用雙引號包起來，例如 `description: "Use when: X happens"`；並確認 frontmatter 上下各只有一行 `---`，前後不能有其他字元 |
| `name` 欄位驗證失敗 | 名稱含空格、底線、括號或中文 | 只能用小寫英文字母、數字、連字號（`-`），例如 `my-skill-name` |
| frontmatter 抓不到內容 / 疑似被截斷 | `name` + `description` 加起來超過 1024 字元上限 | 精簡 `description`，把細節搬到 `SKILL.md` 正文或 `references/` 裡 |
| 兩個技能同時生效、行為互相打架 | 使用者級與專案級同時裝了「同名但版本不同」的技能 | 專案級 `.claude/skills/` 會覆蓋同名的使用者級技能，確認你要生效的是哪一份，另一份改名或移除 |
| Windows 路徑含空白導致複製/連結指令失敗 | PowerShell 指令沒把路徑用雙引號包起來 | 路徑一律加雙引號，例如 `Copy-Item -Recurse "D:\My Folder\skill-name" "$HOME\.claude\skills\"` |

### 使用期

| 錯誤現象 | 原因 | 解決方式 |
|---|---|---|
| 明明情境符合，但 AI 沒有主動套用該技能 | `description` 寫成「這個技能做什麼」而不是「什麼情況該用」 | 改寫成以 `Use when...` 開頭、聚焦「觸發條件/症狀」的第三人稱描述，避免摘要技能的執行流程（否則 AI 會抄描述當結論，不會真的展開讀技能全文）——詳見 `skill-authoring` → `writing-skills` |
| 技能有讀到，但 AI 只做了一半流程就停 | 描述裡先劇透了流程步驟，AI 讀了描述就以為知道全部了 | 描述只寫觸發條件，流程細節留在 `SKILL.md` 正文，逼 AI 真的展開讀完 |
| 技能內連到 `references/xxx.md` 的連結失效 / AI 說找不到檔案 | 相對路徑寫錯，或搬動資料夾後忘記同步更新引用路徑 | 用 `Glob`/`grep` 檢查 `references/` 底下實際檔名，修正 `SKILL.md` 裡的相對路徑；避免用 `@` 語法強制載入整份參考檔（會一次燒光大量 context） |
| 同一輪對話塞爆 context / 回應變慢 | 一次載入太多技能全文，尤其是本倉庫 `marketing`（47 個子技能）這種大集合 | 讓 AI 先讀頂層 `SKILL.md` 判斷該深入哪個 `references/<子技能>`，而不是整包一次讀完；必要時把不常用的子技能拆到獨立資料夾，需要才載入 |
| 兩個技能的觸發條件重疊，AI 選錯 | 描述用詞太相近（例如兩個都寫「code review」） | 讓描述更具體地區分場景（誰發起審查 vs 誰回應審查、審查程式碼品質 vs 審查資安），必要時在 `SKILL.md` 裡互相加上「若情境是 X 請改用 Y」的提示 |

> 更完整的技能撰寫規範（YAML 欄位、觸發語句寫法、token 效率、如何用壓力測試驗證技能是否真的有效）見 [`skill-authoring/references/writing-skills/SKILL.md`](skill-authoring/references/writing-skills/SKILL.md)。
