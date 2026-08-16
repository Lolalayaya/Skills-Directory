# Third-Party Licenses

Content vendored into this repo from external sources, kept separate from this repo's own [`README.md`](README.md) copyright notice because it's distributed across multiple top-level skill folders rather than living in one place.

## Matt Pocock — `mattpocock-skills` (aihero.dev)

The following sub-skills, imported 2026-07-31 and integrated into this repo's existing top-level categories (see [`SKILL-AUDIT.md`](SKILL-AUDIT.md) for the full placement reasoning), originate from Matt Pocock's open-source skill collection ([github.com/mattpocock/skills](https://github.com/mattpocock/skills)):

- `agentic-dev-workflow/references/`: `ask-matt`, `grill-with-docs`, `domain-modeling`, `to-spec`, `to-tickets`, `wayfinder`, `resolving-merge-conflicts`, `prototype`, `setup-matt-pocock-skills`, `grilling`, `grill-me`, `handoff`, `request-refactor-plan`, `git-guardrails-claude-code`
- `code-quality-review/references/`: `improve-codebase-architecture`, `codebase-design`, `code-review`, `design-an-interface`, `setup-ts-deep-modules`, `setup-pre-commit`
- `incident-runbooks/references/`: `triage`, `qa`
- `deep-research/references/`: `background-research` (renamed from the original `research` to avoid colliding with this repo's own pipeline-stage skill of that name)
- `personal-learning/references/`: `teach`
- `internal-writing-comms/references/`: `writing-fragments`, `writing-shape`, `to-questionnaire`
- `skill-authoring/references/`: `writing-great-skills`
- `business-automation/references/`: `loop-me`
- `infrastructure-ops/references/`: `wizard`

Two further mattpocock-skills sub-skills (`tdd`, `diagnosing-bugs`) were not kept as separate files — their unique content was merged into this repo's own `product-verification/references/test-driven-development` and `incident-runbooks/references/systematic-debugging` respectively. Those two files are therefore partly derived from mattpocock-skills content as well, even though they don't appear in the list above.

```
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## forrestchang — `andrej-karpathy-skills`

The following sub-skill, imported 2026-08-01 and folded into this repo's existing `agentic-dev-workflow` category, originates from forrestchang's open-source skill pack ([github.com/forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills), mirrored at [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)):

- `agentic-dev-workflow/references/`: `karpathy-guidelines`

```
MIT License

Copyright (c) 2026 forrestchang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Shubham Saboo / Matt Van Horn — `awesome-llm-apps` (`agent_skills/`)

The following sub-skills, imported 2026-08-01 and distributed across this repo's existing top-level categories (see [`SKILL-AUDIT.md`](SKILL-AUDIT.md) for the full placement reasoning), originate from the `agent_skills/` folder of Shubham Saboo's [`awesome-llm-apps`](https://github.com/Shubhamsaboo/awesome-llm-apps) repo. Per-skill `metadata.author` in each `SKILL.md` credits the individual author (Shubham Saboo or Matt Van Horn); the repo itself is licensed Apache-2.0 as a whole:

- `incident-runbooks/references/`: `commit-archaeologist` (author: Matt Van Horn)
- `business-automation/references/`: `project-graveyard` (author: Shubham Saboo)
- `code-quality-review/references/`: `scope-creep-detector` (author: Matt Van Horn)
- `agentic-dev-workflow/references/`: `thinking-out-loud` (author: Shubham Saboo)

A fifth sub-skill in that folder, `advisor-orchestrator-worker`, was deliberately not imported — it duplicates this environment's native multi-agent `Workflow` tool. Each imported skill's own per-repo `README.md` (marketing copy, install instructions for the source repo's own `npx skills add` CLI, externally-hosted demo GIFs) was dropped rather than copied, per this repo's own convention that `SKILL.md` is the only index going forward.

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   Copyright 2026 Shubham Saboo

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## Mugdha Vairagade — `claude-skill-ip-guard`

The following sub-skill, imported 2026-08-02 and folded into this repo's existing `code-quality-review` category, originates from Mugdha Vairagade's open-source skill ([github.com/mugdhav/claude-skill-ip-guard](https://github.com/mugdhav/claude-skill-ip-guard)):

- `code-quality-review/references/`: `ip-guard`

The source repo's own `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, and `user-reports/` example files were dropped rather than copied, per this repo's own convention that `SKILL.md` is the only index going forward.

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

   (See the Apache License 2.0 full text under the Shubham Saboo section
   above for the complete terms — identical license, reproduced there in
   full to avoid triplicating ~180 lines of boilerplate in this file.)

   Copyright 2026 Mugdha Vairagade

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## Leonxlnx — `taste-skill`

The following 12 sub-skills, imported 2026-08-05, originate from Leonxlnx's open-source Claude Code plugin ([github.com/Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)). 11 were integrated into this repo's `scaffolding-templating` category; the 12th (`output-skill`, not a design skill) into `product-verification` — see [`SKILL-AUDIT.md`](SKILL-AUDIT.md) for the full placement reasoning:

- `scaffolding-templating/references/design/`: `taste-skill`, `taste-skill-v1`, `brandkit`, `brutalist-skill`, `gpt-tasteskill`, `image-to-code-skill`, `imagegen-frontend-mobile`, `imagegen-frontend-web`, `minimalist-skill`, `redesign-skill`, `soft-skill`, `stitch-skill`
- `product-verification/references/`: `output-skill`

```
MIT License

Copyright (c) 2026 Leonxlnx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Nutlope — `hallmark`

The following sub-skill, imported 2026-08-05 and folded into this repo's existing `scaffolding-templating` category, originates from Nutlope's open-source design skill ([github.com/Nutlope/hallmark](https://github.com/Nutlope/hallmark)):

- `scaffolding-templating/references/design/`: `hallmark` (full `SKILL.md` + its own `references/` tree; the source repo's CLI, demo site, and docs were not vendored — see [`SKILL-AUDIT.md`](SKILL-AUDIT.md))

```
MIT License

Copyright (c) 2026 Hallmark contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## AnySearch Team — `anysearch-skill`

The following sub-skill, imported 2026-08-07 and folded into this repo's existing `browser-automation` category, originates from the AnySearch Team's open-source skill ([github.com/anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill)):

- `browser-automation/references/`: `anysearch` (`SKILL.md` + its bundled multi-runtime `scripts/` tree, `runtime.conf.example`, `.env.example`; the source repo's own `README.md`, `README_zh.md`, `SECURITY.md`, `LICENSE`, and `NOTICE` were not vendored — see [`SKILL-AUDIT.md`](SKILL-AUDIT.md))

```
AnySearch Skill
Copyright 2026 AnySearch

Licensed under the Apache License, Version 2.0.
```

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

   (See the Apache License 2.0 full text under the Shubham Saboo section
   above for the complete terms — identical license, reproduced there in
   full to avoid triplicating ~180 lines of boilerplate in this file.)

   Copyright 2026 AnySearch

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## Emil Kowalski — `emilkowalski/skills`

The following sub-skills, imported 2026-08-09 and folded into this repo's existing `scaffolding-templating` category, originate from Emil Kowalski's open-source skill collection ([github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)):

- `scaffolding-templating/references/design/`: `emil-design-eng`, `animate` (+ `RECIPES.md`), `animation-vocabulary`, `apple-design`, `find-animation-opportunities`, `improve-animations` (+ `AUDIT.md`, `PLAN-TEMPLATE.md`), `pick-ui-library`, `review-animations` (+ `STANDARDS.md`), `prototype-variants` (+ `PICKER.md`; renamed from the source repo's `prototype` to avoid colliding with this repo's own `agentic-dev-workflow/references/prototype` — see [`SKILL-AUDIT.md`](SKILL-AUDIT.md))

The source repo's own `README.md` was dropped rather than copied, per this repo's own convention that `SKILL.md` is the only index going forward.

```
MIT License

Copyright (c) 2026 Emil Kowalski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Firecrawl — `firecrawl/cli` + `firecrawl/skills`

The following sub-skills, imported 2026-08-16, originate from Firecrawl's own official open-source skill repos ([github.com/firecrawl/cli](https://github.com/firecrawl/cli), [github.com/firecrawl/skills](https://github.com/firecrawl/skills)):

- `library-api-reference/references/`: `firecrawl-build`, `firecrawl-build-scrape`, `firecrawl-build-search`, `firecrawl-build-interact`, `firecrawl-build-onboarding`
- `browser-automation/references/`: `firecrawl-cli` (+ its `rules/install.md`, `rules/security.md`), `firecrawl-agent`, `firecrawl-crawl`, `firecrawl-download`, `firecrawl-interact`, `firecrawl-map`, `firecrawl-monitor`, `firecrawl-parse`, `firecrawl-scrape`, `firecrawl-search`, `firecrawl-developer-index`, `firecrawl-research-index`

The user linked `github.com/firecrawl/firecrawl` (the main product monorepo, which contains no skill content) — that repo's own pointer READMEs name these two actual skill repos, which were fetched instead. Both repos' own root docs (`README.md`, `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, marketplace/plugin manifests) were dropped rather than copied, per this repo's own convention that `SKILL.md` is the only index going forward.

```
ISC License

Copyright (c) Firecrawl

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
```

## ultimatile — `arxiv-skills`

The following sub-skills, imported 2026-08-16 and folded into this repo's existing `library-api-reference` category, originate from ultimatile's open-source skill collection ([github.com/ultimatile/arxiv-skills](https://github.com/ultimatile/arxiv-skills)):

- `library-api-reference/references/`: `arxiv-lookup`, `arxiv-doc-builder` (+ its full `arxiv_doc_builder/` Python package, `tests/`, `references/`)

The source repo's own `README.md`, `ruff.toml`, and `.pre-commit-config.yaml` were dropped rather than copied, per this repo's own convention that `SKILL.md` is the only index going forward.

```
MIT License

Copyright (c) 2026 ultimatile

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Master-cai — `Research-Paper-Writing-Skills`

The following sub-skill, imported 2026-08-16 and folded into this repo's existing `internal-writing-comms` category, originates from Master-cai's open-source skill ([github.com/Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)):

- `internal-writing-comms/references/`: `research-paper-writing` (+ its `references/` tree, including `references/examples/`)

The source repo's own `README.md`, `README_zh.md`, and `agents/openai.yaml` (OpenAI Agent Builder display metadata, not Claude Code skill content) were dropped rather than copied.

```
MIT License

Copyright (c) 2026 Master-cai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## kevintsai1202 — `Humanizer-zh-TW`

The following sub-skill, imported 2026-08-16 and folded into this repo's existing `internal-writing-comms` category, originates from kevintsai1202's open-source skill ([github.com/kevintsai1202/Humanizer-zh-TW](https://github.com/kevintsai1202/Humanizer-zh-TW)):

- `internal-writing-comms/references/`: `humanizer-zh-tw`

Per the skill's own metadata, it is a Traditional Chinese fork of op7418/humanizer-zh, itself translated from blader/humanizer, cross-referencing hardikpandya/stop-slop. The source repo's own `README.md` was dropped rather than copied.

```
MIT License

Copyright (c) 2026 歸藏

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## AccessLint — `skills` (AccessLint/skills)

The following 5 sub-skills, imported 2026-08-16 and folded into this repo's existing `scaffolding-templating` category, originate from AccessLint's open-source skill collection ([github.com/AccessLint/skills](https://github.com/AccessLint/skills)):

- `scaffolding-templating/references/design/accesslint/`: `accessibility-audit`, `accessibility-scan`, `accessibility-inspect` (+ its own `references/checkpoints.md`), `accessibility-diff`, `accessibility-fix`, plus the shared `shared/methodology.md` all 5 reference by relative path

The source repo's own `README.md`, `CHANGELOG.md`, `docs/`, and `benchmark/` (marketing/benchmark scaffolding, not skill content) were dropped rather than copied; its `.claude-plugin/plugin.json` (version 0.10.2) was read for author/version metadata but not copied in. The plugin's own `.mcp.json` declares a required MCP server (`accesslint`, via `npx -y @accesslint/mcp@latest`) that `accessibility-audit`/`accessibility-fix` depend on — noted operationally in `scaffolding-templating/SKILL.md` rather than treated as vendor scaffolding, since it's load-bearing for those two skills to function. No explicit copyright-holder line was found in the source repo (its `README.md`'s License section states only "MIT"); the block below uses the author identity from `plugin.json`/`marketplace.json` (AccessLint, support@accesslint.com, accesslint.com).

```
MIT License

Copyright (c) 2026 AccessLint

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## bencium.io — `typography` + `relationship-design` + `insurgent-campaign`

The following sub-skills, folded into this repo's existing categories, originate from bencium.io's Claude Code plugin marketplace ([github.com/bencium/marketplace](https://github.com/bencium) — see that repo's `.claude-plugin/marketplace.json`):

- `scaffolding-templating/references/design/`: `ui-typography` (imported 2026-08-16; source folder `typography/skills/typography/`, frontmatter `name: ui-typography` as shipped — kept as the folder name here too, for folder/frontmatter consistency; no actual name collision found in this repo either way), `relationship-design` (imported 2026-08-16)
- `marketing/references/research-strategy/`: `insurgent-campaign` (imported 2026-08-16, later same-day batch — full `SKILL.md` + its `references/` tree: `asymmetry-audit-table.md`, `authenticity-playbook.md`, `campaign-archetypes.md`, `channel-tier-stack.md`, `hungarian-case-study.md`, `lift-test-templates.md`, `sector-riders.md`)

Neither of the first two source plugin folders (`typography/`, `relationship-design/`) vendors its own `LICENSE` file; the marketplace's root `README.md` states "License: MIT" for the collection as a whole, and a sibling skill in the same marketplace (`eu-ai-act-reviewer/skills/eu-ai-act-reviewer/LICENSE`) provides the exact copyright line used below. Each source plugin's own `.claude-plugin/plugin.json` confirms `author: { name: "bencium.io", url: "https://bencium.io" }`, including `insurgent-campaign`'s. Vendor root docs (including `insurgent-campaign`'s own root `README.md`) were not copied in.

**Also from this same marketplace, but NOT vendored as whole skills — only one named mechanism was extracted from each into an already-existing file in this repo**, per a user-directed set of 9 precision extractions/installs (see `SKILL-AUDIT.md`'s "2026-08-16（三）" section for the full per-item reasoning and what was left out of each):

- `bencium-innovative-ux-designer`'s glassmorphism ban ("NO glass morphism effects (this is the one banned technique)") → used to flip `scaffolding-templating/references/design/redesign-skill/SKILL.md`'s previous glassmorphism *recommendation* into a ban.
- `bencium-impact-designer`'s "Creative Reframing Prompts" (Designer lens / Context shift / Era lens) → folded into `scaffolding-templating/references/design/taste-skill/SKILL.md` as an optional §0.E lateral-thinking nudge.
- `design-audit`'s doc-grounded, phased/approval-gated audit workflow → folded into `scaffolding-templating/references/design/hallmark/references/verbs/audit.md` as an alternate mode of the existing `audit` verb.
- `human-architect-mindset`'s "Loyalty" foundation (The Human Moat, the Loyalty Decision Matrix, 5 named anti-patterns) → extracted into a new standing-reference file, `agentic-dev-workflow/references/loyalty-mindset/SKILL.md`.
- `bencium-aeo`'s "Authority Level Determines Strategy" table (Challenger vs. Established, Princeton Rank-5/Rank-1 data point) → folded into `marketing/references/paid-acquisition/ai-seo/SKILL.md` as a supplementary section.

Each source plugin above (`bencium-innovative-ux-designer`, `bencium-impact-designer`, `design-audit`, `human-architect-mindset`, `bencium-aeo`) confirms the same `author: { name: "bencium.io", url: "https://bencium.io" }` in its own `.claude-plugin/plugin.json`, covered by the same MIT license block below — no separate license text is needed since none of these five contributed a whole vendored file, only a folded-in fragment with its own inline provenance note at the point of use.

```
MIT License

Copyright (c) 2026 Bencium Limited

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## NousResearch/hermes-agent — `popular-web-designs` + `design-md` + `baoyu-infographic` + `p5js` + `sketch`

The following sub-skills, folded into this repo's existing `scaffolding-templating` category, originate from Nous Research's `hermes-agent` repo ([github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), `skills/creative/`):

- `scaffolding-templating/references/design/`: `popular-web-designs` (imported 2026-08-16, + its `templates/`, 54 files), `design-md` (imported 2026-08-16, + its `templates/starter.md`), `baoyu-infographic` (imported 2026-08-16, + its `PORT_NOTES.md` and `references/` tree: `analysis-framework.md`, `base-prompt.md`, `structured-content-template.md`, `layouts/`, `styles/`), `p5js` (imported 2026-08-16, later same-day batch — full `SKILL.md` + its `references/` tree, 10 files + `templates/viewer.html` + `scripts/` tree: `setup.sh`, `serve.sh`, `render.sh`, `export-frames.js`), `sketch` (imported 2026-08-16, later same-day batch — single `SKILL.md`, no bundled `references/`/`templates/` in the source)

The source repo's own root `README.md`/`CLAUDE.md`/`AGENTS.md` and per-plugin marketplace manifests (vendor scaffolding, not skill content) were not copied in; `p5js`'s own `README.md` was likewise dropped (it only restated the `SKILL.md`'s own tables), per the same convention.

Also from `hermes-agent`'s `skills/creative/`, but NOT vendored as a whole skill — only one named mechanism was extracted into an existing file: `claude-design`'s "Surface-First" 7-archetype naming step was folded into `scaffolding-templating/references/design/frontend-design/SKILL.md` (see that file's own inline provenance note and `SKILL-AUDIT.md`'s "2026-08-16（三）" section for what was left out).

**Two-author attribution, same pattern as the Shubham Saboo / Matt Van Horn section above**: `baoyu-infographic`'s own `SKILL.md` frontmatter reads `author: 宝玉 (JimLiu)`, `license: MIT`, `homepage: https://github.com/JimLiu/baoyu-skills#baoyu-infographic` — it was adapted BY hermes-agent/Nous Research from 宝玉 (JimLiu)'s original `baoyu-infographic` skill, not authored fresh by Nous Research. Both are credited: the repo-level MIT license below (Nous Research) covers the adaptation and the `hermes-agent` repo as a whole; 宝玉/JimLiu is credited by name as the original author of the underlying skill design. Separately, `popular-web-designs`'s own frontmatter credits `author: Hermes Agent + Teknium (design systems sourced from VoltAgent/awesome-design-md)` — also noted here since it's a second instance of the same "adapted from, not authored by, the importing repo" pattern. A third instance: `sketch`'s own "Attribution" section in its `SKILL.md` credits it as adapted from the GSD (Get Shit Done) project's `/gsd-sketch` workflow — MIT © 2025 Lex Christopherson ([github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done), now archived/unmaintained upstream). Both hermes-agent (repo-level MIT below) and Lex Christopherson (original workflow author) are credited for this file.

```
MIT License

Copyright (c) 2025 Nous Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## shadcn — `shadcn-official` + `migrate-radix-to-base`

Two skills vendored verbatim (byte-for-byte, no paraphrasing) from shadcn/ui's own official repo ([github.com/shadcn-ui/ui](https://github.com/shadcn-ui/ui), `skills/` directory), imported 2026-08-16 into this repo's existing `scaffolding-templating` category, alongside this repo's own pre-existing hand-authored `ui-styling` skill (which now cross-references these two rather than duplicating their content):

- `scaffolding-templating/references/design/shadcn-official/`: vendored from `skills/shadcn/` — `SKILL.md`, `cli.md`, `customization.md`, `mcp.md`, `registry.md`, `rules/base-vs-radix.md`, `rules/chat.md`, `rules/composition.md`, `rules/forms.md`, `rules/icons.md`, `rules/styling.md` (11 files). The source's own `agents/openai.yml`, `assets/*.png`, and `evals/evals.json` were not vendored — internal CI/eval tooling for shadcn's own maintainers, not needed to consume the skill.
- `scaffolding-templating/references/design/migrate-radix-to-base/`: vendored from `skills/migrate-radix-to-base/` — `SKILL.md`, `class-mapping.md`, `consumer-props.md`, `disclosure.md`, `display-misc.md`, `form-controls.md`, `menus.md`, `overlays.md`, `universal-patterns.md`, `wrapper-shapes.md` (10 files).

Both frontmatter `name:` values (`shadcn`, `migrate-radix-to-base`) were checked against the whole repo before import — no collisions, kept as-is.

```
MIT License

Copyright (c) 2023 shadcn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Magic UI Design — `magicui`

Imported 2026-08-16 into `scaffolding-templating/references/design/magicui/`, from [github.com/magicuidesign/magicui](https://github.com/magicuidesign/magicui). Two parts:

- Vendored verbatim from the source repo's own official Claude skill (`skills/magic-ui/`): `SKILL.md`, `references/components.md`, `references/recipes.md` — with one deliberate addition (not a vendoring edit): a "Full Source Catalog" section appended to the end of `SKILL.md` pointing at the file below.
- A new file authored for this repo, not vendored: `references/source-catalog.md` — real, unmodified `.tsx` source for 20 representative components fetched directly from the source repo's `apps/www/registry/magicui/` (permitted under this library's plain MIT license, unlike `react-bits` below).

Frontmatter `name: magic-ui` checked against the whole repo before import — no collision.

```
MIT License

Copyright (c) Magic UI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## David Haz — `react-bits` (⚠️ non-standard license — read before reusing)

Imported 2026-08-16 into `scaffolding-templating/references/design/react-bits/SKILL.md`, from [github.com/DavidHDev/react-bits](https://github.com/DavidHDev/react-bits). **Single new file, no component source code** — this is the one deliberate exception to this repo's usual "embed real source" pattern for a design-component library, because of the license below.

react-bits uses **"MIT + Commons Clause License Condition v1.0"**, not plain MIT. The Commons Clause rider forbids selling, sublicensing, or **redistributing the components themselves — alone, in a bundle, or as a ported version**. Because this repo is itself a bundle of reference material that gets copied/distributed (including onto a local `~/.claude/skills/` install), statically storing any react-bits component source (`.tsx`/`.jsx`/`.css`) here would fall under that restriction. The vendored `SKILL.md` therefore contains only category names, comparison prose, and the official CLI install command (which pulls fresh code directly into an end user's *own* project at time of use — the license-permitted path) — never a stored code snippet. See that file's own license note for the reader-facing explanation.

```
MIT License + Commons Clause License Condition v1.0

Copyright (c) 2026 David Haz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, and distribute the Software as part of
an application, website, or product, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Commons Clause Restriction: You may use this Software, including for any
commercial purpose, so long as you do not sell, sublicense, or redistribute
the components themselves — whether alone, in a bundle, or as a ported
version.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Adobe — `react-aria` (Apache-2.0)

Imported 2026-08-16 into `library-api-reference/references/react-aria/` (`SKILL.md`, `references/hooks.md`, `references/components.md`, `references/patterns.md`), authored for this repo directly from source material in Adobe's `adobe/react-spectrum` monorepo ([github.com/adobe/react-spectrum](https://github.com/adobe/react-spectrum)) rather than vendored wholesale — the live docs site (`react-aria.adobe.com`) was unreachable from this environment across repeated attempts, so content was built from the repo's own package READMEs (`packages/react-aria/README.md`, `packages/react-aria-components/README.md`), its `AGENTS.md` layering explanation, and real embedded component source pulled from Adobe's own official Tailwind starter kit (`starters/tailwind/src/`) — not invented from training-data memory. Licensed Apache-2.0, which permits this kind of reuse with attribution.

Frontmatter `name: react-aria` checked against the whole repo before import — no collision.

(See the Apache License 2.0 full text under the Shubham Saboo section above — same license, not reproduced twice.)

```
Copyright 2019 Adobe
```

## `context-engineering-collection`

Kept whole as a single top-level folder rather than distributed, so its own [`LICENSE`](context-engineering-collection/LICENSE) (MIT, Context Engineering Agent Skills Contributors) still applies directly — no duplication needed here.
