# 走查：英文期刊论文，从选题到投稿

场景（脱敏）：研究者小 B 对"某类算法在某场景下的公平性"有兴趣，想投一篇英文期刊，但还没有明确的研究问题。

---

## 起点：用户说 "I'm interested in fairness of X, want to publish, but not sure what to ask"

**conductor 定位：** 模糊兴趣，无 RQ。阶段 1。

**conductor 输出：**
> Start with `deep-research` in socratic mode (or `superpowers:brainstorming`) to turn the interest into an answerable RQ. Don't write yet.

## 阶段 1 → 2

```
Handoff: RQ + hypotheses → literature search terms
Invariant: keep the RQ fixed during the search
```

**conductor 输出：**
> Now run `deep-research` full mode for systematic search + a methodology blueprint. Manage references in `bib-search-citation` from day one.

## 阶段 2 → 3 写作

**conductor 定位：** English journal paper, has RQ + literature + (assume) results.

**conductor 输出：**
> Use `academic-paper` (ARS) to draft. If you have experiments, bring the verified results into the handoff packet. If you have a target venue with a LaTeX template, pair it with `latex-paper-en` for compile + ChkTeX + AXES coherence.

## 阶段 3 → 4 → 5

**conductor 输出：**
> Method figure via `paper-framework-figure-studio-pro`. Then language pass with `latex-paper-en` (grammar, sentence length, anti-citation-stacking). For an English paper, skip `aiwei-zh` (it is for Chinese prose).

## 阶段 5 → 6 审稿

**conductor 输出：**
> Pre-submission, run `academic-paper-reviewer` for a mock peer review (EIC + 3 reviewers + Devil's Advocate), or `paper-audit` for a pass/fail submission gate. Revise at most two rounds; remaining issues go into Limitations, never fabricate to pass.

## 阶段 6 → 8 投稿

**conductor 输出：**
> Final formatting: `academic-pipeline` can run the end-to-end finalize (integrity recheck + reference verification), `bib-search-citation` exports clean BibTeX, and the file-ops skills handle DOCX/PDF for the submission package. If rejected or R&R, come back to stage 6 to parse the reviews.

---

**conductor 全程做了什么：** routed across 7 stages, enforced the "verified data is an invariant" rule at every handoff, and never wrote, polished, or reviewed anything itself.
