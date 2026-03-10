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


<!-- 以下内容暂时隐藏，内容已移至 _disabled_slides.md -->
