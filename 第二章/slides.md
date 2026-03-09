---
title: "第二章 原子的量子态：玻尔模型"
theme: default
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
math: katex
---

# 第二章 原子的量子态： 玻尔模型

金 磊

办公室：瑞安楼703B

邮箱：jinl@tongji.edu.cn

---

# §6-1 黑体辐射-从连续到离散

需要掌握的知识点：

（1） 运用维恩位移律研究黑体辐射

（2）了解普朗克的能量量子假设

---

# 基尔霍夫热辐射定律（1859）

$e(\lambda, T) = a(\lambda, T)$

Gustav Robert Kirchhoff

1824.3.12－1887.10.17

该定律描述了在热平衡状态下，一个物体对特定波长的电磁辐射的吸收和发射的关系

热平衡的几个主要特征


1. 温度均匀：系统内部的所有部分都有相同的温度。

2. 热流平衡：系统内部的热流相互抵消，没有净热流动。

3. 动态平衡：尽管微观层面上的分子运动和能量交换仍在持续，但宏观层面上系统的状态不发生变化。

对于一个特定的波长和温度，所有物体的发射率（表示物体辐射能力的物理量）与它的吸收率（表示物体吸收辐射能力的物理量）与组成的物质无关，它只与辐射的波长和温度有关,并且发射率=吸收率

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 基尔霍夫热辐射定律（1859）

$e(\lambda, T) = a(\lambda, T)$

Gustav Robert Kirchhoff

1824.3.12－1887.10.17

该定律描述了在热平衡状态下，一个物体对特定波长的电磁辐射的吸收和发射的关系

吸收率：指的是物体表面吸收的辐射能量与入射到物体表面的辐射能量之比。吸收率的值介于0和1之间，其中0表示物体不吸收任何辐射能量，1表示物体吸收所有入射的辐射能量

发射率：指的是物体实际辐射能量与理想黑体在同一温度下辐射能量之比。其值介于0和1之间，0表示物体不发射任何辐射能量，1表示物体是一个完美的黑体辐射源

对于一个特定的波长和温度，所有物体的发射率（表示物体辐射能力的物理量）与它的吸收率（表示物体吸收辐射能力的物理量）相等

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 基尔霍夫热辐射定律（1859）

$e(\lambda,T) \to 0$

Gustav Robert Kirchhoff

1824.3.12－1887.10.17

低温时

可见波长   $e(\lambda,T) \neq 0$

波长变长（红外）   $e(\lambda,T)$

高温时可见波长￼取有限值

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Bbbefore-18560.jpg" style="max-width: 289px; max-height: 400px;" />

<img src="/images/Bbafter-18564.jpg" style="max-width: 355px; max-height: 400px;" />

<img src="/images/bracket-right-18578.png" style="max-width: 336px; max-height: 400px;" />

---

# 基尔霍夫热辐射定律（1859）

$e(\lambda,T) \to 0$

Gustav Robert Kirchhoff

1824.3.12－1887.10.17

低温时

可见波长   $e(\lambda,T) \neq 0$

波长变长（红外）   $e(\lambda,T)$

高温时可见波长￼取有限值

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Bbbefore-18560.jpg" style="max-width: 289px; max-height: 400px;" />

<img src="/images/Bbafter-18564.jpg" style="max-width: 355px; max-height: 400px;" />

<img src="/images/bracket-right-18578.png" style="max-width: 336px; max-height: 400px;" />

<video controls style="max-width: 500px;">
  <source src="/images/τâ¡Φ╛Éσ░ä-22283.mov" />
</video>

---

# 黑体

黑体：吸收投射它的全部辐射，而无反射

<img src="/images/CNX_UPhysics_39_01_blackbody-1-18725.jpg" style="max-width: 487px; max-height: 400px;" />

---

# 黑体

假设存在一个H形状的黑体，

当周围的温度高于黑体的温度时，黑体是黑色的

当周围的温度低于黑体的温度时，黑体是发光的

---

# 基尔霍夫热辐射定律（1859）

$e(\lambda,T)$

Gustav Robert Kirchhoff

1824.3.12－1887.10.17

对于黑体发射辐射 $e(\lambda, T) = a(\lambda, T) =1$ 的能力与组成的物质无关，它只与辐射的波长和温度有关

对于黑体

$e(\lambda,T)$ 到底如何变化？

如何做相关的研究？

<img src="/images/Gustav_Robert_Kirchhoff-18470.jpg" style="max-width: 500px; max-height: 400px;" />

<img src="/images/CNX_UPhysics_39_01_blackbody-1-18725.jpg" style="max-width: 487px; max-height: 400px;" />

<video controls style="max-width: 498px;">
  <source src="/images/icegif-1614-24906.gif" />
</video>

---

# 维恩位移律

$\lambda_{max} T = 0.2898\ \ cm \cdot k$

<img src="/images/CNX_UPhysics_39_01_BBradcurve-1-18827.jpg" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Screen Shot 2022-01-21 at 20.23.37-18811.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/wien-12884-portrait-mini-2x-18818.jpg" style="max-width: 464px; max-height: 400px;" />

<img src="/images/60468-18860.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 维恩位移律

$\lambda_{\max }^{(\mathrm{red})} T_{(\mathrm{red})}=2.89810^{-3} \mathrm{mK}=\lambda_{\max }^{(\mathrm{blue})} T_{(\mathrm{blue})}$

参宿四

参宿七

已知参宿四发黄光，参宿七发蓝光，如果把它们看成黑体，问谁的温度高

<img src="/images/CNX_UPhysics_39_01_orion-1-18871.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 瑞利-金斯辐射

$L \gg \lambda$

考虑一个立方体，边长为 $T$ ，在温度为 $\boldsymbol{k}=\left\{k_{x}, k_{y}, k_{z}\right\}$ 时达到热平衡，辐射场可以看成多个波 $\begin{aligned}

k_{x}=\frac{\pi}{L} n_{1}, \quad k_{y}=\frac{\pi}{L} n_{2}, \quad k_{z}=\frac{\pi}{L} n_{3} \\

\Rightarrow k=|\boldsymbol{k}|=\frac{\pi}{L} \sqrt{n_{1}^{2}+n_{2}^{2}+n_{3}^{2}}

\end{aligned}$ 的叠加，并满足驻波条件（辐射场在立方体边缘为0，即辐射场在黑体边缘被完全吸收）

<img src="/images/Screen Shot 2022-02-23 at 21.52.35-22413.png" style="max-width: 500px; max-height: 400px;" />

---

# 瑞利-金斯辐射

$\omega = kc$

可得波长和角频率 $\begin{aligned}

\lambda &=\frac{2 L}{\sqrt{n_{1}^{2}+n_{2}^{2}+n_{3}^{2}}} \\

\omega &=c k=\frac{\pi c}{L} \sqrt{n_{1}^{2}+n_{2}^{2}+n_{3}^{2}} .

\end{aligned}$

用 $(n_1,n_2,n_3)$ 定义一种辐射模式

我们需要求解的是当 $\omega < \omega_m$ 时有多少种辐射模式存在？

<img src="/images/Screen Shot 2022-02-23 at 21.52.35-22413.png" style="max-width: 500px; max-height: 400px;" />

---

# 瑞利-金斯辐射

$k$

在 $k = \frac{\pi}{L} (n_1,n_2,n_3)$ 空间下， $(n_1,n_2,n_3)$ ， $\frac{\pi^3}{L^3}$ 代表着一个格点，每个格点的体积为 $\omega = \omega_m$ ，当 $V=\frac{1}{8} \frac{4}{3} \pi\left(\frac{\omega_{\mathrm{m}}}{c}\right)^{3}$ 时，总的体积为

考虑到电场可能有两种垂直于 $\vec{k}$ 的方向，那么共包含N种辐射模式

note: $\begin{aligned}

N\left(\omega \leq \omega_{\mathrm{m}}\right) &=2\left(\frac{L}{\pi}\right)^{3} \cdot V=2 \frac{1}{8} \frac{4 \pi}{3}\left(\frac{L \omega_{\mathrm{m}}}{\pi c}\right)^{3} \\

&=\frac{1}{3} \frac{L^{3} \omega_{\mathrm{m}}^{3}}{\pi^{2} c^{3}}

\end{aligned}$

<img src="/images/Screen Shot 2022-02-23 at 22.15.16-22535.png" style="max-width: 500px; max-height: 400px;" />

---

# 瑞利-金斯辐射

$n\left(\omega \leq \omega_{\mathrm{m}}\right)=\frac{1}{L^{3}} N\left(\omega<\omega_{\mathrm{m}}\right)=\frac{1}{3} \frac{\omega_{\mathrm{m}}^{3}}{\pi^{2} c^{3}}$

定义辐射模式密度

定义谱辐射模式密度

用频率 $n_{\omega}=\frac{\mathrm{d}}{\mathrm{d} \omega}(n(\omega))=\frac{\omega^{2}}{\pi^{2} c^{3}}$ 表示谱辐射密度

每单位体积，频率在 $\nu = \omega / (2 \pi)$ 与 $n_{v}(v)=\frac{8 \pi v^{2}}{c^{3}}$ 的辐射模式密度

---

# 瑞利-金斯辐射

$w_{v}(v) \mathrm{d} v=n(v) \bar{w}_{v}(T) \mathrm{d} v$

辐射场的谱辐射能量密度为

每种模式的平均振动能量

瑞利-金斯把辐射模式看成一种谐振子的振动，热平衡状态能量分布满足玻尔兹曼分布 $\exp[-\omega / (kT)]$ ，则

---

# 瑞利-金斯辐射（紫外灾难）

$w_{v}(v)=\frac{8 \pi v^{2}}{c^{3}} k T$

<img src="/images/pasted-image-24940.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/pasted-image-24943.png" style="max-width: 450px; max-height: 400px;" />

---

# 普朗克假设

$E_n = n h \nu \ \ \ n=1,2,3...$

能量的背后存在普朗克（量子）谐振子

普朗克谐振子只能取离散的能量

考虑电磁波与黑体交换能量，但只能交换离散的能量，即quanta

￼

每个离散的能量背后对应一个普朗克谐振子的量子态

每吸收特定的能量就会激发到下个量子态

---

# 普朗克黑体辐射公式

$E$

普朗克能量假设

那么能量为 $E=n h v$ 的概率为

以及归一化条件

---

# 瑞利-金斯辐射

$w_{v}(v) \mathrm{d} v=n(v) \bar{w}_{v}(T) \mathrm{d} v$

辐射场的谱辐射能量密度为

每种模式的平均振动能量

瑞利-金斯把辐射模式看成一种谐振子的振动，热平衡状态能量分布满足玻尔兹曼分布 $\exp[-\omega / (kT)]$ ，则

---

# 普朗克黑体辐射公式

$\begin{aligned}

\bar{w}_{v} &=\sum_{n=0}^{\infty} n h v\  p(n h v) \\

&=\frac{\sum n h v \mathrm{e}^{-n h v / k T}}{\sum \mathrm{e}^{-n h v / k T}}=\frac{h v}{\mathrm{e}^{h v / k T}-1}

\end{aligned}$

普朗克能量假设下，每种模式的平均振动能量为

代入辐射场的谱辐射能量密度

---

# 普朗克黑体辐射公式

$w_{v}(v) \mathrm{d} v=\frac{8 \pi h v^{3}}{c^{3}} \frac{1}{\mathrm{e}^{h v / k T}-1}$

普朗克常数

玻尔兹曼常数

<img src="/images/Screen Shot 2024-02-28 at 22.07.15-24963.png" style="max-width: 500px; max-height: 400px;" />

---

# §6-1 黑体辐射 (小结)

所有物体都以电磁波的形式辐射能量，辐射的强度与温度有关，维恩定律告诉我们，温度越高，辐射的波长越短

在经典模型下能量是连续的，但是经典模型没有办法解释黑体辐射曲线

为了解释黑体辐射曲线，普朗克假设能量是离散的，在此假设下提出普朗克黑体辐射公式并成功的解释了黑体辐射曲线

---

# §6-2 光电效应

需要掌握的知识点：

了解光电效应的物理图像

了解为什么光电效应不能用经典理论解释

了解为什么爱因斯坦的方法可以解释光电效应

---

# 光电效应

1887年由赫兹发现，在光的照射下，物质表面因吸收辐射能量而形成电流的现象，我们称之为光电效应

正负极间电压可变

光电子在真空中运动

可忽略动能的损失

单色光源

<img src="/images/CNX_UPhysics_39_02_photoexp-1-2-19460.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 经典理论无法解释的光电效应特性

$10^7$

（一）响应时间

响应时间：电磁波照射到材料上到发出光电子的时间差

经典理论认为这个时间很长~ $< 10^{-9}$ s

实际上￼s

---

# 经典理论无法解释的光电效应特性

$K_{max} = e \Delta V_s$

（二）辐射强度与光电流之间的关系

存在遏止电压：与光电子的动能有关

经典理论认为光电子获取动能是连续的，即光照流强越大，光电子的动能越大

<img src="/images/CNX_UPhysics_39_02_photoexp1-1-19625.jpg" style="max-width: 325px; max-height: 400px;" />

---

# 经典理论无法解释的光电效应特性

（三）存在截止频率（cut-off frequency）

截止频率是每个材料本身的特性

不同材料的斜率是相同的

<img src="/images/CNX_UPhysics_39_02_photoexp2-1-19717.jpg" style="max-width: 440px; max-height: 400px;" />

---

# 光电效应的量子解释

$E_\nu$

爱因斯坦提出光量子假设

1921年诺贝尔物理学奖

光子以光速传播并携带能量 $\nu$ ，能量依赖其频率 $E_\nu = h \nu$ ， $h$

$h$ 普朗克常数

当光子到达材料表面时，或者交换所有的能量，或者彻底不交换能量

在爱因斯坦的解释中，单个电子与光子直接发生相互作用

<img src="/images/60468-18860.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 光电效应的量子解释

$\lambda=\frac{h c}{\varphi}=\frac{1240 \mathrm{eVnm}}{4.73 \mathrm{eV}}=262 \mathrm{~nm}$

当波长为300 nm的电磁波照射在银金属表面时，能否产生光电子

<img src="/images/Screen Shot 2022-01-24 at 16.11.38-20007.png" style="max-width: 500px; max-height: 400px;" />

---

# §6-3 光谱

唯像的讨论氢原子相关的实验现象

需要掌握的知识点：

了解吸收谱线与发射谱线的区别

掌握氢原子光谱规律及光谱线系公式

---

# 唯像理论与第一性原理

杨振宁：美与物理学

实验物理

理论物理

语言

布拉赫（1546-1601）精密测量了行星轨道

开普勒（1571-1630）唯像的提出三定律

牛顿力学与万有引力

唯像理论和第一性原理是相对的

<img src="/images/Screen Shot 2022-02-28 at 13.07.02-23046.png" style="max-width: 300px; max-height: 400px;" />

---

# 唯像理论与第一性原理

<img src="/images/Screen Shot 2023-03-20 at 19.08.25-24628.png" style="max-width: 500px; max-height: 400px;" />

<video controls style="max-width: 500px;">
  <source src="/images/225642347-a07127da-a84e-4af3-96f4-4c7fef5a673b-24632.mp4" />
</video>

---

# 为什么天是蓝色的？

$I(\lambda)_{\text {scattering }} \propto \frac{I(\lambda)_{\text {incident }}}{\lambda^{4}}$

瑞利散射

<img src="/images/images-4-23186.jpeg" style="max-width: 276px; max-height: 400px;" />

<img src="/images/Solar_spectrum_en.svg-23207.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Rayleigh_sunlight_scattering-23200.png" style="max-width: 500px; max-height: 400px;" />

---

# 夫琅和费谱线

1814年德国物理学家J.夫琅和费利用自制光谱装置观察太阳光时，在明亮彩色背景上观察到576条狭细的暗线

其中最明显的8条用A到H字母标记。这些暗线被称为夫琅和费谱线。实际上约有3万多条

<img src="/images/Fraunhofer_lines.svg-20094.png" style="max-width: 500px; max-height: 400px;" />

---

# 夫琅和费谱线

1859年基尔霍夫和本生确认了每一条谱线所对应的化学元素，并推论在太阳光谱中的暗线是由在太阳上层的那些元素吸收造成的

<img src="/images/700px-Spectrum_of_blue_sky.svg-2-23231.png" style="max-width: 500px; max-height: 400px;" />

---

# 光谱仪

光谱—研究原子结构的重要途径之一

1) 光源  2) 光栅棱镜   3)记录仪

<img src="/images/Screen Shot 2022-01-10 at 23.13.25-18709.png" style="max-width: 500px; max-height: 400px;" />

<video controls style="max-width: 350px;">
  <source src="/images/Light_dispersion_conceptual_waves350px-20346.gif" />
</video>

---

# 谱线

谱线：谱线是在均匀且连续的光谱上明亮或黑暗的线条

有吸收谱线或发射谱线两种

连续光谱

发射谱线（离散光谱）

吸收谱线（离散光谱）

In 1901, Max Planck used quanta to mean "quanta of matter and electricity", gas, and heat. In 1905, in response to Planck's work and the experimental work of Lenard (who explained his results by using the term quanta of electricity), Albert Einstein suggested that radiation existed in spatially localized packets which he called "quanta of light"

<img src="/images/2880px-Spectral-lines-continuous.svg-18398.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/2880px-Spectral-lines-emission.svg-18412.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/2880px-Spectral-lines-absorption.svg-18435.png" style="max-width: 500px; max-height: 400px;" />

---

# 谱线

$\lambda$

吸收谱线与发射谱线完全重叠

吸收和发射光谱是特定原子的特征

即使光谱仪的光谱分辨率极高，光谱线也不是完全窄的。这意味着原子不会发射严格的单色辐射，而是在每个波长 $I(\lambda )$ 周围显示出强度分布 $\Delta \lambda$ ，具有有限的半宽￼。

In 1901, Max Planck used quanta to mean "quanta of matter and electricity", gas, and heat. In 1905, in response to Planck's work and the experimental work of Lenard (who explained his results by using the term quanta of electricity), Albert Einstein suggested that radiation existed in spatially localized packets which he called "quanta of light"

---

# 谱线

特定波长的光被吸收

发射特定波长的光

<img src="/images/CNX_UPhysics_39_04_spectra-1-20112.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 氢原子光谱

$\frac{1}{\lambda} = R_H (\frac{1}{2^2}-\frac{1}{n'^2}), \ \ \ n'=3,4,5,...$

氢原子在可见光波段有四条谱线

波长增加

注意亮度变化

1885年巴耳末提出经验公式研究上述谱线

<img src="/images/CNX_UPhysics_39_04_emit-H-1-20212.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 巴耳末系谱线

$\frac{1}{\lambda} = R_H (\frac{1}{2^2}-\frac{1}{n^2}), \ \ \ n=3,4,5,...$

纯经验公式；这组谱线叫Balmer线系

<img src="/images/Screen Shot 2022-01-25 at 16.01.23-20298.png" style="max-width: 214px; max-height: 400px;" />

---

# 里德伯方程

$n$

•1889年，瑞典人J.R.Rydberg提出一个更普遍的公式：





•氢的所有光谱线适用，



•不同的 $n$ 构成不同的光谱系；同一 $n'$ ，不同的 $\frac{1}{\lambda} = R_H \Big[\frac{1}{n^2}-\frac{1}{n'^2}\Big] = T(n) - T(n')$ 构成同一谱系的不同谱线

---

# 里德伯方程

$n$

结论：

1). 氢光谱中任何一条谱线的波数，都可以写成两个整数决定的函数之差。

2). 对于给定的 $n'>n$ 值， $n$ ，可得到同一线系中各光谱的波数值。

3). 改变公式中的￼值，就可得到不同的线系。

<img src="/images/800px-Hydrogen_transitions.svg-20406.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/2880px-Hydrogen_spectrum.svg-20456.png" style="max-width: 500px; max-height: 400px;" />

---

# 其它线系

$\frac{1}{\lambda} = R_H \Big[\frac{1}{1}-\frac{1}{n'^2}\Big], n'=2,3,...$

紫

外

区

红

外

区

1914年 赖曼发现          T.Lyman系：

1908年 帕邢发现           F.Paschen系：

1922年布喇开发现            F.Brackett系:

1924年普芳德发现           H.A.Pfund系:

---

# §玻尔模型

需要掌握的知识点：

解释氢原子的结构

了解氢原子的量子模型

掌握如何使用玻尔模型解释氢原子光谱

---

# 盖革－马斯登实验

汤姆逊1904年提出原子核的布丁模型

Proceedings of the Royal Society of London A.

<img src="/images/PlumPuddingModel_ManyCorpuscles-25001.png" style="max-width: 263px; max-height: 400px;" />

<img src="/images/Plum_pudding-25004.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/440px-Gold_foil_experiment_conclusions.svg-25007.png" style="max-width: 440px; max-height: 400px;" />

---

# 原子的经典模型

$\vec{F} = m_e \vec{a}$

卢瑟福发现原子有核，电子围绕原子核做运动，即电子在库仑力下做圆周运动

$\frac{1}{4 \pi \epsilon_{0}} \frac{e^{2}}{r^{2}}=m_{e} \frac{v^{2}}{r} \quad \Rightarrow v^{2}=\frac{e^{2}}{4 \pi \epsilon_{0}} \frac{1}{m_{e}r}$ :电子电荷

$e$ :电子质量

$m_e$ :圆周半径

$r$ :运动速率

电子的总能量可以写为动能+势能

$v$

$\begin{aligned}

E &=\frac{1}{2} m_{e} v^{2}-\frac{1}{4 \pi \epsilon_{0}} \frac{e^{2}}{r} \\

&=-\frac{1}{2} \frac{e^{2}}{4 \pi \epsilon_{0} r}

\end{aligned}$

---

# 原子的经典模型

根据经典理论，电子绕原子核运行是一个不断加速的过程

任何电子的加速都会辐射电磁波

而消耗电子的能量，使得电子向原子核坠落

在电子逐渐“坠入”原子核的过程中，所发出的电磁波应当是连续变化的，但观察到的原子光谱是分离的

<img src="/images/185081_153314_ans_732d0264d2d0477c9394ed404835c8fc-20814.png" style="max-width: 200px; max-height: 400px;" />

---

# 玻尔模型的三点假设

$n$

带负电荷的电子在某些特定的轨道上围绕带正电荷的原子核做圆周运动

电子的轨道满足量子化条件：在第 $L_n$ 个轨道上的角动量 $L_n = n\hbar, \ \ n=1,\ 2,\ 3,\ ...$ 只能取离散值 $m_{e} v_{n} r_{n}=n \hbar$

即 $\hbar=h/(2\pi)$ ,  $E_n$

电子可以从能量为 $E_{n'}$ 的轨道跃迁到能量为 $h \nu=\left|E_{n}-E_{n'}\right|$ 的轨道，当原子吸收光子时电子会跃迁到高能量的轨道上，当原子发射光子时，电子会退激发到低能量的轨道上

即￼

---

# 玻尔模型的三点假设

$n$

带负电荷的电子在某些特定的轨道上围绕带正电荷的原子核做圆周运动

电子的轨道满足量子化条件：在第 $L_n$ 个轨道上的角动量 $L_n = n\hbar, \ \ n=1,\ 2,\ 3,\ ...$ 只能取离散值 $m_{e} v_{n} r_{n}=n \hbar$

即 $E_n$

电子可以从能量为 $E_{n'}$ 的轨道跃迁到能量为 $h \nu=\left|E_{n}-E_{n'}\right|$ 的轨道，当原子吸收光子时电子会跃迁到高能量的轨道上，当原子发射光子时，电子会退激发到低能量的轨道上

即￼

<video controls style="max-width: 275px;">
  <source src="/images/Bohr_atom_animation_2-20962.gif" />
</video>

---

# 玻尔模型、经典模型与里德伯方程

$\frac{1}{\lambda} = R_H \Big[\frac{1}{n^2}-\frac{1}{n'^2}\Big] = T(n) - T(n')$

里德伯方程：  $\frac{1}{\lambda} = \frac{1}{hc} |E_n-E_n'|$

玻尔模型：  $E_{n'}$

考虑从高能级 $E_n$ 退激发到低能级 $E_n= - \frac{R_Hhc}{n^2}$ ： $E_n=-\frac{1}{2} \frac{e^{2}}{4 \pi \epsilon_{0} r_n}$

经典模型：  $r_n = \frac{e^{2}}{4 \pi \epsilon_{0}}\frac{n^2}{2R_Hhc}$

半经典

---

# 玻尔模型、经典模型与里德伯方程

$\frac{1}{\lambda} = R_H \Big[\frac{1}{n^2}-\frac{1}{n'^2}\Big] = T(n) - T(n')$

里德伯方程：  $\frac{1}{\lambda} = \frac{1}{hc} |E_n-E_n'|$

玻尔模型：  $E_{n'}$

考虑从高能级 $E_n$ 退激发到低能级 $E_n= - \frac{R_Hhc}{n^2}$ ： $E_n=-\frac{1}{2} \frac{e^{2}}{4 \pi \epsilon_{0} r_n}$

经典模型：  $r_n = \frac{e^{2}}{4 \pi \epsilon_{0}}\frac{n^2}{2R_Hhc}$

半经典

特别需要说明的是玻尔模型仍满足能量守恒和动量守恒

---

# 电子轨道的量子化（半经典）

$\frac{1}{4 \pi \epsilon_{0}} \frac{e^{2}}{r_n^{2}}=m_{e} \frac{v_n^{2}}{r_n}$

经典模型：  $m_ev_nr_n=n\hbar$

假定电子轨道是离散的（量子的），但是仍满足经典运动规律

玻尔模型：  $v_n=\frac{1}{4\pi\epsilon_{0}} \frac{e^2}{\hbar}\frac{1}{n}$

可以求得

电子的速率和半径只依赖于 $r_n = 4\pi\epsilon_{0} \frac{\hbar^2}{m_e e^2} n^2$

---

# 电子轨道的数值计算

$r_n = 4\pi\epsilon_{0} \frac{\hbar^2}{m_e e^2} n^2$

$a_0 = 4\pi\epsilon_{0} \frac{\hbar^2}{m_e e^2} \approx 5.29 \times 10^{-11} m = 0.529 \AA$ 通常被称为玻尔半径，则

即电子轨道半径只能取特定的值 $a_0$

---

# 电子能量的量子化（半经典）

$n$

电子在轨道 $E_n$ 上的能量 $T_n$ 是其动能 $U_n$ 和势能 $T_{n}=\frac{1}{2} m_{e} v_{n}^{2}=\frac{1}{32 \pi^{2} \epsilon_{0}^{2}} \frac{m_{e} e^{4}}{\hbar^{2}} \frac{1}{n^{2}}$ 之和

精细结构常数

---

# 电子的能级

$E_{0}=\frac{1}{32 \pi^{2} \epsilon_{0}^{2}} \frac{m_{e} e^{4}}{\hbar^{2}}=2.1710^{-18} \mathrm{~J}=13.6~\mathrm{eV}$

令

那么电子能级的能量可以简写为

这里可以看到氢原子的能量只能取一些分立值，这种现象称之为能量量子化

$E_{n}=-E_{0} \frac{1}{n^{2}}$ ，称为基态

$n=1$

---

# 电子的能级

$n>1$

$n=2$ ，称为激发态

$n=3$ ，第一激发态

$E_2 = -13.6~eV/4 = -3.4~eV$ ，第二激发态

$E_3 = -13.6~eV/9 = -1.51~eV$

问题：

电子逃逸的能量是多少？原子电离的能量是多少？

电子由第一激发态跃迁到第三激发态需能量多少？

电离能：把电子从氢原子第一玻尔轨道移到无穷远所需能量。

---

# 氢原子能谱

$n'$

横线代表着电子在原子中的束缚态

考虑高能级 $n$ 到低能级 $h \nu=\left|E_{n'}-E_{n}\right|=-E_{0} \frac{1}{n'^{2}}+E_{0} \frac{1}{n^{2}}=E_{0}\left(\frac{1}{n'^{2}}-\frac{1}{n^{2}}\right)$ 的退激发

里德伯常数

<img src="/images/CNX_UPhysics_39_04_H-energy-1-2-21744.jpg" style="max-width: 490px; max-height: 400px;" />

---

# 氢原子的连续能谱与光电效应

光电效应

<img src="/images/Screen Shot 2022-03-07 at 10.54.09-23570.png" style="max-width: 500px; max-height: 400px;" />

---

# 习题

$\frac{1}{\lambda}=R_{\mathrm{H}}\left(\frac{1}{1^{2}}-\frac{1}{n^{2}}\right) \Rightarrow n=\frac{1}{\sqrt{1-\frac{1}{\lambda R_{\mathrm{H}}}}}=\frac{1}{\sqrt{1-\frac{1}{\left(93.7 \times 10^{-9} \mathrm{~m}\right)\left(1.097 \times 10^{7} \mathrm{~m}^{-1}\right)}}}=6.07 \Rightarrow n=6$

如果一个处于基态的氢原子吸收了一个93.7 nm 的光子，对应于莱曼级数中的一条线，这对原子的能量和大小有何影响？ 当原子处于这种激发态时，需要多少能量才能使原子电离？

---

# 习题

$E_n - E_1 = \frac{E_1}{n^2} -  E_1 \leq 12.6~eV$

用 12.6eV 的电子轰击基态氢原子，这些氢原子所能达到最高态。

---

# Bohr因其提出的原子结构的量子理论（1913）及其后对量子力学发展所作的贡献，于1922年获Nobel奖

Bohr理论开创了原子光谱和分子光谱的理论研究和实验研究的新时代，是研究原子和分子结构的有力工具，极大地推动了原子和分子结构理论的发展。

<img src="/images/pasted-image-23640.png" style="max-width: 500px; max-height: 400px;" />

---

# 反冲效应

$\frac{1}{4 \pi \epsilon_{0}} \frac{e^{2}}{r_n^{2}}=m_{\mu} \frac{v_n^{2}}{r_n}$

相对于电子，原子核的质量很大，多数情况下可以忽略原子核的运动。但是当实验精度很高的时候，需要考虑原子核的质量对能谱的影响

$m_\mu$ 为折合质量

原子核的质量

<img src="/images/pasted-image-23660.png" style="max-width: 500px; max-height: 400px;" />

---

# 反冲效应

$m_e=0.51099895000(15) \  \mathrm{MeV}/c^2$

对于氢原子而言

$m_A=938.27208816(29) \  \mathrm{MeV}/c^2$

$m_e/m_A=0.000544617021489$

$\frac{1}{4 \pi \epsilon_{0}} \frac{e^{2}}{r_n^{2}}=m_{\mu} \frac{v_n^{2}}{r_n}$

不依赖于质量

---

# 玻尔模型的拓展(类氢离子)

$Z>1$

类氢离子是指原子核外只有一个电子的离子，但 $\frac{1}{4 \pi \epsilon_{0}} \frac{Z e^{2}}{r_n^{2}}=m_{e} \frac{v_n^{2}}{r_n}$

一次电离的氦离子

二次电离的锂离子

三次电离的铍离子

He+     Z=2

Li++     Z=3

Be+++    Z=4

电子与原子核外电子的碰撞，导致了新的电离，这时有两类电子，一个时之前的自由电子， 一个是刚电离出来的电子

<img src="/images/Electron_avalanche-23795.gif" style="max-width: 500px; max-height: 400px;" />

---

# 玻尔模型的拓展(类氢离子)

$\frac{1}{\lambda}=\frac{E_{0}}{h c}\left(\frac{1}{n'^{2}}-\frac{1}{n^{2}}\right) Z^2$

跃迁发射（吸收）光子的波长

在第 $n$ 轨道电子的半径

在第 $r_{n}=\frac{a_{0}}{Z} n^{2}$ 轨道电子的能量

---

# §夫兰克-赫兹实验

$V_1$

1914年夫兰克-赫兹实验证实了能级的存在

1925年诺贝尔物理学奖

两体碰撞问题

原子(质量M)，碰撞前后速率分别为 $V_2$ ， $v_1$

电子(质量m)，碰撞前后速率分别为 $v_2$ ， $\frac{1}{2} m v_{1}^{2}+\frac{1}{2} M V_{1}^{2}=\frac{1}{2} m v_{2}^{2}+\frac{1}{2} M V_{2}^{2}+\Delta E$

系统能量守恒： $\Delta E$

$\Delta E =0$ 为原子内部能量增量

a).若 $\Delta E >0$ 表示只有平移能量交换，原子内部能量不变 ——称为弹性碰撞

b).若￼表示一部分平移能量转换为原子内部能量使原子激发——称为非弹性碰撞

---

# §夫兰克-赫兹实验

在充有水银蒸汽的玻璃管中，电子与汞原子碰撞，汞原子吸收电子能量而激发。

实验原理

KG间加正向电压，电子在电场作用下运动。

GP间加反向电压，电子穿过G达到P形成电流

作IP ~ U0 图

<img src="/images/FHcollisions-24046.png" style="max-width: 191px; max-height: 400px;" />

<img src="/images/pasted-image-24057.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/450px-FranckHertzHgTube-25019.jpg" style="max-width: 450px; max-height: 400px;" />

---

# §夫兰克-赫兹实验

$E_1$

汞原子基态为 $E_2$ ，第一激发态 $E_2 - E_1 =4.9~eV$

Hg原子第一激发态与基态能量之差

Hg原子从第一激发态跃迁到基态, 可观察到一条光谱，测得的波长值与理论结果相符。

验证了原子能级的存在!

<img src="/images/pasted-image-24132.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Franck-Hertz-Neon-3-25024.png" style="max-width: 440px; max-height: 400px;" />

---

# 总结

$h=6.63 \times 10^{-34}~J\cdot s$

量子化：只能取离散的特定值

黑体辐射：维恩位移律、普朗克提出量子化的诱因

普朗克常数： $E = h \nu$

光子能量： $K_{max} =  h\nu -\phi$

光电效应： $\phi$

脱出功 $E_\gamma = E_{n'}-E_n$ ：移出一个电子需要的最小能量

原子的吸收和发射光谱： $\frac{1}{\lambda} = R_H (\frac{1}{n'^2}-\frac{1}{n^2})$

里德伯方程：￼

---

# 总结

$L = n\hbar$

玻尔模型：角动量量子化 $r_n= a_0 n^2$ ，半径 $E_n = - E_0/n^2$ ,

能量 $a_0 = 4\pi\epsilon_{0} \frac{\hbar^2}{m_e e^2} \approx 5.29 \times 10^{-11} m = 0.529 \AA$

玻尔半径： $E_{0}=\frac{1}{32 \pi^{2} \epsilon_{0}^{2}} \frac{m_{e} e^{4}}{\hbar^{2}}=13.6~\mathrm{eV}$

里德伯能量： $r_{n}=\frac{a_{0}}{Z} n^{2}$

类氢离子：半径 $E_{n}=-Z^{2} E_{0} \frac{1}{n^{2}}$ ， 能量￼

---

<!-- 此页内容待补充 -->

---

# 瑞利-金斯辐射

$\Phi(\lambda, T) d\lambda = \frac{8\pi kT}{\lambda^4} d\lambda$

<img src="/images/CNX_UPhysics_39_01_rayleigh-1-18998.jpg" style="max-width: 333px; max-height: 400px;" />

---

# Proceedings of the Royal Society of London A.
