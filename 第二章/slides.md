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
  overflow: hidden;
}
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
}
img {
  max-width: 100%;
  height: auto;
}
</style>

# 第二章 原子的量子态：玻尔模型

<br>

<div class="text-center">

**金 磊**

办公室：瑞安楼703B

邮箱：jinl@tongji.edu.cn

</div>

---

# §6-1 黑体辐射——从连续到离散

<br>

**需要掌握的知识点：**

1. 运用维恩位移律研究黑体辐射

2. 了解普朗克的能量量子假设

---
layout: two-cols
---

# 基尔霍夫热辐射定律（1859）

该定律描述了在热平衡状态下，一个物体对特定波长的电磁辐射的吸收和发射的关系。

**热平衡的几个主要特征：**

1. **温度均匀**：系统内部的所有部分都有相同的温度。
2. **热流平衡**：系统内部的热流相互抵消，没有净热流动。
3. **动态平衡**：尽管微观层面上的分子运动和能量交换仍在持续，但宏观层面上系统的状态不发生变化。

::right::

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<div class="text-center text-sm opacity-60">

Gustav Robert Kirchhoff（1824.3.12－1887.10.17）

</div>

<br>

对于一个特定的波长和温度，所有物体的发射率与吸收率与组成的物质无关，只与辐射的波长和温度有关：

$$e(\lambda, T) = a(\lambda, T)$$

---
layout: two-cols
---

# 基尔霍夫热辐射定律（续）

**吸收率**：物体表面吸收的辐射能量与入射到物体表面的辐射能量之比。值介于0和1之间。

**发射率**：物体实际辐射能量与理想黑体在同一温度下辐射能量之比。值介于0和1之间。

<br>

> 对于一个特定的波长和温度，所有物体的发射率与吸收率相等。

::right::

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

$$e(\lambda, T) = a(\lambda, T)$$

---
layout: two-cols
---

# 基尔霍夫热辐射定律——温度效应

**低温时**：可见波长 $e(\lambda,T) \to 0$

**高温时**：可见波长 $e(\lambda,T) \neq 0$，波长变长（红外）

::right::

<div class="flex gap-2 mt-4">
<img src="/images/Bbbefore-18560.jpg" style="width: 90%; max-height: 300px; object-fit: contain;" />
<img src="/images/Bbafter-18564.jpg" style="width: 90%; max-height: 300px; object-fit: contain;" />
</div>

---
layout: two-cols
---

# 黑体

**黑体**：吸收投射它的全部辐射，而无反射。

<br>

对于黑体 $a(\lambda, T) = 1$，因此发射辐射的能力 $e(\lambda,T)$ 与组成的物质无关，只与辐射的波长和温度有关。

<br>

**核心问题**：$e(\lambda,T)$ 到底如何变化？如何做相关的研究？

::right::

<img src="/images/CNX_UPhysics_39_01_blackbody-1-18725.jpg" style="width: 90%; margin: 10px auto; display: block;" />

---

# 黑体的性质

假设存在一个H形状的黑体：

- 当周围的温度**高于**黑体的温度时，黑体是**黑色**的
- 当周围的温度**低于**黑体的温度时，黑体是**发光**的

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

# 维恩位移律——应用

已知参宿四发黄光，参宿七发蓝光，如果把它们看成黑体，问谁的温度高？

$$\lambda_{\max} T = 2.898 \times 10^{-3}\ \text{mK}$$

由于 $\lambda_{\text{blue}} < \lambda_{\text{red}}$，

所以 $T_{\text{blue}} > T_{\text{red}}$

::right::

<img src="/images/CNX_UPhysics_39_01_orion-1-18871.jpg" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---
layout: two-cols
---

# 瑞利-金斯辐射

考虑一个立方体，边长为 $L \gg \lambda$，在温度为 $T$ 时达到热平衡，辐射场可以看成多个波矢 $\boldsymbol{k}=\{k_x, k_y, k_z\}$ 的叠加，并满足驻波条件。

$$\begin{aligned}
k_x &= \frac{\pi}{L} n_1, \quad k_y = \frac{\pi}{L} n_2, \quad k_z = \frac{\pi}{L} n_3 \\
k &= |\boldsymbol{k}| = \frac{\pi}{L} \sqrt{n_1^2 + n_2^2 + n_3^2}
\end{aligned}$$

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

当 $\omega = \omega_m$ 时，总的体积为 $V = \frac{1}{8}\frac{4}{3}\pi\left(\frac{\omega_m}{c}\right)^3$

考虑电场可能有两种垂直于 $\vec{k}$ 的偏振方向，共包含 $N$ 种辐射模式：

$$\begin{aligned}
N(\omega \leq \omega_m) &= 2\left(\frac{L}{\pi}\right)^3 V = \frac{1}{3}\frac{L^3\omega_m^3}{\pi^2 c^3}
\end{aligned}$$

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

瑞利-金斯把辐射模式看成谐振子的振动，热平衡状态能量满足玻尔兹曼分布。

---
layout: two-cols
---

# 瑞利-金斯辐射（紫外灾难）

$$w_\nu(\nu) = \frac{8\pi\nu^2}{c^3}kT$$

在高频（短波长）区域，能量密度趋于无穷大——这就是著名的**紫外灾难**。

::right::

<img src="/images/pasted-image-24940.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

<img src="/images/pasted-image-24943.png" style="width: 90%; max-height: 300px; object-fit: contain; margin: 10px auto; display: block;" />

---

# 普朗克假设

能量的背后存在普朗克（量子）谐振子。

**普朗克谐振子只能取离散的能量：**

$$E_n = nh\nu, \quad n = 1, 2, 3, \ldots$$

考虑电磁波与黑体交换能量，但只能交换离散的能量（quanta）。

每个离散的能量背后对应一个普朗克谐振子的量子态，每吸收特定的能量就会激发到下个量子态。

---

# 普朗克黑体辐射公式——推导

**普朗克能量假设**：能量为 $E = nh\nu$ 的概率为

$$p(nh\nu) = \frac{e^{-nh\nu/kT}}{\sum_{n=0}^{\infty} e^{-nh\nu/kT}}$$

每种模式的平均振动能量为：

$$\begin{aligned}
\bar{w}_\nu &= \sum_{n=0}^{\infty} nh\nu \cdot p(nh\nu) = \frac{\sum nh\nu\, e^{-nh\nu/kT}}{\sum e^{-nh\nu/kT}} = \frac{h\nu}{e^{h\nu/kT} - 1}
\end{aligned}$$

代入辐射场的谱辐射能量密度：

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

- 所有物体都以电磁波的形式辐射能量，辐射的强度与温度有关，**维恩定律**告诉我们，温度越高，辐射的波长越短。

- 在经典模型下能量是连续的，但是经典模型没有办法解释黑体辐射曲线。

- 为了解释黑体辐射曲线，**普朗克**假设能量是离散的，在此假设下提出**普朗克黑体辐射公式**并成功解释了黑体辐射曲线。

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

# 里德伯方程

1889年，瑞典人J.R.Rydberg提出一个更普遍的公式：

$$\frac{1}{\lambda} = R_H\left[\frac{1}{n^2} - \frac{1}{n'^2}\right] = T(n) - T(n')$$

- 氢的**所有**光谱线适用
- 不同的 $n$ 构成不同的光谱系
- 同一 $n$，不同的 $n'$ 构成同一谱系的不同谱线

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
