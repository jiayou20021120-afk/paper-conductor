# 走查：英文期刊论文，从选题到投稿

场景（脱敏）：研究者小 B 对"某类算法在某场景下的公平性"有兴趣，想投英文期刊，但还没明确的研究问题。

下面展示 paper-conductor 全程陪走：能自己干的直接干，遇到更强专门工具才升级。

---

## 起点："I'm interested in fairness of X, want to publish, but not sure what to ask"

**conductor 定位：** 模糊兴趣，无 RQ。阶段 1。

**conductor 自己做：** Directly run a socratic line of questioning to turn the interest into an answerable RQ with scoped hypotheses. No need to launch another skill first.

> 升级提示：想要 13-agent 深度探索用 `deep-research`(socratic)。

## 阶段 2：文献调研

**conductor 自己做：** Give a first-pass review skeleton, key references, and an initial gap statement.

> 升级提示：systematic search + source verification 用 `deep-research`(full)；本地库用 `bib-search-citation`。

## 阶段 3：写作

**conductor 自己做：** Draft the intro, methods, results narrative, and discussion directly. If experiments exist, weave the verified results into the argument.

> 升级提示：want a 12-agent collaborative drafting pass 用 `academic-paper`；LaTeX template compile + ChkTeX + AXES 用对应排版 skill。

## 阶段 4 → 5：制图与润色

**conductor 自己做：** Provide a text brief for the method figure (what to draw, layout, module relations). Polish the prose directly: cut throat-clearing, vary sentence rhythm, fix Chinglish.

> 升级提示：真出图用 `paper-framework-figure-studio-pro`。英文稿不需要 `aiwei-zh`（它是中文专用）。

## 阶段 6：审稿

**conductor 自己做：** Read the full draft and give one structured self-review pass (contribution clarity, argument validity, method soundness, citation coverage).

> 升级提示：multi-perspective mock review 用 `academic-paper-reviewer`（EIC + 3 reviewers + Devil's Advocate）；pass/fail submission gate 用 `paper-audit`. Revise at most two rounds; remaining issues go into Limitations, never fabricate to pass.

## 阶段 8：投稿

**conductor 自己做：** Tidy the references to the target style, adjust structure to venue norms, draft the cover letter.

> 升级提示：end-to-end finalize（引用/数据 100% 复核）用 `academic-pipeline`；clean BibTeX 用 `bib-search-citation`；DOCX/PDF 用文件操作 skill。If rejected or R&R, come back to stage 6 to parse the reviews.

---

**conductor 全程做了什么：** drafted, polished, self-reviewed, and planned the route itself; only escalated to specialized skills for figures, deep systematic research, multi-reviewer evaluation, and final integrity check. Both hands-on and orchestrating, and it enforced the "verified data is an invariant, never fabricate" rule at every handoff.
