# 文风示例：合并、保留、拆分

以下均为原创虚构材料，用于说明语言动作；数字与结果不能作为研究证据。示范没有唯一答案。适用流程见 [领域自然文风](field-natural-style.md)。

## 1. 共享主语，减少重复起头

原稿：

> We analysed annual rental records from 42 cities between 2010 and 2020. We compared trends across regions. We reported estimates for each city.

可选修订：

> We analysed annual rental records from 42 cities between 2010 and 2020, compared trends across regions, and reported estimates for each city.

三个并列动作共享 we，保留城市数、年份、区域比较和逐城市报告。句子变长，段落的重复减少，内容没有扩展。不能自行加上 thereby demonstrating regional inequality，这会添入原稿未给的判断。作者明确只改语法且想保留原节奏时，原稿也可保留。

## 2. 一个长句可以原样保留

原稿：

> Under the stated assumptions, the algorithm returns a feasible solution for every finite input in the specified class and terminates after at most k iterations, where k is the bound defined in Section 2.

可用决定：保留原句。

主干是算法返回解并终止，前置条件约束两项陈述，句尾解释 k。不能因词数较多就拆散，更不能删除 finite、at most 或 specified class。这里仅检查表达，未验证算法命题。真正的稿件仍需核对上下文是否定义了相应条件。

## 3. 跨主语时，重复可以帮助理解

原稿：

> The archive contains council records from 1880 to 1910. Residents' letters describe housing conditions during the same period.

可选修订：

> The archive contains council records from 1880 to 1910; residents' letters describe housing conditions during the same period.

分号连接两条信息，两个主语保留。原来的两句也可用。不能改成 The archive contains council records and describes housing conditions：后一动作被错误归给 archive。原文也没有说明信件存放于这个档案馆。

## 4. 调整主干，有时需要拆句

原稿：

> The model, which was fitted to the 2018 data and which used the same predictors as the baseline, which was fitted to the 2017 data, produced lower errors in the 2019 test set.

可选修订：

> The model used the same predictors as the baseline and produced lower errors in the 2019 test set. The model was fitted to the 2018 data; the baseline was fitted to the 2017 data.

将层层插入的拟合年份移到第二句，保留各自年份与相同预测变量。lower errors 的比较对象在原句中没有直接写明；若上下文也未说明，应提出问题，不能仅凭出现 baseline 就自动补成 compared with the baseline。

## 5. 条件、否定与引用不能在合并时漂移

原稿中的 [A]、[B] 是虚构引用标记：

> Under dry conditions, the coating reduced wear [A]. In wet conditions, it did not reduce wear [B].

可选修订：

> The coating reduced wear under dry conditions [A] but did not reduce wear under wet conditions [B].

保留两个条件、否定和各自引文，不添加显著性、效应大小或机制。若实际材料使用不同涂层或指标，还需保留对应对象，不能照搬合并句。

## 6. 保留一个有作用的短句

原稿：

> These estimates apply to the surveyed cities. Rural districts were not sampled.

可用决定：保留两句。

第二句清楚提醒采样范围。合成一句也可能成立，但减少句数本身没有价值。不能把后一事实扩成“该关系不适用于乡村”，因为未采样没有建立这种结论。

## 7. 教学说明易懂，专业稿件保留精确内容

作者笔记：算法只对有限输入、给定类别成立；终止上限 k；不要省略条件。

给作者的说明可写：“先交代适用范围，再把结果和终止上限放在一起。”稿件可采用示例 2 的完整句子。不能因作者自称初学者就把稿件改成 The algorithm works and stops quickly，这会删除条件和定量边界。

## 8. 译写时不补造逻辑关系

原稿：

> The archive was incomplete. The analysis used 18 letters.

只凭这两句无法确定作者因档案不完整才使用 18 封信。可以保留两句，或给 and 连接的中性备选；不擅自加 because、therefore 或 consequently。原文有意重复某词来保持主题时也无需为了词汇多样性替换。

## 维护时怎样检查

这些是维护者走查情景及未来行为测试材料，没有实际运行独立语言模型。不能将逐项阅读称为自动行为测试通过。

| 情景 | 要检查的结果 | 失败表现 |
|---|---|---|
| 相同主语的三个动作 | 可合并，含义与权限保持 | 自动添加动作之间的因果关系 |
| 清楚的较长条件句 | 可以整句保留 | 只按词数拆句或删条件 |
| 主体切换 | 保留对应主语或明确指代 | 把后一动作交给前一主体 |
| 多层插入语 | 调序或拆分，保留每个条件 | 增补未说明的比较对象 |
| 两个条件、两个来源 | 条件与引用逐项对应 | 引用全移句末，否定范围改变 |
| 有作用的短句 | 可以保留 | 为显得自然而机械合成长句 |
| 初学者写专业段落 | 讲解易懂，正文保留专业精度 | 按作者身份降低信息完整性 |
| 没有样文或只读摘要 | 明确校准范围，继续可做部分 | 声称掌握整刊或母语者风格 |
| 指南只说建议简洁 | 不发明句长硬阈值 | 宣称所有句子最多 20 词 |
| 期刊确有适用的明文要求 | 核实并遵守，保持含义 | 用已发表长句推翻该要求 |
| 作者指定样文筛选范围 | 依据可核实信息筛选，标明缺口 | 根据姓名判断母语或写作水平 |
| 其他语言稿件 | 使用对应语言及体裁的观察 | 将英语句法偏好套到所有语言 |
