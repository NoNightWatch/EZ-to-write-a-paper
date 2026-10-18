# 学科用词与搭配

用于选择研究动词、动作对象、介词搭配和结果表达，尤其适合去翻译腔、检查近义词、比较跨学科写法。专业概念定义仍查原有词表；本层回答“这个意思在当前对象和语境里怎样表达”。

## 如何选词

先读完整句子和必要的前后文，确定动作主体、动作对象、作者实际做过什么，以及这句话承担的任务。中文“重建”可能指组织调整、实体重建、由观测反演、生态恢复或重新编译；这些任务对应的英文存在意义差别。不可仅凭学科名称全篇替换。

1. 明确对象和所指动作。`restructure an organization`、`rebuild a bridge`、`reconstruct an image`、`restore a habitat` 各有适用条件。
2. 从下方目录读取当前领域，检索候选词及搭配；交叉领域可以同时选用两个入口。
3. 判断候选词会不会改变操作、比较基准、量值、时间范围或证据强度。会改变时保留原词或询问作者。
4. 参考作者提供的同领域、同文章类型、同章节样文。记录实际出现的搭配及位置。只看过几个例子时，只能说“所读样文中出现”，不能说“该学科通常更爱用”。
5. 给出一版修订和必要解释；原词准确且自然时可保留。不要为了减少重复，把同一个技术概念换成不同近义词。

“某词适用于某对象”与“某学科使用某词的频率更高”是两类证据。后者需要明确的语料范围、分母、统计口径及体裁匹配，本包没有建立这种频率语料库。作者国籍、姓名或单位不能证明语言习惯。

## 覆盖与读取

52 个入口包含 208 组用词对照。每组含中文意图、英文候选、搭配、选择条件、自拟例句、替换边界和依据标记。四组是每个入口的初始覆盖，不能代表该领域的完整表达范围。

| 学科群 | 用词资料 |
|---|---|
| 通用 | [写作与研究报告](usage/general.md) |
| 自然科学 | [数学、物理、化学、地球、气候、水文、生命、生态、计算](usage/natural-sciences.md) |
| 工程与技术 | [电气、控制、制造、土木、建筑、材料、能源、化工、交通、环境](usage/engineering.md) |
| 医学与健康 | [基础、临床、公卫、药学、护理、营养、口腔](usage/health.md) |
| 农业与兽医 | [农学、土壤、林学、水产、兽医](usage/agriculture.md) |
| 社会科学 | [经济、金融、管理、教育、心理、社会、政治、法律、传播、情报、人口](usage/social-sciences.md) |
| 人文与艺术 | [历史、哲学、宗教、语言、文学、设计、表演](usage/humanities.md) |

各入口编号与 [学科目录](discipline-map.md) 一致。可直接搜索文件，或在包根目录运行：

```text
python scripts/search_usage.py "重建" --format text
python scripts/search_usage.py "rebuild" --domain n10 --format text
python scripts/search_usage.py "restructure" --exact --format text
python scripts/search_usage.py --list-domains
```

检索只返回候选及边界，不编辑稿件，不自动判定最佳词。原有 `search_terms.py` 的行为保持兼容。

## 依据标记

- `E`：编辑整理的工作用法与原创例句，未逐条建立文献频率证据，遇专业歧义需回到作者材料确认。
- `S01` 至 `S08`：下表所列来源支持特定词义或正式搭配；例句仍为原创。不能把来源的支持范围扩展到该行所有候选词或整册内容。

核验日期：2026-10-18。来源记录保留所支持的具体区别，不附第三方全文。

| 编号 | 来源与实际支持范围 |
|---|---|
| S01 | [NOAA Fish Stock Sustainability](https://www.fisheries.noaa.gov/national/population-assessments/fish-stock-sustainability)：使用 rebuild a stock 表达将资源量恢复至管理目标；不能据此替代一般生态恢复术语。 |
| S02 | [Microsoft Build and clean projects](https://learn.microsoft.com/en-us/visualstudio/ide/building-and-cleaning-projects-and-solutions-in-visual-studio)：Build、Rebuild、Clean 的工具语义；不用于证明所有编译系统行为相同。 |
| S03 | [IUPAC sorption](https://goldbook.iupac.org/terms/view/S05769/plain)：sorption 涵盖吸附或吸收；支持避免把未区分机制的过程直接写成 adsorption。 |
| S04 | [SER ecological restoration](https://chapter.ser.org/northeast/about/ecological-restoration/)：restoration 表达协助生态系统恢复，recovery 指恢复过程或状态；未达到目标时不能声称已完全恢复。 |
| S05 | [IMF Sovereign Debt FAQ](https://www.imf.org/en/about/faq/sovereign-debt)：债务语境采用 restructuring、rescheduling、reprofiling；具体安排需按条款描述。 |
| S06 | [Cochrane Handbook Chapter 6](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-06)：risk ratio、odds ratio、rate ratio、hazard ratio 为不同效应量，不能因都译作风险而互换。 |
| S07 | [ICOMOS recovery and reconstruction guidance](https://openarchive.icomos.org/id/eprint/1763/)：文化遗产恢复与重建为具体保护语境；本次读取出版记录，不将其视为 restoration 与 reconstruction 全部定义的核验。 |
| S08 | [Journal of Experimental Botany styling points](https://academic.oup.com/jxb/pages/styling-points)：植物名称和分类格式的本刊说明；同一物种的全名、缩写需保持可识别。 |

## 使用案例

| 作者原意 | 可用表达 | 需要保留的区别 |
|---|---|---|
| 用观测数据重建图像 | reconstruct an image from measurements | 不应换成 restructure an image；是否适合 recover 还取决于反问题及原文定义。 |
| 重组团队 | restructure the team | rebuild the team 可能意味着重建人员配置或能力，须确认原意。 |
| 生态功能恢复 | restore ecosystem function / ecosystem function recovered | 前者描述干预目标或作用，后者描述观察到的变化；目标不能写成已实现的结果。 |
| 软件重新构建 | rebuild the project | refactor 描述代码结构调整，不能据“重构”这个中文词混用。 |

以上均为自拟表达，不对应真实实验。更多句间组织见 [领域自然文风](field-natural-style.md)。期刊硬性要求仍按 [期刊适配](journal-adaptation.md) 核对。

## 缺少覆盖时

先完成能够确认的语言修改。作者提供参考论文时，按 [作者文献流程](author-literature.md) 建立本稿用词卡：候选、对象、原文位置、采用原因、不能替换的情况。只需读取与当前段落有关的部分，不要求每次搜集全领域论文。临时卡不自动写入共享包。

维护检查见 [本轮检查记录](../tests/usage-journal-audit.md)。
