# 控制与机器人：基础术语

领域编号：e02。本册 40 条短释义，用于阅读定位和中英用语对照。正式技术条件以稿件采用的来源为准。未逐条外部审定；[来源属性](../foundation-sources.md)。

[返回学科目录](../discipline-map.md)

| 英文 | 中文 | 入门释义 |
|---|---|---|
| <a id="t01"></a>plant | 被控对象 | 控制系统试图调节的对象 |
| <a id="t02"></a>controller | 控制器 | 根据目标和反馈产生控制输入 |
| <a id="t03"></a>actuator | 执行器 | 把控制信号转成实际动作的装置 |
| <a id="t04"></a>feedback | 反馈 | 把系统输出信息返回控制环节 |
| <a id="t05"></a>feedforward | 前馈 | 利用参考或扰动信息提前调节 |
| <a id="t06"></a>setpoint | 设定值 | 希望系统达到的目标值 |
| <a id="t07"></a>tracking error | 跟踪误差 | 目标轨迹与实际输出的差值 |
| <a id="t08"></a>state | 状态 | 描述系统当前动态所需的变量 |
| <a id="t09"></a>state-space model | 状态空间模型 | 用状态变量描述动态的模型 |
| <a id="t10"></a>transfer function | 传递函数 | 线性系统输入输出的频域关系 |
| <a id="t11"></a>stability | 稳定性 | 扰动后状态行为的受限性质 |
| <a id="t12"></a>controllability | 可控性 | 输入能否使状态到达目标的性质 |
| <a id="t13"></a>observability | 可观性 | 能否从输出推知内部状态的性质 |
| <a id="t14"></a>system identification | 系统辨识 | 从数据确定系统模型的过程 |
| <a id="t15"></a>PID control | PID 控制 | 结合比例积分微分项的控制方式 |
| <a id="t16"></a>model predictive control | 模型预测控制 | 用预测模型滚动选择控制动作 |
| <a id="t17"></a>robust control | 鲁棒控制 | 针对模型不确定性设计的控制 |
| <a id="t18"></a>adaptive control | 自适应控制 | 运行中调整控制参数的方法 |
| <a id="t19"></a>optimal control | 最优控制 | 依据目标函数选择控制过程 |
| <a id="t20"></a>state estimation | 状态估计 | 从测量和模型估算内部状态 |
| <a id="t21"></a>Kalman filter | 卡尔曼滤波 | 递推结合预测与观测的估计方法 |
| <a id="t22"></a>trajectory | 轨迹 | 位置或状态随时间的路径 |
| <a id="t23"></a>path planning | 路径规划 | 选择通向目标的几何路线 |
| <a id="t24"></a>motion planning | 运动规划 | 生成满足运动约束的动作过程 |
| <a id="t25"></a>kinematics | 运动学 | 描述运动几何而不追究作用力 |
| <a id="t26"></a>dynamics | 动力学 | 研究作用力与运动之间的关系 |
| <a id="t27"></a>forward kinematics | 正运动学 | 由关节变量求末端位姿 |
| <a id="t28"></a>inverse kinematics | 逆运动学 | 由目标位姿求关节变量 |
| <a id="t29"></a>degree of freedom | 自由度 | 描述运动所需的独立变量数 |
| <a id="t30"></a>joint | 关节 | 机器人相邻连杆间的运动连接 |
| <a id="t31"></a>end effector | 末端执行器 | 机器人与任务对象交互的末端部件 |
| <a id="t32"></a>workspace | 工作空间 | 机器人末端可到达的空间集合 |
| <a id="t33"></a>pose | 位姿 | 位置与方向的组合 |
| <a id="t34"></a>localization | 定位 | 估算设备在环境中的位置或位姿 |
| <a id="t35"></a>mapping | 建图 | 建立环境的空间表示 |
| <a id="t36"></a>SLAM | 同步定位与建图 | 同时估算位姿和环境地图 |
| <a id="t37"></a>sensor fusion | 传感器融合 | 结合多种观测形成状态信息 |
| <a id="t38"></a>impedance control | 阻抗控制 | 调节运动与接触力关系的控制 |
| <a id="t39"></a>haptic feedback | 触觉反馈 | 以力或触觉方式返回交互信息 |
| <a id="t40"></a>human-robot interaction | 人机交互 | 人与机器人之间的信息和动作联系 |

## 使用时

按稿件语境解释；相同英文跨领域可有不同含义。不能用本册简释替换原文的正式定义或条件。例句与修改解释见 [教学示例](../worked-examples.md)。
