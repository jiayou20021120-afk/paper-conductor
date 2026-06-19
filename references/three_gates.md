# 三道闸：动笔前想清楚、动笔时留痕、定稿前硬检

这三样是 conductor 在「自己下场写」时给自己上的约束。它们都不依赖外部 skill，是 conductor 本体能力的一部分。灵感来自 PaperSpine 的 motivation gate、writing rationale matrix 和确定性 guard，按中文期刊投稿场景重做。

三道闸落在三个阶段：

| 闸 | 阶段 | 形态 | 作用 |
|---|---|---|---|
| 1. motivation 闸门 | 选题质询（1）→ 写作（3）之间 | `confirmed_motivation.md` | 没拍板 motivation 不许动笔，且禁止把一个窄贡献注水成多条 claim |
| 2. rationale 矩阵 | 写作（3） | `writing_rationale_matrix.md` | 逐段记「为什么这么写」，事中留痕，审稿和返修直接复用 |
| 3. 确定性 guard | 润色（5）/ 投稿（8） | `scripts/ai_tell_guard.py` | 破折号、直引号、本文密度、口水词，外加超长句与术语锚点，按固定规则零 token 复检，不让模型自评 |

---

## 闸 1：motivation 闸门

**规则：** 进入写作前，先和用户敲定一句话 motivation 并写进 `confirmed_motivation.md`。用户没确认就停在这里，不要先写引言。

**反注水：** 一篇论文一条主 motivation。如果它需要三个并列的「我们还做了…」才撑得起，多半是把一个窄发现吹大了。宁可窄而实，不要宽而虚。这正治选题发散。

**模板（写进 `confirmed_motivation.md`）：**

```markdown
# Confirmed Motivation

一句话 motivation：____（≤ 40 字，一个具体命题，不是一串卖点）

- 它回答的研究问题（RQ）：____
- 为什么现在值得做（gap / 反常 / 政策窗口）：____
- 它**不**主张什么（划掉的越界 claim）：____
- 验证它需要的最小证据：____
- 用户确认：是 / 否　（否就停，回阶段 1）
```

收尾自检：能不能用「本文检验了 X 是否 Y」一句话复述？复述不出来就是还没收敛。

---

## 闸 2：writing_rationale 矩阵

**规则：** 写每个主要单元（章 / 节 / 关键段）前，先在矩阵里补一行：这段干什么、服务哪条 motivation、用什么证据、最后要过什么检查。它是事中的执行计划，不是写完补的总结。

**为什么值钱：** 审稿和返修时，「这段当初为什么这么写」一翻就有；reviewer 问到某段的依据，直接对照证据列回应，不用重读全文。

**模板（写进 `writing_rationale_matrix.md`）：**

```markdown
# Writing Rationale Matrix

| 单元 | 功能 | 服务的 motivation | 用到的证据 | 学到的范例结构 | 定稿要过的检查 |
|---|---|---|---|---|---|
| 引言·第1段 | 抛反常现象勾住读者 | 主 motivation | 张静庐史料某条 | 范文A的开篇钩子 | 无空泛大词、本文≤1次 |
| 方法·分期检验 | 说清怎么测 | 主 motivation | 变点检测结果表 | 范文B的方法骨架 | 可复现、参数交代全 |
| … | … | … | … | … | … |
```

不变量：证据列里的数据、已核验引用、已定 RQ 属于 handoff 不变量，下游润色 / 排版不许动。

---

## 闸 3：确定性 AI-tell guard

**规则：** 润色完一轮、以及投稿前，跑一次脚本。它不是让模型再读一遍自评，而是按固定规则判定，同一份稿子永远同一个结论，零 token。

**用法：**

```bash
# 直接扫 docx（stdlib 抽取，无需 python-docx）
python3 scripts/ai_tell_guard.py 论文_定稿.docx --markdown

# 也吃 .md / .txt，或从 stdin 读
python3 scripts/ai_tell_guard.py draft.md
cat draft.txt | python3 scripts/ai_tell_guard.py -
```

**判定：**

- **FAIL（拦截，退出码 1）：** 破折号家族（`—` `―` `——` 等）、紧邻中文的直引号 `"` `'`（纯 ASCII / 英文引号 / 代码上下文不报，避免误杀）。这两条是硬规则，FAIL 不清零就不算定稿。
- **WARN（提示，不拦截）：** 本文密度 > 约 1/千字、口水词（值得注意的是 / 综上所述 / 显而易见…）、枚举脚手架（首先，/ 其一，…）、单行全角括号堆叠，以及照 `paper-humanlike-checklist` 七症状补的：须字辈合规旁白（须注意 / 还须澄清…）、元叙述过渡腔（本文将 / 接下来将 / 如前所述…）、评论散文笔法（再往深处看 / 真正的问题或许是…）、自问自答（论证段问完立答）、设问开场（那么，/ 难道…）。研究问题用问号收尾不会误报。此外按可读性体检（认知负荷维度，正交于 AI 味）补两项：超长句（单句 > 60 字，阈值见脚本 `LONG_SENTENCE_CHARS`）、高门槛术语首现无锚点（能见度 / 右删失 / 部均…，词表 `JARGON_ANCHOR`，计量稿嫌吵可删，修复动作见 [`readability_pass.md`](readability_pass.md)）。

**边界：** 它只查可程序化的硬指纹，不替代阶段 5 的语义润色，也不替代 `aiwei-zh` 的六维深洗。它是定稿前那道「机器先过一遍、人再过」的栅栏。改规则改 `scripts/ai_tell_guard.py` 顶部的 `EM_DASHES` / `STRAIGHT_QUOTES` / `FILLER` / `LONG_SENTENCE_CHARS` / `JARGON_ANCHOR` 列表即可。
