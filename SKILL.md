---
name: paper-conductor
description: >-
  论文流水线总调度与编排层（Academic paper pipeline conductor）。当用户面对一个完整的学术论文任务、
  不确定下一步该用哪个工具、想把多个学术 skill 串成一条流程、或需要在阶段之间交接产物时，
  识别用户当前所处的阶段（选题质询 → 文献调研 → 写作 → 制图 → 润色去AI味 → 审稿 → 答辩 → 投稿），
  推荐该阶段最合适的 skill、给出触发例句、并说明上一步的产物如何交给下一步（handoff）。
  它只导航与编排，自己不写作、不润色、不审稿、不制图：这些由它推荐的 skill 执行。
  中文触发：论文全流程、从头到尾写论文、下一步该做什么、该用哪个 skill、把这些 skill 串起来、
  论文流水线、学术工作流、给我一条论文路线图、论文总调度、跨阶段交接。
  English triggers: end-to-end paper workflow, what skill should I use next, orchestrate my academic
  skills, paper pipeline roadmap, hand off between stages, which tool for this paper stage.
  Do NOT trigger when the user has a single clear task (route directly to that skill instead), and
  never perform the writing, polishing, review, or figure work itself.
metadata:
  version: "0.1.0"
  license: MIT
  author: jiayou20021120-afk
  task_type: open-ended
---

# paper-conductor 论文流水线总调度

一句话：它是论文生产的调度台。自己不干活，只判断你在哪个阶段、该唤起哪个 skill、上一步的产物怎么交给下一步。

## 定位与边界（先读这条）

| 它做 | 它不做 |
|---|---|
| 识别用户所处的论文阶段 | 亲自写作 / 润色 / 审稿 / 制图 |
| 推荐该阶段的 skill + 触发例句 | 替用户自动执行那些 skill |
| 给出阶段间的 handoff（产物交接） | 取代任何被它调度的 skill |
| 给出一条贯穿全程的路线图 | 在单一明确任务时抢触发 |

**关键纪律：** 当用户已经有一个清楚的单点任务（"帮我审这篇稿""把这段去 AI 味"），不要走调度，直接说"这步用 X skill"或让对应 skill 接手。paper-conductor 的价值只在"全流程 / 跨阶段 / 不知从何下手"这类场景。

## 八个阶段（路由总表）

下表是默认推荐栈。每一阶段的"识别信号 / 输入 / 输出 / handoff"详见 [`references/stage_cards.md`](references/stage_cards.md)。默认推荐的 skill 可被替换，见 [`references/swappable_skills.md`](references/swappable_skills.md)。

| # | 阶段 | 默认推荐 skill | 一句话触发例 |
|---|---|---|---|
| 1 | 选题质询 | `superpowers:brainstorming`、`mattpocock-skills:grill-me`、`deep-research`(socratic) | "我有个模糊的想法，帮我把研究问题问清楚" |
| 2 | 文献调研 | `deep-research`、`industrial-ai-research`(垂类)、`bib-search-citation` | "帮我做这个题目的文献调研" |
| 3 | 写作 | `academic-paper`(英文)、`ultimate-academic-writing`(中文人文社科)、`chinese-thesis-workbench`(中文毕业论文)、`latex-paper-en`/`latex-thesis-zh`/`typst-paper`(按格式) | "帮我写引言 / 把这个项目写成论文" |
| 4 | 框架图 | `paper-framework-figure-studio-pro` | "给这篇画一个方法概览图" |
| 5 | 润色去AI味 | `aiwei-zh`(中文去AI味)、`latex-paper-en`/`typst-paper`(语法/表达检查) | "读起来太像 AI 了，帮我清一遍" |
| 6 | 审稿 | `academic-paper-reviewer`(同行评审)、`paper-audit`(投稿门控) | "把这篇当审稿人审一下 / 能不能投" |
| 7 | 答辩 | `thesis-defense-deck` | "帮我做答辩 PPT" |
| 8 | 投稿格式 | `academic-pipeline`(全流程编排)、`bib-search-citation`、文件操作 skill(docx/pptx/pdf) | "整理参考文献 / 转成投稿格式" |

## 怎么用（编排逻辑）

1. **定位阶段。** 先判断用户在 1 到 8 哪一阶段。看手头有什么产物（只有想法 = 阶段 1；有数据没文字 = 阶段 3；有草稿要改 = 阶段 5/6）。判断不了就问一句"你现在手上有什么了？"。
2. **给该阶段的推荐。** 报出默认 skill + 触发例句。若用户的栈里没有这个 skill，给 `swappable_skills.md` 里的替代或公开来源。
3. **给 handoff。** 说明这一步做完会产出什么，下一步需要什么，怎么把前者变成后者。详见 [`references/handoff_protocol.md`](references/handoff_protocol.md)。
4. **给路线图（可选）。** 用户要"全流程"时，按 1 到 8 给一条贯穿路线，标出在哪些阶段会有交接和检查点。

## handoff 协议（一句话版）

每次阶段交接，产出一个"交接包"：本阶段产物清单 + 下阶段需要的输入 + 尚未解决的问题。这样跨 skill、跨会话都不丢上下文。完整模板见 [`references/handoff_protocol.md`](references/handoff_protocol.md)。

## 默认栈可替换

本 skill 不绑定任何特定 skill 供应商。默认推荐填的是公开可得的主流学术 skill，用户可以在 [`references/swappable_skills.md`](references/swappable_skills.md) 里换成自己的。paper-conductor 只负责"按阶段路由"这个通用逻辑。

## 例子

- [`examples/zh_thesis_zero_to_defense.md`](examples/zh_thesis_zero_to_defense.md)：中文毕业论文，从一个项目到答辩 PPT 的全程走查。
- [`examples/en_journal_submission.md`](examples/en_journal_submission.md)：英文期刊论文，从选题到投稿的全程走查。
