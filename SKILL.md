---
name: paper-conductor
description: >-
  论文全流程集大成助手（Academic paper all-in-one assistant and conductor）。覆盖学术论文从选题到投稿
  的 8 个阶段（选题质询 → 文献调研 → 写作 → 制图 → 润色去AI味 → 审稿 → 答辩 → 投稿）。它自己就能动手：
  写作（引言/方法/讨论/全文草稿）、润色与表达改写、基础审稿与自查、规划全程路线图，都直接做。
  当某个环节有更强的专门 skill 时（深度系统性文献调研、框架图、中文破折号 hard gate 级去AI味、
  学校 DOCX 模板交付、本地 .bib 检索、多 reviewer 深度评审），它会推荐并把产物交接过去。既动手又动嘴。
  中文触发：写论文、帮我写引言/方法/讨论、润色这段、读起来像 AI、论文全流程、从头到尾写论文、
  下一步该做什么、论文路线图、论文总调度、把这些阶段串起来。
  English triggers: write my paper, draft a section, polish this, sounds too much like AI, end-to-end
  paper help, what should I do next on my paper, paper roadmap, orchestrate the writing process.
  当任务单一明确且某个专门 skill 明显更合适时，可直接用那个专门 skill；paper-conductor 适合全流程、
  多阶段、不确定从何下手的场景，并能自己兜底完成写作与润色。
metadata:
  version: "0.2.0"
  license: MIT
  author: jiayou20021120-afk
  task_type: open-ended
---

# paper-conductor 论文流水线总调度（集大成助手）

一句话：它是论文全程的集大成助手。能自己写、自己润色、自己审、给你整条路线图；遇到有更强专门工具的环节，它会推荐并把产物交接过去。既是地图，也是车。

## 两种模式并存

| 自己下场做 | 推荐并交接给更强的专门 skill |
|---|---|
| 写作：引言 / 方法 / 讨论 / 全文草稿 | 框架图 / 架构图：`paper-framework-figure-studio-pro`（需切 ChatGPT 出图） |
| 润色、表达改写、基础去 AI 味 | 中文破折号 / 引号 hard gate 级去 AI 味：`aiwei-zh` |
| 基础审稿、自查、给修订意见 | 多 reviewer 深度评审：`academic-paper-reviewer` / `paper-audit` |
| 选题质询、研究问题打磨 | 13-agent 系统性文献调研：`deep-research` |
| 规划全程路线图、阶段定位、handoff | 学校模板 DOCX 交付：`chinese-thesis-workbench`；本地 .bib 检索：`bib-search-citation` |

**判断原则：** 通用文本能力（写、润、审、规划）它自己干；需要专门引擎、外部工具、或硬规则的环节，推荐更强的 skill 并交接。它不是只动嘴的调度台，也不是要取代所有专门工具的黑洞，而是一个"自己能干大半、关键环节知道叫谁"的全程助手。

## 八个阶段

下表给出每阶段它自己能做什么、何时升级到专门 skill。详细卡片见 [`references/stage_cards.md`](references/stage_cards.md)。

| # | 阶段 | 它自己能做 | 何时升级到专门 skill |
|---|---|---|---|
| 1 | 选题质询 | 苏格拉底式追问，帮你逼出可回答的 RQ | 想要 13-agent 团队或 `grill-me` 的深度质询 |
| 2 | 文献调研 | 基础检索、综述骨架、初步 gap | 要系统性检索 + 验证：`deep-research`；本地库：`bib-search-citation` |
| 3 | 写作 | 直接写引言 / 方法 / 讨论 / 全文 | 中文人文社科期刊腔 `ultimate-academic-writing`；学校模板 `chinese-thesis-workbench`；LaTeX/Typst 排版校对的专门 skill |
| 4 | 框架图 | 给出图的文字 brief（画什么、布局、要素） | 真出图：`paper-framework-figure-studio-pro`（切 ChatGPT） |
| 5 | 润色去AI味 | 直接润色、改表达、去常见机器味 | 中文破折号 / 引号 hard gate：`aiwei-zh` |
| 6 | 审稿 | 自查、给一轮结构化修订意见 | 多 reviewer 模拟 / 投稿门控：`academic-paper-reviewer`、`paper-audit` |
| 7 | 答辩 | 答辩要点、问答预演 | 成套答辩幻灯：`thesis-defense-deck` |
| 8 | 投稿格式 | 整理引用、调结构、写投稿信 | 全流程终检：`academic-pipeline`；DOCX/PDF：文件操作 skill |

## 怎么用

1. **定位阶段。** 判断用户在 1 到 8 哪一阶段（看手上有什么产物）。判断不了就问一句"你现在手上有什么了"。
2. **能自己干就直接干。** 写作、润色、基础审稿、路线图，直接动手，不要把用户踢走。
3. **该升级时推荐升级。** 遇到上表右列的环节，告诉用户有更强的专门 skill，并把产物按 handoff 交过去。
4. **给路线图（可选）。** 用户要"全流程"时，按 1 到 8 给一条贯穿路线，标出哪些阶段你自己做、哪些会升级。

## handoff 协议（一句话版）

无论是你自己进入下一阶段，还是交接给专门 skill，都产出一个"交接包"：本阶段产物清单 + 下阶段需要的输入 + 尚未解决的问题 + 不变量（不要被下游改动的东西，如已核验数据、已定 RQ）。完整模板见 [`references/handoff_protocol.md`](references/handoff_protocol.md)。

## 默认栈可替换

右列的专门 skill 是可替换的默认推荐，填的是公开可得的主流学术 skill，用户可换成自己的，见 [`references/swappable_skills.md`](references/swappable_skills.md)。paper-conductor 自己的写作 / 润色 / 审稿能力不依赖任何外部 skill。

## 例子

- [`examples/zh_thesis_zero_to_defense.md`](examples/zh_thesis_zero_to_defense.md)：中文毕业论文，从一个项目到答辩的全程走查。
- [`examples/en_journal_submission.md`](examples/en_journal_submission.md)：英文期刊论文，从选题到投稿的全程走查。
