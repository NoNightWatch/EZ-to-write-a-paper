# 工程与技术用词

按 [选词说明](../usage-selection.md) 使用。E 为编辑工作用法，全部例句自拟；先核对系统、对象和实际完成的动作。

<a id="e01"></a>
## e01 电气电子与通信

写作关注：区分器件、信号、链路与系统指标，保留测试条件和带宽范围。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e01-01"></a>recover / reconstruct / decode | 恢复、重建、解码 | recover a signal; reconstruct a waveform; decode a message | decode 针对编码信息；reconstruct 针对由数据重建对象。 | The receiver recovered the transmitted waveform. | 信号恢复不必意味着消息正确解码。 | E |
| <a id="u-e01-02"></a>attenuate / filter / suppress | 衰减、滤波、抑制 | attenuate a signal; filter noise; suppress interference | 按物理幅度变化或处理任务区分。 | The filter attenuated the out-of-band components. | 不把所有幅度下降都称为去噪。 | E |
| <a id="u-e01-03"></a>transmit / deliver / propagate | 发送、交付、传播 | transmit packets; deliver data; waves propagate | 发送、接收完成与介质传播各有任务主体。 | The transmitter sent packets at the specified rate. | 已发送不等于已成功交付。 | E |
| <a id="u-e01-04"></a>gain / efficiency / throughput | 增益、效率、吞吐量 | antenna gain; power efficiency; link throughput | 保留指标的分子分母和单位。 | Link throughput was measured under the stated load. | 数据速率不能任意改写成能效。 | E |

<a id="e02"></a>
## e02 控制与机器人

写作关注：分别描述参考信号、控制动作、系统状态和评估指标。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e02-01"></a>track / regulate / stabilize | 跟踪、调节、稳定 | track a trajectory; regulate temperature; stabilize a system | track 跟随参考；regulate 调节量；stabilize 对应稳定性目标。 | The controller tracked the reference trajectory. | 跟踪误差小不能自动改成已证明稳定。 | E |
| <a id="u-e02-02"></a>estimate / observe / sense | 估计、观测、感知 | estimate a state; observe a system; sense proximity | 区分状态推断与传感器获取。 | The observer estimates the unmeasured state. | observer 在控制中可为算法，不必指人类观察者。 | E |
| <a id="u-e02-03"></a>plan / replan / reconfigure | 规划、重规划、重配置 | plan a path; replan a route; reconfigure a robot | 按路径计算或系统配置变化选词。 | The robot replanned its route after detecting the obstacle. | 重新计算路线不等于改变硬件结构。 | E |
| <a id="u-e02-04"></a>robust / stable / reliable | 鲁棒、稳定、可靠 | robust control; stable equilibrium; reliable operation | 三者的判断条件须按论文定义保留。 | The analysis considers robustness to parameter uncertainty. | 不能用 reliable 替换有形式定义的 robust。 | E |

<a id="e03"></a>
## e03 机械与制造

写作关注：标清零件、工艺、尺寸与性能；区分设计、制造和在役修复。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e03-01"></a>fabricate / manufacture / assemble | 加工、制造、装配 | fabricate a component; manufacture parts; assemble a device | assemble 连接已有部件；其余依工艺和规模选择。 | The device was assembled from prefabricated components. | 装配不能自动写成所有部件均自行制造。 | E |
| <a id="u-e03-02"></a>repair / refurbish / remanufacture | 修理、翻新、再制造 | repair a defect; refurbish equipment; remanufacture a component | 动作范围及质量目标需与实际工艺一致。 | The procedure repaired the damaged surface. | 局部修理不自动满足 remanufacturing 的质量要求。 | E |
| <a id="u-e03-03"></a>deform / deflect / fail | 变形、挠曲、失效 | deform plastically; a beam deflects; a component fails | deflect 常描述位移或挠度；fail 需失效判据。 | The beam deflected under the applied load. | 可恢复位移不能自动叫 failure。 | E |
| <a id="u-e03-04"></a>optimize / improve / tune | 优化、改进、调参 | optimize a design; improve efficiency; tune parameters | optimize 需说明优化任务；improve 需比较基准。 | We tuned the parameters within the stated design space. | 调参不等于达到全局最优。 | E |

<a id="e04"></a>
## e04 土木与结构工程

写作关注：明确结构、构件、荷载和性能指标，避免“恢复”对象不清。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e04-01"></a>rebuild / retrofit / rehabilitate | 重建、改造、修复 | rebuild a bridge; retrofit a building; rehabilitate a structure | rebuild 重建实体；retrofit 修改现有结构；rehabilitate 恢复使用或性能。 | The study evaluates seismic retrofitting of existing buildings. | 改造现有建筑不能自动写成拆除重建。 | E |
| <a id="u-e04-02"></a>strengthen / stiffen / reinforce | 增强、增刚、加固 | strengthen a member; stiffen a panel; reinforce concrete | strength、stiffness 与增设增强材料须区分。 | The added ribs stiffened the panel. | 刚度变化不能任意改成强度变化。 | E |
| <a id="u-e04-03"></a>settle / subside / displace | 沉降、下陷、位移 | a foundation settles; land subsides; a joint displaces | 按空间对象和观测量选择。 | The monitoring recorded foundation settlement. | 局部基础沉降不能外推为区域地面下陷。 | E |
| <a id="u-e04-04"></a>load / stress / strain | 荷载、应力、应变 | applied load; tensile stress; axial strain | 按物理量与单位保留术语。 | Axial strain was recorded during loading. | 不把 strain 换成 stress 来减少重复。 | E |

<a id="e05"></a>
## e05 建筑与城市规划

写作关注：交代物质空间、社会使用和规划尺度，不给一般改造附加社会成效。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e05-01"></a>redevelop / regenerate / renew | 再开发、再生、更新 | redevelop a site; urban regeneration; renew infrastructure | redevelopment 强调开发变化；regeneration 可含更广社会经济目标。 | The proposal redevelops the former industrial site. | 物质空间更新不能单独证明社区社会状况改善。 | E |
| <a id="u-e05-02"></a>restore / reconstruct / conserve | 修复、重建、保护 | restore a facade; reconstruct a building; conserve heritage | 依实际保护介入和所用标准区分。 | The project concerns post-disaster reconstruction. | 本词组不替代遗产规范对真实性及材料的具体定义。 | S07 |
| <a id="u-e05-03"></a>densify / infill / expand | 增密、填充开发、扩张 | densify a district; infill development; expand the urban area | 按现有建成区或边界变化选择。 | The plan prioritizes infill development. | 新增建筑不必都属于城市空间扩张。 | E |
| <a id="u-e05-04"></a>access / accessibility / mobility | 进入、可达性、流动性 | access to services; spatial accessibility; urban mobility | accessibility 关注到达机会；mobility 关注移动。 | The analysis compares access to public services. | 出行速度提高不自动表示所有群体可达性提高。 | E |

<a id="e06"></a>
## e06 材料科学

写作关注：区分制备、结构表征与性能测试，保留相态和尺度。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e06-01"></a>reconstruct / reorganize / recrystallize | 重构、重排、再结晶 | surface reconstruction; molecular reorganization; grains recrystallize | 各词涉及不同结构变化；按证据与领域定义。 | The analysis examines surface reconstruction. | 不把任意形貌变化写成晶体表面 reconstruction。 | E |
| <a id="u-e06-02"></a>reinforce / toughen / harden | 增强、增韧、硬化 | reinforce a composite; toughen a matrix; harden a surface | 对应增强方式与性能量。 | The study reports increased surface hardness. | 硬度增加不能自动写成韧性增加。 | E |
| <a id="u-e06-03"></a>coat / deposit / functionalize | 涂覆、沉积、功能化 | coat a substrate; deposit a film; functionalize a surface | functionalize 需对应表面化学功能改变。 | A film was deposited on the substrate. | 物理覆层不能自动声称化学功能化。 | E |
| <a id="u-e06-04"></a>characterize / test / image | 表征、测试、成像 | characterize microstructure; test strength; image a surface | 依数据类型选具体动词。 | We imaged the fracture surface. | 成像本身不能代替定量力学测试。 | E |

<a id="e07"></a>
## e07 能源工程

写作关注：分开容量、功率、能量和效率，说明运行工况与时间范围。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e07-01"></a>generate / store / deliver | 发电、储存、交付 | generate electricity; store energy; deliver power | 按系统边界和实际输出区分。 | The system stores energy for later use. | 储能容量不能改成即时输出功率。 | E |
| <a id="u-e07-02"></a>recover / harvest / capture | 回收、获取、捕集 | recover waste heat; harvest solar energy; capture carbon dioxide | recover 强调回收；harvest 获取可利用能量；capture 指目标物捕集。 | The design recovers heat from the exhaust stream. | 热回收不能写成能量生成。 | E |
| <a id="u-e07-03"></a>decarbonize / electrify / improve | 脱碳、电气化、改进 | decarbonize a sector; electrify heating; improve efficiency | electrification 是能源使用形式变化；其排放结果需另有核算。 | The scenario examines electrification of heating. | 不把电气化直接写成零排放。 | E |
| <a id="u-e07-04"></a>capacity / output / efficiency | 容量、产出、效率 | installed capacity; annual output; conversion efficiency | 选择与量值及单位匹配的术语。 | Annual energy output was estimated for the specified site. | 不混淆装机容量和年发电量。 | E |

<a id="e08"></a>
## e08 化学工程

写作关注：说明物流、相态与过程边界，区分转化、分离和去除。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e08-01"></a>convert / separate / remove | 转化、分离、去除 | convert a feedstock; separate phases; remove a solute | 按物种转化或物理分离选择。 | The process separates the two liquid phases. | 分离不能直接改成化学降解。 | E |
| <a id="u-e08-02"></a>recover / recycle / regenerate | 回收、循环使用、再生 | recover a solvent; recycle a stream; regenerate a sorbent | regenerate 需指性能恢复；recycle 指回用。 | The solvent was recovered for reuse. | 回收量不等于实际完成的循环利用量。 | E |
| <a id="u-e08-03"></a>scale up / intensify / integrate | 放大、过程强化、集成 | scale up a process; process intensification; integrate operations | 按尺寸或产能变化、过程形式、单元连接区分。 | The study examines integration of the separation units. | 单元集成不自动代表已完成工业放大。 | E |
| <a id="u-e08-04"></a>conversion / selectivity / yield | 转化率、选择性、收率 | reactant conversion; product selectivity; isolated yield | 保留分母、目标物和测定口径。 | Product selectivity was reported alongside conversion. | 三个比例不能当同义词替换。 | E |

<a id="e09"></a>
## e09 交通与航空航天

写作关注：明确交通系统或飞行器的工作情境，区分安全、性能与运行指标。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e09-01"></a>reroute / reschedule / reconfigure | 改道、重排时刻、重配置 | reroute traffic; reschedule departures; reconfigure a network | 分别改变路径、时间和网络配置。 | The model reroutes traffic around the closed segment. | 路径变化不能自动写成出发时间变化。 | E |
| <a id="u-e09-02"></a>delay / travel time / headway | 延误、旅行时间、间隔 | departure delay; mean travel time; service headway | delay 需要参照时间；headway 为相邻服务间隔。 | Mean travel time was measured along the corridor. | 行程耗时不全是延误。 | E |
| <a id="u-e09-03"></a>lift / thrust / drag | 升力、推力、阻力 | generate lift; produce thrust; reduce drag | 保留受力方向与物理对象。 | The design reduced drag under the tested conditions. | 阻力变化不能泛化为所有飞行性能改善。 | E |
| <a id="u-e09-04"></a>simulate / test / certify | 仿真、试验、认证 | simulate flight; test a component; certify a system | certify 具有正式认证含义。 | The component was tested under laboratory conditions. | 实验室测试不能写成已获认证。 | E |

<a id="e10"></a>
## e10 环境工程

写作关注：保留污染物形态、浓度和质量口径；明确处理过程及测试环境。

| 候选词 | 中文意图 | 常见搭配 | 选择条件 | 自拟例句 | 替换边界 | 依据 |
|---|---|---|---|---|---|---|
| <a id="u-e10-01"></a>remediate / treat / restore | 修复、处理、恢复 | remediate contaminated soil; treat wastewater; restore habitat | remediation 聚焦污染处置；restoration 可指生态状态。 | The study evaluates treatment of the contaminated water. | 污染浓度降低不自动表示生态功能恢复。 | E |
| <a id="u-e10-02"></a>remove / degrade / mineralize | 去除、降解、矿化 | remove a contaminant; degrade a compound; mineralize organic carbon | removal 是指定边界内减少；后两者有转化含义。 | The analysis reports contaminant removal from the aqueous phase. | 水相去除不等于完全矿化。 | E |
| <a id="u-e10-03"></a>immobilize / stabilize / sequester | 固定、稳定、封存 | immobilize metals; stabilize waste; sequester carbon | 按迁移性、处理性质和储存时间目标区分。 | The treatment reduced metal mobility. | 迁移性降低不能直接写成永久封存。 | E |
| <a id="u-e10-04"></a>monitor / sample / characterize | 监测、采样、表征 | monitor water quality; sample effluent; characterize sludge | monitor 常有重复或持续观测；sample 指取材。 | We sampled effluent at the specified locations. | 一次取样不能自动描述为长期监测。 | E |
