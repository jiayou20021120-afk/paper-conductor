# 走查：中文毕业论文，从一个项目到答辩

场景（脱敏）：本科生小 A 做了一个移动端待办应用，想把它写成毕业设计论文，学校给了 Word 模板，最后要答辩。

下面展示 paper-conductor 怎么按阶段把人接力下去。它本身一行论文都不写，只导航和交接。

---

## 起点：用户说"我做了个 App，想写成毕设，不知道从哪开始"

**conductor 定位：** 有真实项目、有模糊意图、没有研究问题也没有文字。判定在阶段 1 和阶段 3 之间，但缺一个研究问题。先回阶段 1。

**conductor 输出：**
> 你手上是一个完整的工程项目，但论文需要一个能回答的问题。先用 `superpowers:brainstorming` 或 `mattpocock-skills:grill-me` 把"这个 App 解决了什么、和已有方案比好在哪、能验证什么"问清楚。产出一个研究问题，再进下一步。

## 阶段 1 → 2 交接

```
本阶段产物：RQ（这个 App 的某项设计是否提升了某指标）+ 范围
下阶段需要：围绕 RQ 的文献检索词
不变量：RQ 不在调研里被偷换
```

**conductor 输出：**
> 现在去 `deep-research` 做这个题目的文献调研，参考文献用 `bib-search-citation` 管起来（投稿/查重阶段会省事）。

## 阶段 2 → 3 写作

**conductor 定位：** 有项目、有 RQ、有文献，是中文毕业论文且有学校 Word 模板。

**conductor 输出：**
> 这步最适合 `chinese-thesis-workbench`，它能按学校模板填充、控制章节字数、处理 Word 批注。把交接包（RQ + 文献清单 + gap + 你的项目材料）喂给它。

## 阶段 3 → 4 → 5

**conductor 输出（连续交接）：**
> 草稿出来后：方法/系统架构那章用 `paper-framework-figure-studio-pro` 画一张系统框架图（Claude Code 内只出文本 brief，图像切 ChatGPT 网页版）。图回填后，全文用 `aiwei-zh` 去一遍 AI 味，破折号和引号它会硬卡。

## 阶段 5 → 6 审稿

**conductor 输出：**
> 投答辩前先自审。`academic-paper-reviewer` 模拟一组评审，或 `paper-audit` 做投稿门控，给你 must-fix 清单。按意见回阶段 3 或 5 修订，最多两轮。

## 阶段 6 → 7 答辩

**conductor 输出：**
> 定稿后用 `thesis-defense-deck`。注意它的纪律：答辩 PPT 不是论文搬家，面向的是听众理解。

---

**conductor 全程做了什么：** 8 次定位 + 7 次交接 + 0 次代写。每一步它都把人交到正确的 skill 手里，并保证 RQ、数据、文献这些不变量不被下游悄悄改掉。
