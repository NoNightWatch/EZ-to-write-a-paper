<p align="center">
  <img src="assets/writing-guild.png" width="960" alt="Paper Quest · The Writing Guild：星夜图书馆里，初学者与导师一起修改稿件。" />
</p>
<p align="center">
  <img src="assets/guild/invitation.svg" width="960" alt="How to write a paper · 从已有文字，走向下一段。" />
</p>

<h1 align="center">从第一段，写到一篇清楚的论文。</h1>

<p align="center">
  面向学术写作初学者与已有稿件作者的 AI 写作导师 skill。<br />
  带上你的稿件、笔记或参考文献，让助手按学科、期刊与本轮需求帮助你修改，并讲清楚理由。
</p>

<p align="center">
  <a href="docs/guide.zh-CN.md"><img src="assets/guild/start.svg" width="280" alt="开始使用：中文用户指南" /></a>
  &nbsp;
  <a href="https://github.com/NoNightWatch/EZ-to-write-a-paper/releases/latest"><img src="assets/guild/download.svg" width="280" alt="下载完整技能包 v3.2.0" /></a>
</p>
<p align="center">
  <a href="docs/guide.zh-CN.md">中文指南</a> ·
  <a href="README.en.md">English</a> ·
  <a href="docs/guide.en.md">English guide</a> ·
  <a href="academic-manuscript-polish/SKILL.md">Skill 入口</a> ·
  <a href="#quick-start">快速开始</a>
</p>
<p align="center"><strong>Codex · Claude Code · 可读取本地资料的 AI 助手</strong><br /><sub>v3.2.0 · 完整包可独立使用 · 中英用户指南 · 教材主体为中文</sub></p>

<img src="assets/guild/inventory.svg" width="960" alt="52 个学科入口 · 2,080 条基础词表记录 · 10 类写作路径 · 15 份期刊资料卡" />

<sub>2,080 条记录含跨领域重复，英文词头字面去重为 2,043 项。学科入口提供基础覆盖；期刊卡为注明范围与日期的参考，实际投稿需查当前要求。</sub>

<img src="assets/guild/quests.svg" width="960" alt="01 · 选择当前任务" />

## 你现在卡在哪里？

<table>
<tr>
<td width="50%" valign="top">
<img src="assets/guild/mentor.svg" width="460" alt="写作导师：先给可用修改，再解释关键处" />
<h3>有东西想说，却不知道怎样写</h3>
<p>从中文笔记、零散句子或一个段落开始。先得到一版可用修改，再了解一两处关键改动。愿意练习时，导师带你完成一个小目标。</p>
<p><a href="academic-manuscript-polish/references/beginner-guide.md">新手入口</a> · <a href="academic-manuscript-polish/references/mentor-lessons.md">九节小课</a></p>
</td>
<td width="50%" valign="top">
<img src="assets/guild/review.svg" width="460" alt="综述写作：比较材料，组织有来源的段落" />
<h3>读了很多文献，还是写成逐篇介绍</h3>
<p>围绕一个具体问题比较材料，把相同点、差异与适用范围组织进段落。先区分引言小段、学位论文章节和独立综述，再选择对应流程。</p>
<p><a href="academic-manuscript-polish/references/literature-review-mentor.md">综述导师</a> · <a href="academic-manuscript-polish/references/review-worked-example.md">完整练习</a></p>
</td>
</tr>
</table>

| 你的任务 | 可以直接这样说 | 本轮交付 |
| :--- | :--- | :--- |
| 已有初稿，只想改语言 | “保持内容，只改语法、表达和衔接。” | 修订文字与必要问题 |
| 不知道章节怎样展开 | “先帮我整理这节的顺序，再解释调整。” | 基于已有材料的结构与修订 |
| 跨学科词语容易混用 | “检查全文里的术语与缩写是否一致。” | 有上下文的术语核对 |
| 准备投某本期刊 | “按目标刊的当前作者指南检查这部分。” | 已核验要求、修改与未决项 |
| 想学会自己改 | “先示范一段，再给我一个可选练习。” | 修改、解释与练习参考 |

你可以随时说“直接给稿”或“讲细一点”。无需先学会写作分类，也无需填完一套表格。

<a id="quick-start"></a>
<img src="assets/guild/start-here.svg" width="960" alt="02 · 第一次使用" />

## 三步开始

### 1. 下载完整文件夹

从 [Releases](https://github.com/NoNightWatch/EZ-to-write-a-paper/releases/latest) 下载技能 ZIP 并解压。保留完整的 `academic-manuscript-polish/` 文件夹，包括 `SKILL.md`、`references/`、`assets/` 和其他文件。也可使用 GitHub 的 **Code → Download ZIP** 下载整个仓库。

### 2. 放进助手能读取的位置

| 使用环境 | 项目内安装位置 |
| :--- | :--- |
| Codex | `<你的项目>/.agents/skills/academic-manuscript-polish/` |
| Claude Code | `<你的项目>/.claude/skills/academic-manuscript-polish/` |
| 其他可读文件的助手 | 保持目录完整，请它读取 `SKILL.md` 并按需访问相对链接 |

支持范围取决于宿主与组织设置。[安装与排错](docs/guide.zh-CN.md#install) 包含用户级目录和检查方法；路径依据 [OpenAI](https://learn.chatgpt.com/docs/build-skills) 与 [Claude Code](https://code.claude.com/docs/en/skills) 官方说明。

### 3. 给它一个真实片段

```text
请使用 academic-manuscript-polish。

材料：下面是我的稿件 / 中文笔记 / 提纲。
目标期刊：［刊名；未定也可以］。
本轮范围：［一句 / 一段 / 一个章节 / 全文］。
输出语言：［中文 / 英文］。

先给可用修订，再解释最重要的两三处。
保留数字、引用和原意；专业内容不确定时请问我。
［在这里粘贴材料，或提供可访问的文件］
```

安装后，Codex 可使用 `$academic-manuscript-polish`；Claude Code 可使用 `/academic-manuscript-polish`。第一次建议选一个段落，确认修改幅度合适后再扩大范围。

<img src="assets/guild/library.svg" width="960" alt="03 · 技能包里有什么" />

## 打开这间写作资料室

| 资料 | 内容与入口 |
| :--- | :--- |
| **学科与术语** | [52 个入口](academic-manuscript-polish/references/discipline-map.md)，覆盖自然科学、工程与技术、医学与健康、农业科学、社会科学、人文与艺术，另含通用写作与统计表达 |
| **术语细读** | [基础词表](academic-manuscript-polish/references/foundation-index.md)及[九册详细词表](academic-manuscript-polish/references/glossary-index.md)，详细部分 308 条，含用法与边界 |
| **文章组织** | [十类写作路径](academic-manuscript-polish/references/writing-framework.md)，分别讲引言如何进入、主体如何排序、讨论如何组织已有解释 |
| **逐节写作** | [章节手册](academic-manuscript-polish/references/section-handbook.md)、[英语表达工具页](academic-manuscript-polish/references/language-toolkit.md)、12 个[修改示例](academic-manuscript-polish/references/worked-examples.md) |
| **边写边学** | [九节小课](academic-manuscript-polish/references/mentor-lessons.md)、[六组导师对话](academic-manuscript-polish/references/mentor-dialogues.md)、[52 个领域练习](academic-manuscript-polish/references/domain-practice.md) |
| **文献综述** | [阅读与综合流程](academic-manuscript-polish/references/literature-review-mentor.md)、[完整练习](academic-manuscript-polish/references/review-worked-example.md)、[四个跨学科练习](academic-manuscript-polish/references/review-transfer-cases.md) |
| **期刊适配** | [15 份资料卡](academic-manuscript-polish/references/journal-cards.md)与[适配流程](academic-manuscript-polish/references/journal-adaptation.md)，区分刊方要求、样文观察和未核验内容 |
| **你的领域尚未覆盖** | 用[作者补充文献流程](academic-manuscript-polish/references/author-literature.md)建立本稿专用术语与体裁参考 |

基础释义是工作用短释义，未逐条经外部专家核验。详细词条与基础词表有重合。模型应按当前稿件选择相关资料，正式定义回到原始文献或标准核对。

<details>
<summary><strong>展开：十类写作路径</strong></summary>

| 路径 | 适合的文字任务 |
| :--- | :--- |
| A · 概念、模型与形式证明 | 交代对象、定义与推导依赖 |
| B · 过程说明 | 按环节、位置或时间组织已有材料 |
| C · 比较研究 | 用相同指标讲清比较对象 |
| D · 问题逐项回应 | 让问题、结果与讨论一一对应 |
| E · 条件与时间展开 | 从总体结果展开不同阶段或条件 |
| F · 图谱与预测报告 | 交代覆盖范围、任务与原稿指标 |
| G · 方法与工具介绍 | 从具体使用任务进入已有表现 |
| H · 定义与测量比较 | 区分概念、指标与方法对应关系 |
| I · 历史、文本与情境叙事 | 按时序、主题或材料单元展开 |
| J · 文献综合 | 按问题与比较维度组织多篇文献 |

这些路径可以组合。它们服务于文字组织，专业理论与研究设计需要作者材料支持。

</details>

<img src="assets/guild/field-notes.svg" width="960" alt="04 · 看一次具体修改" />

## 改完之后，你应该知道改了什么

以下为虚构教学示例，不可作为研究证据引用。

**作者给的材料**

> 我们访谈了 18 位学生。访谈中有 12 人说反馈来得太晚。我们想说明他们怎么看反馈的时间。

**英文修订示例**

> We interviewed 18 students about their perceptions of feedback timing. Twelve participants reported that feedback arrived too late.

**导师解释**

1. 第一句交代对象、人数和主题，读者可以立刻定位研究。
2. 第二句保留 `reported`，明确这是受访者的陈述。
3. 两个数字均保留。没有补写反馈对成绩的影响，因为材料没有提供这项结果。

**下一步可选任务**：补充作者实际使用的访谈时间窗，再决定是否需要写进方法段。你也可以直接继续下一段。

<img src="assets/guild/workflow.svg" width="960" alt="05 · 从材料到修订稿" />

## 每次修改都有清楚的范围

| 阶段 | 助手处理什么 | 你能检查什么 |
| :--- | :--- | :--- |
| 读材料 | 确认实际能读到的内容和本轮任务 | 哪些部分已读，哪些不可读 |
| 找资料 | 按需匹配学科词表、章节与期刊规则 | 用了哪些资料，哪些要求待核验 |
| 做修改 | 在约定幅度内修改语言或组织 | 修订稿与原文的对应 |
| 讲理由 | 解释最重要的几处，可附练习 | 为什么改、保留了什么 |
| 做核对 | 复核数字、单位、引用、术语和可见格式 | 已完成部分与仍需作者处理的事项 |

综述任务会额外记录实际阅读范围，先核对每项主张的来源，再组织综合段落。长稿可分批推进；需要续接时可生成一张进度卡，保存须由作者提出。

<img src="assets/guild/faq.svg" width="960" alt="06 · 常见问题与使用边界" />

## 出发前，先知道这些

<details>
<summary><strong>没有完整稿件，也没选期刊，可以用吗？</strong></summary>

可以。先给已有笔记、提纲或一个段落。期刊未定时做通用修改。只有选题、没有实质材料时，先整理问题和材料清单，不生成研究事实。

</details>

<details>
<summary><strong>我的学科不在目录里，怎么办？</strong></summary>

提供与你的稿件相近的文献或术语定义，并说明希望参考什么。助手会记录来源与适用范围，建立仅供当前稿件使用的资料。几篇样文不能代表整个学科或期刊。

</details>

<details>
<summary><strong>能帮我写文献综述吗？</strong></summary>

可以从你实际提供的材料开始，帮助比较、组织与表达。只有摘要时会标明读取层级。未完成检索、筛选和相应方法流程的材料，不应被命名为系统综述。详见[综述使用指南](docs/guide.zh-CN.md#review)。

</details>

<details>
<summary><strong>整包都是中英双语吗？</strong></summary>

首页和用户指南提供完整中英两版；术语包含中英对应。导师教材与大部分内部说明以中文为主。使用时可要求助手用英文修订和解释，本仓库未声称全部教材已逐页译成英文。

</details>

<details>
<summary><strong>需要 Python 吗？能离线使用吗？</strong></summary>

阅读教材和让助手按流程编辑无需运行脚本。离线查词与校验工具需要 Python 3.9+，只用标准库。AI 助手是否联网、如何处理稿件，由你使用的宿主和账户设置决定；本地存放 skill 不意味着模型在本地运行。

</details>

<details>
<summary><strong>会自动上传稿件、投稿或改动我的原文件吗？</strong></summary>

技能指令要求保留原稿，未经明确要求不发布、投稿或把稿件写入共享包。请检查宿主权限、机构保密要求和目标期刊的 AI 使用政策，再提供未发表材料。不要把私人稿件贴到本仓库的公开 Issue 中。

</details>

**写作边界**：保留作者事实与研究判断，不编造数据、引用、机制或伦理信息，不保证录用。期刊偏好要有来源；当前官方作者指南优先。医学内容限于阅读与学术表达，危险操作细节不由本包补全。

**检查范围**：v3.2.0 完成五轮自审修补，38 项结构与检索测试通过。这些检查不运行语言模型，也不证明教学效果或全部专业定义正确。查看[检查记录](academic-manuscript-polish/tests/release-checks.md)与[资料来源](academic-manuscript-polish/references/sources.md)。

<details>
<summary><strong>展开：目录与可选本地命令</strong></summary>

```text
academic-manuscript-polish/
  SKILL.md               技能入口
  references/            术语、教程、期刊与写作资料
  assets/                可选任务卡与交付模板
  agents/                宿主显示元数据
  scripts/               查词与结构校验
  tests/                 自动测试与检查记录
  bundle-manifest.json   版本与内容清单
```

在技能文件夹内运行：

```sh
python scripts/search_terms.py "validity" --exact
python scripts/search_terms.py --list-domains
python scripts/validate_bundle.py
python -B tests/test_bundle.py
```

</details>

<p align="center"><img src="assets/guild/next.svg" width="960" alt="下一段，从这里开始。" /></p>
<p align="center"><strong>准备一个段落，选一个小目标，然后开始。</strong></p>
<p align="center"><a href="docs/guide.zh-CN.md">阅读中文指南</a> · <a href="docs/guide.en.md">Read the English guide</a> · <a href="https://github.com/NoNightWatch/EZ-to-write-a-paper/releases/latest">下载技能包</a></p>
<p align="center"><sub>觉得有用，可以 Star 收藏。发现问题，欢迎提交不含私人稿件的 <a href="https://github.com/NoNightWatch/EZ-to-write-a-paper/issues">Issue</a>。</sub></p>
