# 从一个段落开始

[English](START-HERE.en.md) · [完整资料](README.md) · [在线用户指南](https://github.com/NoNightWatch/EZ-to-write-a-paper/blob/main/docs/guide.zh-CN.md)

这个文件夹是给 AI 助手读取的写作指令与资料。无需先学术语或选写作流派。教材与检索可在本地阅读，AI 服务的数据处理取决于宿主设置。

如果还不知怎样开始，打开[先说清一件事](references/one-clear-thing.md)，或告诉助手：“先只问我材料里的一件事，让我用平时说话的方式回答。暂时别展开整篇课程。”一句话就可以作为这一轮的产物；已有明确任务时直接继续下面的入口。

## 先试用，可以暂不安装

解压后，把完整文件夹放在助手可读取的工作目录中，然后发送：

```text
请读取 academic-manuscript-polish/SKILL.md，按其中流程帮助我。
先确认入口文件和它需要的资料确实可访问，不安装、不修改配置。
请使用 assets/first-session-demo.md 中的虚构段落做一次示范。
英文修订，中文解释，暂不保存文件。
```

路径不在当前目录时提供实际位置。文件路径形式只表示本地读取；它不等于原生技能已经安装。不能读文件的聊天界面，需要你另行提供相关内容。首次体验无需私人稿件。

## 换成你的文字

```text
请按 academic-manuscript-polish 修改这一段。
只改语言，保留原意；正文沿用原稿语言，解释使用中文。
［粘贴文字］
```

期刊未定也可开始。有目标期刊再补刊名、文章类型和当前作者指南。需要英文解释时直接说明。

## 你可以随时调整

想从零学写整篇，可读[完整论文课程](references/first-paper-course.md)，发送：“用虚构案例带我做 E01。先让我试，再给具体反馈，中文讲解。”课程含完整范文、[中文练习册](references/paper-workbook.zh-CN.md)和新材料练习；需要直接看答案时随时说明。

- “只诊断，先别改。”
- “给干净稿和关键改前改后。”
- “保留这个术语，第二句恢复原句。”
- “我只想要答案，不要练习。”
- “先示范一个句子，再让我试。”

助手应保留原稿，说明实际完成范围。遇到专业定义、数据或原因解释缺失时，需要作者材料支持。

## 经常使用时再安装

将整个文件夹复制到 Codex 项目的 `.agents/skills/` 或 Claude Code 项目的 `.claude/skills/`，在对应项目中启动会话；目录位置以宿主当前说明为准。不要仅复制 `SKILL.md`。新会话中让助手报告实际读取的入口位置，随后用上方示例确认能访问资料。

已有同名版本时先比较版本和自定义改动，保留旧副本到技能扫描目录之外，再替换已确认的目标。不要把两版混在同一个文件夹，或把备份留在会自动加载的 guides 目录里。下载本包不会自动安装或更新现有技能。

## 按当前任务进入

| 你要做什么 | 打开什么 |
|---|---|
| 先看一次输出 | [虚构试用稿](assets/first-session-demo.md) |
| 控制改动和讲解方式 | [本轮控制](references/session-controls.md) |
| 从笔记或句子练写 | [新手入口](references/beginner-guide.md) |
| 把文献组织成段落 | [综述导师](references/literature-review-mentor.md) |
| 回应审稿意见 | [修回流程](references/reviewer-response.md) |
| 学科尚未覆盖 | [补充文献](references/author-literature.md) |

可选离线查词：在本文件夹打开终端，运行 `python scripts/search_terms.py "SOC" --exact --format text`。需要 Python 3.9+；日常改稿不要求运行脚本。
