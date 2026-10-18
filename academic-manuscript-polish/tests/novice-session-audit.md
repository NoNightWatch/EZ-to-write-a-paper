# v3.7.1 新手实际对话试走

日期：2026-10-18。对象：[一句话入口](../references/one-clear-thing.md) / [English entry](../references/one-clear-thing.en.md)及[导师执行流程](../references/gentle-start-mentor.md)。[逐轮对话记录](novice-session-transcripts.json)保留学生与导师的实际输出措辞，省略工具通信并统一空行；末尾回顾为简要归纳。

## 怎样运行

中文首轮与复测各使用一对全新、相互隔离的学生和导师代理。学生只获得虚构背景、两版图书馆说明和学生入口；导师读取执行指南及按需资源，不获得预期答案、疑似问题或首轮结论。维护者逐轮原样转发消息，未在一轮试走中纠正导师。学生自然决定提问与暂停。

首轮读取 v3.7.0，复测读取修订后的工作副本。各有 5 次导师回复。另用一个全新导师运行 2 轮英文请求，检查“开放问题答不上来、要求示范、随后暂停”；英文学生请求由维护者编写，不能计为独立学生模拟。共记录 12 次导师回复。没有设置模型或推理强度覆盖。

这与 [v3.7 的编写式情景走查](gentle-start-audit.md)分开记录。这里确实运行了多轮代理对话，仍属于 AI 角色模拟，未招募真实学生。

## 首轮出现了什么

| 位置 | 实际表现 | 判断与修补 |
|---|---|---|
| 首轮 1 | 学生问两版短说明“这也算材料吗” | 学生页补一句原文、记录、说明和笔记都可用于起步；材料是否足够成篇另行判断 |
| 首轮 1 至 2 | 导师先把“顺一点”改成“更连贯”，学生追问“我觉得”能否放进论文 | 先交代感受句的用途；已有原文时，可从其中可核对的变化形成描述，避免只换词便让学生误以为已完成分析 |
| 首轮 3 至 4 | 导师给“说明了____的先后关系”；学生说自己知道内容，却不知道怎样填进去 | 自由回答优先，句式提示可选；学生原话清楚就直接沿用，避免额外的句式转换任务 |
| 首轮 2 | 导师写“保留了原有的操作顺序” | 文字核对发现该说法范围过宽：新版“日期和座位”并列两项，未单独规定两项之间的先后。补充关系词范围提醒，保留原文实际表达的关系 |
| 首轮 5 | 学生担心字数，并要求暂停 | 导师保留局部成果，请下次带作业要求再判断材料需要；没有扩写凑字数。这项表现保留，无需新增规则 |

前三项属于起步与交流问题；第四项是维护者核对原文发现的表达范围问题，未把它冒充为学生报告的困难。

## 修订后怎样表现

- **复测 1 至 2**：导师先指出两版文字可作为材料，标明“读着顺”是个人感受，再请学生用自己的话比较句子数量。学生实际写出“四句话”与“一句话”的比较，导师保留原句并解释描述可以作为分析起点。
- **复测 3**：学生解释“和”“后”，并追问与顺畅感的联系。导师区分并列与先后关系；关联只表述为可能与个人感受有关，没有声称测过读者效果。
- **复测 4 至 5**：学生询问1500字作业的下一步。导师给出查作业说明的动作及可向老师发送的问题，随后按要求停止。没有把两个句子称作完整论文。
- **英文 1 至 2**：导师从已给博物馆标签的标点提问，未反复要求学生回答宽泛问题。学生请求示范并暂停后，导师给出一句比较，明确来源为虚构标签，随后结束。

首轮的填空句式卡点在这次复测中未复现。复测中的追问仍然存在，涉及句子的用途和怎样继续；导师在当前材料范围内回应。这些记录支持本轮局部修订，无法证明对所有学生或模型均有效。

## 以后复查怎样使用这份记录

用新的学生和导师上下文，向学生提供背景与原始材料，向导师提供执行指南。开始前不把本页结论或已有对话给代理。逐轮记录实际输出，再核对学生是否参与表达、导师是否保留材料含义、困惑是否得到具体回应，以及明确的示范或暂停请求是否得到遵循。发现问题后做局部修改，再换新上下文复测。

不要求逐字复现范句，不用情绪词频、回复长短或静态文字匹配代表教学质量。已看过示范后的回答不计为独立迁移表现。

## 验证边界

仅覆盖一个中文文本比较背景及一个英文短探针。没有测试真实学生、学习迁移、情绪变化、完整论文质量、各学科覆盖或录用结果。学生回顾同样由 AI 生成；审查者也是维护者。两次运行有随机差异，不能把全部差异归因于规则修改。

结构、检索、课程数据和语言入口继续由原有 86 项包内测试与 10 项公共页面测试检查。对话审查与软件检查分开报告，不把 12 次回复加进自动测试数量。

本轮上述 96 项检查通过；结构校验、入口校验、202 处公共页面本地链接和全库相对引用检查通过。中英版本标牌已渲染核对。分发包按提交文件构建，并在新目录复跑包内测试与逐文件字节比对。

## English summary

Two fresh Chinese student/tutor pairs completed five replies each, before and after targeted revisions. The learner contexts received only the fictional persona, raw texts, and learner entry; tutors received the execution guide without expected answers. A separate two-turn English probe used maintainer-written learner inputs.

The first run exposed uncertainty about what counts as material, the use of an impression sentence, and a sentence frame that obstructed an otherwise clear answer. Source review also found an overbroad claim about preserved operation order. The revision clarifies material and sentence purpose, prefers the learner's own words, and preserves the scope of relationships in the source. The fresh retest did not reproduce the sentence-frame obstacle and ended with a concrete next action and a respected pause.

These are AI role-play observations, not evidence of human learning, emotional improvement, or general tutoring reliability. Exact dialogue wording is available in the linked JSON record; student debriefs are summarized.
