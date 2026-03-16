---
title: "第二章 原子的量子态：玻尔模型"
theme: default
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
math: katex
css: unocss
---

<style>
.slidev-layout {
  overflow-x: hidden;
  overflow-y: auto;
}
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
}
img {
  max-width: 100%;
  height: auto;
}
.slidev-layout {
  font-family: "Kaiti SC", "STKaiti", "KaiTi", "楷体", serif !important;
}
.slidev-layout h1 {
  font-size: 1.85em !important;
  white-space: nowrap !important;
}
.kaiti-accent {
  color: #C71585 !important;
  font-weight: bold !important;
}
.slidev-layout.two-columns {
  gap: 1rem;
}
.slidev-layout.two-columns .col-left,
.slidev-layout.two-columns .col-right {
  min-height: 0;
}
.slidev-layout.two-columns .col-left {
  font-size: 0.95rem;
  line-height: 1.35;
}
.slidev-layout.two-columns .col-left h1 {
  margin-bottom: 0.75rem;
}
.slidev-layout.two-columns .col-left ul,
.slidev-layout.two-columns .col-left ol,
.slidev-layout.two-columns .col-left p {
  margin-top: 0.4rem;
  margin-bottom: 0.4rem;
}
.slidev-layout.two-columns .col-right {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.5rem;
}
.slidev-layout.two-columns .col-right img,
.slidev-layout.two-columns .col-right video {
  max-height: 220px !important;
  margin: 0 auto !important;
  object-fit: contain;
}
</style>

# 第二章 原子的量子态：玻尔模型

<img src="/images/qrcode.png" style="position: absolute; top: 30px; right: 30px; width: 180px; height: 180px;" />

<br>

<div class="text-center">

**金 磊**

办公室：瑞安楼703B

邮箱：jinl@tongji.edu.cn

</div>

---

# §6-1 黑体辐射——<span class="kaiti-accent">从连续到离散</span>

<br>

**需要掌握的知识点：**

1. 运用维恩位移律研究黑体辐射

2. 了解普朗克的能量量子假设

---
layout: two-cols
---

# 基尔霍夫热辐射定律（1859）

该定律描述了在热平衡状态下，一个物体对特定波长的电磁辐射的吸收和发射的关系。

<div style="border: 1px solid #d4a574; border-radius: 8px; padding: 10px 14px; margin-top: 6px; background: #fdf6ee; font-size: 0.9em;">

1. **温度均匀**：系统内部所有部分有相同的温度。
2. **热流平衡**：系统内部热流相互抵消，无净热流。
3. **动态平衡**：微观运动持续，但宏观状态不变。

</div>

**表述一**：辐射本领 $e$ 与吸收比 $a$ 之比是普适函数：

$$\frac{e(\nu, T)}{a(\nu, T)} = J(\nu, T) = e_{\text{黑体}}(\nu, T)$$

**表述二**：定义发射率 $\varepsilon = e / e_{\text{黑体}}$，则发射率 = 吸收比：

$$\varepsilon(\nu, T) = a(\nu, T)$$

::right::

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="width: 90%; max-height: 280px; object-fit: contain; margin: 10px auto; display: block;" />

<div class="text-center text-sm opacity-60">

Gustav Robert Kirchhoff（1824.3.12－1887.10.17）

</div>

---
layout: two-cols
---

# 基尔霍夫定律——热力学证明

**吸收比** $a$：物体表面吸收的辐射能量与入射辐射能量之比（0到1之间）。

**辐射本领** $e$：单位面积单位时间辐射的能量。

<br>

**证明（反证法）**：设想两个不同材质的物体封闭在绝热容器中，达到热平衡后温度处处相同。

- 若 $e_1/a_1 \neq e_2/a_2$，则 $e/a$ 较大者净辐射能量给另一方
- 一个变热、一个变冷 → 自发产生温差
- **违反热力学第二定律！**

因此 $e/a$ 必须是只依赖于 $\nu$ 和 $T$ 的普适函数。

::right::

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

$$\frac{e(\nu, T)}{a(\nu, T)} = J(\nu, T)$$

> 证明只需要热力学第二定律，不涉及任何微观机制——这正是其普适性的来源。

---

# 基尔霍夫热辐射定律——温度效应

<div class="flex justify-center gap-4">
<img src="/images/Bbbefore-18560.jpg" style="max-height: 300px; object-fit: contain;" />
<img src="/images/Bbafter-18564.jpg" style="max-height: 300px; object-fit: contain;" />
</div>

**低温时**：辐射集中在红外，可见光波段 $e(\lambda,T) \approx 0$，物体看起来不发光。

**高温时**：辐射峰值移向短波长（维恩位移律），可见光波段 $e(\lambda,T) \neq 0$，物体开始发光——从暗红→橙→黄白。

---

# 基尔霍夫热辐射定律——温度效应

<video controls style="max-width: 80%; max-height: 400px; margin: 10px auto; display: block;">
  <source src="/images/热辐射.mov" />
</video>

---
layout: two-cols
---

# 黑体

**黑体**：吸收投射它的全部辐射，而无反射。

<br>

<span style="color: #2266cc;">对于黑体</span> $a(\lambda, T) = 1$

对于黑体发射辐射 $e(\lambda,T)$ 的能力与组成的物质无关，只与辐射的波长和温度有关。

<span style="color: #cc2222; font-size: 1.1em;">$e(\lambda,T)$ 到底如何变化？</span>

<span style="color: #cc2222; font-size: 1.1em;">如何做相关的研究？</span>

::right::

<img src="/images/CNX_UPhysics_39_01_blackbody-1-18725.jpg" style="width: 85%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<div class="text-center text-xs opacity-60">

黑体腔模型：小孔近似理想黑体

</div>

---

# 黑体的性质

假设存在一个H形状的黑体：

- 当周围的温度**高于**黑体的温度时，黑体是**黑色**的
- 当周围的温度**低于**黑体的温度时，黑体是**发光**的

<img src="/images/blackbody_H_shape.png" style="max-width: 60%; max-height: 250px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 斯特藩-玻尔兹曼定律

1879年，斯特藩从实验数据发现，黑体辐射的**总功率**（对所有频率积分）与温度的四次方成正比：

$$P = \sigma T^4$$

其中 $\sigma = 5.67 \times 10^{-8}$ W·m$^{-2}$·K$^{-4}$ 为斯特藩-玻尔兹曼常数。

1884年，玻尔兹曼从热力学出发，利用辐射压 $p = u/3$ 严格推导了这一关系。

<br>

> 该定律告诉我们辐射的**总量**如何随温度变化，但不告诉我们能量在不同频率间如何分配。

---
layout: two-cols
---

# 维恩位移律

$$\lambda_{\max} T = 0.2898 \ \text{cm} \cdot \text{K}$$

<img src="/images/CNX_UPhysics_39_01_BBradcurve-1-18827.jpg" style="width: 90%; max-height: 250px; object-fit: contain;" />

::right::

<img src="/images/wien-12884-portrait-mini-2x-18818.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<img src="/images/60468-18860.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 维恩位移律——天文应用

已知参宿四（Betelgeuse）发偏红光，参宿七（Rigel）发蓝白光，若视为黑体：

**问题：哪颗恒星温度更高？**

<div v-click>

由维恩位移律 $\lambda_{\max} T = 2.898 \times 10^{-3}$ m$\cdot$K

$\lambda_{\text{blue}} < \lambda_{\text{red}} \Rightarrow T_{\text{Rigel}} > T_{\text{Betelgeuse}}$

| 恒星 | 颜色 | 表面温度 |
|------|------|----------|
| 参宿四 | 红色 | ~3500 K |
| 太阳 | 黄白色 | ~5800 K |
| 参宿七 | 蓝白色 | ~12000 K |

</div>

::right::

<img src="/images/CNX_UPhysics_39_01_orion-1-18871.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 瑞利-金斯辐射

考虑一个立方体，边长为 $L \gg \lambda$，在温度为 $T$ 时达到热平衡，辐射场可以看成多个波矢 $\boldsymbol{k}=\{k_x, k_y, k_z\}$ 的叠加，并满足驻波条件（辐射场在立方体边缘为0，即辐射场在黑体边缘被完全吸收）。

<div v-click>

即 $n \dfrac{\lambda}{2} = L$，$k = \dfrac{2\pi}{\lambda}$，因此：

$$\begin{aligned}
k_x &= \frac{\pi}{L} n_1, \quad k_y = \frac{\pi}{L} n_2, \quad k_z = \frac{\pi}{L} n_3 \\
k &= |\boldsymbol{k}| = \frac{\pi}{L} \sqrt{n_1^2 + n_2^2 + n_3^2}
\end{aligned}$$

</div>

::right::

<img src="/images/Screen Shot 2022-02-23 at 21.52.35-22413.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 瑞利-金斯辐射（续）

由 $\omega = kc$ 可得波长和角频率：

$$\begin{aligned}
\lambda &= \frac{2L}{\sqrt{n_1^2 + n_2^2 + n_3^2}} \\
\omega &= ck = \frac{\pi c}{L}\sqrt{n_1^2 + n_2^2 + n_3^2}
\end{aligned}$$

用 $(n_1, n_2, n_3)$ 定义一种辐射模式。

我们需要求解的是当 $\omega < \omega_m$ 时有多少种辐射模式存在？

::right::

<img src="/images/Screen Shot 2022-02-23 at 21.52.35-22413.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 瑞利-金斯辐射——模式计数

在 $k = \frac{\pi}{L}(n_1, n_2, n_3)$ 空间下，每个格点的体积为 $\frac{\pi^3}{L^3}$。

<br>

当 $\omega = \omega_m$ 时，总的体积为 $V = \frac{1}{8}\frac{4}{3}\pi\left(\frac{\omega_m}{c}\right)^3$

<br>

考虑电场可能有两种垂直于 $\vec{k}$ 的偏振方向，共包含 $N$ 种辐射模式：

$$N(\omega \leq \omega_m) = 2\left(\frac{L}{\pi}\right)^3 V = \frac{1}{3}\frac{L^3\omega_m^3}{\pi^2 c^3}$$

::right::

<img src="/images/Screen Shot 2022-02-23 at 22.15.16-22535.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 瑞利-金斯辐射——谱辐射密度

辐射模式密度：

$$n(\omega) = \frac{1}{L^3}N(\omega) = \frac{\omega^3}{3\pi^2 c^3}$$

谱辐射模式密度：

$$n_\omega = \frac{\mathrm{d}n}{\mathrm{d}\omega} = \frac{\omega^2}{\pi^2 c^3}$$

用频率 $\nu = \omega/(2\pi)$ 表示：

$$n_\nu(\nu) = \frac{8\pi\nu^2}{c^3}$$

---

# 瑞利-金斯辐射——能量密度

辐射场的谱辐射能量密度为：

$$w_\nu(\nu)\mathrm{d}\nu = n(\nu)\bar{w}_\nu(T)\mathrm{d}\nu$$

其中 $\bar{w}_\nu(T)$ 为每种模式的平均振动能量。

瑞利-金斯把辐射模式看成谐振子的振动，由经典**能量均分定理**，每个自由度分配 $\frac{1}{2}kT$，谐振子有动能和势能两个自由度，因此：

$$\bar{w}_\nu(T) = kT$$

代入得 $w_\nu(\nu) = \frac{8\pi\nu^2}{c^3}kT$ ——这就是瑞利-金斯公式。

---

# 瑞利-金斯辐射（紫外灾难）

<img src="/images/ultraviolet_catastrophe.png" style="height: 300px; object-fit: contain; display: block; margin: 0 auto;" />

<div style="text-align: center; margin-top: 10px;">

$w_\nu(\nu) = \frac{8\pi\nu^2}{c^3}kT$ &nbsp;&nbsp; 在高频（短波长）区域，能量密度趋于无穷大——这就是著名的**紫外灾难**。

</div>

---

# 🧪 思考实验：如果你是1900年的普朗克

**背景**：你是柏林大学的理论物理教授。瑞利-金斯公式在低频区完美吻合实验，维恩公式在高频区精确符合。但没有一个公式能同时描述整条光谱。更糟的是，瑞利-金斯公式在高频区给出无穷大——**紫外灾难**。

你的推导每一步都无可挑剔：模式计数正确，能量均分定理是经典统计力学的基石。

<div v-click>

**问题出在哪？**

推导中唯一的假设是：每个模式分配 $kT$ 的能量（能量均分定理）。这意味着无论频率多高，每个模式都"平等"地分到能量。

**但如果能量不是连续的呢？** 如果每个模式要获得能量，必须"整份购买"呢？

</div>

<div v-click>

> 普朗克后来说："这是一个出于绝望的举动。"他不得不放弃能量连续性这个经典物理的基石，引入了人类历史上第一个量子假设。

</div>

---

# 普朗克假设

能量的背后存在普朗克（量子）谐振子。

**普朗克谐振子只能取离散的能量：**

$$E_n = nh\nu, \quad n = 0, 1, 2, 3, \ldots$$

电磁波与黑体只能交换离散的能量（quanta）。

**为什么量子化能解决紫外灾变？**

频率为 $\nu$ 的模式要获得一份能量，至少需要 $h\nu$。当 $h\nu \gg k_BT$ 时，热运动的能量不足以激发哪怕一个量子，这些高频模式被"**冻结**"了。就像自动售货机只接受整数金额：水价100元而你只有5元，一瓶也买不到——经典理论却说你能买0.05瓶。

---

# 普朗克黑体辐射公式——推导

**普朗克能量假设**：能量为 $E = nh\nu$ 的概率为

$$p(nh\nu) = \frac{e^{-nh\nu/kT}}{\sum_{n=0}^{\infty} e^{-nh\nu/kT}}$$

每种模式的平均振动能量为：

$$\begin{aligned}
\bar{w}_\nu &= \sum_{n=0}^{\infty} nh\nu \cdot p(nh\nu) = \frac{\sum nh\nu\, e^{-nh\nu/kT}}{\sum e^{-nh\nu/kT}} = \frac{h\nu}{e^{h\nu/kT} - 1}
\end{aligned}$$

代入谱辐射模式密度 $n_\nu = \frac{8\pi\nu^2}{c^3}$，得到**普朗克黑体辐射公式**：

$$w_\nu(\nu) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/kT} - 1}$$

---

# 经典 vs 量子：积分变求和

**经典**（连续积分，能量均分定理）：

$$\langle E \rangle_{\text{classical}} = \frac{\int_0^\infty E \, e^{-E/k_BT} dE}{\int_0^\infty e^{-E/k_BT} dE} = k_BT \quad \text{（与频率无关！）}$$

**量子**（离散求和）：

$$\langle E \rangle_{\text{quantum}} = \frac{h\nu}{e^{h\nu/k_BT} - 1}$$

- 当 $h\nu \ll k_BT$：量子 $\to$ 经典 $k_BT$（低频，连续近似成立）
- 当 $h\nu \gg k_BT$：量子 $\to h\nu \, e^{-h\nu/k_BT} \to 0$（高频模式被冻结）

> **自然界在最基本层面是"数字"的，连续性只是低频近似。**

---
layout: two-cols
---

# 普朗克黑体辐射公式

$$w_\nu(\nu)\mathrm{d}\nu = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/kT} - 1}$$

其中：
- $h$ ：普朗克常数
- $k$ ：玻尔兹曼常数

::right::

<img src="/images/Screen Shot 2024-02-28 at 22.07.15-24963.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# §6-1 黑体辐射（小结）

- **基尔霍夫定律**：$e/a = J(\nu,T)$ 是普适函数（仅由热力学第二定律证明）

- **斯特藩-玻尔兹曼定律**：总辐射功率 $P = \sigma T^4$

- **维恩位移律**：$\lambda_{\max} T = b$，温度越高，辐射波长越短

- **瑞利-金斯公式**：经典理论推导，导致紫外灾变（高频发散）

- **普朗克假设**：能量离散化 $E_n = nh\nu$，高频模式被"冻结"，消除紫外灾变

- **普朗克公式**在低频退化为瑞利-金斯，高频退化为维恩，统一了两个经验定律

---

# 黑体辐射的宇宙学应用

普朗克公式不仅是一个实验室中的物理定律。

1965年，彭齐亚斯(Penzias)和威尔逊(Wilson)在调试微波天线时发现了一种无法消除的**均匀背景噪声**——来自各个方向，昼夜不变，无法用仪器故障解释。

这就是**宇宙微波背景辐射(CMB)**——大爆炸的"余辉"。

它是宇宙在约 **38万年** 时释放的热辐射，经过 **138亿年** 的宇宙膨胀红移后冷却至今。

<br>

> **问题**：CMB的光谱到底有多接近黑体？偏差有多大？如果有偏差，意味着什么新物理？

---
layout: two-cols
---

# COBE卫星：最精密的黑体测量

1989年NASA发射了**宇宙背景探测者(COBE)**卫星。

搭载的**FIRAS仪器**（远红外绝对分光光度计）覆盖 60 GHz 到 600 GHz（2–21 cm$^{-1}$），共 **43个频率点**。

1990年1月，John Mather 在美国天文学会展示结果时，**全场起立鼓掌**——这在天文学会议上极为罕见。

<br>

$$\boxed{T_{\text{CMB}} = 2.725 \pm 0.002\ \text{K}}$$

光谱偏离黑体的程度不超过**万分之一**。

::right::

<div class="mt-8">

**为什么CMB是如此完美的黑体？**

早期宇宙极端致密，光子与物质的相互作用速率远高于宇宙膨胀速率，有充分时间建立精确的热平衡。

<br>

**意义：**

- 大爆炸宇宙学的**最强证据**之一
- Mather 因此获得 **2006年诺贝尔物理学奖**
- 至今仍是自然界中与理论吻合最好的黑体谱

</div>

---

# COBE/FIRAS 数据：一个参数拟合整条光谱

<img src="/images/cobe_firas_fit.png" style="width: 95%; max-height: 380px; object-fit: contain; margin: 0 auto; display: block;" />

左图：43个数据点与普朗克公式的拟合——只用了**一个自由参数** $T$。右图：残差与零相容，偏差在噪声水平以内。

---

# CMB谱畸变：偏离黑体意味着新物理

如果CMB光谱**完美地**是黑体，说明早期宇宙没有额外的能量注入。但如果检测到偏差，就意味着存在**新物理过程**。

**$\mu$ 型畸变（化学势型）：** 发生在红移 $5\times10^4 < z < 2\times10^6$ 的宇宙早期。此时光子与电子的康普顿散射频繁到可以重新分配动量，但光子**数目无法调整**（双光子过程已冻结）。结果：谱从普朗克分布变为含化学势的 Bose-Einstein 分布 $n(\nu) = 1/(e^{h\nu/k_BT + \mu} - 1)$。

**$y$ 型畸变（康普顿型）：** 发生在较晚期 $z < 5\times10^4$。高温电子通过逆康普顿散射将低频光子"踢"到高频，产生低频亏损、高频增益。

| 参数 | COBE/FIRAS 约束 | 物理来源 |
|------|----------------|----------|
| $\|\mu\|$ | $< 9\times10^{-5}$ | 暗物质湮灭、原初黑洞蒸发 |
| $\|y\|$ | $< 1.5\times10^{-5}$ | 星系团热气体、再电离 |

> 这些极其严格的上限排除了许多新物理模型。下一代实验(如PIXIE)目标：灵敏度提高1000倍。

---

# 宇宙热历史：CMB曾经是可见光

CMB温度随宇宙膨胀而降低。**关键公式：**

$$\boxed{T(z) = T_0(1+z)}, \quad T_0 = 2.725\ \text{K}$$

**物理原因：** 光子波长随宇宙尺度因子线性拉伸 $\lambda \propto a \propto 1/(1+z)$。由维恩位移定律 $\lambda_{\max}T = b$ 可得 $T \propto (1+z)$。

**一个优美的性质：** 普朗克分布在绝热膨胀下**保持黑体形状不变**——所有光子的频率按同一比例降低，只改变温度参数，不改变谱的函数形式。

<br>

> **思考**：如果膨胀会破坏黑体形状，那今天测到的CMB就不应该是完美黑体了。

---

# 从可见光到微波：关键里程碑

| 红移 $z$ | 宇宙年龄 | 温度 | 峰值波长 | 辐射波段 |
|-----------|----------|------|----------|----------|
| 0（今天） | 138亿年 | 2.7 K | 1.06 mm | 微波 |
| ~1 | 58亿年 | 5.5 K | 0.53 mm | 远红外 |
| ~10 | 5亿年 | 30 K | 97 $\mu$m | 近红外 |
| ~100 | 1700万年 | 273 K | 11 $\mu$m | 中红外 |
| **~1100** | **38万年** | **3000 K** | **1 $\mu$m** | **可见光/近红外** |

$z \approx 1100$ 时发生了**光子退耦(photon decoupling)**：宇宙冷却到 ~3000 K，自由电子与质子复合为中性氢 $e^- + p \to \text{H} + \gamma$，光子不再被频繁散射，宇宙从"不透明"变为"透明"。

如果那时有观测者，**天空将是一片均匀的橙红色光芒**（类似铁水的颜色）。

---

# 不同红移下的CMB辐射谱

<img src="/images/cosmic_thermal_history.png" style="width: 85%; max-height: 380px; object-fit: contain; margin: 0 auto; display: block;" />

每条曲线是同一个黑体谱在不同宇宙年龄的快照。随着宇宙膨胀，峰值从可见光（紫色）经红外逐步移到微波（蓝色），但**谱形始终保持普朗克分布**。

---

# 维恩定律的天文应用：如何测量恒星温度？

**理论上**：测量恒星光谱，找到峰值波长，用维恩位移定律 $\lambda_{\max}T = b$ 算温度。

**实际困难**：完整光谱观测很昂贵！光谱仪把光分散到数百个波长通道，每个通道光子数大减。对暗弱恒星，需要数小时甚至不可能。

**天文学家的聪明办法**：不测完整光谱，只用**几个宽波段滤光片**拍照。

<br>

这就是**测光(photometry)**——用少量数据点"采样"黑体谱，代替完整光谱。

---

# Johnson UBVRI 测光系统

1953年 Johnson 和 Morgan 建立的标准化系统，后扩展为五波段：

| 波段 | 中心波长 | 带宽 | 覆盖区域 |
|------|----------|------|----------|
| **U** (紫外) | 365 nm | 66 nm | 大气紫外截止附近 |
| **B** (蓝) | 440 nm | 94 nm | 蓝光区 |
| **V** (可见) | 550 nm | 88 nm | 人眼最敏感区 |
| **R** (红) | 640 nm | 138 nm | 红光区 |
| **I** (近红外) | 798 nm | 149 nm | CCD灵敏区边缘 |

**星等定义**：$m = -2.5\log_{10}(F/F_0)$，星等越小越亮。零点以**织女星(Vega)** 为基准。

<br>

> 恒星在每个波段的亮度不同——蓝星B波段亮，红星I波段亮。这个差异就是温度信息。

---

# 色指数：不需要知道距离就能测温度

**色指数** = 两个波段的星等之差，最常用的是 $B-V$。

**为什么色指数不依赖距离？** 恒星的观测流量 $F = (\text{表面流量}) \times (R_\star/d)^2$，取对数后 $(R_\star/d)^2$ 变成加法项，两个波段**相减时恰好消去**！

$$\underbrace{(m_B - m_V)}_{\text{色指数}} = -2.5\log_{10}\frac{F_B}{F_V} = -2.5\log_{10}\frac{\int B_\lambda(\lambda,T)\,\phi_B\,d\lambda}{\int B_\lambda(\lambda,T)\,\phi_V\,d\lambda}$$

只剩下温度 $T$！

| 恒星 | $B-V$ | 颜色 | 有效温度 |
|------|-------|------|----------|
| 参宿七(Rigel) | $-0.03$ | 蓝白 | ~12000 K |
| 织女星(Vega) | $+0.00$ | 白 | ~9600 K |
| 太阳 | $+0.64$ | 黄白 | ~5778 K |
| 参宿四(Betelgeuse) | $+1.93$ | 红 | ~3500 K |

---

# 色指数与温度的定量关系

<img src="/images/color_index_temperature.png" style="width: 85%; max-height: 380px; object-fit: contain; margin: 0 auto; display: block;" />

$B-V$ 色指数与温度呈单调关系：温度越高，$B-V$ 越负（越蓝）；温度越低，$B-V$ 越正（越红）。利用这条曲线，只需测量两个波段的亮度就能精确定温。

---

# 赫茨普龙-罗素图（HR图）

<img src="/images/hr_diagram.png" style="width: 48%; max-height: 400px; object-fit: contain; float: right; margin-left: 15px;" />

1911年赫茨普龙、1913年罗素独立发现：将恒星的**光度**（绝对星等 $M_V$）对**表面温度**作图，恒星**不是随机分布**的。

**主序带**(Main Sequence)：从左上到右下的狭长带，包含**绝大多数恒星**——它们正在核心进行氢聚变。质量越大，温度越高、光度越大。

**红巨星**（右上方）：温度低但光度极高。由 $L = 4\pi R^2 \sigma T^4$ 可知，低温高光度意味着**巨大的半径**——恒星外层膨胀。

**白矮星**（左下方）：温度高但光度极低，意味着**极小的半径**——大约地球大小的致密天体。

> HR图是恒星演化的"路线图"：恒星一生从主序出发，演化到红巨星，最终可能变成白矮星。

---

# 硅基视角：紫外灾变就是过拟合

回顾紫外灾变的本质：经典理论给每个频率模式分配**相同的能量** $k_BT$，不管频率多高。

这在机器学习中有一个精确的对应物——

| 黑体辐射（物理） | 机器学习 |
|------|----------|
| 频率模式 $\nu_i$ | 模型的特征(feature) |
| 能量均分：每个模式 $k_BT$ | 等权：每个特征相同权重 |
| 高频模式数 $\propto \nu^2 \to \infty$ | 过参数化：特征数 → ∞ |
| 总能量发散 → **紫外灾变** | 过拟合 → **泛化崩溃** |

<br>

**核心问题一样**：如何限制"昂贵"（高频/高复杂度）分量的贡献？

---

# 正则化如何"推导出"量子化

机器学习的解决方案是**正则化**——在损失函数中惩罚"昂贵"的特征：

**L1 正则化 (LASSO)**：$\mathcal{R} = \lambda\sum|w_i|$

超过代价阈值的特征权重**直接置零**（硬截断），产生**稀疏解**。

**L2 正则化 (Ridge)**：$\mathcal{R} = \lambda\sum w_i^2$

所有权重**平滑衰减**，高代价特征被压制但不完全消失。

**普朗克的量子化**：频率 $\nu$ 的模式需要至少 $h\nu$ 才能激发。

当 $h\nu \gg k_BT$：模式被**指数衰减地冻结**，行为介于L1和L2之间。

$$\frac{\langle E \rangle_{\text{quantum}}}{k_BT} = \frac{h\nu/k_BT}{e^{h\nu/k_BT} - 1} \quad \xrightarrow{h\nu \gg k_BT} \quad \sim e^{-h\nu/k_BT} \to 0$$

> **普朗克常数** $h$ = 自然界的**正则化超参数**，它设定了能量分配的最小粒度。

---

# 正则化 vs 量子化：数值对比

<img src="/images/regularization_comparison.png" style="width: 98%; max-height: 370px; object-fit: contain; margin: 0 auto; display: block;" />

左：经典等权分配(红)不衰减，L1硬截断(绿)，L2平滑衰减(橙)，量子化(蓝)指数衰减。中：乘以模式密度 $\nu^2$ 后，经典发散，量子收敛。右：累积积分，经典 → ∞，量子有限。

---

# AI能"重新发现"普朗克公式吗？

如果给AI一堆黑体辐射数据（不告诉它公式），它能找到 $u \propto \nu^3/(e^{h\nu/k_BT}-1)$ 吗？

**路径一：神经网络**（黑箱逼近器）

输入 $(\nu, T)$，输出 $u(\nu,T)$。训练后可以**精确拟合**训练范围内的数据，但：**不给出解析公式**，外推能力有限，无法判断它是否"理解"了物理。

**路径二：符号回归**（PySR库）

不是拟合黑箱函数，而是在**解析表达式空间**中搜索。核心算法：**遗传编程**——维护一群"公式"，通过变异、交叉和选择来演化，输出不同复杂度下的最佳公式（Pareto前沿）。

---

# 符号回归的关键技巧：无量纲化

直接对 $u(\nu, T)$ 搜索几乎不可能成功——两个变量、多个物理常数，搜索空间太大。

**但如果做无量纲化**（物理学家的传统智慧）：

$$x = \frac{h\nu}{k_BT} \quad \text{(无量纲频率)}, \qquad y = \frac{u(\nu,T)}{8\pi h\nu^3/c^3} \quad \text{(除以已知前因子)}$$

那么普朗克公式变成了一个**单变量函数**：

$$\boxed{y = \frac{1}{e^x - 1}}$$

符号回归只需要从 $\{+,-,\times,\div,\exp\}$ 这几个运算符中组合出这个函数！

> **启示**：正确的无量纲化 = 正确的"特征工程"。物理直觉帮AI缩小了搜索空间。

---

# PySR实测结果：AI确实发现了普朗克公式

<img src="/images/pysr_pareto.png" style="width: 95%; max-height: 340px; object-fit: contain; margin: 0 auto; display: block;" />

左：Pareto前沿显示，复杂度=3时AI发现了 $0.85/x$（瑞利-金斯极限），复杂度=6时发现了 $1/(e^x-1)$（普朗克公式），MSE下降3个数量级。右：AI发现的公式与真实普朗克公式几乎完全重合。

> 如果1900年就有符号回归，普朗克或许不需要那么多年的思索。当然，**无量纲化本身就需要物理直觉**——AI需要人类指路。


---

# §6-2 光电效应

<br>

**需要掌握的知识点：**

1. 了解光电效应的物理图像

2. 了解为什么光电效应不能用经典理论解释

3. 了解为什么爱因斯坦的方法可以解释光电效应

---
layout: two-cols
---

# 光电效应

1887年由赫兹发现，在光的照射下，物质表面因吸收辐射能量而形成电流的现象，我们称之为**光电效应**。

- 正负极间电压可变
- 光电子在真空中运动，可忽略动能的损失
- 单色光源

::right::

<img src="/images/CNX_UPhysics_39_02_photoexp-1-2-19460.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 经典理论无法解释的光电效应特性

**(一) 响应时间**

响应时间：电磁波照射到材料上到发出光电子的时间差。

- 经典理论认为这个时间很长
- 实际上 $< 10^{-9}$ s

---
layout: two-cols
---

# 经典理论无法解释的光电效应特性

**(二) 辐射强度与光电流之间的关系**

存在**遏止电压**：与光电子的动能有关

$$K_{\max} = e\Delta V_s$$

经典理论认为光电子获取动能是连续的，即光照强度越大，光电子的动能越大。

::right::

<img src="/images/CNX_UPhysics_39_02_photoexp1-1-19625.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 经典理论无法解释的光电效应特性

**(三) 存在截止频率（cut-off frequency）**

- 截止频率是每个材料本身的特性
- 不同材料的斜率是相同的

::right::

<img src="/images/CNX_UPhysics_39_02_photoexp2-1-19717.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 🧪 思考实验：如果你是1905年的物理学家

**背景**：你在柏林的实验室里，桌上有一套光电效应装置。你已经观察到三个经典理论无法解释的现象：瞬时响应、遏止电压与光强无关、存在截止频率。

你还知道：5年前普朗克刚提出了能量量子化假设 $E = nh\nu$，但那只是用来解释黑体辐射的"数学技巧"。

<div v-click>

**问题**：

1. 如果光的能量真的是连续的电磁波，为什么弱光也能瞬间打出电子？
2. 普朗克说振子的能量是量子化的，那光本身呢？
3. 你能否大胆地把"量子化"从振子推广到光？如果光也是一份一份的，上面三个困难是否立刻迎刃而解？

</div>

<div v-click>

> 爱因斯坦正是做出了这个"不合理"的推广，而他因此获得了诺贝尔奖——不是因为相对论，而是因为光电效应。

</div>

---
layout: two-cols
---

# 光电效应的量子解释

**爱因斯坦提出光量子假设**（1921年诺贝尔物理学奖）

光子以光速传播并携带能量，能量依赖其频率：

$$E_\nu = h\nu$$

其中 $h$ 为普朗克常数。

当光子到达材料表面时，**或者交换所有的能量，或者彻底不交换能量**。

在爱因斯坦的解释中，单个电子与光子直接发生相互作用。

::right::

<img src="/images/60468-18860.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 光电效应的量子解释——例题

**问题**：当波长为300 nm的电磁波照射在银金属表面时，能否产生光电子？

$$\lambda = \frac{hc}{\varphi} = \frac{1240\ \text{eV·nm}}{4.73\ \text{eV}} = 262\ \text{nm}$$

300 nm > 262 nm（截止波长），因此**不能**产生光电子。

::right::

<img src="/images/Screen Shot 2022-01-24 at 16.11.38-20007.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# §6-3 光谱

唯像的讨论氢原子相关的实验现象。

<br>

**需要掌握的知识点：**

1. 了解吸收谱线与发射谱线的区别

2. 掌握氢原子光谱规律及光谱线系公式

---
layout: two-cols
---

# 唯像理论与第一性原理

| 阶段 | 内容 |
|------|------|
| 实验物理 | 布拉赫（1546-1601）精密测量了行星轨道 |
| 唯像理论 | 开普勒（1571-1630）提出三定律 |
| 第一性原理 | 牛顿力学与万有引力 |

<br>

> 唯像理论和第一性原理是相对的。——杨振宁《美与物理学》

::right::

<img src="/images/Screen Shot 2022-02-28 at 13.07.02-23046.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 唯像理论与第一性原理（续）

<img src="/images/Screen Shot 2023-03-20 at 19.08.25-24628.png" style="max-width: 70%; margin: 20px auto; display: block;" />

<video controls style="max-width: 60%; margin: 10px auto; display: block;">
  <source src="/images/225642347-a07127da-a84e-4af3-96f4-4c7fef5a673b-24632.mp4" />
</video>

---
layout: two-cols
---

# 为什么天是蓝色的？

**瑞利散射**：

$$I(\lambda)_{\text{scattering}} \propto \frac{I(\lambda)_{\text{incident}}}{\lambda^4}$$

短波长（蓝光）散射更强。

::right::

<img src="/images/Rayleigh_sunlight_scattering-23200.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<img src="/images/Solar_spectrum_en.svg-23207.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 夫琅和费谱线

1814年德国物理学家J.夫琅和费利用自制光谱装置观察太阳光时，在明亮彩色背景上观察到576条狭细的暗线。

其中最明显的8条用A到H字母标记。实际上约有3万多条。

<img src="/images/Fraunhofer_lines.svg-20094.png" style="max-width: 80%; margin: 20px auto; display: block;" />

---

# 夫琅和费谱线（续）

1859年基尔霍夫和本生确认了每一条谱线所对应的化学元素，并推论在太阳光谱中的暗线是由在太阳上层的那些元素吸收造成的。

<img src="/images/700px-Spectrum_of_blue_sky.svg-2-23231.png" style="max-width: 75%; margin: 20px auto; display: block;" />

---
layout: two-cols
---

# 光谱仪

光谱——研究原子结构的重要途径之一。

组成：1) 光源　2) 光栅/棱镜　3) 记录仪

<img src="/images/Screen Shot 2022-01-10 at 23.13.25-18709.png" style="width: 90%; max-height: 250px; object-fit: contain;" />

::right::

<video controls style="width: 90%; max-height: 280px; margin: 10px auto; display: block;">
  <source src="/images/Light_dispersion_conceptual_waves350px-20346.gif" />
</video>

---

# 谱线

**谱线**：在均匀且连续的光谱上明亮或黑暗的线条，有**吸收谱线**或**发射谱线**两种。

<div class="flex justify-center gap-2 mt-4">
<img src="/images/2880px-Spectral-lines-continuous.svg-18398.png" style="width: 28%;" />
<img src="/images/2880px-Spectral-lines-emission.svg-18412.png" style="width: 28%;" />
<img src="/images/2880px-Spectral-lines-absorption.svg-18435.png" style="width: 28%;" />
</div>

<div class="flex justify-center gap-8 mt-2 text-xs opacity-70">
<span>连续光谱</span>
<span>发射谱线</span>
<span>吸收谱线</span>
</div>

---

# 谱线的特征

- 吸收谱线与发射谱线**完全重叠**
- 吸收和发射光谱是**特定原子的特征**
- 光谱线不是完全窄的——在每个波长 $\lambda$ 周围有强度分布 $I(\lambda)$，具有有限的半宽 $\Delta\lambda$

---
layout: two-cols
---

# 谱线——吸收与发射

- 特定波长的光被吸收
- 发射特定波长的光

::right::

<img src="/images/CNX_UPhysics_39_04_spectra-1-20112.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 🧪 思考实验：如果你是1885年的巴尔末

**背景**：你是瑞士巴塞尔的一位60岁数学老师。你的物理学家朋友给了你一张纸条，上面写着氢原子在可见光区的四条谱线波长：

$$656.3 \text{ nm}, \quad 486.1 \text{ nm}, \quad 434.0 \text{ nm}, \quad 410.2 \text{ nm}$$

这四个数看起来毫无关联。但你擅长数论和数字规律。

<div v-click>

**挑战**：试着用计算器做以下操作：

1. 算一算这四个数的比值？有没有简单分数？
2. 算一算倒数 $1/\lambda$？它们之间等差吗？
3. 如果有某个"基数" $B$，使得 $\lambda / B$ 是简单分数……

</div>

<div v-click>

> 巴尔末用的"算法"就是人脑+耐心。他发现 $\lambda = B \cdot n^2/(n^2-4)$，用一个常数和一个整数精确重现了所有谱线——这是人类最早的"符号回归"。

</div>

---

# 🖥️ AI Workshop: 巴尔末的符号回归机

用算法重现巴尔末1885年的发现过程——从四个数字到物理定律。

<br>

<div style="text-align: center;">

**点击链接体验：**

[AI-workshop/balmer-regression.html](../AI-workshop/balmer-regression.html)

</div>

<br>

<div style="font-size: 0.85em; color: #666;">

包含：

1. 氢原子光谱可视化（真实颜色谱线）
2. 动态搜索动画——看公式被逐个尝试、评估、淘汰
3. 一个常数 + 一个整数 → 精确编码无穷多条谱线
4. 交互式预测：用发现的公式推导 Lyman、Paschen 等线系

</div>

---
layout: two-cols
---

# 氢原子光谱

氢原子在可见光波段有四条谱线，波长增加，注意亮度变化。

1885年巴耳末提出经验公式：

$$\frac{1}{\lambda} = R_H\left(\frac{1}{2^2} - \frac{1}{n'^2}\right), \quad n' = 3, 4, 5, \ldots$$

::right::

<img src="/images/CNX_UPhysics_39_04_emit-H-1-20212.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 巴耳末系谱线

纯经验公式，这组谱线叫 **Balmer 线系**：

$$\frac{1}{\lambda} = R_H\left(\frac{1}{2^2} - \frac{1}{n^2}\right), \quad n = 3, 4, 5, \ldots$$

::right::

<img src="/images/Screen Shot 2022-01-25 at 16.01.23-20298.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 从巴尔末到里德伯——推广的逻辑

巴尔末公式可以改写为波数形式：

$$\frac{1}{\lambda} = \frac{4}{B}\left(\frac{1}{4} - \frac{1}{n^2}\right)$$

<div v-click>

关键一步：注意到 $4 = 2^2$ ！于是：

$$\frac{1}{\lambda} = R_H\left(\frac{1}{\textcolor{#C71585}{2^2}} - \frac{1}{n^2}\right)$$

</div>

<div v-click>

**里德伯的问题**：这里的 $\textcolor{#C71585}{2}$ 有什么特殊的？如果换成 1、3、4、5 会怎样？

</div>

---

# 里德伯推广的三条线索

里德伯不是在"猜"——他有三条线索：

**(一) 碱金属光谱的共性**

里德伯研究了锂、钠、钾等大量碱金属的光谱，发现它们也有类似的"线系"结构，每条谱线都可以写成**两个"项"(term)的差**：

$$\frac{1}{\lambda} = T(n_1) - T(n_2)$$

这个结构在不同元素中反复出现——不是巧合。

<div v-click>

**(二) 氢的特殊简洁性**

对氢原子，项函数恰好是最简单的 $T(n) = R_H / n^2$。巴尔末系就是 $T(2) - T(n)$。那 $T(1) - T(n)$、$T(3) - T(n)$ 对应什么？——**一定存在其他线系！**

</div>

<div v-click>

**(三) 里兹组合原理(1908)**

如果两条谱线的波数分别是 $T(a)-T(b)$ 和 $T(b)-T(c)$，那么它们的**和** $T(a)-T(c)$ 也应该对应一条谱线。实验验证了这一点！

</div>

---

# 里德伯方程

里德伯的推广不是"凑"出来的，而是从多种元素的光谱数据中归纳出的**结构性规律**：

$$\frac{1}{\lambda} = R_H\left[\frac{1}{n^2} - \frac{1}{n'^2}\right] = T(n) - T(n')$$

所有光谱线 = **两个项之差**。

这是一种比单纯拟合更深层的模式识别：巴尔末是"数据→公式"，里德伯是"公式→更一般的公式"。

---
layout: two-cols
---

# 里德伯方程——结论

1. 氢光谱中任何一条谱线的波数，都可以写成两个整数决定的函数之差。

2. 对于给定的 $n$ 值，$n' > n$，可得到同一线系中各光谱的波数值。

3. 改变公式中的 $n$ 值，就可得到不同的线系。

::right::

<img src="/images/800px-Hydrogen_transitions.svg-20406.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<img src="/images/2880px-Hydrogen_spectrum.svg-20456.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 其它线系

<div class="text-sm">

| 线系 | $n$ | $n'$ | 区域 |
|------|-----|------|------|
| Lyman系（1914） | 1 | 2, 3, … | 紫外区 |
| Balmer系（1885） | 2 | 3, 4, … | 可见光 |
| Paschen系（1908） | 3 | 4, 5, … | 红外区 |
| Brackett系（1922） | 4 | 5, 6, … | 红外区 |
| Pfund系（1924） | 5 | 6, 7, … | 红外区 |

</div>

$$\frac{1}{\lambda} = R_H\left[\frac{1}{n^2} - \frac{1}{n'^2}\right]$$

---

# §玻尔模型

<br>

**需要掌握的知识点：**

1. 解释氢原子的结构

2. 了解氢原子的量子模型

3. 掌握如何使用玻尔模型解释氢原子光谱

---
layout: two-cols
---

# 盖革-马斯登实验

汤姆逊1904年提出原子核的**布丁模型**。

*Proceedings of the Royal Society of London A.*

::right::

<div class="flex flex-col gap-2 mt-4">
<img src="/images/PlumPuddingModel_ManyCorpuscles-25001.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: auto;" />
<img src="/images/440px-Gold_foil_experiment_conclusions.svg-25007.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: auto;" />
</div>

---

# 原子的经典模型

卢瑟福发现原子有核，电子围绕原子核做运动，即电子在库仑力下做圆周运动：

$$\frac{1}{4\pi\epsilon_0}\frac{e^2}{r^2} = m_e\frac{v^2}{r} \quad \Rightarrow \quad v^2 = \frac{e^2}{4\pi\epsilon_0}\frac{1}{m_e r}$$

其中 $e$ 为电子电荷，$m_e$ 为电子质量，$r$ 为圆周半径，$v$ 为运动速率。

电子的总能量 = 动能 + 势能：

$$E = \frac{1}{2}m_e v^2 - \frac{1}{4\pi\epsilon_0}\frac{e^2}{r} = -\frac{1}{2}\frac{e^2}{4\pi\epsilon_0 r}$$

---
layout: two-cols
---

# 原子的经典模型——困难

根据经典理论：

- 电子绕原子核运行是一个不断加速的过程
- 任何电子的加速都会辐射电磁波
- 辐射消耗电子的能量，使得电子向原子核**坠落**

在电子逐渐"坠入"原子核的过程中，所发出的电磁波应当是**连续变化**的，但观察到的原子光谱是**分离的**。

::right::

<img src="/images/185081_153314_ans_732d0264d2d0477c9394ed404835c8fc-20814.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 🧪 思考实验：如果你是1913年的玻尔

**背景**：你是28岁的丹麦物理学家，刚从曼彻斯特的卢瑟福实验室回来。你手上有三件宝贝：

1. 卢瑟福的核式模型（电子绕核运动）
2. 里德伯公式：$1/\lambda = R_H(1/n^2 - 1/n'^2)$，整数 $n$ 完美描述光谱
3. 普朗克-爱因斯坦的量子思想：$E = h\nu$

但经典理论说电子必须辐射能量而坠落。怎么办？

<div v-click>

**关键线索**：

- 里德伯公式中出现了**整数**——这暗示原子内部有离散的结构
- 普朗克常数 $h$ 的量纲是 $\text{J}\cdot\text{s}$——与角动量的量纲相同！
- 如果角动量也是量子化的：$L = n\hbar$……

</div>

<div v-click>

> 玻尔的天才在于：他不去修补经典理论，而是直接宣布某些经典规律在原子尺度上**不适用**，然后强行引入量子化规则。这种"不讲理"的做法，恰恰是物理学范式转换的标志。

</div>

---

# 玻尔模型的三点假设

**假设一**：电子在某些**特定轨道**上围绕原子核做圆周运动。

**假设二**：角动量**量子化**：

$$L_n = m_e v_n r_n = n\hbar, \quad n = 1, 2, 3, \ldots$$

**假设三**：电子在不同轨道间**跃迁**，辐射（吸收）光子：

$$h\nu = |E_n - E_{n'}|$$

---

# 玻尔模型、经典模型与里德伯方程

**里德伯方程**：

$$\frac{1}{\lambda} = R_H\left[\frac{1}{n^2} - \frac{1}{n'^2}\right]$$

**玻尔模型**：$E_n = -R_H hc / n^2$

**经典模型**：$E_n = -e^2/(8\pi\epsilon_0 r_n)$

**半经典结合**：

$$r_n = \frac{e^2 n^2}{8\pi\epsilon_0 R_H hc}$$

> 玻尔模型仍满足能量守恒和动量守恒。

---

# 电子轨道的量子化（半经典）

假定电子轨道是离散的（量子的），但仍满足经典运动规律：

**经典模型**：$\frac{1}{4\pi\epsilon_0}\frac{e^2}{r_n^2} = m_e\frac{v_n^2}{r_n}$

**玻尔模型**：$m_e v_n r_n = n\hbar$

可以求得电子的速率和半径只依赖于 $n$：

$$v_n = \frac{1}{4\pi\epsilon_0}\frac{e^2}{\hbar}\frac{1}{n}$$

$$r_n = 4\pi\epsilon_0\frac{\hbar^2}{m_e e^2}n^2$$

---

# 电子轨道的数值计算

$$r_n = 4\pi\epsilon_0\frac{\hbar^2}{m_e e^2}n^2$$

令 $a_0 = 4\pi\epsilon_0\frac{\hbar^2}{m_e e^2} \approx 5.29\times10^{-11}\ \text{m} = 0.529\ \text{Å}$

$a_0$ 通常被称为**玻尔半径**，则：

$$\boxed{r_n = a_0\, n^2}$$

即电子轨道半径只能取特定的值。

---

# 电子能量的量子化（半经典）

电子在轨道 $n$ 上的能量 $E_n$ 是其动能 $T_n$ 和势能 $U_n$ 之和：

$$T_n = \frac{1}{2}m_e v_n^2 = \frac{1}{32\pi^2\epsilon_0^2}\frac{m_e e^4}{\hbar^2}\frac{1}{n^2}$$

**精细结构常数**：$\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c} \approx \frac{1}{137}$

---

# 电子的能级

令 $E_0 = \frac{1}{32\pi^2\epsilon_0^2}\frac{m_e e^4}{\hbar^2} = 2.17\times10^{-18}\ \text{J} = 13.6\ \text{eV}$

那么电子能级的能量可以简写为：

$$\boxed{E_n = -E_0\frac{1}{n^2}}$$

氢原子的能量只能取一些分立值——**能量量子化**。

$n = 1$ 称为**基态**。

---

# 电子的能级——激发态

$n > 1$ 称为**激发态**：

| 量子数 | 状态 | 能量 |
|--------|------|------|
| $n = 1$ | 基态 | $E_1 = -13.6\ \text{eV}$ |
| $n = 2$ | 第一激发态 | $E_2 = -13.6/4 = -3.4\ \text{eV}$ |
| $n = 3$ | 第二激发态 | $E_3 = -13.6/9 = -1.51\ \text{eV}$ |

<br>

**问题：**
- 电子逃逸的能量是多少？原子电离的能量是多少？
- 电子由第一激发态跃迁到第三激发态需能量多少？
- **电离能**：把电子从氢原子第一玻尔轨道移到无穷远所需能量。

---
layout: two-cols
---

# 氢原子能谱

横线代表着电子在原子中的束缚态。

考虑高能级 $n'$ 到低能级 $n$ 的退激发：

$$h\nu = |E_{n'} - E_n| = E_0\left(\frac{1}{n^2} - \frac{1}{n'^2}\right)$$

由此得到**里德伯常数**。

::right::

<img src="/images/CNX_UPhysics_39_04_H-energy-1-2-21744.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 氢原子的连续能谱与光电效应

当入射光子能量足够大时，电子可以从束缚态跃迁到连续能谱（自由态），这就是**光电效应**。

::right::

<img src="/images/Screen Shot 2022-03-07 at 10.54.09-23570.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 习题1

**问题**：如果一个处于基态的氢原子吸收了一个93.7 nm的光子，对应于莱曼级数中的一条线，这对原子的能量和大小有何影响？当原子处于这种激发态时，需要多少能量才能使原子电离？

$$\frac{1}{\lambda} = R_H\left(\frac{1}{1^2} - \frac{1}{n^2}\right)$$

$$n = \frac{1}{\sqrt{1 - \frac{1}{\lambda R_H}}} \approx 6$$

---

# 习题2

**问题**：用12.6 eV的电子轰击基态氢原子，这些氢原子所能达到的最高态。

$$E_n - E_1 = \frac{E_1}{n^2} - E_1 \leq 12.6\ \text{eV}$$

---
layout: two-cols
---

# Bohr的贡献

Bohr因其提出的原子结构的量子理论（1913）及其后对量子力学发展所作的贡献，于**1922年获Nobel奖**。

Bohr理论开创了原子光谱和分子光谱的理论研究和实验研究的新时代。

::right::

<img src="/images/pasted-image-23640.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 反冲效应

原子核质量远大于电子，多数情况可忽略核运动。但高精度实验中需考虑核质量的影响。

$$\frac{1}{4\pi\epsilon_0}\frac{e^2}{r_n^2} = m_\mu\frac{v_n^2}{r_n}$$

$m_\mu$ 为**折合质量**。

::right::

<img src="/images/pasted-image-23660.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 反冲效应——数值

对于氢原子：

| 物理量 | 数值 |
|--------|------|
| $m_e$ | $0.511$ MeV/$c^2$ |
| $m_A$ | $938.272$ MeV/$c^2$ |
| $m_e/m_A$ | $5.446 \times 10^{-4}$ |

速度不依赖于质量，半径依赖于质量。

---
layout: two-cols
---

# 玻尔模型的拓展——类氢离子

类氢离子：原子核外只有一个电子的离子，但 $Z > 1$。

$$\frac{1}{4\pi\epsilon_0}\frac{Ze^2}{r_n^2} = m_e\frac{v_n^2}{r_n}$$

| 离子 | Z |
|------|---|
| He⁺ | 2 |
| Li²⁺ | 3 |
| Be³⁺ | 4 |

::right::

<img src="/images/Electron_avalanche-23795.gif" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 类氢离子——公式

跃迁发射（吸收）光子的波长：

$$\frac{1}{\lambda} = \frac{E_0}{hc}\left(\frac{1}{n'^2} - \frac{1}{n^2}\right)Z^2$$

在第 $n$ 轨道电子的半径：$r_n = \frac{a_0}{Z}n^2$

在第 $n$ 轨道电子的能量：$E_n = -Z^2 E_0\frac{1}{n^2}$

---

# 🧪 思考实验：如果你是1914年的实验物理学家

**背景**：1913年玻尔发表了他的原子理论，预言原子只能处于离散的能级上。但这只是理论推导——光谱数据是间接证据。你想设计一个实验，**不通过光谱**，直接验证原子能级的离散性。

你的实验室有：电子枪（可以产生可控能量的电子束）、各种气体（汞蒸气等）、电流计。

<div v-click>

**思路**：

1. 如果原子能级是离散的，那么原子只能吸收**特定大小**的能量
2. 用电子去"撞"原子——逐渐增大电子动能，看原子何时开始吸收能量
3. 被激发的原子会让电子突然失去动能——电流会突然下降！

</div>

<div v-click>

> 这正是弗兰克和赫兹的实验思路。有趣的是，他们最初并不知道玻尔的理论——他们以为自己在测汞的电离能。**伟大的实验可以揭示出连实验者自己都未预料到的真理。**

</div>

---
layout: two-cols
---

# §夫兰克-赫兹实验

1914年夫兰克-赫兹实验证实了能级的存在（**1925年诺贝尔物理学奖**）。

**两体碰撞问题**：原子（质量$M$）与电子（质量$m$）

$$\frac{1}{2}mv_1^2 + \frac{1}{2}MV_1^2 = \frac{1}{2}mv_2^2 + \frac{1}{2}MV_2^2 + \Delta E$$


- $\Delta E = 0$：弹性碰撞
- $\Delta E > 0$：非弹性碰撞（原子被激发）

::right::

<img src="/images/FHcollisions-24046.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 夫兰克-赫兹实验——装置

在充有水银蒸汽的玻璃管中，电子与汞原子碰撞，汞原子吸收电子能量而激发。

**实验原理**：
- KG间加正向电压，电子在电场作用下运动
- GP间加反向电压，电子穿过G达到P形成电流
- 作 $I_P \sim U_0$ 图

::right::

<img src="/images/pasted-image-24057.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<img src="/images/450px-FranckHertzHgTube-25019.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 夫兰克-赫兹实验——结果

汞原子基态为 $E_1$，第一激发态 $E_2$：

$$E_2 - E_1 = 4.9\ \text{eV}$$

Hg原子从第一激发态跃迁到基态，可观察到一条光谱，测得的波长值与理论结果相符。

**验证了原子能级的存在！**

::right::

<img src="/images/pasted-image-24132.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<img src="/images/Franck-Hertz-Neon-3-25024.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 总结（一）

<div class="text-sm">

| 概念 | 公式/说明 |
|------|-----------|
| **量子化** | 只能取离散的特定值 |
| **黑体辐射** | 维恩位移律 |
| **普朗克常数** | $h = 6.63\times10^{-34}$ J·s |
| **光子能量** | $E = h\nu$ |
| **光电效应** | $K_{\max} = h\nu - \phi$ |
| **脱出功** | 移出电子需要的最小能量 |
| **里德伯方程** | $1/\lambda = R_H(1/n^2 - 1/n'^2)$ |

</div>

---

# 总结（二）

<div class="text-sm">

| 概念 | 公式 |
|------|------|
| **玻尔模型** | $L = n\hbar$ |
| **半径** | $r_n = a_0 n^2$ |
| **能量** | $E_n = -E_0/n^2$ |
| **玻尔半径** | $a_0 \approx 0.529$ Å |
| **里德伯能量** | $E_0 = 13.6$ eV |
| **类氢离子半径** | $r_n = a_0 n^2 / Z$ |
| **类氢离子能量** | $E_n = -Z^2 E_0/n^2$ |

</div>

---
layout: two-cols
---

# 补充：瑞利-金斯公式

$$\Phi(\lambda, T)\mathrm{d}\lambda = \frac{8\pi kT}{\lambda^4}\mathrm{d}\lambda$$

::right::

<img src="/images/CNX_UPhysics_39_01_rayleigh-1-18998.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />
