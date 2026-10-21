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

## Patrick Szymkowiak — `rtk` (Apache-2.0)

Imported 2026-09-14 into `incident-runbooks/references/`: `issue-triage`, `pr-triage`, `repo-recap`, `pr-review`, `full-triage` (renamed from the source's `rtk-triage` — see [`SKILL-AUDIT.md`](SKILL-AUDIT.md) for why), originating from Patrick Szymkowiak's [`rtk-ai/rtk`](https://github.com/rtk-ai/rtk) repo's `.claude/skills/` directory. Only these 5 of the repo's 12 skills were kept — the other 7 (`code-simplifier`, `design-patterns`, `performance`, `security-guardian`, `ship`, `rtk-tdd`, `tdd-rust`) are hardcoded to RTK's own Rust CLI internals (specific file paths, performance targets, its own binary) and were judged non-portable; see `SKILL-AUDIT.md`. Content was translated from French to English (the source defaulted to French output with an `en` override; this repo standardizes on English-only) and de-branded (RTK-specific hardcoded repo references, save paths, and attribution footers replaced with generic/dynamic equivalents) — substance and mechanics otherwise unchanged. Two bundled templates (`templates/issue-comment.md`, `templates/review-comment.md`) were carried over the same way.

(See the Apache License 2.0 full text under the Shubham Saboo section above — same license, not reproduced twice.)

```
Copyright 2026 Patrick Szymkowiak
```

## Paul Bakaus — `impeccable` (Apache-2.0)

Imported 2026-10-07 into `scaffolding-templating/references/design/impeccable/` (`SKILL.md` + full `reference/` of ~40 files + `scripts/`), originating from Paul Bakaus's [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) repo's `.claude/skills/impeccable/` directory (the source repo also vendors identical copies into `.agent/`, `.agents/`, `.cursor/` for other tool ecosystems — only the Claude Code copy was taken, since this repo only needs one).

**Modified from upstream** (disclosed per this repo's own transparency practice, not a silent fork): a new "Setup → 0. First-run confirmation gate" section was added to the vendored `SKILL.md`, not present in the source. The skill's own launcher (`scripts/impeccable`, a plain-text, fully-read shell/batch script — confirmed no suspicious patterns) downloads a **closed-source compiled binary** from `github.com/pbakaus/impeccable/releases/` on its first invocation per machine/version (checksum-verified against a `.sha256` sidecar, fails closed without one — this is a legitimate, well-engineered update mechanism, not an arbitrary/unverified fetch, but the binary itself remains unauditable, unlike every other tool vendored into this repo so far). The upstream skill runs this silently as step 1 of its own Setup. This repo's copy gates that specific first-download-and-execute moment behind an explicit user confirmation instead — see `SKILL-AUDIT.md` for the full reasoning and the user's explicit decision to accept the risk with that mitigation in place.

**Sub-attribution** (per the source's own `NOTICE.md`): `reference/ios.md` and `reference/android.md` are distilled from ehmo's `platform-design-skills` (MIT) — https://github.com/ehmo/platform-design-skills.

Frontmatter `name: impeccable` checked against the whole repo before import — no collision.

(See the Apache License 2.0 full text under the Shubham Saboo section above — same license, not reproduced twice.)

```
Copyright 2026 Paul Bakaus
```

## changemaner — `design-taste-frontend` (MIT) — partial import as `taste-deck`

Imported 2026-10-07 as `scaffolding-templating/references/design/taste-deck/`, originating from changemaner's [`design-taste-frontend`](https://github.com/changemaner/design-taste-frontend) repo. **Partial, not wholesale**: a background-agent comparison (full-content read on both sides, not description-skimming — see `SKILL-AUDIT.md`) found the source's general frontend-design content (its `SKILL.md` §0-14 plus `reference/{pre-flight-checklist,ai-tell-catalog,redesign-protocol,dial-definitions}.md`) is near word-for-word identical to this repo's own pre-existing `scaffolding-templating/references/design/taste-skill/` (imported 2026-08-05 from a different upstream, Leonxlnx's `taste-skill`) — same dial system, same banned-pattern examples, same checklists. That duplicate content was declined. Only the genuinely novel deck/slide-generation half was kept: `reference/deck-mode.md` (vendored as top-level `deck-mode.md`), `freeplay-declaration.md`, `deploy-guide.md`, `annotation-guide.md`, `manifest-schema.md`, `design-manifest.json`, and the full `showcase/` + `refero-styles/` asset library (30 real-brand design-token sources + demo decks + QA/export Python scripts + self-hosted Google Fonts, all individually OFL-licensed and redistributable).

**Explicitly excluded, per the source's own text, not this repo's judgment**: `brand-style-reference.md` states in its own first line that it is "not distributed under the repo's MIT license" (it's a style-learning report referencing real brands' public websites/trademarks) — respected as-is, not vendored.

**Language note**: several vendored files (`deck-mode.md`, `deploy-guide.md`, `annotation-guide.md`, `manifest-schema.md`, `freeplay-declaration.md`) mix English with Simplified Chinese, matching the source project's working language — left as-is (not translated) since the content is functional and translation wasn't requested; flagged in `taste-deck/SKILL.md`'s own Notes section.

Frontmatter `name: taste-deck` checked against the whole repo before import — no collision. Cross-reference notes added in both directions: `taste-skill/SKILL.md` §13 (Out of Scope) now points deck briefs to `taste-deck`; `taste-deck/SKILL.md` points general frontend briefs back to `taste-skill`/`hallmark`; the existing lightweight `slides/SKILL.md` now cross-references `taste-deck` for the value-locked case.

```
MIT License

Copyright (c) 2026 changemaner

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

## Remotion — `remotion-dev/skills` (⚠️ non-standard license — read before reusing)

Imported 2026-10-07 into `library-api-reference/references/remotion/`, fetched via the official `skills` CLI (`npx skills use "https://github.com/remotion-dev/skills" --skill "remotion-best-practices"`) rather than a raw git clone — this is the first import done through that distribution mechanism rather than `git clone`/raw-file fetch. The CLI resolved the router skill `remotion-best-practices` (v4.0.533) plus its full set of sub-skills (`remotion-create`, `remotion-markup`, `remotion-maps` with provider techniques for Cesium/Mapbox/MapLibre/MapTiler, `remotion-multimedia`, `remotion-interactivity`, `remotion-studio`, `remotion-render`, `remotion-captions`, `remotion-saas`, `remotion-docs`, `remotion-upgrade`) and wrote them to a local temp directory, vendored here byte-for-byte (141 files, ~1.5MB).

**Not plain MIT/Apache like most of this repo.** Remotion itself (`remotion-dev/remotion`, of which `remotion-dev/skills` is `packages/skills`) ships under the project's own "Remotion License": free for individuals, non-profits, and for-profit organizations with ≤3 employees, to create videos/images (commercially or not); a paid Company License is required above that size; explicitly **forbids copying/modifying Remotion to sell, rent, license, relicense, or sublicense your own derivative of Remotion**. This repo's own standing disclaimers already scope all content here to personal study/reference use, not commercial redistribution (see the copyright notice in `README.md`) — consistent with the Free License's "individual" tier — but this is flagged explicitly, the same way `react-bits`' Commons Clause was flagged, rather than mislabeled as a standard permissive license. Read the full terms at the source before any other kind of reuse: https://github.com/remotion-dev/remotion/blob/main/LICENSE.md.

No overlap with existing content — first Remotion-related skill in this repo.

```
Remotion License (see https://github.com/remotion-dev/remotion/blob/main/LICENSE.md for full, current text — not reproduced in full here because the source itself says the license may change in Remotion 5.0 and links to the authoritative current version rather than pinning one)

Copyright © 2026 Remotion
```

## 歸藏 (op7418) — `guizang-ppt-skill` (⚠️ AGPL-3.0 — the first copyleft source in this repo)

Imported 2026-10-21 into `scaffolding-templating/references/design/guizang-ppt-skill/` (`SKILL.md` + full `assets/`, `references/`, `scripts/`), originating from 歸藏's [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) repo — a single-file HTML horizontal-swipe deck generator with two complete named aesthetic systems (electronic-magazine/Monocle-style, and Swiss International), a full presenter/rehearsal mode (speaker view, audience-screen sync, laser pointer), WebGL backgrounds, and an auto-update-check mechanism. Vendored whole, no partial extraction — the content is a single cohesive system, not a bundle of separable pieces. The three bundled validator scripts (`validate-presenter-mode.mjs`, `validate-swiss-deck.mjs`, `check-presenter-runtime-sync.mjs`) were read in full before vendoring: plain Node scripts, no `eval`/`child_process`/unexpected network calls, with the Playwright-based rendering checks already designed by the source to degrade gracefully to static-only analysis when Playwright isn't installed.

**Not MIT/Apache/ISC/source-available like everything else imported so far — this is AGPL-3.0, a copyleft license**, and this repository is public on GitHub. AGPL permits inclusion alongside differently-licensed files (a repo can be a "mere aggregate" of independently-licensed works without the whole repo becoming AGPL — see the License's own §4(e) "aggregate" clause, reproduced below), so this doesn't relicense the rest of this repo. But anyone — including a future session here — who **modifies** this skill's own files and then conveys (distributes) that modified version, or runs a modified version as a network-accessible service, must make the corresponding modified source available under AGPL-3.0 to recipients/users of that service (License §13, the clause that distinguishes AGPL from plain GPL). This repo's own standing disclaimer already scopes everything here to personal study/reference use (see `README.md`'s copyright section), which doesn't trigger those obligations on its own — but this is flagged explicitly, the same treatment given to `react-bits`' Commons Clause and Remotion's non-standard license, rather than silently treated as just another permissive import.

**Monorepo-specific modification** (disclosed, not silent): the vendored `SKILL.md`'s "Step 0" auto-update mechanism (`git -C "<SKILL_ROOT>" fetch`/`pull`) assumes `<SKILL_ROOT>` is its own standalone git clone with an upstream remote, per the source's own recommended standalone-install method. That assumption breaks when vendored as a subfolder of this monorepo (no independent `.git`, and running those commands here would operate on this repo's own git state instead). Added an explanatory note directing the monorepo case to update via this repo's own `git pull` instead, and reserving the original mechanism for a standalone install done the source's own recommended way.

Frontmatter `name: guizang-ppt-skill` checked against the whole repo before import — no collision. Cross-reference notes added in all directions with the two existing deck/slide skills (`slides`, `taste-deck`) — mechanically distinct (horizontal swipe + two curated in-house aesthetics vs. fixed-stage real-brand-token fidelity vs. Chart.js strategic decks), not a duplicate of either.

```
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
our General Public Licenses are intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  Developers that use our General Public Licenses protect your rights
with two steps: (1) assert copyright on the software, and (2) offer
you this License which gives you legal permission to copy, distribute
and/or modify the software.

  A secondary benefit of defending all users' freedom is that
improvements made in alternate versions of the program, if they
receive widespread use, become available for other developers to
incorporate.  Many developers of free software are heartened and
encouraged by the resulting cooperation.  However, in the case of
software used on network servers, this result may fail to come about.
The GNU General Public License permits making a modified version and
letting the public access it on a server without ever releasing its
source code to the public.

  The GNU Affero General Public License is designed specifically to
ensure that, in such cases, the modified source code becomes available
to the community.  It requires the operator of a network server to
provide the source code of the modified version running there to the
users of that server.  Therefore, public use of a modified version, on
a publicly accessible server, gives the public access to the source
code of the modified version.

  An older license, called the Affero General Public License and
published by Affero, was designed to accomplish similar goals.  This is
a different license, not a version of the Affero GPL, but Affero has
released a new version of the Affero GPL which permits relicensing under
this license.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU Affero General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Remote Network Interaction; Use with the GNU General Public License.

  Notwithstanding any other provision of this License, if you modify the
Program, your modified version must prominently offer all users
interacting with it remotely through a computer network (if your version
supports such interaction) an opportunity to receive the Corresponding
Source of your version by providing access to the Corresponding Source
from a network server at no charge, through some standard or customary
means of facilitating copying of software.  This Corresponding Source
shall include the Corresponding Source for any work covered by version 3
of the GNU General Public License that is incorporated pursuant to the
following paragraph.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the work with which it is combined will remain governed by version
3 of the GNU General Public License.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU Affero General Public License from time to time.  Such new versions
will be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU Affero General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU Affero General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU Affero General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

Copyright (C) 2026 歸藏 (op7418)
```

## `context-engineering-collection`

Kept whole as a single top-level folder rather than distributed, so its own [`LICENSE`](context-engineering-collection/LICENSE) (MIT, Context Engineering Agent Skills Contributors) still applies directly — no duplication needed here.
