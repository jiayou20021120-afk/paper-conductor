# 设计文档：paper-conductor

日期：2026-05-22
作者：jiayou20021120-afk
状态：v0.1.0 首版

## 问题

学术写作的 skill 生态越来越丰富（调研、写作、制图、去 AI 味、审稿、答辩 PPT），每个都很强但各自为战。真正写一篇论文时，最难的常常不是某一步，而是"现在该用哪个、上一步产物怎么交给下一步、有没有一条完整路线"。缺的是编排层。

## 目标

1. 一个通用的"按阶段路由"层，覆盖论文生产全程的 8 个阶段。
2. 每阶段给出推荐 skill、触发例句、handoff 协议。
3. 通用且可替换：默认推荐公开 skill，用户可换成自己的栈。
4. 原创、MIT、独立发布，不内嵌任何被推荐 skill 的代码。

## 非目标（YAGNI）

- 不亲自执行写作 / 润色 / 审稿 / 制图。这是硬边界，写进 description 防止抢触发。
- 不做 GUI。
- 不做自动执行（不替用户跑被推荐的 skill）。
- 首版只做中英双语触发，不做更多语言。

## 架构

纯文档型 skill（无脚本）。

```
paper-conductor/
├── SKILL.md              # 触发 + 路由总表 + 编排逻辑 + handoff 摘要
├── references/
│   ├── stage_cards.md    # 八阶段详细卡片
│   ├── handoff_protocol.md  # 交接包模板 + 速查 + 不变量规则
│   └── swappable_skills.md  # 默认推荐 + 公开来源 + 替换说明
├── examples/             # 中文毕业论文 / 英文期刊 两个全程走查
├── README.md
├── LICENSE               # MIT
└── .claude-plugin/       # plugin.json + marketplace.json
```

## 关键设计决策

1. **编排不执行。** 边界写死进 description。当用户有单一明确任务时，直接路由到对应 skill，不走 conductor。这避免与被调度 skill 的触发冲突。
2. **通用框架 + 默认栈。** 路由逻辑通用（按 8 阶段），默认推荐填公开 skill，用户可替换。比"导出私人配置"更有公开价值。
3. **只指向，不再分发。** 不复制任何被推荐 skill 的源码，因此不受其 license 约束（ARS 是 CC BY-NC 4.0，AWS 是 MIT），只在推荐时注明出处。这让 paper-conductor 自身可以干净地用 MIT。
4. **不变量规则。** handoff 协议要求每次交接显式列出"不变量"（已核验数据、已定 RQ、术语表），给下游 skill 立护栏，防止数据被悄悄改写或编造。

## 与 ARS / AWS 的关系

paper-conductor 把 ARS、AWS 等都当作它路由图上的节点。之前尝试把 AWS 合并进 ARS 上游被婉拒（维护负担），作者建议用 companion-plugin 模式。paper-conductor 正是这个模式的干净实现：它不求任何上游收录，而是做那个统筹各家的编排层，并在 README 大方致谢所有被路由的项目。

## 未来（不在 v0.1.0）

- 更多语言触发。
- 阶段卡片里加"质量门"（每阶段最小验收标准）。
- 可选的状态追踪（记录用户走到哪一阶段）。
