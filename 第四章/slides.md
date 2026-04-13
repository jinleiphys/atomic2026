---
title: "第四章 原子的精细结构"
theme: default
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
math: katex
---

<style>
/* 让所有 slide 可以垂直滚动，内容超出屏幕也能看完 */
.slidev-layout {
  overflow-y: auto !important;
  overflow-x: hidden !important;
  max-height: 100vh;
  scrollbar-width: thin;
  scrollbar-color: #C71585 transparent;
}
.slidev-layout::-webkit-scrollbar {
  width: 8px;
}
.slidev-layout::-webkit-scrollbar-track {
  background: transparent;
}
.slidev-layout::-webkit-scrollbar-thumb {
  background-color: rgba(199, 21, 133, 0.4);
  border-radius: 4px;
}
.slidev-layout::-webkit-scrollbar-thumb:hover {
  background-color: rgba(199, 21, 133, 0.7);
}
</style>

# 第四章 原子的精细结构：电子的自旋

金 磊

办公室：瑞安楼703B

邮箱：jinl@tongji.edu.cn

---

# §17 氢原子

需要掌握的知识点：

（1）理解氢原子是原子物理的"圣杯"，1926 年薛定谔解出氢原子是量子力学的第一个伟大胜利

（2）掌握中心势 $U(r)$ 下定态薛定谔方程的求解流程，球坐标 → 分离变量 → 角向方程 + 径向方程

（3）理解三个量子数 $(n, \ell, m)$ 的物理意义和取值规则

（4）掌握能级公式 $E_n = -E_0/n^2$ 和简并度 $n^2$，理解为何"量子化自然涌现"

（5）区分玻尔模型与薛定谔模型，理解后者为何更深刻

---

# 1885 年的谜：巴尔末公式

1885 年，瑞士中学数学教师 J. Balmer 发现氢原子可见光谱的 4 条谱线波长满足

$$\lambda_n = b\, \frac{n^2}{n^2 - 4}, \qquad n = 3, 4, 5, 6$$

其中 $b = 364.6\ \mathrm{nm}$ 是经验常数。

<v-click>

1888 年，Rydberg 把公式推广为

$$\frac{1}{\lambda} = R_H\!\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \qquad R_H = 1.0973\times 10^7\ \mathrm{m^{-1}}$$

每条氢原子谱线都对应一个整数对 $(n_1, n_2)$。

**没有人知道为什么。**

</v-click>

<v-click>

> "我们当时面对的，是一组实验数据，没有任何理论可以解释。每个学物理的人都觉得，这背后一定有什么深刻的东西。"（N. Bohr 1962 年回忆）

</v-click>

---

# 玻尔模型（1913）的成功与困境

玻尔通过假设角动量量子化 $L = n\hbar$，正确推出 Rydberg 常数：

$$E_n = -\frac{m_e e^4}{2(4\pi\epsilon_0)^2 \hbar^2}\, \frac{1}{n^2} = -\frac{13.6\ \mathrm{eV}}{n^2}$$

<v-click>

但玻尔模型有三大困境：

1. "电子轨道"违反经典电动力学，加速电荷应该辐射能量
2. 角动量量子化是**人为假设**，没有物理来源
3. 无法解释精细结构、塞曼效应、谱线强度

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.6em;">

**1926 年薛定谔的挑战**：用新的波动力学，从一个统一的方程出发，推出氢原子的所有性质。

如果成功，量子力学就赢了。

</div>

</v-click>

---

# 氢原子的哈密顿量

假设质子静止（$m_p \approx 1836\, m_e$，质子可视为不动），电子在质子的库仑场中运动：

$$U(r) = -\frac{1}{4\pi\epsilon_0}\, \frac{e^2}{r}$$

势能**只依赖于 $r$**，不依赖时间，定态薛定谔方程为：

$$\left[-\frac{\hbar^2}{2 m_e}\nabla^2 - \frac{1}{4\pi\epsilon_0}\frac{e^2}{r}\right]\psi(\vec{r}) = E\, \psi(\vec{r})$$

<img src="/images/CNX_UPhysics_41_01_HydAtom-1-26259.jpg" style="max-width: 320px; max-height: 220px; margin: 0.4em auto; display: block;" />

<v-click>

**核心难点**：库仑势是中心势，不能在直角坐标里轻松分离变量。我们要换到球坐标，但要先复习几个简单的"前置案例"，把求解的套路搞清楚。

</v-click>

---

# 预备 ①：一维无限深方势阱

最简单的束缚态问题。粒子被关在 $0 < x < a$ 中：

$$V(x) = \begin{cases} 0, & 0 < x < a \\ +\infty, & \text{otherwise} \end{cases}$$

<v-click>

阱内 $V = 0$，定态薛定谔方程为

$$\frac{d^2 \psi}{dx^2} + k^2 \psi = 0, \qquad k^2 = \frac{2 m E}{\hbar^2}$$

通解（Ansatz）：$\psi(x) = A e^{ikx} + B e^{-ikx}$，等价于 $\psi(x) = C\sin(kx) + D\cos(kx)$。

</v-click>

<v-click>

阱外波函数恒为零，边界条件 $\psi(0) = \psi(a) = 0$ 决定了 $D = 0$ 和

$$\sin(k a) = 0 \quad\Longrightarrow\quad k_n = \frac{n\pi}{a}, \qquad n = 1, 2, 3, \ldots$$

</v-click>

<v-click>

归一化后得到完整的束缚态：

$$\boxed{\;\psi_n(x) = \sqrt{\frac{2}{a}}\sin\!\left(\frac{n\pi x}{a}\right), \qquad E_n = \frac{\pi^2 \hbar^2}{2 m a^2}\, n^2\;}$$

能级**离散**，$n$ 是因为边界条件**自然出现**的量子数。

</v-click>

---

# 一维方势阱：波函数与能级

<div class="grid grid-cols-2 gap-4">

<div>

<img src="/images/Screenshot 2023-04-03 at 12.51.24-35724.png" style="max-width: 100%; max-height: 320px; object-fit: contain;" />

**波函数 $\psi_n(x)$**

第 $n$ 个本征态有 $n - 1$ 个节点（除端点外的零点）。

</div>

<div>

<img src="/images/Screenshot 2023-04-03 at 12.59.42-35753.png" style="max-width: 100%; max-height: 320px; object-fit: contain;" />

**能级 $E_n \propto n^2$**

最低能级 $E_1 = \dfrac{\pi^2 \hbar^2}{2 m a^2}$，**不能为零**，称为"零点能"。

</div>

</div>

---

# 零点能与不确定性原理

为什么 $E_{\min} \neq 0$？用不确定性原理直接看出：

$$\Delta x \approx a, \quad \Delta p \geq \frac{\hbar}{2 a}$$

<v-click>

$$E_{\min} \approx \frac{(\Delta p)^2}{2 m} \geq \frac{\hbar^2}{8 m a^2}$$

数量级与精确值 $E_1 = \dfrac{\pi^2\hbar^2}{2 m a^2} \approx \dfrac{10\, \hbar^2}{m a^2}$ 完全一致。

</v-click>

<v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #ff8c00; margin-top: 0.6em;">

**物理直觉**：量子粒子被关在更小的盒子里，动量涨落必然增大，零点能必然增大。

后面我们会看到，**原子的稳定性正是这个机制的胜利**。如果电子掉到原子核上，$\Delta r \to 0$，零点能 $\to \infty$。所以电子不会塌缩到核上，原子是稳定的。

经典物理永远无法解释原子的稳定性，量子力学一行不等式就解释清楚了。

</div>

</v-click>

---

# 预备 ②：有限深方势阱

如果阱壁不是无穷高，而是有限的高度 $V_0$：

$$V(x) = \begin{cases} 0, & 0 \leq x \leq a \\ V_0, & \text{otherwise} \end{cases}$$

<img src="/images/Screenshot 2023-04-03 at 13.18.12-35842.png" style="max-width: 380px; max-height: 220px; margin: 0.4em auto; display: block;" />

<v-click>

**新现象**：阱外波函数不再恒为零，而是以 $e^{-\kappa |x|}$ 指数衰减"渗入"到经典禁区。

这就是后面**隧穿效应**的起源。粒子有非零概率出现在经典上"不可能到达"的地方。

</v-click>

<v-click>

如果 $E > V_0$，粒子完全自由，谱由束缚态变成连续谱。这就是**散射态**。

</v-click>

---

# 预备 ③：二维无限深方势阱（分离变量）

势能在 $x, y$ 方向都是无限深，$0 \leq x \leq a$，$0 \leq y \leq b$。哈密顿量

$$\hat H = -\frac{\hbar^2}{2 m}\!\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right) + V(x, y)$$

<v-click>

**Ansatz**：波函数可分离 $\psi(x, y) = f(x)\, g(y)$。代入定态方程并两边除以 $f g$：

$$\underbrace{-\frac{\hbar^2}{2 m f}\frac{d^2 f}{d x^2}}_{\text{只依赖 } x} + \underbrace{\left(-\frac{\hbar^2}{2 m g}\frac{d^2 g}{d y^2}\right)}_{\text{只依赖 } y} = E$$

</v-click>

<v-click>

左边只依赖 $x$，右边只依赖 $y$，要让等式恒成立，每一项都必须等于一个常数。问题**完美分离**为两个独立的一维问题。

</v-click>

<img src="/images/Screen Shot 2022-03-28 at 18.58.46-30733.png" style="max-width: 380px; max-height: 200px; margin: 0.4em auto; display: block;" />

---

# 二维方势阱：解与简并

把每个一维问题各自求解后，整体波函数是两个一维波函数的乘积：

$$\boxed{\;\psi_{n_x, n_y}(x, y) = \frac{2}{\sqrt{a b}}\sin\!\left(\frac{n_x \pi x}{a}\right)\sin\!\left(\frac{n_y \pi y}{b}\right)\;}$$

$$E_{n_x, n_y} = \frac{\pi^2 \hbar^2}{2 m}\!\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2}\right)$$

<v-click>

**特殊情形 $a = b$**：方形阱有**简并能级**。例如 $E_{1,2} = E_{2,1} = \dfrac{5\pi^2\hbar^2}{2 m a^2}$，两个独立波函数对应同一能级。

简并的物理来源：方形阱有 $C_4$ 旋转对称性。一旦 $a \neq b$，简并立刻被打破。这是后面氢原子简并度讨论的预演。

</v-click>

<img src="/images/Screenshot 2023-04-03 at 13.46.16-35904.png" style="max-width: 380px; max-height: 200px; margin: 0.4em auto; display: block;" />

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**关键教训**：当势能在某种坐标系下"分离"时，问题就化成几个独立的一维问题。**氢原子的库仑势在直角坐标下不分离，但在球坐标下完美分离**，这是下面所有工作的出发点。

</div>

</v-click>

---

# 经典 vs 量子角动量

**经典角动量**：$\vec L = \vec r \times \vec p$，是一个普通的连续矢量。

**量子角动量**：把动量替换为算符 $\hat p = -i\hbar\nabla$，得到三个角动量分量算符：

$$\hat L_x = -i\hbar\!\left(y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y}\right)$$

$$\hat L_y = -i\hbar\!\left(z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z}\right)$$

$$\hat L_z = -i\hbar\!\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right)$$

<v-click>

这些都是直角坐标下的形式。但是氢原子势能是中心势 $U(r)$，**直角坐标下不可分离**。我们必须把角动量算符改写到球坐标系。

</v-click>

---

# 直角坐标 ↔ 球坐标

<div class="grid grid-cols-2 gap-4">

<img src="/images/3D_Cartesian.svg-31297.png" style="max-width: 100%; max-height: 240px; object-fit: contain;" />

<img src="/images/480px-3D_Spherical.svg-26376.png" style="max-width: 100%; max-height: 240px; object-fit: contain;" />

</div>

$$x = r\sin\theta\cos\varphi, \quad y = r\sin\theta\sin\varphi, \quad z = r\cos\theta$$

逆变换：
$$r = \sqrt{x^2 + y^2 + z^2}, \quad \cos\theta = \frac{z}{r}, \quad \tan\varphi = \frac{y}{x}$$

<v-click>

要把算符 $\hat L_x, \hat L_y, \hat L_z$ 和 $\nabla^2$ 改写到球坐标，必须用**链式法则**求出偏导数 $\dfrac{\partial}{\partial x}, \dfrac{\partial}{\partial y}, \dfrac{\partial}{\partial z}$ 在 $(r, \theta, \varphi)$ 下的形式。

</v-click>

---

# 球坐标下的偏导（链式法则）

以 $\dfrac{\partial}{\partial y}$ 为例：

$$\frac{\partial}{\partial y} = \frac{\partial r}{\partial y}\frac{\partial}{\partial r} + \frac{\partial \theta}{\partial y}\frac{\partial}{\partial \theta} + \frac{\partial \varphi}{\partial y}\frac{\partial}{\partial \varphi}$$

<v-click>

由 $r^2 = x^2 + y^2 + z^2$ 求导得 $\dfrac{\partial r}{\partial y} = \dfrac{y}{r} = \sin\theta\sin\varphi$。

由 $\cos\theta = z/r$ 求导得 $-\sin\theta\, \dfrac{\partial \theta}{\partial y} = -\dfrac{z y}{r^3}$，即 $\dfrac{\partial \theta}{\partial y} = \dfrac{\cos\theta\sin\varphi}{r}$。

由 $\tan\varphi = y/x$ 求导得 $\dfrac{\partial \varphi}{\partial y} = \dfrac{\cos\varphi}{r\sin\theta}$。

</v-click>

<v-click>

合起来：

$$\frac{\partial}{\partial y} = \sin\theta\sin\varphi\, \frac{\partial}{\partial r} + \frac{\cos\theta\sin\varphi}{r}\frac{\partial}{\partial \theta} + \frac{\cos\varphi}{r\sin\theta}\frac{\partial}{\partial \varphi}$$

$\dfrac{\partial}{\partial x}$ 和 $\dfrac{\partial}{\partial z}$ 同理。剩下的就是机械的代数运算，把这些代回 $\hat L_i$ 的直角坐标表达式。

</v-click>

---

# 球坐标下的角动量算符

经过冗长但直接的代数运算，结果出乎意料地简洁：

$$\hat L_x = i\hbar\!\left(\sin\varphi\, \frac{\partial}{\partial \theta} + \cot\theta\cos\varphi\, \frac{\partial}{\partial \varphi}\right)$$

$$\hat L_y = i\hbar\!\left(-\cos\varphi\, \frac{\partial}{\partial \theta} + \cot\theta\sin\varphi\, \frac{\partial}{\partial \varphi}\right)$$

$$\boxed{\;\hat L_z = -i\hbar\, \frac{\partial}{\partial \varphi}\;}$$

<v-click>

**关键观察**：$\hat L_z$ 只依赖于 $\varphi$！这意味着 $\varphi$ 方向的"绕 $z$ 轴旋转"对应 $\hat L_z$ 的本征态。$\hat L_z$ 的本征函数必然形如 $e^{im\varphi}$，因为这是 $-i\partial_\varphi$ 的本征函数。

这就是**磁量子数 $m$ 的几何起源**。

</v-click>

---

# 角动量平方算符与球坐标拉普拉斯

把三个分量平方相加：

$$\hat L^2 \;=\; \hat L_x^2 + \hat L_y^2 + \hat L_z^2 \;=\; -\hbar^2\!\left[\frac{1}{\sin\theta}\frac{\partial}{\partial \theta}\!\left(\sin\theta\, \frac{\partial}{\partial \theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial \varphi^2}\right]$$

<v-click>

球坐标下的拉普拉斯算符可以分成"径向部分 + 角向部分"：

$$\boxed{\;\nabla^2 \;=\; \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial}{\partial r}\right) - \frac{1}{\hbar^2 r^2}\hat L^2\;}$$

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**这是最关键的一步**。拉普拉斯算符的角向部分**正好就是** $\hat L^2/(\hbar^2 r^2)$。这意味着求解中心势薛定谔方程，自然就要解 $\hat L^2$ 的本征值问题。

**角动量量子化是几何的必然结果**。

</div>

</v-click>

---

# 中心势：分离变量

代入定态方程：

$$-\frac{\hbar^2}{2 m_e}\!\left[\frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial \psi}{\partial r}\right) - \frac{1}{\hbar^2 r^2}\hat L^2 \psi\right] + U(r)\, \psi \;=\; E\, \psi$$

<v-click>

**Ansatz**：$\psi(r, \theta, \varphi) = R(r)\, Y(\theta, \varphi)$。代入并两边乘 $\dfrac{2 m_e r^2}{\hbar^2 R Y}$：

$$\underbrace{\frac{1}{R}\frac{d}{d r}\!\left(r^2 \frac{d R}{d r}\right) - \frac{2 m_e r^2}{\hbar^2}\!\left[U(r) - E\right]}_{\text{只依赖 } r} \;=\; \underbrace{\frac{1}{Y}\!\left[\frac{1}{\hbar^2}\hat L^2 Y\right]}_{\text{只依赖 } \theta, \varphi}$$

</v-click>

<v-click>

左边只依赖 $r$，右边只依赖 $\theta, \varphi$，必须等于同一常数 $\lambda$。**中心势的薛定谔方程精确分离**为角向方程和径向方程：

$$\hat L^2 Y(\theta, \varphi) = \lambda \hbar^2\, Y(\theta, \varphi)$$

$$\frac{1}{r^2}\frac{d}{d r}\!\left(r^2 \frac{d R}{d r}\right) + \frac{2 m_e}{\hbar^2}\!\left[E - U(r) - \frac{\lambda \hbar^2}{2 m_e r^2}\right] R = 0$$

</v-click>

---

# 角向方程：球谐函数 $Y_\ell^m$

$\hat L^2$ 的本征值问题

$$\hat L^2\, Y(\theta, \varphi) = \lambda \hbar^2\, Y(\theta, \varphi)$$

是数学物理方法中的标准问题。它的解称为**球谐函数**：

$$Y_\ell^m(\theta, \varphi) = (-1)^m\sqrt{\frac{(2\ell+1)(\ell-m)!}{4\pi(\ell+m)!}}\, e^{im\varphi}\, P_\ell^{m}(\cos\theta)$$

其中 $P_\ell^{m}$ 是连带勒让德多项式。

<v-click>

本征值的取值由 $Y$ 在 $\theta, \varphi$ 上必须**单值连续有限**这个物理条件决定：

$$\boxed{\;\hat L^2\, Y_\ell^m = \ell(\ell+1)\hbar^2\, Y_\ell^m, \quad \hat L_z\, Y_\ell^m = m\hbar\, Y_\ell^m\;}$$

</v-click>

<v-click>

其中：

- $\ell = 0, 1, 2, \ldots$ 是**角动量量子数**（$|\vec L| = \sqrt{\ell(\ell+1)}\hbar$）
- $m = -\ell, -\ell+1, \ldots, \ell$ 是**磁量子数**（$L_z = m\hbar$）

对每个 $\ell$，有 $2\ell + 1$ 个独立的 $m$ 值。这个 "$2\ell+1$" 后面会在 §22 塞曼效应里再次出现。

</v-click>

---

# 量子化的物理根源

数物课上你们从微分方程出发解出了球谐函数。现在换一个角度：**为什么必须量子化？**

<img src="/images/standing-waves-1d-2d-3d.svg" style="max-width: 82%; max-height: 155px; margin: 0 auto; display: block;" />

<v-click>

**$m$ 量子化**：$\varphi$ 方向是环，$\psi(\varphi + 2\pi) = \psi(\varphi)$ → $m$ 必须是整数。

</v-click>

<v-click>

**$\ell$ 量子化**：$\theta$ 方向的 Legendre 方程，幂级数解 $y = \sum a_k x^k$（$x = \cos\theta$）的递推关系为

$$a_{k+2} = a_k \cdot \frac{k(k+1) - \ell(\ell+1)}{(k+1)(k+2)}$$

不截断则两极发散。截断要求分子为零：$k = \ell$ → $\ell$ 必须是非负整数。

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 8px; padding: 0.15em 0.8em; border-left: 3px solid #C71585; font-size: 0.85em;">

谐振子同理：Hermite 不截断则发散，截断给出 $n=0,1,2,\ldots$。**有限性 → 分子为零 → 量子数取整数。**

</div>

</v-click>

---

# 用节线理解球谐函数

球谐函数 $Y_\ell^m(\theta, \varphi)$ 可以用**节线**（波函数为零的线）来直观理解：

<div class="grid grid-cols-2 gap-6">

<div>

**节线的规则**

- $\ell$ = 节线总数
- $|m|$ = 经线方向的节线数（过两极）
- $\ell - |m|$ = 纬线方向的节线数

<v-click>

| $\ell$ | $m$ | 经线节线 | 纬线节线 | 轨道名 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | $s$ |
| 1 | 0 | 0 | 1 | $p_z$ |
| 1 | $\pm 1$ | 1 | 0 | $p_\pm$ |

</v-click>

</div>

<div>

**节线越多，角动量越大**

节线多 → 角向"波长"短 → 角动量大。$\ell$ 大的态对应更高的角动量，和鼓面振动模式的逻辑一样：模式越复杂，频率越高。

<v-click>

**实验验证**：Stern-Gerlach 实验中，原子束分裂成恰好 $2\ell+1$ 个离散点，而非连续条纹。这个数字直接来自 $m = -\ell, \ldots, \ell$ 的取值个数。

</v-click>

</div>

</div>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 8px; padding: 0.2em 0.8em; border-left: 3px solid #C71585; margin-top: 0.1em; font-size: 0.88em;">

**思考题**：为什么 $|\vec L| = \sqrt{\ell(\ell+1)}\hbar$ 而不是 $\ell\hbar$？提示：如果 $|\vec L|=\ell\hbar$，当 $m=\ell$ 时角动量完全沿 $z$ 轴，$L_x=L_y=0$，这和测不准关系矛盾。

</div>

</v-click>

---

# 角动量量子化：经典 vs 量子

| | **经典力学** | **量子力学** |
|---|---|---|
| $\|\vec L\|$ 取值 | 任意连续值 | $\sqrt{\ell(\ell+1)}\, \hbar$，$\ell = 0, 1, 2, \ldots$ |
| $L_z$ 取值 | 任意连续 | $m\hbar$，$m = -\ell, \ldots, \ell$ |
| 同时确定 $L_x, L_y, L_z$ | 可以 | **不可以**！$\hat L_i$ 之间不对易 |
| 几何图像 | 一个矢量 | 一个"圆锥"，$L_z$ 确定，$L_x, L_y$ 不确定 |

<v-click>

**对易关系**：

$$[\hat L_x, \hat L_y] = i\hbar\, \hat L_z, \quad [\hat L_y, \hat L_z] = i\hbar\, \hat L_x, \quad [\hat L_z, \hat L_x] = i\hbar\, \hat L_y$$

但 $[\hat L^2, \hat L_z] = 0$，所以 $\hat L^2$ 和 $\hat L_z$ 可以同时对角化。这就是为什么 $Y_\ell^m$ 同时是这两个算符的本征函数。

</v-click>

<v-click>

**测不准关系**：$\Delta L_x \Delta L_y \geq \dfrac{\hbar}{2}|\langle \hat L_z\rangle|$。当 $L_z$ 确定时，$L_x, L_y$ 必然有不确定性，这就是"圆锥"图像的物理来源。

</v-click>

<v-click>

</v-click>

---

# 球谐函数：低阶公式表

| $\ell$ | $m$ | $Y_\ell^m(\theta, \varphi)$ | 名称 |
|---|---|---|---|
| 0 | 0 | $\dfrac{1}{2\sqrt\pi}$ | $s$ |
| 1 | 0 | $\dfrac{1}{2}\sqrt{\dfrac{3}{\pi}}\cos\theta$ | $p_z$ |
| 1 | $\pm 1$ | $\mp\dfrac{1}{2}\sqrt{\dfrac{3}{2\pi}}\sin\theta\, e^{\pm i\varphi}$ | $p_\pm$ |
| 2 | 0 | $\dfrac{1}{4}\sqrt{\dfrac{5}{\pi}}(3\cos^2\theta - 1)$ | $d_{z^2}$ |
| 2 | $\pm 1$ | $\mp\dfrac{1}{2}\sqrt{\dfrac{15}{2\pi}}\sin\theta\cos\theta\, e^{\pm i\varphi}$ | $d_{xz, yz}$ |
| 2 | $\pm 2$ | $\dfrac{1}{4}\sqrt{\dfrac{15}{2\pi}}\sin^2\theta\, e^{\pm 2 i\varphi}$ | $d_{x^2-y^2, xy}$ |

<v-click>

化学家用的 $s, p, d, f$ 标记就是 $\ell = 0, 1, 2, 3$ 的另一种叫法，来自 19 世纪光谱学家的经验术语 sharp, principal, diffuse, fundamental。

</v-click>

---

# 球谐函数：交互式 3D 可视化

<div style="text-align: center; margin-top: 1em;">

<img src="/images/Screen Shot 2022-04-06 at 22.34.28-32655.png" style="max-width: 550px; max-height: 300px; margin: 0 auto; display: block;" />

</div>

<v-click>

<div style="text-align: center; margin-top: 1em;">

<a href="/AI-workshop/spherical-harmonics.html" target="_blank" style="display: inline-block; padding: 12px 32px; background: rgba(199,21,133,0.2); border: 2px solid #C71585; border-radius: 8px; color: #C71585; font-size: 1.2em; text-decoration: none; font-weight: bold; transition: all 0.2s;">
打开交互式演示 →
</a>

</div>

调整 $\ell$ 和 $m$，实时观察球谐函数的3D形状变化。支持拖拽旋转，两种可视化模式（变形球面/球面着色）。

</v-click>

<v-click>

**两种可视化方法**：
- **变形球面**：半径 $r \propto |Y_\ell^m|$，得到"花瓣形"，直观看节线
- **球面着色**：固定球面上画颜色分布，品红色为正，蓝色为负

</v-click>

---

# 量子角动量：一个微妙的事实

$\hat L^2$ 作用在 $\psi = R(r) Y_\ell^m$ 上：

$$\hat L^2 \psi = R(r)\, \hat L^2 Y_\ell^m = R(r)\cdot \ell(\ell+1)\hbar^2\, Y_\ell^m = \ell(\ell+1)\hbar^2\, \psi$$

所以 $\psi$ 是 $\hat L^2$ 的本征态，本征值 $\ell(\ell+1)\hbar^2$。

<v-click>

但是 $\hat L_x \psi \neq$ 某个常数 $\times \psi$！换句话说，$\psi$ **不是 $\hat L_x$ 的本征态**。这是量子力学的"反直觉"之处。

由 $\hat L^2 = \hat L_x^2 + \hat L_y^2 + \hat L_z^2$ 我们可以算出：

$$\langle \hat L_x^2 + \hat L_y^2 \rangle = \ell(\ell+1)\hbar^2 - m^2\hbar^2$$

但 $\langle \hat L_x \rangle = \langle \hat L_y \rangle = 0$，因为对 $\varphi$ 积分时正负相消。

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**几何图像**：在 $\hat L^2, \hat L_z$ 同时确定的态上，角动量矢量长度为 $\sqrt{\ell(\ell+1)}\hbar$，$z$ 投影是 $m\hbar$，但 $L_x, L_y$ 在 $xy$ 平面上随机取向。这就是熟悉的"圆锥"图像。

</div>

</v-click>

---

# 径向方程：离心势垒

把角向部分的本征值 $\lambda = \ell(\ell+1)$ 代回，径向方程为

$$-\frac{\hbar^2}{2 m_e}\frac{1}{r^2}\frac{d}{dr}\!\left(r^2 \frac{d R}{dr}\right) + \!\left[U(r) + \frac{\ell(\ell+1)\hbar^2}{2 m_e r^2}\right] R = E\, R$$

<v-click>

引入 $u(r) = r R(r)$，方程化简为一维形式：

$$-\frac{\hbar^2}{2 m_e}\frac{d^2 u}{dr^2} + V_\text{eff}(r)\, u = E\, u$$

其中**有效势能**

$$V_\text{eff}(r) = U(r) + \frac{\ell(\ell+1)\hbar^2}{2 m_e r^2}$$

后一项是**离心势垒**（centrifugal barrier），来源于角动量不为零时电子无法落到原点。

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**这就是把 3D 中心势问题化成 1D 方程的关键技巧**：径向问题等价于"在有效势 $V_\text{eff}$ 中运动的一维粒子"。

</div>

</v-click>

---

# 玻尔半径与里德伯能量自然出现

代入库仑势 $U(r) = -\dfrac{1}{4\pi\epsilon_0}\dfrac{e^2}{r}$，引入无量纲变量 $\rho = r/a_0$ 和 $\lambda = \sqrt{-E/E_0}$，方程变为：

$$\frac{d^2 u}{d\rho^2} + \!\left[\frac{2}{\rho} - \frac{\ell(\ell+1)}{\rho^2} - \lambda^2\right] u = 0$$

<v-click>

为了让方程无量纲化，**长度尺度**和**能量尺度**自动出现：

$$\boxed{\;a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_e e^2} = 0.529\ \mathrm{\AA}\;}$$

$$\boxed{\;E_0 = \frac{m_e e^4}{2 (4\pi\epsilon_0)^2 \hbar^2} = 13.6\ \mathrm{eV}\;}$$

</v-click>

<v-click>

这就是**玻尔半径**和**里德伯能量**！但**没有用任何"量子化假设"**，它们是从薛定谔方程的求解中自然涌现的物理尺度。

玻尔在 1913 年是"猜出"这两个常数的，薛定谔在 1926 年是"算出"这两个常数的。这是质的飞跃。

</v-click>

---

# 求解径向方程：又是级数截断

求解思路和角动量完全一样：渐近分析 → 代换 → 幂级数 → 截断。

**渐近行为**：$\rho \to \infty$ 时 $u'' = \lambda^2 u$，束缚态解 $u \to e^{-\lambda\rho}$。$\rho \to 0$ 时离心势垒主导，$u \sim \rho^{\ell+1}$。

<v-click>

**Ansatz**：$u(\rho) = e^{-\lambda\rho}\, \rho^{\ell+1} \sum_{q=0}^\infty c_q\, \rho^q$，代入比较系数得递推关系：

$$\frac{c_q}{c_{q-1}} = \frac{2[\lambda(q + \ell) - 1]}{q(q + 2\ell + 1)}$$

</v-click>

<v-click>

和 Legendre 方程一样的故事：**级数不截断则发散**。截断条件是分子为零：

$$\lambda(j + \ell) = 1 \quad\Longrightarrow\quad \lambda = \frac{1}{n}, \quad n \equiv j + \ell = 1, 2, 3, \ldots$$

</v-click>

<v-click>

由 $\lambda = \sqrt{-E/E_0}$ 立即得到

$$\boxed{\;E_n = -\frac{E_0}{n^2} = -\frac{13.6\ \mathrm{eV}}{n^2}, \qquad n = 1, 2, 3, \ldots\;}$$

</v-click>

<v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 8px; padding: 0.3em 0.8em; border-left: 3px solid #ff8c00; font-size: 0.88em;">

角动量：有限性 → $k(k+1)=\ell(\ell+1)$ → $\ell$ 取整数。径向：可归一 → $\lambda(j+\ell)=1$ → $n$ 取整数。**同一个数学机制，两次量子化。**

</div>

</v-click>

---

# 简并度：$n^2$

由 $n = j + \ell$，对于固定的 $n$：

- $\ell$ 可以取 $0, 1, 2, \ldots, n-1$（共 $n$ 个值）
- 每个 $\ell$ 又有 $2\ell + 1$ 个 $m$ 值

总状态数：

$$\sum_{\ell=0}^{n-1}(2\ell + 1) = n^2$$

<v-click>

**例**：

- $n = 1$：$1^2 = 1$ 态（基态 $1s$）
- $n = 2$：$2^2 = 4$ 态（$2s + 2p_x + 2p_y + 2p_z$）
- $n = 3$：$3^2 = 9$ 态（$3s + 3p \times 3 + 3d \times 5$）

</v-click>

<v-click>

**为什么简并？** 能级 $E_n$ 只依赖 $n = j + \ell$。这是库仑势 $1/r$ 的"额外对称性"（实际上是 SO(4) 对称性，由 Runge-Lenz 矢量守恒带来），不是普通的转动对称。

**任何偏离 $1/r$ 的修正都会破坏这个简并**。比如多电子原子里电子-电子相互作用让 $2s$ 和 $2p$ 不再简并，这是周期表填充顺序复杂的原因。

</v-click>

---

# 完整波函数与三个量子数

$$\boxed{\;\psi_{n\ell m}(r, \theta, \varphi) = R_{n\ell}(r)\, Y_\ell^m(\theta, \varphi)\;}$$

| 量子数 | 取值 | 决定什么 |
|---|---|---|
| $n$（主） | $1, 2, 3, \ldots$ | 能量 $E_n = -E_0/n^2$，平均距离 $\langle r \rangle \sim n^2 a_0$ |
| $\ell$（角） | $0, 1, \ldots, n-1$ | $|\vec L| = \sqrt{\ell(\ell+1)}\hbar$，轨道"形状"（$s,p,d,f$） |
| $m$（磁） | $-\ell, \ldots, \ell$ | $L_z = m\hbar$，轨道在空间中的"取向" |

<v-click>

径向部分 $R_{n\ell}(r)$ 是 Laguerre 多项式乘指数衰减。前几个：

$$R_{10} = \frac{2}{a_0^{3/2}} e^{-r/a_0}, \quad R_{20} = \frac{1}{2\sqrt 2\, a_0^{3/2}}\!\left(2 - \frac{r}{a_0}\right) e^{-r/(2a_0)}, \quad R_{21} = \frac{1}{2\sqrt 6\, a_0^{3/2}} \frac{r}{a_0} e^{-r/(2a_0)}$$

</v-click>

<v-click>

<img src="/images/CNX_UPhysics_41_01_EOrbitals-1-27608.jpg" style="max-width: 500px; max-height: 200px; margin: 0.3em auto; display: block;" />

</v-click>

---

# 径向波函数与概率密度

<div class="grid grid-cols-2 gap-2">

<div>

**径向波函数 $R_{n\ell}(r)$**

<img src="/images/Screen Shot 2023-04-10 at 20.27.27-36168.png" style="max-width: 100%; max-height: 240px; object-fit: contain;" />

节点数 $= n - \ell - 1$

</div>

<div>

**径向概率密度 $r^2 |R_{n\ell}|^2$**

<img src="/images/Screen Shot 2023-04-10 at 20.31.01-36187.png" style="max-width: 100%; max-height: 240px; object-fit: contain;" />

峰值位置 $\sim n^2 a_0$

</div>

</div>

<v-click>

**为什么是 $r^2 |R|^2$ 而不是 $|R|^2$**？因为概率元素 $dV = r^2 \sin\theta\, dr\, d\theta\, d\varphi$，球壳体积随 $r^2$ 增长。所以"在 $r$ 附近找到电子的概率"是

$$P(r)\, dr = r^2 |R(r)|^2\, dr\int |Y|^2 d\Omega = r^2 |R(r)|^2\, dr$$

</v-click>

---

# 氢原子轨道可视化

<img src="/images/Screen Shot 2023-04-10 at 20.41.04-36228.png" style="max-width: 650px; max-height: 320px; margin: 0 auto; display: block;" />

<v-click>

每个 $(n, \ell, m)$ 对应一种电子云形状。化学的**周期表**就是这些轨道按能量顺序填充的结果。

<div style="text-align: center; margin-top: 0.5em;">
<a href="/AI-workshop/spherical-harmonics.html" target="_blank" style="display: inline-block; padding: 8px 24px; background: rgba(199,21,133,0.15); border: 1.5px solid #C71585; border-radius: 6px; color: #C71585; font-size: 1em; text-decoration: none; transition: all 0.2s;">
交互式球谐函数演示 →
</a>
</div>

</v-click>

---

# 平均距离 $\langle r \rangle$ vs 玻尔半径

基态 $1s$ 的概率密度：

$$P(r)\, dr = 4\pi r^2 |R_{10}|^2\, dr = \frac{4 r^2}{a_0^3}\, e^{-2 r/a_0}\, dr$$

<v-click>

**最概然位置**（$P(r)$ 取最大）：求 $\dfrac{dP}{dr} = 0$ 得 $r_{\max} = a_0$，正好是玻尔半径。

</v-click>

<v-click>

**平均距离**（期望值）：

$$\langle r \rangle = \int_0^\infty r\, P(r)\, dr = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2 r/a_0}\, dr = \frac{3}{2}\, a_0$$

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.6em;">

**注意**：$\langle r \rangle = \dfrac{3}{2} a_0 \neq a_0$！

玻尔模型说"电子在半径 $a_0$ 的圆上运行"，薛定谔模型说"电子的概率分布平均距离是 $\dfrac{3}{2} a_0$"。这两个数字不一样，因为玻尔模型是错的，电子不在轨道上。

但巧合的是，最概然位置 $r_\max = a_0$，这是为什么我们至今还在用"玻尔半径"这个名字。

</div>

</v-click>

<img src="/images/Screen Shot 2023-04-10 at 21.03.06-36315.png" style="max-width: 380px; max-height: 200px; margin: 0.4em auto; display: block;" />

---

# 玻尔模型 vs 薛定谔模型：终极对比

| | **玻尔模型（1913）** | **薛定谔模型（1926）** |
|---|---|---|
| 电子状态 | 经典圆轨道 | 复波函数 $\psi_{n\ell m}(\vec r)$ |
| 角动量 $\|\vec L\|$ | $n\hbar$（人为假设） | $\sqrt{\ell(\ell+1)}\hbar$（自然导出） |
| 基态角动量 | $1\hbar \neq 0$（**错**）| $0$（**对**）|
| 能级 $E_n$ | $-E_0/n^2$ | $-E_0/n^2$（一致） |
| 简并度 | 没有概念 | $n^2$（自然出现） |
| 轨道形状 | 圆 | $s, p, d, f, \ldots$ |
| 解释精细结构 | 不能 | 不能（要加自旋，§21） |
| 解释塞曼效应 | 部分（正常） | 全部（含反常，§22） |
| 数学基础 | ad hoc 量子化 | 一个统一的方程 |

<v-click>

**最深刻的胜利**：薛定谔基态角动量是 $0$，玻尔模型说是 $1\hbar$。**实验验证薛定谔是对的**（碰撞实验、磁矩测量、X 射线衍射都证明了 $1s$ 态是球对称的）。

玻尔的"轨道"图像虽然简单好教，但物理上是错的。它的成功是巧合，因为对于圆轨道，能量恰好和 $\ell(\ell+1)\hbar^2/r^2$ 的形式吻合。

</v-click>

---

# §17 思考 1　<span style="color: #C71585; font-size: 0.7em;">概念</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

为什么氢原子的能级 $E_n$ 只依赖于 $n$，与 $\ell$ 和 $m$ 无关？这种简并对所有中心势都成立吗？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**$m$ 简并**：对任何中心势 $U(r)$，能级都不依赖 $m$。这是**球对称性**的直接结果，绕任意轴的旋转是哈密顿量的对称变换，而 $m$ 是 $\hat L_z$ 的本征值，不同 $m$ 互为对称变换。

**$\ell$ 简并**：能级不依赖 $\ell$ 是**库仑势 $1/r$ 的特殊性质**，不是普遍的中心势性质。库仑势比一般中心势"对称性更高"，被称为 SO(4) 对称（除了 SO(3) 空间转动之外，还有一个"Runge-Lenz 矢量"守恒）。

**实验验证**：把库仑势换成屏蔽库仑势（多电子原子），$\ell$ 简并立即消失，$2s$ 和 $2p$ 能级不同。这就是为什么周期表的填充顺序不是简单的 $1s, 2s, 2p, 3s, 3p, 3d$，而是 $1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, \ldots$。

</div>

</v-click>

---

# §17 思考 2　<span style="color: #C71585; font-size: 0.7em;">计算</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

求基态 $1s$ 氢原子电子的最概然位置 $r_\max$，并与 $\langle r \rangle$ 比较。

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

基态径向波函数 $R_{10}(r) = \dfrac{2}{a_0^{3/2}}\, e^{-r/a_0}$，径向概率密度

$$P(r) = 4\pi r^2 |R_{10}|^2 = \frac{4 r^2}{a_0^3}\, e^{-2 r/a_0}$$

求 $\dfrac{dP}{dr} = 0$：

$$\frac{dP}{dr} = \frac{4}{a_0^3}\!\left(2 r e^{-2 r/a_0} - \frac{2 r^2}{a_0} e^{-2 r/a_0}\right) = 0$$

$$2 r - \frac{2 r^2}{a_0} = 0 \quad\Longrightarrow\quad r_\max = a_0$$

**最概然位置正好是玻尔半径**。但平均距离 $\langle r \rangle = \dfrac{3}{2} a_0$，因为概率分布的"尾巴"很长，把均值往大处拉。

</div>

</v-click>

---

# §17 思考 3　<span style="color: #C71585; font-size: 0.7em;">深入</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #30d158; font-size: 0.85em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

为什么基态 $1s$ 的角动量是 $0$？这违反我们对"绕核运动"的直觉。如果电子不绕核转，怎么不掉到核里？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**$\ell = 0$ 的物理含义**：$|\vec L|^2 = \ell(\ell+1)\hbar^2 = 0$，所以角动量为零。这意味着电子的运动**不是绕核的圆周运动**，而是**纯径向**的（甚至连"运动"这个经典概念都不对，应该说波函数是球对称的"概率云"）。

**为什么不掉到核里**？因为零点能。如果电子被压到 $\Delta r \to 0$ 的小区域，由不确定性原理 $\Delta p \sim \hbar/\Delta r \to \infty$，动能 $\sim (\Delta p)^2/(2 m_e) \to \infty$，能量发散。所以电子的"最优配置"是在一个有限大小（约 $a_0$）的区域分布，让动能（涨落带来的）和库仑势能达到最低总和。

**这正是原子稳定性的量子力学解释**：原子之所以存在，不是因为电子在轨道上"不掉下来"，而是因为塌缩到核上需要无穷大的零点能。

经典物理永远无法解释原子的稳定性，量子力学一行公式就解释清楚了。

</div>

</v-click>

---

# §17 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] J. J. Balmer, "Notiz über die Spectrallinien des Wasserstoffs," *Annalen der Physik* **261**, 80 (1885). 巴尔末公式的原始论文。

[2] J. R. Rydberg, "Recherches sur la constitution des spectres d'émission des éléments chimiques," *Kongl. Svenska Vetenskaps-Akademiens Handlingar* **23**, 1 (1890). Rydberg 公式的原始论文。

[3] N. Bohr, "On the constitution of atoms and molecules," *Philosophical Magazine* **26**, 1 (1913). 玻尔模型奠基论文。

[4] E. Schrödinger, "Quantisierung als Eigenwertproblem (Erste Mitteilung)," *Annalen der Physik* **384**, 361 (1926). 薛定谔解出氢原子的经典论文。

[5] W. Pauli, "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik," *Z. Phys.* **36**, 336 (1926). Pauli 用矩阵力学独立解出氢原子（与薛定谔同年）。

[6] D. J. Griffiths & D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., Ch. 4 (Cambridge Univ. Press, 2018). 标准本科教材，氢原子求解。

[7] L. D. Landau & E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory*, 3rd ed., §36 (Pergamon, 1977). 经典严格的氢原子求解。

[8] M. Bander & C. Itzykson, "Group Theory and the Hydrogen Atom (I)," *Rev. Mod. Phys.* **38**, 330 (1966). 氢原子的 SO(4) 对称性。

[9] N. F. Barber et al., *International Centre for Global Earth Models (ICGEM)*, *Earth Syst. Sci. Data* **11**, 647 (2019). 球谐函数在地球重力场中的现代应用。

</div>

---

# §18 原子轨道磁矩

需要掌握的知识点：

（1）解释为什么氢原子具有磁性，磁性的来源是电子的轨道运动

（2）从经典电流回路出发，半经典推导出电子轨道磁矩 $\vec\mu = -\dfrac{e}{2 m_e}\vec L$

（3）理解**玻尔磁子** $\mu_B = \dfrac{e\hbar}{2 m_e} \approx 9.27 \times 10^{-24}$ J/T 的定义和数值

（4）使用量子数 $\ell, m$ 计算氢原子轨道磁偶极矩的大小和 $z$ 投影

（5）为后面 §19 Stern-Gerlach 和 §22 塞曼效应做铺垫

---

# 半经典推导：电子的"电流回路"

把电子想象成在玻尔轨道上做半径为 $r$ 的匀速圆周运动，速度 $v$。这是一个电流回路：

$$I = \frac{e}{T} = \frac{e v}{2\pi r}$$

回路面积 $A = \pi r^2$，磁偶极矩

$$\mu = I A = \frac{e v}{2\pi r}\cdot \pi r^2 = \frac{e v r}{2}$$

<v-click>

用经典角动量 $L = m_e v r$ 改写：

$$\mu = \frac{e v r}{2} = \frac{e}{2 m_e}\cdot m_e v r = \frac{e}{2 m_e}\, L$$

写成矢量（电子带负电，方向相反）：

$$\boxed{\;\vec\mu = -\frac{e}{2 m_e}\vec L\;}$$

</v-click>

<img src="/images/CNX_UPhysics_41_02_AtomicLoop-1-27950.jpg" style="max-width: 360px; max-height: 220px; margin: 0.4em auto; display: block;" />

---

# 玻尔磁子 $\mu_B$

把量子化的角动量 $|\vec L| = \sqrt{\ell(\ell+1)}\, \hbar$ 代入：

$$|\vec\mu| = \frac{e}{2 m_e}\sqrt{\ell(\ell+1)}\, \hbar = \mu_B\sqrt{\ell(\ell+1)}$$

$z$ 投影 $L_z = m\hbar$ 给出

$$\mu_z = -\frac{e}{2 m_e}\cdot m\hbar = -m\, \mu_B$$

<v-click>

定义**玻尔磁子**：

$$\boxed{\;\mu_B \equiv \frac{e\hbar}{2 m_e} = 9.274 \times 10^{-24}\ \mathrm{J/T} = 5.788\times 10^{-5}\ \mathrm{eV/T}\;}$$

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**$\mu_B$ 是原子磁性的"自然单位"**。所有原子的磁矩都用 $\mu_B$ 表示。

注意：$\mu_B$ 是用**经典电流回路 + 量子化角动量**（半经典）推导出来的。后面会发现电子自旋的磁矩是 $g_s\, \mu_B \approx 2\, \mu_B$，这个 $g_s \approx 2$ 是经典物理永远无法解释的，**只有相对论量子力学（Dirac 1928）才能给出**。

</div>

</v-click>

---

# 半经典 vs 严格量子结果的对照

注意：上面的"$\vec\mu = -\dfrac{e}{2 m_e}\vec L$"是用**经典电流回路**推出来的。它对吗？

<v-click>

**严格量子力学**：把磁矩算符定义为

$$\hat{\vec\mu} = -\frac{e}{2 m_e}\hat{\vec L}$$

（这是把经典关系**直接量子化**，不再用电流回路图像）。

</v-click>

<v-click>

然后计算磁矩在外磁场中的能量：

$$\hat H_\text{磁} = -\hat{\vec\mu}\cdot \vec B = \frac{e}{2 m_e}\hat{\vec L}\cdot \vec B$$

如果 $\vec B = B\hat z$，能量本征值

$$\Delta E = m\, \mu_B B$$

其中 $m = -\ell, \ldots, \ell$。这是 $2\ell+1$ 个等间距的能级，正是后面 §22 **正常塞曼效应**的来源。

</v-click>

<v-click>

**结论**：半经典推导给出的 $\vec\mu = -\dfrac{e}{2 m_e}\vec L$ 在量子力学框架下**仍然成立**，只是 $\vec L$ 现在是算符。$\mu_B$ 是同一个 $\mu_B$。

</v-click>

---

# 习题：氢原子各态的磁矩

**问**：氢原子分别处于 $s, p, d$ 态时，磁矩 $|\vec\mu|$ 的大小和 $\mu_z$ 的可能取值是多少？

<v-click>

**$s$ 态**（$\ell = 0$）：

$$|\vec\mu| = 0, \qquad \mu_z = 0$$

s 态没有轨道磁矩。这是基态 $1s$ 的特征。

</v-click>

<v-click>

**$p$ 态**（$\ell = 1$）：

$$|\vec\mu| = \mu_B \sqrt{1\cdot 2} = \sqrt{2}\, \mu_B$$

$$\mu_z = -m\, \mu_B,\quad m = -1, 0, 1 \;\Longrightarrow\; \mu_z \in \{-\mu_B,\, 0,\, +\mu_B\}$$

3 个可能取向。

</v-click>

<v-click>

**$d$ 态**（$\ell = 2$）：

$$|\vec\mu| = \mu_B\sqrt{2\cdot 3} = \sqrt{6}\, \mu_B$$

$$\mu_z = -m\, \mu_B,\quad m = -2,-1, 0, 1, 2 \;\Longrightarrow\; \mu_z \in \{-2\mu_B, -\mu_B, 0, +\mu_B, +2\mu_B\}$$

5 个可能取向。

</v-click>

<v-click>

**规律**：$\ell$ 态有 $2\ell + 1$ 个 $\mu_z$ 取值。这正是 §19 Stern-Gerlach 实验要测量的"空间量子化"。

</v-click>

---

# §18 思考 1　<span style="color: #C71585; font-size: 0.7em;">概念</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

§17 已经讲过基态 $1s$ 的角动量是 $0$，所以基态磁矩也是 $0$。但氢气是有顺磁性的，这怎么解释？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**两个层次的回答**：

**（1）轨道磁矩为零**：基态 $1s$ 的 $\ell = 0$，确实没有轨道磁矩。这一点 $1s$ 与 $2s, 3s, \ldots$ 一样。

**（2）但电子还有自旋磁矩**：基态电子虽然没有轨道角动量，但它有**自旋角动量** $S = \dfrac{1}{2}\hbar$ 和自旋磁矩 $\mu_s \approx \mu_B$。这就是基态氢原子顺磁性的来源。

**（3）实验验证**：1922 年 Stern 和 Gerlach 用银原子做实验，银原子基态也是 $\ell = 0$（电子组态 $[Kr]\, 4d^{10}\, 5s^1$，最外层是 $5s$）。按"只有轨道磁矩"的预期，银原子应该不偏转。但实验上看到了**两束**对称分裂！这就是后面 §19 和 §20 的故事。

**这个矛盾正是发现电子自旋的契机**。

</div>

</v-click>

---

# §18 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] N. Bohr, "On the constitution of atoms and molecules," *Philosophical Magazine* **26**, 1 (1913). 玻尔模型的原始论文，电子轨道概念的来源。

[2] A. Sommerfeld, *Atombau und Spektrallinien* (Vieweg, Braunschweig, 1919). 第一本系统讲解原子结构的教科书，玻尔磁子在此被命名。

[3] D. J. Griffiths & D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., §4.4 (Cambridge Univ. Press, 2018). 半经典磁矩推导。

[4] B. H. Bransden & C. J. Joachain, *Physics of Atoms and Molecules*, 2nd ed., Ch. 1 (Pearson, 2003). 原子物理的标准教材，磁矩推导和实验验证。

[5] P. F. Bernath, *Spectra of Atoms and Molecules*, 4th ed. (Oxford Univ. Press, 2020). 现代光谱学教材，磁矩与塞曼效应的实验。

</div>

---

# §19 Stern / Gerlach 实验

需要掌握的知识点：

（1）理解 1922 年 Stern 和 Gerlach 的实验设计：用非均匀磁场探测原子磁矩在空间的取向

（2）掌握"空间量子化"的物理含义：原子磁矩 $\mu_z$ 只能取离散值

（3）理解实验结果（**银原子分裂为 2 束**）与当时理论预期（$2\ell+1$ 束，应为奇数）的根本矛盾

（4）认识到这个"矛盾"是后面 §20 发现电子自旋的关键

（5）明白为什么 Stern-Gerlach 被誉为"被误解的史上最重要实验"

---

# 1922 年法兰克福：实验背景

20 世纪初，物理学家面对一个奇怪的问题：原子里的电子按玻尔模型有"轨道"，那磁矩应该沿空间任意方向取向。但 Sommerfeld 1916 年提出"空间量子化"假设，磁矩只能取**离散**的方向。

<v-click>

这两个图像哪个对？需要直接的实验。

</v-click>

<v-click>

1921 年 Otto Stern（法兰克福大学）设计了实验：让一束原子穿过非均匀磁场，看磁矩如何分布。

如果**经典图像对**：原子束应该被磁场"涂抹"成一片连续的带（任意取向连续分布）。

如果**空间量子化对**：原子束应该被分裂为离散的几束。

</v-click>

<v-click>

1922 年 Walther Gerlach 加入实验，两人合作完成了这个里程碑实验。**1943 年 Stern 因此获诺贝尔物理学奖**（Gerlach 因为后来在二战中加入纳粹原子能项目而被排除在外）。

</v-click>

---

# 原子在非均匀磁场中的受力

均匀磁场只对磁矩产生**力矩** $\vec\tau = \vec\mu\times \vec B$，让磁矩进动，但**没有平移力**。

<v-click>

非均匀磁场则不同。势能

$$U = -\vec\mu\cdot \vec B = -\mu_z B_z(z)$$

（假设磁场沿 $z$ 方向且 $B_z$ 随 $z$ 变化）

</v-click>

<v-click>

合力

$$F_z = -\frac{\partial U}{\partial z} = \mu_z\, \frac{\partial B_z}{\partial z}$$

**受力大小直接正比于 $\mu_z$**！原子被磁场"踢"的距离揭示出它的 $\mu_z$ 是多少。

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**实验设计的精髓**：把"原子内部的微观磁矩取向"转化为"宏观可测量的偏转距离"。这是 20 世纪原子物理实验的一个范式。

</div>

</v-click>

---

# 实验装置

<div class="grid grid-cols-2 gap-4">

<div>

<video controls style="width: 100%; max-height: 300px;">
  <source src="/images/spin-28555.mp4" />
</video>

</div>

<div>

**装置要素**：

1. **银原子炉**：把银加热到 ~1000°C，蒸气从小孔喷出
2. **准直缝**：让原子束沿单一方向飞行
3. **非均匀磁场**：一对特制磁极（一个尖楔形，一个槽形），$\partial B_z/\partial z$ 很大
4. **探测板**：玻璃板，原子撞击后留下痕迹

</div>

</div>

<v-click>

**为什么用银**？银的基态电子组态是 $[Kr]\, 4d^{10}\, 5s^1$，最外层一个 $5s$ 电子。$5s$ 是 $\ell = 0$，所以**没有轨道磁矩**。如果"只有轨道磁矩"的图像对，银原子应该完全不偏转。

</v-click>

<v-click>

**著名的"硫熏出银"段子**：原子撞到玻璃板上，痕迹太淡看不见。Stern 在烟酒店买廉价雪茄烟（含硫）抽烟，呼出的硫烟与板上的银反应生成黑色硫化银，**银轨迹突然清晰可见**。这是 20 世纪物理史上最有名的"实验事故救场"之一。

</v-click>

---

# 实验结果与经典预期的对比

**经典预期**（连续 $\mu_z$）：原子束在板上形成一个连续的带状图像。

**Sommerfeld 量子化预期**（$\ell$ 整数）：

$$\text{条数} = 2\ell + 1 \;=\; \begin{cases} 1, & \ell = 0 \\ 3, & \ell = 1 \\ 5, & \ell = 2 \\ \ldots & \end{cases}$$

**永远是奇数**。对于 $\ell = 0$ 的银原子，应该是 1 条（即不分裂）。

<v-click>

**实际结果**：

<img src="/images/showOpenGraphArticleImage-28714.gif" style="max-width: 480px; max-height: 240px; margin: 0.5em auto; display: block;" />

银原子束**分裂为完全对称的 2 条**！

</v-click>

<v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #ff8c00; margin-top: 0.5em;">

**这是一个三重危机**：

1. 不是 1 条（基态 $\ell=0$ 的预期）
2. 不是连续带（经典预期）
3. **是 2 条**，这违反了 $2\ell+1$ 总是奇数的规则！

物理上似乎需要一个"半整数 $\ell$"，但 1922 年没有人能想象这种东西。

</div>

</v-click>

---

# 实验分析与"半整数之谜"

设原子以速度 $v$ 通过长度为 $L$ 的磁场区域，在 $z$ 方向受力 $F_z = \mu_z\, \dfrac{\partial B_z}{\partial z}$，加速度 $a = F_z/M$。

<v-click>

通过磁场的时间 $t = L/v$，偏转距离

$$\Delta z = \frac{1}{2}\, a\, t^2 = \frac{\mu_z}{2 M}\, \frac{\partial B_z}{\partial z}\!\left(\frac{L}{v}\right)^2$$

<br/>

**$\Delta z \propto \mu_z$**。两条对称的痕迹意味着 $\mu_z$ 只取**两个等大反号**的值。

</v-click>

<v-click>

**问题**：根据 §17 和 §18，对 $\ell$ 态：

$$\mu_z = -m\, \mu_B, \qquad m = -\ell, -\ell+1, \ldots, +\ell$$

**永远是 $2\ell+1$ 个值，永远是奇数**。

银原子基态 $\ell = 0$，按理只有 $m = 0$，1 条；如果是 $\ell = 1$，应该 3 条；$\ell = 2$ 是 5 条……

**实验结果"2 条"无论如何对不上整数 $\ell$！**

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.6em;">

**1922 年这个矛盾让所有人困惑了三年**。直到 1925 年 Pauli、Uhlenbeck、Goudsmit 才意识到：电子有一个**新的内禀自由度**，量子数是 $\dfrac{1}{2}$，可以贡献 $2 \times \dfrac{1}{2} + 1 = 2$ 条。

这就是后面 §20 要讲的**电子自旋**。Stern-Gerlach 实验**实际上发现了自旋**，但当时**没有人知道**。

</div>

</v-click>

---

# 一个被误解的史上最重要实验

**讽刺的事实**：Stern 和 Gerlach 设计实验时是为了**证实空间量子化（轨道角动量）**，他们成功证实了"某种"空间量子化。但当时没有人知道，他们实际上发现的是**自旋量子化**，不是轨道量子化。

<v-click>

按当时的理解：
- 银原子基态 $\ell = 0$，应该没有磁矩
- 实验看到了磁矩
- "肯定是 $\ell = 1$"，这是当时的（错误）解释

</v-click>

<v-click>

**真相**（1925 年才明白）：
- 银原子基态确实 $\ell = 0$，**没有轨道磁矩**
- 看到的磁矩**完全来自电子自旋**
- 两束分裂对应 $m_s = \pm \dfrac{1}{2}$

</v-click>

<v-click>

<div style="background: rgba(88,86,214,0.08); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #5856d6; margin-top: 0.5em;">

**历史的吊诡之处**：

> "We were trying to verify Bohr-Sommerfeld theory; we ended up discovering electron spin without knowing it. Sometimes the universe answers a different question than the one you asked."

如果 Stern-Gerlach 的银原子分成 1 条或 3 条，物理学的发展会少了一个最关键的提示。**正是"2 条"这个偶数，逼着 Pauli 等人想出了半整数的自旋量子数**。

</div>

</v-click>

---

# §19 思考 1　<span style="color: #C71585; font-size: 0.7em;">概念</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

为什么 Stern-Gerlach 实验必须用**非均匀**磁场？均匀磁场不行吗？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**均匀磁场只产生力矩，不产生力**。

均匀磁场中，磁偶极子的能量 $U = -\vec\mu\cdot\vec B$ 不随位置改变，所以没有梯度，也就没有平移力 $\vec F = -\nabla U$。原子只会以原速度直线前进，最多绕磁场进动一下，但不会偏转。

**非均匀磁场** $\partial B_z/\partial z \neq 0$ 才能产生 $\vec F = \nabla(\vec\mu\cdot\vec B)$，让原子在 $z$ 方向受力偏转。这就是为什么 Stern-Gerlach 设计了"尖楔形 + 槽形"的特殊磁极对，制造一个强梯度的非均匀场。

**类比**：均匀重力场让所有物体匀加速下落（不能区分质量），但放在引力梯度场中（如朝向地心的方向梯度），可以测出"潮汐力"。Stern-Gerlach 装置就是磁矩的"潮汐力探测器"。

</div>

</v-click>

---

# §19 思考 2　<span style="color: #C71585; font-size: 0.7em;">深入</span>

<div class="q-card">

如果按照 1922 年的理论（只有轨道磁矩），银原子的实验结果应该是什么？为什么实验结果让所有人困惑？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**1922 年的理论只承认轨道磁矩**。银原子基态 $5s$ 是 $\ell = 0$，按这个理论它**没有任何磁矩**，应该完全不偏转，在板上形成 1 条没有分裂的痕迹。

**实验结果**：2 条对称的痕迹，相距很远。

**让所有人困惑的原因**：

1. 不是 1 条（驳斥了"基态 $\ell = 0$ 无磁矩"）
2. 不是 3 条或更多奇数（不能用 $\ell = 1, 2, \ldots$ 解释）
3. **是 2 条，永远是 2 条**

把 $2\ell + 1 = 2$ 解出来 $\ell = 1/2$，但 1922 年的物理学家无法接受半整数角动量量子数。这违反了"角动量量子数必须是整数"的当时认知。

**结果**：1922 到 1925 年这三年，物理学家假装没看见这个矛盾。直到 1925 年 Pauli 提出"电子有第四个量子数"，Uhlenbeck 和 Goudsmit 大胆提出"电子有自旋 $1/2$"，才解释了这个 2 条分裂。

**教训**：好的实验比好的理论更重要。Stern-Gerlach 的实验**直接看到了**自旋量子化，比理论预言早了 3 年。

</div>

</v-click>

---

# §19 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] W. Gerlach & O. Stern, "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld," *Z. Phys.* **9**, 349 (1922). 实验的原始论文。

[2] W. Gerlach & O. Stern, "Das magnetische Moment des Silberatoms," *Z. Phys.* **9**, 353 (1922). 同期发表的银原子磁矩测量。

[3] B. Friedrich & D. Herschbach, "Stern and Gerlach: How a bad cigar helped reorient atomic physics," *Physics Today* **56** (12), 53 (2003). 详细的历史叙事，含"硫熏出银轨迹"的故事。

[4] D. Castelvecchi, "The Stern-Gerlach experiment at 100," *Nature Physics* **18**, 364 (2022). 实验百年纪念回顾，强调它对量子力学的奠基性意义。

[5] J. J. Sakurai & J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., §1.1 (Cambridge Univ. Press, 2020). Sakurai 用 Stern-Gerlach 作为整本书的开篇，强调它的概念意义。

</div>

---

# §20 电子的自旋

需要掌握的知识点：

（1）理解 1925 年 Pauli 提出"第四个量子数"的动机：解释 Stern-Gerlach 的"2 条"和反常塞曼效应

（2）掌握 Uhlenbeck 和 Goudsmit 的自旋假设：电子有内禀角动量 $S = \dfrac{\hbar}{2}$

（3）理解自旋的反常 $g$ 因子 $g_s \approx 2$，知道这是经典物理无法解释的纯量子效应

（4）了解 Dirac 1928 年方程为什么自然推出自旋和 $g_s = 2$

（5）使用完整的 5 个量子数 $(n, \ell, m_\ell, s, m_s)$ 标记电子状态

---

# 1925 年的危机：四条证据指向"第四量子数"

到 1925 年初，物理学界积累了 4 个用整数量子数 $(n, \ell, m)$ **无法解释**的现象：

<v-click>

1. **Stern-Gerlach 的 2 条**（1922）：银原子分裂为偶数条，永远对不上 $2\ell+1$
2. **碱金属双线**（多年来）：钠 D 线是两条非常靠近的线 $D_1, D_2$，每条单态都"莫名其妙"地分裂
3. **反常塞曼效应**（多年来）：很多原子在弱磁场下分裂的条数和正常塞曼预言不一致
4. **元素周期表的填充**：每个轨道实际能容纳 **2 倍**于按 $(n, \ell, m)$ 数出来的状态数

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**Wolfgang Pauli 1925 年 1 月的洞察**：

> "电子必须有一个**第四个量子数**，它有两个可能的取值。这个第四量子数没有经典对应物。"

Pauli 把这条假设称为他的"**不相容原理**"（Pauli exclusion principle）：每个完整量子态最多容纳一个电子。但他**没有解释**这个第四量子数是什么。

</div>

</v-click>

---

# Uhlenbeck 和 Goudsmit 的大胆假设

1925 年 10 月，荷兰莱顿大学两个**研究生** George Uhlenbeck 和 Samuel Goudsmit 大胆地提出：

<v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #ff8c00; margin-top: 0.4em;">

**电子像一个旋转的小陀螺，有"自转角动量"**，记作 $\vec S$，量子数 $s = \dfrac{1}{2}$：

$$|\vec S| = \sqrt{s(s+1)}\, \hbar = \sqrt{\frac{1}{2}\cdot\frac{3}{2}}\, \hbar = \frac{\sqrt 3}{2}\hbar$$

$$S_z = m_s\, \hbar, \qquad m_s = \pm \frac{1}{2}$$

只有两个 $m_s$ 取值，正好对应 Stern-Gerlach 的"两条分裂"和 Pauli 的"第四量子数"！

</div>

</v-click>

<v-click>

**Pauli 起初强烈反对**这个假设。他认为"电子在自转"违反相对论：要让电子表面有 $\hbar$ 量级的角动量，赤道速度必须**超过光速**。

但 Lorentz 算了一下，告诉 Uhlenbeck 等：

> "如果电子真的在自转，它的赤道速度大约是光速的 10 倍。"

Uhlenbeck 想撤回论文，但导师 Ehrenfest 已经把它寄出去发表了。

</v-click>

<v-click>

最后所有人都意识到：**"自转"只是一个比喻**。电子的"自旋"是一种纯粹的量子内禀属性，没有经典对应物。它就是电子的"内秉角动量"，与电子是不是真的在旋转无关。

</v-click>

---

# 自旋的内禀性质

类比轨道角动量 $\vec L$：

| 性质 | 轨道角动量 $\vec L$ | 自旋角动量 $\vec S$ |
|---|---|---|
| 量子数 | $\ell = 0, 1, 2, \ldots$（整数） | $s = \dfrac{1}{2}$（**半整数**，电子固定为 $1/2$） |
| 大小 | $\sqrt{\ell(\ell+1)}\, \hbar$ | $\sqrt{s(s+1)}\, \hbar = \dfrac{\sqrt 3}{2}\hbar$ |
| $z$ 投影 | $L_z = m_\ell\, \hbar$ | $S_z = m_s\, \hbar$ |
| 投影量子数 | $m_\ell = -\ell, \ldots, \ell$（$2\ell+1$ 个） | $m_s = \pm\dfrac{1}{2}$（**2 个**） |
| 物理来源 | 电子绕核运动 | **内禀**，无经典对应 |

<v-click>

<img src="/images/CNX_UPhysics_41_03_SpinDir-1-28845.jpg" style="max-width: 320px; max-height: 240px; margin: 0.4em auto; display: block;" />

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**$s$ 是固定的**（对电子永远是 $\dfrac{1}{2}$），这与 $\ell$ 不同（$\ell$ 可以从 $0$ 到 $n-1$ 变化）。这是因为自旋是粒子的**内禀属性**，与运动状态无关，就像电子的电荷 $-e$ 和质量 $m_e$ 一样。

不同基本粒子有不同自旋：电子 $1/2$，光子 $1$，希格斯玻色子 $0$，引力子 $2$（如果存在）。

</div>

</v-click>

---

# 自旋磁矩与反常 $g_s \approx 2$

类比轨道磁矩 $\vec\mu_L = -\dfrac{e}{2 m_e}\vec L$，自旋磁矩似乎应该是

$$\vec\mu_s \stackrel{?}{=} -\frac{e}{2 m_e}\vec S$$

<v-click>

但**实验测量**显示，自旋磁矩比这个大**两倍**：

$$\boxed{\;\vec\mu_s = -g_s\, \frac{e}{2 m_e}\vec S \;\;\text{with}\;\; g_s \approx 2\;}$$

或者写成

$$|\vec\mu_s| = g_s\, \mu_B\, \sqrt{s(s+1)} = g_s\, \mu_B\, \frac{\sqrt 3}{2}, \quad \mu_{s,z} = -g_s\, m_s\, \mu_B = \mp\, \mu_B$$

</v-click>

<v-click>

**$g_s \approx 2$ 是经典物理无法解释的**！如果电子真的是一个旋转的带电小球，应该 $g = 1$。

$g_s = 2$ 是 1925 年最大的谜之一，直到 1928 年 **Dirac 方程**才自然推出来。

</v-click>

---

# Dirac 1928：自旋的相对论起源

Paul Dirac 1928 年试图把薛定谔方程**相对论化**。他假设波函数有 4 个分量（不是 1 个），并要求方程对**洛伦兹变换**协变。

<v-click>

结果令人震惊：

$$(i\gamma^\mu \partial_\mu - mc/\hbar)\psi = 0$$

这个方程**自动包含**：
1. 电子有自旋 $s = \dfrac{1}{2}$
2. 自旋的 $g_s = 2$（**精确**地，不需要任何假设）
3. 还预言了**反电子**（正电子）的存在，1932 年 Anderson 实验发现

</v-click>

<v-click>

<div style="background: rgba(88,86,214,0.08); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #5856d6; margin-top: 0.5em;">

**自旋是相对论的内禀属性**。它不是"电子在转"，而是当你把量子力学和相对论结合时，**必然出现的一个新自由度**。

> "Spin is a relativistic effect, but a peculiar one: it survives even in the non-relativistic limit."（A. Pais）

经典物理永远理解不了自旋，因为经典物理没有相对论 + 量子力学的组合。

</div>

</v-click>

<v-click>

**精确数值**：实验测得 $g_s = 2.002\,319\,304\,361...$，比 Dirac 的 $g = 2$ 略大。这个 0.001 来自**量子电动力学（QED）的虚光子修正**。1948 年 Schwinger 算出 $g_s - 2 \approx \alpha/\pi$，今天 $g_s$ 已经测到 12 位精度，是**物理学历史上最精确的预言之一**。

</v-click>

---

# 完整的电子状态：5 个量子数

加上自旋后，氢原子电子的完整状态由 **5 个量子数**描述：

| 量子数 | 名称 | 取值 | 物理意义 |
|---|---|---|---|
| $n$ | 主量子数 | $1, 2, 3, \ldots$ | 决定能量 $E_n = -E_0/n^2$ |
| $\ell$ | 角量子数 | $0, 1, \ldots, n-1$ | 决定 $\|\vec L\|$ 和轨道形状 |
| $m_\ell$ | 磁量子数 | $-\ell, \ldots, \ell$ | 决定 $L_z$，轨道空间取向 |
| $s$ | 自旋量子数 | $\dfrac{1}{2}$（**固定**） | 决定 $\|\vec S\|$ |
| $m_s$ | 自旋磁量子数 | $\pm\dfrac{1}{2}$ | 决定 $S_z$，自旋"上"或"下" |

<v-click>

**新的简并度**：原来 $n$ 能级有 $n^2$ 态，加上自旋后变成 $2 n^2$ 态。

- $n=1$：$2 \times 1 = 2$（$1s\uparrow, 1s\downarrow$）
- $n=2$：$2 \times 4 = 8$
- $n=3$：$2 \times 9 = 18$

</v-click>

<v-click>

**这就是元素周期表的"2, 8, 18, 32"的来源**！周期表的每一行能容纳的元素数是 $2 n^2$。Pauli 的不相容原理（每个完整量子态最多一个电子）+ 自旋的两个 $m_s$ = 周期表的全部规律。

</v-click>

---

# 总角动量 $\vec J = \vec L + \vec S$

电子既有轨道角动量 $\vec L$ 又有自旋 $\vec S$。它们都是矢量，要相加得到**总角动量**：

$$\vec J = \vec L + \vec S$$

<v-click>

类比 $\hat L^2$，总角动量也满足量子化：

$$|\vec J|^2 = j(j+1)\hbar^2, \quad J_z = m_j\, \hbar$$

其中量子数 $j$ 由 $\ell$ 和 $s$ 的"耦合"决定。

</v-click>

<v-click>

**角动量加法规则**（详见量子力学）：

$$j = |\ell - s|, |\ell - s| + 1, \ldots, \ell + s$$

对电子 $s = 1/2$，所以

$$j = \begin{cases} \ell + \dfrac{1}{2} & (\ell \geq 0)\\[2pt] \ell - \dfrac{1}{2} & (\ell \geq 1)\end{cases}$$

</v-click>

<v-click>

**例**：

- $\ell = 0$（$s$ 态）：只有 $j = 1/2$
- $\ell = 1$（$p$ 态）：$j = 1/2$ 或 $j = 3/2$
- $\ell = 2$（$d$ 态）：$j = 3/2$ 或 $j = 5/2$

每个 $j$ 又有 $2 j + 1$ 个 $m_j$ 值。

</v-click>

<img src="/images/Screen Shot 2022-02-21 at 13.00.33-29150.png" style="max-width: 320px; max-height: 220px; margin: 0.4em auto; display: block;" />

---

# 电子的总磁矩

$$\vec\mu = \vec\mu_L + \vec\mu_s = -\frac{e}{2 m_e}\vec L - g_s\, \frac{e}{2 m_e}\vec S = -\frac{e}{2 m_e}(\vec L + g_s \vec S)$$

<v-click>

**关键差别**：因为 $g_s \approx 2$ 而 $g_L = 1$，所以 $\vec\mu$ 与 $\vec L + g_s\vec S \neq \vec J$。这意味着**总磁矩 $\vec\mu$ 与总角动量 $\vec J$ 不平行**！

</v-click>

<v-click>

但 $\vec L$ 和 $\vec S$ 都绕 $\vec J$ 进动（这是后面 §21 自旋轨道耦合的内容），所以**只有 $\vec\mu$ 沿 $\vec J$ 方向的投影是稳定的**：

$$\mu_J = -g_J\, \mu_B\, \sqrt{j(j+1)}$$

其中 $g_J$ 是**朗德 $g$ 因子**，由 $\ell, s, j$ 决定（详细公式见 §22 塞曼效应）。

</v-click>

<img src="/images/WechatIMG1114-29260.png" style="max-width: 200px; max-height: 200px; margin: 0.4em auto; display: block;" />

---

# §20 思考 1　<span style="color: #C71585; font-size: 0.7em;">概念</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

为什么 Pauli 一开始反对 Uhlenbeck 和 Goudsmit 的"自旋"假设？他后来又是怎么接受的？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**Pauli 的反对理由**：把电子想象成一个旋转的小球，要让它表面有 $\hbar$ 量级的角动量，需要赤道速度**超过光速**很多倍。这违反相对论，所以"电子在自转"在物理上不可能。

具体计算：经典电子半径 $r_e \sim 2.8\times 10^{-15}$ m，自转角动量 $\sim m_e v r_e \sim \hbar/2$，解出 $v \sim 10^{10}$ m/s，**约为光速的 30 倍**。

**Uhlenbeck 想撤回论文**，但 Ehrenfest 已经寄出去了。

**Pauli 后来的转变**：意识到"自转"只是比喻，**自旋是一种内禀的量子自由度**，与电子在不在旋转无关。它就是在 $SU(2)$ 表示下变换的那部分波函数。1927 年 Pauli 写下了著名的 "Pauli 矩阵"和 Pauli 方程（含自旋的非相对论薛定谔方程），把自旋纳入量子力学的标准框架。

1928 年 Dirac 方程进一步从相对论原理直接**推出**自旋，证明它是"相对论的产物"。Pauli 后来评价：

> "It is one of the great experiences of physics that something which was thought to be impossible turned out not only to be possible, but to be necessary."

**教训**：物理中"经典上不可能"经常意味着"需要新的图像"，不一定意味着"物理上不存在"。

</div>

</v-click>

---

# §20 思考 2　<span style="color: #C71585; font-size: 0.7em;">前沿</span>

<div class="q-card">

电子的反常 $g_s \approx 2.00232$，比 Dirac 预言的 $g_s = 2$ 大约 $0.001$。这个微小的偏差怎么解释？现代实验测量它有多精确？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**物理来源**：偏差 $a_e \equiv (g_s - 2)/2 \approx 0.00116$ 来自**量子电动力学（QED）的辐射修正**。简单说，电子在真空中"穿着"一团虚光子"云"，这团云改变了电子与外磁场的耦合。

**Schwinger 1948**：第一个算出了 leading order 修正

$$a_e^{(1)} = \frac{\alpha}{2\pi} \approx 0.001\,162$$

只用一个 Feynman 图（"单环"）就给出。

**到今天**：理论已经算到 5 环以上，含约 12000 个 Feynman 图。理论值

$$a_e^\text{theory} = 0.001\,159\,652\,181\,664\,(763)$$

**实验测量**（Hanneke, Fogwell, Gabrielse 2008，Penning 阱单电子）：

$$a_e^\text{exp} = 0.001\,159\,652\,180\,73\,(28)$$

**精度**：12 位有效数字一致！这是物理学历史上**理论与实验吻合最精确**的预言之一。

**意义**：QED 是物理学最精确的理论，比任何其他理论都精确。整个 Standard Model 的可信度，很大程度上建立在 $g_s - 2$ 这个数字上。

**现代用途**：现在物理学家在测量**$\mu$ 子的 $g - 2$**（$\mu$ 子是电子的"重表亲"）。Fermilab 最近的结果显示与标准模型偏差约 4.2 sigma，**可能是新物理的线索**。这是当前粒子物理的热点。

</div>

</v-click>

---

# §20 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] W. Pauli, "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren," *Z. Phys.* **31**, 765 (1925). Pauli 不相容原理和"第四个量子数"的提出。

[2] G. E. Uhlenbeck & S. Goudsmit, "Ersetzung der Hypothese vom unmechanischen Zwang durch eine Forderung bezüglich des inneren Verhaltens jedes einzelnen Elektrons," *Naturwissenschaften* **13**, 953 (1925). 自旋假设的原始论文。

[3] W. Pauli, "Zur Quantenmechanik des magnetischen Elektrons," *Z. Phys.* **43**, 601 (1927). Pauli 矩阵和 Pauli 方程，把自旋纳入量子力学。

[4] P. A. M. Dirac, "The quantum theory of the electron," *Proc. Roy. Soc. A* **117**, 610 (1928). Dirac 方程，自旋的相对论起源。

[5] J. Schwinger, "On Quantum-Electrodynamics and the Magnetic Moment of the Electron," *Phys. Rev.* **73**, 416 (1948). Schwinger 1948，第一次 QED 计算 $g - 2$。

[6] D. Hanneke, S. Fogwell, & G. Gabrielse, "New Measurement of the Electron Magnetic Moment and the Fine Structure Constant," *Phys. Rev. Lett.* **100**, 120801 (2008). 电子 $g$ 因子的精密测量。

[7] B. Abi et al. (Muon $g - 2$ Collaboration), "Measurement of the Positive Muon Anomalous Magnetic Moment to 0.46 ppm," *Phys. Rev. Lett.* **126**, 141801 (2021). $\mu$ 子 $g - 2$ 实验，可能的新物理线索。

[8] S. Tomonaga, *The Story of Spin* (University of Chicago Press, 1997). 朝永振一郎写的自旋发现史。

</div>

---

# §21 自旋轨道相互作用

需要掌握的知识点：

（1）理解自旋轨道相互作用的物理图像：电子在自身坐标系中"看到"原子核运动产生的磁场

（2）理解 1926 年 Thomas 因子 1/2 的来源（相对论参考系变换的修正）

（3）掌握 $\hat H_\text{LS} = \xi(r)\, \vec L\cdot \vec S$ 的形式

（4）使用 $\vec J = \vec L + \vec S$ 计算 $\vec L\cdot\vec S$ 的本征值

（5）理解精细结构能级劈裂 $\Delta E_\text{LS}/E_n \sim \alpha^2$，**精细结构常数**自然出场

（6）通过钠 D 双线认识精细结构的实验验证

---

# 物理图像：电子坐标系中的内磁场

考虑电子绕原子核运动。**在电子静止的参考系中**，是带正电荷的核以速度 $-\vec v$ 反向绕电子运动。这是一个**电流回路**，在电子处产生磁场：

$$\vec B_\text{核} = \frac{\mu_0\, Z e}{4\pi r^3}\, (-\vec v)\times (-\vec r) = \frac{\mu_0\, Z e}{4\pi r^3}\, \vec v\times\vec r = -\frac{\mu_0\, Z e}{4\pi m_e r^3}\, \vec L$$

<v-click>

电子的自旋磁矩 $\vec\mu_s = -g_s\dfrac{e}{2 m_e}\vec S$ 在这个磁场中有势能：

$$\Delta E_\text{LS} = -\vec\mu_s\cdot\vec B_\text{核} \;\sim\; \frac{1}{m_e^2 r^3}\, (\vec L\cdot\vec S)$$

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.5em;">

这就是**自旋轨道相互作用**：电子的自旋"感受"到自己运动产生的磁场。

它**只能存在于带角动量 $\vec L \neq 0$ 的态**（如 $p, d, f$ 态），$s$ 态（$\ell = 0$）不受自旋轨道耦合修正。

</div>

</v-click>

<img src="/images/Screen Shot 2022-02-21 at 21.43.00-29299.png" style="max-width: 380px; max-height: 200px; margin: 0.4em auto; display: block;" />

---

# Thomas 1926：相对论的"1/2 因子"

上面的"电子静止系"推导有一个**致命的疏忽**：从原子核坐标系变到电子坐标系不是简单的伽利略变换，而是相对论变换。

<v-click>

电子在做曲线运动（绕核），它的瞬时静止系是一个**非惯性参考系**。从一个非惯性系看另一个，需要洛伦兹变换的相对论修正。

</v-click>

<v-click>

1926 年 Llewellyn Thomas 算了这个修正，发现真正的自旋轨道势比上面的推导**小了一半**：

$$\boxed{\;\hat H_\text{LS} = \xi(r)\, \vec L\cdot\vec S, \qquad \xi(r) = \frac{1}{2 m_e^2 c^2}\frac{1}{r}\frac{dU}{dr}\;}$$

那个 $\dfrac{1}{2}$ 因子叫做 **Thomas 因子**或 **Thomas precession**。

</v-click>

<v-click>

<div style="background: rgba(88,86,214,0.08); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #5856d6; margin-top: 0.4em;">

**Thomas 因子的发现**让 Pauli 改变了对自旋的态度。1925 年 Pauli 试图算自旋轨道分裂时，得到的是一个少了 1/2 的结果，与实验差一倍。Pauli 认为这说明"自旋"假设是错的。

直到 Thomas 1926 年发现这个相对论因子，理论才与实验一致。Pauli 后来在写给 Bohr 的信里承认：

> "I feel that this Thomas factor will give a great relief in the discomfort about the spin hypothesis."

</div>

</v-click>

<img src="/images/37_622fa36000641da57a5bc7b17af7039c-29565.png" style="max-width: 380px; max-height: 220px; margin: 0.4em auto; display: block;" />

---

# 用 $\vec J^2$ 算 $\vec L\cdot\vec S$ 的本征值

在 $\vec L^2, \vec S^2, \vec L\cdot\vec S$ 不全互相对易的情况下，怎么算 $\vec L\cdot\vec S$ 的本征值？

<v-click>

**技巧**：考虑总角动量 $\vec J = \vec L + \vec S$。两边平方：

$$\vec J^2 = \vec L^2 + \vec S^2 + 2\, \vec L\cdot\vec S$$

所以

$$\vec L\cdot\vec S = \frac{1}{2}\!\left(\vec J^2 - \vec L^2 - \vec S^2\right)$$

</v-click>

<v-click>

在 $|j, m_j, \ell, s\rangle$ 本征态上：

$$\langle\vec L\cdot\vec S\rangle = \frac{\hbar^2}{2}\!\left[j(j+1) - \ell(\ell+1) - s(s+1)\right]$$

</v-click>

<v-click>

**对电子** $s = 1/2$，$j = \ell \pm 1/2$：

$$\langle\vec L\cdot\vec S\rangle = \begin{cases} +\dfrac{\hbar^2}{2}\, \ell, & j = \ell + \dfrac{1}{2} \\[6pt] -\dfrac{\hbar^2}{2}\,(\ell + 1), & j = \ell - \dfrac{1}{2}\end{cases}$$

</v-click>

<v-click>

**核心结果**：自旋轨道耦合让原来 $\ell$ 简并的能级**分裂为两条**（$j = \ell + 1/2$ 和 $j = \ell - 1/2$），分别向上和向下移动。

</v-click>

---

# 精细结构能级公式

考虑一阶微扰：

$$\Delta E_\text{LS} = \langle \xi(r) \rangle\, \langle \vec L\cdot\vec S \rangle$$

<v-click>

对氢原子，$U(r) = -\dfrac{e^2}{4\pi\epsilon_0 r}$，$\xi(r) = \dfrac{1}{2 m_e^2 c^2}\dfrac{e^2}{4\pi\epsilon_0 r^3}$。

经过对径向波函数的积分（$\langle 1/r^3\rangle$），最终得到**精细结构能级公式**：

$$\boxed{\;\Delta E_\text{LS} = -E_n\, \frac{Z^2 \alpha^2}{n}\, \frac{1/2}{\ell(\ell + \frac{1}{2})(\ell + 1)}\,\big[j(j+1) - \ell(\ell+1) - s(s+1)\big]\;}$$

</v-click>

<v-click>

其中 $\alpha$ 是**精细结构常数**：

$$\boxed{\;\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c} \approx \frac{1}{137.036}\;}$$

</v-click>

<v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #ff8c00; margin-top: 0.4em;">

**$\alpha$ 是如何"自然出场"的**：精细结构能级修正与玻尔能级的比值

$$\frac{\Delta E_\text{LS}}{E_n} \sim \frac{Z^2 \alpha^2}{n}$$

对于 $Z = 1$ 的氢原子，这个比值约 $10^{-4}$，所以叫"精细结构"。**$\alpha^2 \approx 5\times 10^{-5}$ 是一个无量纲的小量**，它就是相对论修正的展开参数。

精细结构常数 $\alpha = 1/137.036$ 出现在物理学的很多地方（QED 耦合常数、Lamb 移位、Rydberg 常数与电子 Compton 波长的比值），但它的来源至今没有人能从更深层的理论推出。Feynman 称之为"物理学最神秘的常数"。

</div>

</v-click>

<img src="/images/Screen Shot 2022-02-22 at 15.13.53-29676.png" style="max-width: 380px; max-height: 220px; margin: 0.4em auto; display: block;" />

---

# 精细结构的两条能级

对于固定的 $n, \ell$，精细结构把原来一条能级**劈成两条**：

$$j_+ = \ell + \frac{1}{2}, \qquad j_- = \ell - \frac{1}{2}$$

<v-click>

两条能级的能量差：

$$\Delta E = E(j_+) - E(j_-) \;=\; -E_n\, \frac{Z^2 \alpha^2}{n \ell(\ell + 1)}$$

代入数值（$E_n = -13.6/n^2$ eV）：

$$\Delta E \approx 5.3\times 10^{-5}\, |E_n|\, \frac{Z^2}{n\ell(\ell+1)}$$

</v-click>

<v-click>

**例：氢原子 $2p$ 态**（$n = 2, \ell = 1$）：

$$\Delta E = 5.3\times 10^{-5} \times 3.4\, \mathrm{eV}\times \frac{1}{2\cdot 1\cdot 2} \approx 4.5\times 10^{-5}\ \mathrm{eV}$$

对应频率 $\sim 10$ GHz，对应波长差 $\sim 0.001$ nm。这就是 $H_\alpha$ 谱线（Balmer $n=3 \to n=2$）的精细结构分裂。

</v-click>

---

# 实验验证：钠 D 双线

**钠原子的 D 线**是一对著名的黄色谱线（路灯发的就是），来源于 $3p \to 3s$ 跃迁。但 D 线**实际上是两条**，相差约 0.6 nm：

$$D_1: \lambda = 589.59\ \mathrm{nm}\quad (3 p_{1/2} \to 3 s_{1/2})$$

$$D_2: \lambda = 588.99\ \mathrm{nm}\quad (3 p_{3/2} \to 3 s_{1/2})$$

<v-click>

**这就是精细结构的实验证据**！钠的 $3 p$ 态分裂为 $3 p_{1/2}$（$j = 1/2$）和 $3 p_{3/2}$（$j = 3/2$），两个 $j$ 态的能量差恰好对应这 $0.6$ nm 的劈裂。

</v-click>

<v-click>

**历史**：钠 D 双线在 1814 年就被 Fraunhofer 观察到（太阳光谱中），但直到 1925 年自旋假设提出后才有了正确解释。

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.4em;">

**为什么钠 D 双线对原子物理这么重要**：它是一个用肉眼或分光镜就能直接看到的精细结构现象。任何原子物理课程都应该让学生**亲眼**看一次钠 D 双线。

</div>

</v-click>

<v-click>

**其他原子的精细结构**：

- **氢 $H_\alpha$**：原本一条 $\lambda = 656.3$ nm 的红线，精细结构把它分成 7 条（有些过于接近不易分辨）
- **重元素**：$Z$ 越大，$\alpha^2 Z^4$ 越大，精细结构越显著。$Z = 50$ 的原子精细结构能级差能达到 ~eV 量级
- **类氢离子（$\mathrm{He^+}$, $\mathrm{Li^{2+}}$）**：精细结构与 Dirac 方程预言精确符合

</v-click>

---

# §21 思考 1　<span style="color: #C71585; font-size: 0.7em;">概念</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

为什么 $s$ 态（$\ell = 0$）没有精细结构能级分裂？这与"自旋轨道耦合"的物理图像一致吗？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**直接原因**：$\hat H_\text{LS} = \xi(r)\, \vec L\cdot\vec S$，对 $\ell = 0$ 态，$\vec L = 0$，所以 $\vec L\cdot\vec S = 0$，能级修正为零。

**物理图像一致性**：自旋轨道耦合的物理来源是"电子轨道运动产生的内磁场作用于电子自旋"。如果电子没有轨道角动量（$\ell = 0$），它的运动是"纯径向"的（球对称概率云），**没有净环流**，所以也没有产生磁场。自旋没有外磁场可以耦合，能量自然不变。

**但有个微妙之处**：实验上，氢原子的 $1s$ 态确实**有一个超精细分裂**（相差 5.9 微 eV，对应 21 cm 射电谱线，整个射电天文学的基础）。但这不是自旋轨道耦合，而是**电子自旋与质子自旋的耦合**（核磁矩相互作用）。这个分裂是自旋轨道分裂的 $m_e/m_p \sim 1/1836$，所以叫"超精细"（hyperfine）。

更准确地说，氢的 $1s$ 态确实有一个 **Lamb 移位**（QED 真空涨落引起，1947 年 Lamb 和 Retherford 发现），但这是 §21 之外的话题。

**结论**：$s$ 态在精细结构层级（自旋轨道耦合）确实没有分裂，但它有**更细的**结构（超精细 + Lamb 移位），需要更精确的理论才能描述。

</div>

</v-click>

---

# §21 思考 2　<span style="color: #C71585; font-size: 0.7em;">前沿</span>

<div class="q-card">

精细结构常数 $\alpha = 1/137.036$ 是物理学最神秘的数字之一。它的物理意义是什么？为什么 Feynman 称它为"上帝在我们的方程上写的一只手指印"？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**$\alpha$ 的多重身份**：

1. **QED 的耦合常数**：电磁相互作用的强度。在自然单位下，电荷 $e = \sqrt{4\pi\alpha}$。
2. **相对论 vs 经典的展开参数**：电子在玻尔轨道上的速度 $v/c \approx \alpha$，所以非相对论展开的"小量"就是 $\alpha$。
3. **精细结构能级劈裂的尺度**：$\Delta E_\text{fs}/E_n \sim \alpha^2$。
4. **Bohr 半径 vs 经典电子半径**：$r_e/a_0 = \alpha^2$。
5. **氢原子能级 vs 电子静止能量**：$E_0/m_e c^2 = \alpha^2/2$。

**为什么神秘**：

- $\alpha$ 是**无量纲数**，所以它的值不依赖于单位选择，是一个"宇宙常数"。
- 它接近 $1/137$，但**没有任何已知理论能从更基本的原理推出 137**。
- 它出现在物理学几乎所有地方，把电磁、量子、相对论、原子物理串到一起。

**Feynman 的话**：

> "It has been a mystery ever since it was discovered more than fifty years ago, and all good theoretical physicists put this number up on their wall and worry about it. ... It's one of the greatest damn mysteries of physics: a magic number that comes to us with no understanding by man."

**现代实验**：$\alpha$ 是物理学测得最精确的常数之一，11 位有效数字（2018 年 Berkeley 的 Cs 反冲实验，结合 LKB 巴黎的氢原子谱线测量）。它的测量精度本身就是检验 QED 和标准模型的最严格手段之一。

**类比**：经典物理告诉我们粒子的"软参数"（质量、电荷），但 $\alpha$ 这种**无量纲的纯数**应该来自更深的理论（也许是超弦？也许是某种统一场？），但目前无解。

</div>

</v-click>

---

# §21 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] L. H. Thomas, "The Motion of the Spinning Electron," *Nature* **117**, 514 (1926). Thomas 因子 1/2 的原始论文。

[2] L. H. Thomas, "The Kinematics of an Electron with an Axis," *Phil. Mag.* **3**, 1 (1927). Thomas 进动的详细推导。

[3] A. Sommerfeld, "Zur Quantentheorie der Spektrallinien," *Ann. Phys.* **51**, 1 (1916). Sommerfeld 1916 年首次引入精细结构常数 $\alpha$，用旧量子论给出氢的精细结构。

[4] P. A. M. Dirac, "The quantum theory of the electron," *Proc. Roy. Soc. A* **117**, 610 (1928). Dirac 方程，自然给出精细结构（含 Thomas 因子）。

[5] H. Bethe & E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957). 单电子和双电子原子的标准教材，精细结构详细计算。

[6] R. Parker et al., "Measurement of the fine-structure constant as a test of the Standard Model," *Science* **360**, 191 (2018). 用 Cs 反冲实验测得 $\alpha$ 的最精密值。

[7] L. Morel et al., "Determination of the fine-structure constant with an accuracy of 81 parts per trillion," *Nature* **588**, 61 (2020). LKB 巴黎组的 Rb 反冲测量。

[8] R. P. Feynman, *QED: The Strange Theory of Light and Matter*, Ch. 4 (Princeton Univ. Press, 1985). Feynman 关于 $\alpha$ 的著名论述。

</div>

---

# §22 塞曼效应

需要掌握的知识点：

（1）了解 1896 年 Pieter Zeeman 实验，原子谱线在外磁场中分裂

（2）掌握**正常塞曼效应**（不考虑自旋）的三条等距分裂

（3）理解**反常塞曼效应**（含自旋）的复杂分裂，由朗德 g 因子描述

（4）了解强磁场下的 **Paschen-Back 效应**

（5）认识塞曼效应的现代应用：NMR、ESR、MRI、太阳磁场探测

（6）理解为什么塞曼效应是验证电子自旋的最直接证据

---

# 1896 年莱顿：Zeeman 的发现

1896 年荷兰物理学家 Pieter Zeeman 把一根钠光谱灯放在强电磁铁的两极间，发现钠 D 线**变宽并分裂**。

<v-click>

**理论支持**：洛伦兹（H. A. Lorentz，Zeeman 的导师）当年立即用经典电子论解释了这个现象。把电子看作受弹性回复力束缚的振子，在磁场中振动方向被洛伦兹力修改，导致辐射频率改变 $\Delta\omega = \pm \omega_L$，其中

$$\omega_L = \frac{e B}{2 m_e}$$

是**拉莫尔频率**。

</v-click>

<v-click>

**1902 年诺贝尔物理学奖**同时颁给 Zeeman 和 Lorentz，"以表彰他们关于磁场对辐射现象影响的研究"。这是诺贝尔物理学奖的第二次颁发，紧随伦琴的 X 射线之后。

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.5em;">

**塞曼效应的物理意义**：直接证明原子里有"带电运动的微观成分"。这是发现电子（J. J. Thomson 1897）的间接证据之一。

</div>

</v-click>

---

# 正常塞曼效应：不考虑自旋

考虑外磁场 $\vec B = B\hat z$。**只考虑轨道磁矩**（暂时无视自旋）：

$$\hat H_\text{磁} = -\vec\mu_L\cdot \vec B = \frac{e B}{2 m_e}\hat L_z$$

<v-click>

由 $\hat L_z |n, \ell, m_\ell\rangle = m_\ell\hbar |n, \ell, m_\ell\rangle$，能级修正

$$\boxed{\;\Delta E = m_\ell\, \mu_B\, B\;}$$

每个 $\ell$ 能级**分裂为 $2\ell + 1$ 条等距能级**。

</v-click>

<v-click>

**例：$2p$ 态**（$\ell = 1$，$m_\ell = -1, 0, +1$）在外磁场中分裂为 3 条：

$$E_{2p} \to \begin{cases} E_{2p} + \mu_B B & (m_\ell = +1)\\ E_{2p} & (m_\ell = 0) \\ E_{2p} - \mu_B B & (m_\ell = -1)\end{cases}$$

**等距分裂，间距 $\mu_B B$**。

</v-click>

<v-click>

**谱线分裂规则**：跃迁要满足 $\Delta m_\ell = 0, \pm 1$（电偶极辐射的选择定则）。

对一条单一原始谱线，外磁场分裂为**正中**（$\Delta m_\ell = 0$，$\pi$ 偏振）+ **两侧**（$\Delta m_\ell = \pm 1$，$\sigma_+, \sigma_-$ 偏振），共**三条**。

这就是 19 世纪末观察到的**正常塞曼效应**。

</v-click>

<img src="/images/Screen Shot 2022-02-23 at 14.02.48-29868.png" style="max-width: 380px; max-height: 220px; margin: 0.4em auto; display: block;" />

---

# 反常塞曼效应：当自旋登场

但 19 世纪末的实验家很快发现，**许多谱线分裂的条数不是 3**，有时是 4、6、9、12 条。这违反了"正常塞曼效应只有 3 条"的预期。

<v-click>

物理学家把这种"对不上"的情形称为**反常塞曼效应**（anomalous Zeeman effect）。这个谜从 1898 年一直困扰物理界直到 1925 年。

</v-click>

<v-click>

**关键洞察**：考虑电子的**自旋**。能级修正变为

$$\hat H_\text{磁} = \frac{e}{2 m_e}(\hat L_z + g_s \hat S_z)\, B = \mu_B(\hat L_z + 2 \hat S_z)\, B/\hbar$$

注意 $g_s \approx 2$，所以 $\hat L_z$ 和 $\hat S_z$ 不能简单合并。

</v-click>

<v-click>

如果**自旋轨道耦合远大于磁场作用**（弱场极限），电子的"好量子数"是 $j, m_j$ 而不是 $m_\ell, m_s$。能级修正为

$$\Delta E = g_J\, m_j\, \mu_B B$$

其中 $g_J$ 是**朗德 $g$ 因子**：

$$\boxed{\;g_J = 1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2 j(j+1)}\;}$$

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-top: 0.4em;">

**$g_J$ 因 $(j, \ell, s)$ 而异**：不同的 $j, \ell$ 组合给出不同的 $g_J$，所以能级间距和分裂条数千差万别。这就是反常塞曼效应"反常"的根源。

</div>

</v-click>

---

# 朗德 $g$ 因子的实例

**例 1**：纯轨道（$s = 0$，假想情形）

$$g_J = 1 + 0 = 1$$

退化为正常塞曼效应。

<v-click>

**例 2**：纯自旋（$\ell = 0$，如 $1s, 2s$ 态，$j = 1/2$）

$$g_J = 1 + \frac{\frac{1}{2}\cdot\frac{3}{2} + \frac{1}{2}\cdot\frac{3}{2} - 0}{2\cdot \frac{1}{2}\cdot\frac{3}{2}} = 1 + 1 = 2$$

正好是 $g_s = 2$。

</v-click>

<v-click>

**例 3**：$2p_{1/2}$ 态（$\ell = 1, s = 1/2, j = 1/2$）

$$g_J = 1 + \frac{\frac{1}{2}\cdot\frac{3}{2} + \frac{1}{2}\cdot\frac{3}{2} - 1\cdot 2}{2\cdot\frac{1}{2}\cdot\frac{3}{2}} = 1 + \frac{0.75 + 0.75 - 2}{1.5} = 1 - \frac{1}{3} = \frac{2}{3}$$

</v-click>

<v-click>

**例 4**：$2p_{3/2}$ 态（$\ell = 1, s = 1/2, j = 3/2$）

$$g_J = 1 + \frac{\frac{3}{2}\cdot\frac{5}{2} + \frac{1}{2}\cdot\frac{3}{2} - 1\cdot 2}{2\cdot\frac{3}{2}\cdot\frac{5}{2}} = 1 + \frac{3.75 + 0.75 - 2}{7.5} = 1 + \frac{1}{3} = \frac{4}{3}$$

</v-click>

<v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #ff8c00; margin-top: 0.5em;">

**结论**：钠 D 双线（$3p_{1/2} \to 3 s_{1/2}$ 和 $3 p_{3/2} \to 3 s_{1/2}$）在外磁场中的分裂条数和间距由不同的 $g_J$ 决定。$D_1$ 分裂为 4 条，$D_2$ 分裂为 6 条。

历史上 1925 年 Lande 用经验拟合给出了这个 $g$ 因子公式（早于自旋假设），后来才发现这可以从角动量耦合的量子力学严格推导。

</div>

</v-click>

---

# 强场极限：Paschen-Back 效应

当外磁场 $B$ 非常强时（$\mu_B B \gg$ 自旋轨道耦合能），磁场作用比 $\hat H_\text{LS}$ 大得多。这时**$\vec L$ 和 $\vec S$ 各自独立绕 $\vec B$ 进动**，$j$ 不再是好量子数，$m_\ell, m_s$ 才是好量子数。

<v-click>

能级修正：

$$\Delta E = (m_\ell + 2 m_s)\, \mu_B B$$

这个公式更简单，但要求 $B$ 足够大。

</v-click>

<v-click>

**临界磁场**：让磁场作用与精细结构能级差相等

$$\mu_B B \sim \Delta E_\text{LS} \sim \alpha^2 |E_n|$$

对氢的 $2p$ 态，$\Delta E_\text{LS} \sim 4.5\times 10^{-5}$ eV，对应 $B \sim 0.8$ T。

</v-click>

<v-click>

<img src="/images/pasted-image-35639.png" style="max-width: 380px; max-height: 220px; margin: 0.4em auto; display: block;" />

</v-click>

<v-click>

**实验**：1921 年 Paschen 和 Back 在强磁场（5 T 以上）下观察到反常塞曼效应"复原"为简单的三条线，正是因为强场让自旋轨道耦合被磁场效应"压垮"。这就叫 **Paschen-Back 效应**。

</v-click>

---

# 现代应用：从 NMR 到太阳磁场

塞曼效应不只是历史，它是现代物理和应用科学的基础：

<v-click>

**1. 核磁共振（NMR）**：核自旋在磁场中也有塞曼分裂（核磁矩 $\sim m_e/m_p$ 倍小）。在射频场驱动下，自旋翻转给出共振峰。NMR 是化学结构分析的标准工具，也是有机化学、生物化学的支柱。

</v-click>

<v-click>

**2. 磁共振成像（MRI）**：人体内的水分子里 $^1$H 核（质子）的塞曼分裂，加上射频脉冲和梯度磁场，重建出 3D 图像。是现代医学诊断的核心技术之一。

</v-click>

<v-click>

**3. 电子自旋共振（ESR/EPR）**：未配对电子的塞曼分裂，用于研究自由基、过渡金属络合物、半导体缺陷。

</v-click>

<v-click>

**4. 太阳和恒星磁场探测**：太阳黑子里的强磁场让光谱线产生塞曼分裂。Hale 1908 年第一次用塞曼效应直接测出太阳黑子的磁场（$\sim 0.4$ T）。今天天文学用 Zeeman Doppler Imaging 测绘恒星表面磁场。

</v-click>

<v-click>

**5. 量子计算**：超导量子比特、离子阱量子比特、自旋量子比特，都用磁场塞曼分裂作为"能级间隔可调"的工具。

</v-click>

<v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.4em;">

**塞曼 1896 年的实验**为整个 20 世纪的物理 + 化学 + 生物医学奠定了基础。它是最好的"基础研究最终改变世界"的例子。

</div>

</v-click>

---

# §22 思考 1　<span style="color: #C71585; font-size: 0.7em;">概念</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

为什么"反常"塞曼效应反而是更普遍的情形？为什么"正常"塞曼效应只在特定情况下出现？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**历史命名的误导**：当年 Zeeman 和 Lorentz 用纯经典电子论（**不知道自旋**）预言了"三条线"。所以这个不含自旋的 3 条分裂被称为"正常"。

**真相**：**真正普遍的是反常塞曼效应**。绝大多数原子的电子有非零自旋（电子 $s = 1/2$，原子总自旋经常是 $1/2, 1, 3/2, \ldots$），所以 $g_J \neq 1$，分裂数和间距由 $g_J$ 决定，超过 3 条。

**正常塞曼效应只发生在**：

- 总自旋 $S = 0$ 的态。比如某些偶数电子原子的单态（spin singlet），$g_J = 1$，正好是"三条等距"。
- 例：$\mathrm{He}$ 原子的 $1s 2s$ 单态（$S = 0$），跃迁会给出正常塞曼图样。
- 例：$\mathrm{Hg}$ 原子的某些跃迁。

**历史教训**：1896 年 Zeeman 用的钠原子单电子态 $S = 1/2 \neq 0$，他**理论上应该看到反常塞曼**。但是 1896 年的分光仪分辨率不够，他只看到一条变宽的线，被解释为"分裂了"。直到几年后高分辨率分光仪才看到具体几条。

**反常塞曼是当年物理学的核心谜题**之一，正是它逼着 Pauli 和 Sommerfeld 等人想出"半整数 $j$"，进而引向自旋的发现。如果一开始所有原子都"正常"，量子力学的发展会慢很多。

**现代视角**："正常"和"反常"是历史包袱。今天我们应该统一称为"塞曼效应"，由 $g_J$ 公式涵盖所有情形。

</div>

</v-click>

---

# §22 思考 2　<span style="color: #C71585; font-size: 0.7em;">应用</span>

<div class="q-card">

NMR（核磁共振）和 MRI 都基于塞曼效应。质子在 1 T 磁场中的塞曼能级差对应多大的频率？为什么 MRI 需要 1.5–3 T 的强磁场？

</div>

<v-click>

<div class="a-card">

<h4>答案</h4>

**质子的塞曼分裂**：

$$\Delta E = g_p\, \mu_N\, B = g_p\,\frac{e\hbar}{2 m_p}\, B$$

其中 $\mu_N = \dfrac{e\hbar}{2 m_p} = 5.05\times 10^{-27}$ J/T 是**核磁子**（约 $\mu_B$ 的 1/1836），$g_p \approx 5.586$ 是质子的 $g$ 因子（同样不是 $1$，因为质子不是基本粒子，是 uud 夸克束缚态）。

**1 T 下的能级差**：

$$\Delta E = 5.586 \times 5.05\times 10^{-27}\, \mathrm{J} \approx 2.82\times 10^{-26}\, \mathrm{J}$$

对应频率

$$\nu = \frac{\Delta E}{h} \approx 42.6\ \mathrm{MHz}$$

也就是说 **1 T 下质子 NMR 频率是 42.6 MHz**。这就是所有 NMR 谱仪的频率/磁场对应关系。

**为什么 MRI 用 1.5–3 T**：

1. **信号强度 $\propto B^2$**（一个 $B$ 来自塞曼分裂，一个来自玻尔兹曼布居比 $\Delta N/N \sim \Delta E/k_B T \propto B$）。所以更高磁场给更亮的图。

2. **分辨率 $\propto B$**：化学位移（不同分子环境的频率差）也按 $B$ 成正比。3 T MRI 的水脂分辨率明显好于 1.5 T。

3. **信噪比与采样时间的平衡**：MRI 一次扫描要几分钟，病人不能动。SNR 越高，扫描时间越短，病人越舒服。

**前沿**：现代研究 MRI 用 7 T 甚至 11.7 T 的超强场（neuro/research 级别）。10 T 以上的场需要超导磁体 + 液氦，成本很高，但对脑部细微结构分辨率提升显著。MIT/Harvard 的 11.7 T 人体 MRI 是世界上最强的。

**联系塞曼效应**：MRI 完全建立在 1896 年 Zeeman 实验的基础上。100 多年前一个"看光谱线分裂"的好奇心驱动的实验，今天每年帮助救治数千万患者。**这是基础研究产业化的最佳例子**。

</div>

</v-click>

---

# §22 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] P. Zeeman, "On the influence of magnetism on the nature of the light emitted by a substance," *Phil. Mag.* **43**, 226 (1897). 塞曼效应的原始论文。

[2] H. A. Lorentz, "The theorem of Poynting concerning the energy in the electromagnetic field and two general propositions concerning the propagation of light," *Versl. Kon. Akad. Wetensch.* **4**, 176 (1895). Lorentz 关于电子运动产生光辐射的理论，预言了塞曼效应。

[3] A. Lande, "Über den anomalen Zeemaneffekt I, II," *Z. Phys.* **5**, 231; **7**, 398 (1921). Lande $g$ 因子公式的原始论文。

[4] F. Paschen & E. Back, "Normale und anomale Zeemaneffekte," *Ann. Phys.* **39**, 897 (1912). Paschen-Back 效应的发现。

[5] G. E. Hale, "On the probable existence of a magnetic field in sun-spots," *Astrophys. J.* **28**, 315 (1908). 用塞曼效应第一次测得太阳黑子磁场。

[6] F. Bloch, "Nuclear Induction," *Phys. Rev.* **70**, 460 (1946). 核磁共振的发现，1952 年与 Purcell 共获诺贝尔物理学奖。

[7] P. C. Lauterbur, "Image Formation by Induced Local Interactions: Examples Employing Nuclear Magnetic Resonance," *Nature* **242**, 190 (1973). MRI 的奠基性论文，2003 年与 Mansfield 共获诺贝尔生理学或医学奖。

[8] J. F. Donati & J. D. Landstreet, "Magnetic Fields of Nondegenerate Stars," *Annu. Rev. Astron. Astrophys.* **47**, 333 (2009). Zeeman Doppler Imaging 在恒星磁场探测中的应用。

[9] B. H. Bransden & C. J. Joachain, *Physics of Atoms and Molecules*, 2nd ed., Ch. 9 (Pearson, 2003). 塞曼效应的标准教材推导。

</div>

---

# 第四章总结（一）：氢原子与轨道角动量

- **氢原子哈密顿量**：库仑势 $U(r) = -\dfrac{e^2}{4\pi\epsilon_0 r}$，球对称中心势

- **球坐标分离变量**：$\psi_{n\ell m}(\vec r) = R_{n\ell}(r)\, Y_\ell^m(\theta, \varphi)$

- **角动量量子化**：$|\vec L| = \sqrt{\ell(\ell+1)}\hbar$，$L_z = m\hbar$，从波函数标准条件**自然涌现**

- **能级公式**：$E_n = -\dfrac{13.6\ \mathrm{eV}}{n^2}$，简并度 $n^2$（库仑势的 SO(4) 特殊对称）

- **三个量子数 $(n, \ell, m)$**：$n$ 决定能量，$\ell$ 决定 $|\vec L|$，$m$ 决定 $L_z$

- **玻尔半径自然出现**：$a_0 = 0.529$ Å，最概然位置 $r_\max = a_0$，平均距离 $\langle r\rangle = \frac{3}{2} a_0$

- **玻尔模型 vs 薛定谔模型**：基态角动量 $1\hbar$（玻尔，错）vs $0$（薛定谔，对）

---

# 第四章总结（二）：磁矩与自旋

- **轨道磁矩**：$\vec\mu_L = -\dfrac{e}{2 m_e}\vec L$，玻尔磁子 $\mu_B = \dfrac{e\hbar}{2 m_e} \approx 9.27\times 10^{-24}$ J/T

- **Stern-Gerlach 实验（1922）**：银原子在非均匀磁场中分裂为**2 条**，违反 $2\ell+1$ 整数规则

- **Pauli 第四量子数（1925）**：电子有一个新的内禀自由度，2 个取值

- **Uhlenbeck-Goudsmit 自旋（1925）**：$s = \dfrac{1}{2}$，$m_s = \pm\dfrac{1}{2}$

- **反常 $g_s \approx 2$**：$\vec\mu_s = -g_s\dfrac{e}{2 m_e}\vec S$，QED 修正给出 $g_s = 2.00232\ldots$

- **Dirac 方程（1928）**：自旋是相对论的内禀属性，$g_s = 2$ 自然出现

- **完整 5 量子数**：$(n, \ell, m_\ell, s, m_s)$，每个 $n$ 能级有 $2 n^2$ 态，给出元素周期表的填充规律

---

# 第四章总结（三）：精细结构与塞曼效应

- **总角动量**：$\vec J = \vec L + \vec S$，量子数 $j = \ell \pm \dfrac{1}{2}$（电子）

- **自旋轨道耦合**：$\hat H_\text{LS} = \xi(r)\, \vec L\cdot\vec S$（含 Thomas 1926 因子 1/2）

- **精细结构能级劈裂**：$\dfrac{\Delta E_\text{LS}}{E_n} \sim Z^2 \alpha^2$，**精细结构常数** $\alpha \approx \dfrac{1}{137}$ 自然出场

- **钠 D 双线**：$3p_{1/2}, 3p_{3/2} \to 3s_{1/2}$ 是精细结构的肉眼可见证据

- **正常塞曼效应**（无自旋）：能级分裂 $\Delta E = m_\ell\, \mu_B B$，谱线 3 条等距

- **反常塞曼效应**（含自旋）：$\Delta E = g_J\, m_j\, \mu_B B$，**朗德 g 因子** $g_J$ 因 $(j, \ell, s)$ 而异

- **Paschen-Back 效应**（强场）：磁场压垮自旋轨道耦合，$\Delta E = (m_\ell + 2 m_s)\mu_B B$

- **现代应用**：NMR / MRI / ESR / 太阳磁场探测 / 量子计算，全部基于塞曼效应

---

# 第四章思考题（综合）

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.9em; border-left: 3px solid #C71585; margin-bottom: 0.4em; font-size: 0.85em; }
.q-tag { color: #C71585; font-weight: bold; }
</style>

<div class="q-card">

**思考 1**　<span class="q-tag">综合</span>　从第三章的"波函数 + 薛定谔方程"到第四章的"三量子数 + 自旋 + 精细结构"，量子力学解释了氢原子的哪些实验事实？还有哪些没解释？（提示：考虑超精细结构、Lamb 移位、电子自能。）

</div>

<div class="q-card">

**思考 2**　<span class="q-tag">概念</span>　"角动量量子化"是从波函数的什么物理条件得到的？为什么这些条件在经典物理中不存在？

</div>

<div class="q-card">

**思考 3**　<span class="q-tag">历史</span>　如果 Stern-Gerlach 当年用的是 $\mathrm{Zn}$（基态 $\ell = 0, S = 0$），实验会看到什么？这会改写量子力学的发展史吗？

</div>

<div class="q-card">

**思考 4**　<span class="q-tag">前沿</span>　$\alpha$、$g_s - 2$、$E_n = -E_0/n^2$ 这三个数字哪一个测量得最精确？它们各自检验了物理学的哪个层次（QM、QED、Standard Model）？

</div>

<div class="q-card">

**思考 5**　<span class="q-tag">深入</span>　电子自旋的实在性：电子真的在"转动"吗？如果不是，那么"自旋角动量"的物理意义是什么？想一想 Stern-Gerlach 实验和 Bell 不等式的实验结论。

</div>

---

# 第四章主要参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

**原始论文**：

[1] E. Schrödinger, "Quantisierung als Eigenwertproblem (Erste Mitteilung)," *Ann. Phys.* **384**, 361 (1926). 薛定谔解出氢原子。

[2] W. Pauli, "Über den Zusammenhang...," *Z. Phys.* **31**, 765 (1925). Pauli 不相容原理。

[3] G. E. Uhlenbeck & S. Goudsmit, *Naturwissenschaften* **13**, 953 (1925). 自旋假设的提出。

[4] P. A. M. Dirac, "The quantum theory of the electron," *Proc. Roy. Soc. A* **117**, 610 (1928). Dirac 方程。

[5] W. Gerlach & O. Stern, "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld," *Z. Phys.* **9**, 349 (1922). Stern-Gerlach 实验。

[6] L. H. Thomas, "The Motion of the Spinning Electron," *Nature* **117**, 514 (1926). Thomas 因子。

[7] P. Zeeman, "On the influence of magnetism...," *Phil. Mag.* **43**, 226 (1897). 塞曼效应。

**标准教材**：

[8] D. J. Griffiths & D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed. (Cambridge Univ. Press, 2018). 本科标准教材。

[9] J. J. Sakurai & J. Napolitano, *Modern Quantum Mechanics*, 3rd ed. (Cambridge Univ. Press, 2020). 研究生标准教材，从 Stern-Gerlach 开始讲量子力学。

[10] B. H. Bransden & C. J. Joachain, *Physics of Atoms and Molecules*, 2nd ed. (Pearson, 2003). 原子物理标准教材。

[11] H. Bethe & E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957). 单电子原子的权威专著。

[12] L. D. Landau & E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory*, 3rd ed., Vol. 3 (Pergamon, 1977). 经典理论物理教程。

**前沿与历史**：

[13] D. Hanneke, S. Fogwell, & G. Gabrielse, *Phys. Rev. Lett.* **100**, 120801 (2008). 电子 $g - 2$ 的精密测量。

[14] R. Parker et al., *Science* **360**, 191 (2018). 精细结构常数 $\alpha$ 的最精密测量。

[15] B. Friedrich & D. Herschbach, "Stern and Gerlach: How a bad cigar helped reorient atomic physics," *Physics Today* **56** (12), 53 (2003). Stern-Gerlach 历史。

[16] S. Tomonaga, *The Story of Spin* (Univ. of Chicago Press, 1997). 朝永振一郎写的自旋发现史。

[17] D. Castelvecchi, "The Stern-Gerlach experiment at 100," *Nature Physics* **18**, 364 (2022). 实验百年纪念。

</div>
