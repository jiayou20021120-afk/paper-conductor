# 升级清单：何时换用更强的专门 skill

paper-conductor 自己就能做通用的写作、润色、基础审稿、路线规划。下面这些专门 skill 是各环节的"增强"：当你需要比通用能力更强的东西时（专门引擎、外部工具、硬规则），升级到它们。每个都可替换成你自己的栈。

## 怎么替换

在你的会话里直接告诉 paper-conductor："我这个阶段用 X 不用默认的 Y"，或在自己的 fork 里改本文件的"默认推荐"列。paper-conductor 不依赖任何特定供应商。

## 默认推荐与来源

| 阶段 | 升级到的专门 skill | 公开来源 | 替代选项 |
|---|---|---|---|
| 1 选题 | `superpowers:brainstorming`、`mattpocock-skills:grill-me` | obra/superpowers、mattpocock 社区插件 | 任何苏格拉底式质询工具 |
| 2 调研 | `deep-research`、`bib-search-citation` | ARS（Imbad0202）、AWS（bahayonghang） | 任何文献检索 / 综述工具 |
| 3 写作（英） | `academic-paper` | ARS（Imbad0202，CC BY-NC 4.0） | 任何论文写作 agent |
| 3 写作（中文人文社科） | `ultimate-academic-writing` | anthropic skills | 任何中文学术写作工具 |
| 3 写作（中文毕业论文） | `chinese-thesis-workbench` | ZyhSechub | 任何按学校模板交付的工具 |
| 3 排版 | `latex-paper-en`、`latex-thesis-zh`、`typst-paper` | AWS（bahayonghang，MIT） | 任何 LaTeX/Typst 助手 |
| 4 制图 | `paper-framework-figure-studio-pro` | c-narcissus | 任何框架图工具 |
| 5 去 AI 味 | `aiwei-zh` | AWS（bahayonghang，MIT） | 任何中文去 AI 味工具 |
| 6 审稿 | `academic-paper-reviewer`、`paper-audit` | ARS、AWS | 任何同行评审模拟工具 |
| 7 答辩 | `thesis-defense-deck` | 社区 | 任何答辩 PPT 工具 |
| 8 投稿格式 | `academic-pipeline`、`docx`/`pptx`/`pdf` | ARS、anthropic skills | 任何编排 / 文件操作工具 |

## 关于来源的说明

paper-conductor 本身是 MIT，原创，不内嵌上面任何一个 skill 的代码。它只是在文档里"指向"这些独立 skill，由用户自行安装。这与各上游的 license 完全兼容：

- 指向（link / route），不是再分发（redistribute）。
- ARS 是 CC BY-NC 4.0，AWS 是 MIT；paper-conductor 不复制它们的任何文件，因此不受其 license 约束，只在推荐时注明出处。
- 用户没装某个推荐 skill 时，paper-conductor 给出公开来源，由用户决定是否安装。
