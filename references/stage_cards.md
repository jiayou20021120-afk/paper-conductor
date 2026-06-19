# 阶段卡片（八张）

每张卡片回答：怎么认出用户在这一阶段、conductor 自己能做什么、何时升级到更强的专门 skill、需要什么输入、产出什么、怎么交给下一阶段、常见坑。

核心原则：通用文本能力（写、润、审、规划）conductor 自己直接做；需要专门引擎、外部工具、或硬规则的环节，推荐更强的 skill 并交接。

---

## 阶段 1：选题质询（Topic & Framing）

- **识别信号：** 用户只有模糊兴趣，没有可回答的研究问题。
- **conductor 自己做：** 苏格拉底式追问，帮用户逼出可回答的 RQ、初步假设、范围边界。
- **何时升级：** 想要 13-agent 团队的深度探索用 `deep-research`(socratic)；想被狠狠质询用 `mattpocock-skills:grill-me`。
- **输入：** 一个兴趣领域 / 观察 / 现象。**产出：** 可回答的 RQ + 假设 + 范围。
- **motivation 闸门（闸 1）：** 在交到写作前，敲定一句话 motivation 写进 `confirmed_motivation.md`；一篇一条主 motivation，禁止把窄贡献注水成多 claim。用户没确认就停在这里。模板见 [`references/three_gates.md`](three_gates.md)。
- **handoff 到 2：** RQ + 假设 + confirmed_motivation 打包，作为检索起点。
- **常见坑：** 跳过这步直接写，导致论文没有清晰问题；或把一个窄发现吹成一串卖点。

---

## 阶段 2：文献调研（Literature Research）

- **识别信号：** 已有 RQ，需要知道别人做过什么、空白在哪。
- **conductor 自己做：** 基础检索、综述骨架、初步 gap 识别、给方法蓝图草案；**本地证据可回溯文献问答**——对用户手上的几篇全文做"逐块取证 + 逐句引用 + 证据不足拒答"的问答，无需 API key，协议见 [`references/local_evidence_qa.md`](local_evidence_qa.md)。
- **何时升级：** 要系统性**网络**检索 + 来源验证 + 偏倚评估用 `deep-research`(full/systematic)；已有结构化 .bib 库检索用 `bib-search-citation`。（本地全文取证问答是 conductor 自己做的，与这两者互补。）
- **输入：** 阶段 1 的 RQ。**产出：** 综述骨架 + 关键文献 + gap + 方法蓝图。
- **handoff 到 3：** RQ Brief + 方法蓝图 + 文献清单 = 写作原料。
- **常见坑：** 把综述写成罗列。要有比较、有冲突、从冲突里推 gap。

---

## 阶段 3：写作（Drafting）

- **识别信号：** 有 RQ、文献、（可能）数据，要变成文字。
- **conductor 自己做：** 直接写引言 / 方法 / 讨论 / 结论 / 全文草稿，按 IMRaD 或学科结构组织论证。
- **rationale 矩阵（闸 2）：** 写每个主要单元前先在 `writing_rationale_matrix.md` 补一行（功能 / 服务哪条 motivation / 用什么证据 / 定稿要过什么检查）。事中留痕，审稿返修直接复用。模板见 [`references/three_gates.md`](three_gates.md)。
- **何时升级：** 中文人文社科期刊腔用 `ultimate-academic-writing`；中文毕业论文按学校模板交付用 `chinese-thesis-workbench`；已定 LaTeX/Typst 格式且要编译校对用对应排版 skill；要 12-agent 协作写作用 `academic-paper`。
- **输入：** 阶段 2 交接包 + confirmed_motivation（+ 实验结果，若有）。**产出：** 论文草稿 + rationale 矩阵。
- **handoff 到 4/5：** 方法/架构章节交给制图；全文交给润色。
- **常见坑：** 边写边抠格式。先把内容写顺，排版和去 AI 味放后面。

---

## 阶段 4：框架图（Figures）

- **识别信号：** 需要方法概览图、架构图、流水线图。
- **conductor 自己做：** 给出图的文字 brief（画什么、布局、要素、各模块关系），可直接嵌进草稿描述。
- **何时升级：** 真要出图用 `paper-framework-figure-studio-pro`（Claude Code 内只跑文本工作流，图像步骤切 ChatGPT 网页版或 Codex）。
- **输入：** 草稿的方法/架构文字。**产出：** 图的 brief 或成图。
- **handoff 到 5：** 图配 caption 回填草稿，再整体润色。
- **常见坑：** 方法没定稿就画图，图文不一致。

---

## 阶段 5：润色与去 AI 味（Polish & De-AI）

- **识别信号：** 内容定了，读起来生硬、像 AI、或要停下来逐句解码。
- **conductor 自己做（两关正交）：** ① 去 AI 味——口水词、千篇一律的段落结构、过渡腔，治的是「像不像机器写的」指纹。② 可读性体检——术语密度、超长句、抽象无锚点、防御性堆叠、数据轰炸结论后置，治的是「读者带宽够不够」的认知负荷。一篇可以零 AI 味却依旧难读，两关都要过。七个信号和修复动作见 [`references/readability_pass.md`](readability_pass.md)。
- **确定性 guard（闸 3）：** 润色完跑一次 `python3 scripts/ai_tell_guard.py 稿件 --markdown`，按固定规则零 token 复检；破折号、直引号是 FAIL，不清零不算过。FAIL 查机器指纹，WARN 兼查超长句与术语锚点这类认知负荷信号。它在语义润色之外加一道机器栅栏，不替代 `aiwei-zh` 的深洗。见 [`references/three_gates.md`](three_gates.md)。
- **何时升级：** 中文要破折号/引号 hard gate 级、皇甫 2026 六维框架严格清洗用 `aiwei-zh`；LaTeX/Typst 语法层用对应排版 skill。
- **输入：** 阶段 3/4 草稿。**产出：** 通顺、去机器味、过了可读性体检和 guard 的稿子。
- **handoff 到 6：** 干净稿交审稿。
- **常见坑：** 两个。一是把润色和审稿混为一谈——润色管"读起来怎样"，审稿管"立得住吗"。二是只去 AI 味、不查可读性——破折号清零了，读者还是每句卡死；去了指纹不等于降了负荷。

---

## 阶段 6：审稿（Review）

- **识别信号：** 稿子完整，想知道能不能投、有什么硬伤。
- **conductor 自己做：** 自查、给一轮结构化修订意见（贡献是否清晰、论证是否成立、方法是否站得住、引用是否到位）。
- **何时升级：** 要多视角模拟评审（EIC + 3 reviewers + Devil's Advocate）用 `academic-paper-reviewer`；要 pass/fail 投稿门控用 `paper-audit`。
- **输入：** 阶段 5 干净稿。**产出：** 修订意见 + 决策。
- **handoff 回 3/5：** 按意见回写作或润色，最多两轮，剩余写进局限。
- **常见坑：** 把 AI 审稿当真同行评审。它是自查工具，不替代真实评审。

---

## 阶段 7：答辩（Defense）

- **识别信号：** 论文定了，要做面向答辩委员会的展示。
- **conductor 自己做：** 提炼答辩要点、预演可能的提问与回答、给讲稿骨架。
- **何时升级：** 要成套答辩幻灯用 `thesis-defense-deck`（它有七条纪律，避免把论文整段搬上 PPT）。
- **输入：** 定稿论文。**产出：** 答辩要点 + 问答预演（+ 幻灯，若升级）。
- **handoff：** 通常是终点之一；答辩反馈可回流到下一篇选题（回阶段 1）。
- **常见坑：** 把论文整段搬上 PPT。答辩面向听众理解，不是信息完整。

---

## 阶段 8：投稿与格式（Submission & Formatting）

- **识别信号：** 内容语言都好了，要处理参考文献、排版、投稿格式。
- **conductor 自己做：** 整理引用、调整结构符合目标体例、起草投稿信（cover letter）。
- **确定性 guard（闸 3，终检）：** 投稿前对最终 docx 再跑一次 `python3 scripts/ai_tell_guard.py 定稿.docx --markdown`，确保破折号、直引号 FAIL 清零。这是交出去前最后一道机器栅栏。
- **何时升级：** 要全流程终检（引用/数据 100% 复核）用 `academic-pipeline`；.bib 导出用 `bib-search-citation`；DOCX/PDF 文件操作用对应 skill。
- **输入：** 定稿 + 目标期刊格式要求。**产出：** 投稿就绪文件包。
- **handoff：** 投出。被拒/返修则回阶段 6 解析意见，再到 3/5 修订。
- **常见坑：** 临投稿才发现引用格式不对。参考文献在阶段 2 就该管起来。
