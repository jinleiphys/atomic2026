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

# 第四章 原子的精细结构：电子的自旋

金 磊

办公室：瑞安楼703B

邮箱：jinl@tongji.edu.cn

---

# §17 氢原子

需要掌握的知识点：

用波函数、概率密度、总能量和轨道角动量来描述氢原子

识别氢原子的每个量子数 (n,l,m) 的物理意义

区分原子的玻尔模型和薛定谔模型

使用量子数计算有关氢原子的重要信息

---

# 氢原子

$m_p\approx 1800~m_e$

假设质子不动，电子围绕质子运动

相互作用势能为

$U(r) =-\frac{1}{4\pi\epsilon_0}\frac{e^2}{r}$

$U(r)$ 不依赖于时间，因此满足定态薛定谔方程

<img src="/images/CNX_UPhysics_41_01_HydAtom-1-26259.jpg" style="max-width: 429px; max-height: 400px;" />

---

# 一维薛定谔方程的解

$V_\mathrm{pot} = 0$

考虑一维无限深方势阱

$0<x<a$

这种势能分布即为无限深方势阱

粒子处于束缚态：

粒子被限制在￼范围内，不可能到此范围外

<img src="/images/Screen Shot 2022-03-28 at 15.36.27-30332.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/CodeCogsEqn-2-30381.png" style="max-width: 500px; max-height: 400px;" />

---

# 一维薛定谔方程的解

$V_\mathrm{pot} = 0$

$V=0$

由于势函数不随时间变化，所以属定态解。

阱内： $\frac{\mathrm{d}^{2} \psi}{\mathrm{d} x^{2}}+k^{2} \psi=0 \quad \text { with } \quad k^{2}=\frac{2 m E}{\hbar^{2}}$ ，方程为

满足边界条件，

$\psi(x<0)=\psi(x>a)=0$

即粒子不能到达上述区域

Ansatz：薛定谔方程的解为 $\psi(x)=A \mathrm{e}^{\mathrm{i} k x}+B \mathrm{e}^{-\mathrm{i} k x}$

边界条件 $\psi(x=0)=0$ ，给出 $A+B =0$

代入薛定谔方程的解可为 $\psi(x)=A\left(\mathrm{e}^{\mathrm{i} k x}-\mathrm{e}^{-\mathrm{i} k x}\right)=2 \mathrm{i} A \sin (k x)$

<img src="/images/Screen Shot 2022-03-28 at 15.36.27-30332.png" style="max-width: 500px; max-height: 400px;" />

---

# 一维薛定谔方程的解

$V_\mathrm{pot} = 0$

$\psi(x)=2 \mathrm{i} A \sin \left(\frac{n \pi}{a} x\right)=C \sin \left(\frac{n \pi}{a} x\right)$

因此波函数可变为 $\psi(x=a)=0$

边界条件 $2 \mathrm{i} A \sin (k a)=0 \Rightarrow k a=n \pi \quad(n=1,2,3, \ldots) .$ ，给出 $k a=n \pi$

由归一化条件有

<img src="/images/Screen Shot 2022-03-28 at 15.36.27-30332.png" style="max-width: 500px; max-height: 400px;" />

---

# 一维薛定谔方程的解

$V_\mathrm{pot} = 0$

$k^{2}=\frac{2 m E}{\hbar^{2}}$

由 $k=\frac{n \pi}{a}$ 和 $E_{n}=\frac{\pi^{2} \hbar^{2}}{2 m a^{2}} n^{2} \quad n=1,2,3, \cdots$ 解得：

定态能量本征值：

$n=1$

零点能:最低的能级是 $E_{1}=\frac{\pi^{2} \hbar^{2}}{2 m a^{2}} \neq 0$ 能级

$E=0$

若 $p=\sqrt{2 m E}=0$ ， $\Delta p =0$ ,  $\Delta x \to \infty$ , 则 $\Delta x = a$ ，但势阱中 $E$ ，所以￼不能为零。

<img src="/images/Screen Shot 2022-03-28 at 15.36.27-30332.png" style="max-width: 500px; max-height: 400px;" />

---

# 一维无限深势阱

$\psi(x)$

<img src="/images/Screenshot 2023-04-03 at 12.51.24-35724.png" style="max-width: 500px; max-height: 400px;" />

---

# 一维无限深势阱

$E_{n}=\frac{\pi^{2} \hbar^{2}}{2 m a^{2}} n^{2} \quad n=1,2,3, \cdots$

<img src="/images/Screenshot 2023-04-03 at 12.59.42-35753.png" style="max-width: 500px; max-height: 400px;" />

---

# 一维无限深势阱-不确定性原理

$\Delta p \Delta x \geq h / 2$

不确定性原理： $\Delta x =a$

$p \geq \Delta p \geq \frac{h}{2 a} \Rightarrow E_{\min }=\frac{p_{\min }^2}{2 m} \geq \frac{h^2}{8 m a^2}=\frac{\hbar^2 \pi^2}{2 m a^2}$ ，可得

同时可得

---

# 一维无限深势阱V.S.有限深方势阱

$E_{\mathrm{pot}}= \begin{cases}E_0 & \text { elsewhere } \\ 0 &  \text { for } 0 \leq x \leq a\end{cases}$

how about  $E> E_0$ ?

<img src="/images/Screenshot 2023-04-03 at 13.18.12-35842.png" style="max-width: 500px; max-height: 400px;" />

---

# 二维薛定谔方程的解

$V_\mathrm{pot} = \infty$

$\psi(x, y)=f(x) g(y)$

考虑二维无限深方势阱

Ansatz：波函数可分离 $-\frac{\hbar^{2}}{2 m} (\frac{\partial^{2} }{\partial x^{2}}+\frac{\partial^{2} }{\partial y^{2}})\psi+V_{\text {pot }} \psi=E \psi$

波函数满足薛定谔方程

满足边界条件 $\psi(0,\ 0)=\psi(0,\ b)= \psi(a,0)=\psi(a,b)=0$

<img src="/images/Screen Shot 2022-03-28 at 18.58.46-30733.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/CodeCogsEqn-3-30776.png" style="max-width: 500px; max-height: 400px;" />

---

# 二维薛定谔方程的解

$V_\mathrm{pot} = \infty$

$\begin{aligned}

&f(x)=A \sin \left(\frac{n_{x} \pi x}{a}\right) \\

&g(y)=B \sin \left(\frac{n_{y} \pi y}{b}\right)

\end{aligned}$

类似于一维无限深势阱，

因此波函数可写为

满足归一化条件

<img src="/images/Screen Shot 2022-03-28 at 18.58.46-30733.png" style="max-width: 500px; max-height: 400px;" />

---

# 二维薛定谔方程的解

$E(n_x,n_y)=\frac{\pi^{2} \hbar^{2}}{2 m } \Big(\frac{n_x^{2}}{a^{2}}+\frac{n_y^{2}}{b^{2}}\Big)$

定态能量本征值：

$a>b$

<img src="/images/Screenshot 2023-04-03 at 13.35.38-35880.png" style="max-width: 500px; max-height: 400px;" />

---

# 二维薛定谔方程的解

$\psi(x, y)=\frac{2}{\sqrt{ab}} \sin \left(\frac{n_{x} \pi x}{a}\right) \sin \left(\frac{n_{y} \pi y}{b}\right)$

波函数：

￼

<img src="/images/Screenshot 2023-04-03 at 13.46.16-35904.png" style="max-width: 500px; max-height: 400px;" />

---

# 角动量

$\vec{r}$

经典情况下的角动量

量子力学下的角动量

---

# 量子力学下的角动量

$\hat{L}_x=\hat{y}\hat{p}_z-\hat{z}\hat{p}_y,$

直角坐标

---

# 直角坐标与球坐标的转换

$x,y,z \in (-\infty,\infty)$

<img src="/images/3D_Cartesian.svg-31297.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/480px-3D_Spherical.svg-26376.png" style="max-width: 480px; max-height: 400px;" />

---

# 球坐标下的角动量（量子）

$\hat{L}_z=-i\hbar (x\frac{\partial }{\partial y}-y\frac{\partial }{\partial x})$

以 $\hat{L}_z$ 为例讨论如何做坐标变换

需要求解的项

---

# 球坐标下的角动量（量子）

$r^{2}=x^{2}+y^{2}+z^{2}$

对等式两边分别求导

---

# 球坐标下的角动量（量子）

$\cos \theta=\frac{z}{r} \underset{\frac{\partial}{\partial y}}{\Longrightarrow}-\sin \theta \frac{\partial \theta}{\partial y}=z \frac{\partial}{\partial y}\left(\frac{1}{r}\right)$

---

# 球坐标下的角动量（量子）

$\tan \varphi=\frac{y}{x} \underset{\frac{\partial}{\partial y}}{\Longrightarrow}  \frac{1}{\cos ^{2} \varphi} \frac{\partial \varphi}{\partial y}=\frac{1}{x}$

---

# 球坐标下的角动量（量子）

$\frac{\partial}{\partial y}=\sin \theta \sin \varphi \frac{\partial}{\partial r}+\frac{\cos \theta \sin \varphi}{r} \frac{\partial}{\partial \theta}+\frac{\cos \varphi}{r \sin \theta} \frac{\partial}{\partial \varphi}$

---

# 球坐标下的角动量（量子）

$\hat{L}_{x}=i \hbar\left(\sin \phi \frac{\partial}{\partial \theta}+\frac{\cos \phi}{\tan \theta} \frac{\partial}{\partial \phi}\right)$

---

# 球坐标下的拉普拉斯算符

$\begin{aligned}

\frac{\partial}{\partial x} &=\frac{\partial}{\partial r} \frac{\partial r}{\partial x}+\frac{\partial}{\partial \theta} \frac{\partial \theta}{\partial x}+\frac{\partial}{\partial \varphi} \frac{\partial \varphi}{\partial x} \\

&=\sin \theta \cos \varphi \frac{\partial}{\partial r}+\frac{1}{r} \cos \theta \cos \varphi \frac{\partial}{\partial \theta}-\frac{\sin \varphi}{r \sin \theta} \frac{\partial}{\partial \theta} \\

\end{aligned}$

已知

---

# 球坐标下的拉普拉斯算符

$\nabla^{2}=\vec{\nabla} \cdot \vec{\nabla}=\left(\hat{r} \frac{\partial}{\partial r}+\frac{\hat{\theta}}{r} \frac{\partial}{\partial \theta}+\frac{\hat{\varphi}}{r \sin \theta} \frac{\partial}{\partial \varphi}\right) \cdot\left(\hat{r} \frac{\partial}{\partial r}+\frac{\hat{\theta}}{r} \frac{\partial}{\partial \theta}+\frac{\hat{\varphi}}{r \sin \theta} \frac{\partial}{\partial \varphi}\right) .$

---

# 等式左边

等式右边

$\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial}{\partial r}\right)f(r)=\frac{1}{r} \frac{\partial^{2}}{\partial r^{2}} r f(r)$

---

# 球坐标下的拉普拉斯方程（数学物理方法）

$\nabla^{2} f=\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial f}{\partial r}\right)-\frac{1}{\hbar^{2} r^{2}} \hat{L}^{2} f=0$

Ansatz：方程的解 $f(r, \theta, \varphi)=R(r) Y(\theta, \varphi)$ ，代入上式可得

上式左右两边同时乘以 $Y\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial R}{\partial r}\right)-\frac{R}{\hbar^{2} r^{2}} \hat{L}^{2} Y=0$ ,可得

---

# 球谐函数

$\lambda=\ell(\ell+1)$

其中 $\hat{L}^2$ ，即 $\ell(\ell+1)\hbar^2$ 的本征值为 $Y_{\ell}^{m}(\theta, \varphi)=N e^{i m \varphi} P_{\ell}^{m}(\cos \theta)$ ，本征函数为 $\ell$

对于给定的 $2\ell+1$ 值，有 $\quad \frac{1}{Y} \frac{1}{\hbar^2}\hat{L}^2Y=\lambda$ 个这种形式的独立解

$\hat{L}^2Y= \lambda\hbar^2 Y$ 的取值范围为 $\ell$

同时 $\ell = 0, 1, 2,...$ 还是 $Y_{\ell}^{m}(\theta, \varphi)$ 的本征函数

$\hat{L}_z$ 的取值范围为 $\hat{L}_z\  Y_\ell ^m(\theta, \varphi ) = m\hbar \ Y_\ell ^m(\theta, \varphi )$

---

# 球坐标下的定态薛定谔方程

$-\frac{\hbar^{2}}{2 m_e}\left[\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial \psi}{\partial r}\right)-\frac{1}{\hbar^{2} r^{2}} \hat{L}^{2}\psi\right]+U \psi=E \psi$

使用分离变量法 $\psi(r, \theta, \varphi)=R(r) Y(\theta, \varphi)$ ，则

两边除以 $-\frac{\hbar^{2}}{2 m_e}\left[\frac{Y}{r^{2}} \frac{d}{d r}\left(r^{2} \frac{d R}{d r}\right)-\frac{R}{\hbar^{2} r^{2}} \hat{L}^{2}Y\right]+U R Y=E R Y$ ，并乘 $RY$ 系数可得

即

当U为中心势场，只依赖于r时

---

# 球谐函数与角动量 $\ell$

$\ell$

对于一个固定整数 $Y$ ，每个解 $r^{2} \nabla^{2} Y=-\ell(\ell+1) Y$ 满足

宏观上角动量定义为

连续值

量子力学中角动量定义为

量子化，只能取离散的值

---

# 球谐函数与量子角动量

伴随勒让德多项式

$Y_{l}^{m}(\theta, \varphi)=(-1)^{m} \sqrt{\frac{(2 l+1)(l-m) !}{4 \pi(l+m) !}} e^{i m \varphi} P_{l}^{m}(\cos \theta)$

把 $\theta$ 和 $\varphi$ 相关的量分离可得

其中

---

# 球谐函数的可视化

$Y_{l}^{m}(\theta, \varphi)=\frac{(-1)^{l}}{2^{l} l !} \sqrt{\frac{(2 l+1)(l+m) !}{4 \pi(l-m) !}} e^{i m \varphi}(\sin \theta)^{-m} \frac{d^{l-m}}{d(\cos \theta)^{l-m}}(\sin \theta)^{2 l}$

红色：正值  蓝色：负值

<img src="/images/Screen Shot 2022-04-06 at 22.34.28-32655.png" style="max-width: 500px; max-height: 400px;" />

---

# 球谐函数的可视化

$Y_{l}^{m}(\theta, \varphi)=\frac{(-1)^{l}}{2^{l} l !} \sqrt{\frac{(2 l+1)(l+m) !}{4 \pi(l-m) !}} e^{i m \varphi}(\sin \theta)^{-m} \frac{d^{l-m}}{d(\cos \theta)^{l-m}}(\sin \theta)^{2 l}$

红色：正值  蓝色：负值

<video controls style="max-width: 500px;">
  <source src="/images/11-32871.gif" />
</video>

---

# 球谐函数的可视化

$Y_{l}^{m}(\theta, \varphi)=\frac{(-1)^{l}}{2^{l} l !} \sqrt{\frac{(2 l+1)(l+m) !}{4 \pi(l-m) !}} e^{i m \varphi}(\sin \theta)^{-m} \frac{d^{l-m}}{d(\cos \theta)^{l-m}}(\sin \theta)^{2 l}$

---

# 球谐函数的可视化

$Y_{0}^{0}(\theta, \varphi)=\frac{1}{\sqrt{4 \pi}}$

---

# 球谐函数的可视化

$Y_{l}^{m}(\theta, \varphi)=\frac{(-1)^{l}}{2^{l} l !} \sqrt{\frac{(2 l+1)(l+m) !}{4 \pi(l-m) !}} e^{i m \varphi}(\sin \theta)^{-m} \frac{d^{l-m}}{d(\cos \theta)^{l-m}}(\sin \theta)^{2 l}$

---

# 球谐函数的可视化

$Y_{1}^{-1}(\theta, \varphi)=\sqrt{\frac{3}{8 \pi}} e^{-i \varphi} \sin \theta=\sqrt{\frac{3}{8 \pi}} \cos \varphi \sin \theta-i \sqrt{\frac{3}{8 \pi}} \sin \varphi \sin \theta$

<img src="/images/Screen Shot 2022-04-06 at 23.35.54-33035.png" style="max-width: 428px; max-height: 400px;" />

<img src="/images/Screen Shot 2022-04-06 at 23.35.54-33035.png" style="max-width: 428px; max-height: 400px;" />

---

# 球谐函数的可视化

$Y_{1}^{-1}(\theta, \varphi)=\sqrt{\frac{3}{8 \pi}} e^{-i \varphi} \sin \theta=\sqrt{\frac{3}{8 \pi}} \cos \varphi \sin \theta-i \sqrt{\frac{3}{8 \pi}} \sin \varphi \sin \theta$

<img src="/images/Screen Shot 2022-04-06 at 23.35.54-33035.png" style="max-width: 428px; max-height: 400px;" />

<img src="/images/Screen Shot 2022-04-06 at 23.35.54-33035.png" style="max-width: 428px; max-height: 400px;" />

---

# 球谐函数的可视化

$Y_{1}^{-1}(\theta, \varphi)=\sqrt{\frac{3}{8 \pi}} e^{-i \varphi} \sin \theta=\sqrt{\frac{3}{8 \pi}} \cos \varphi \sin \theta-i \sqrt{\frac{3}{8 \pi}} \sin \varphi \sin \theta$

<video controls style="max-width: 500px;">
  <source src="/images/11-32871.gif" />
</video>

<video controls style="max-width: 500px;">
  <source src="/images/11-32871.gif" />
</video>

---

# 球谐函数的可视化

$Y_{l}^{m}(\theta, \varphi)=\frac{(-1)^{l}}{2^{l} l !} \sqrt{\frac{(2 l+1)(l+m) !}{4 \pi(l-m) !}} e^{i m \varphi}(\sin \theta)^{-m} \frac{d^{l-m}}{d(\cos \theta)^{l-m}}(\sin \theta)^{2 l}$

<img src="/images/Screen Shot 2022-04-06 at 23.59.22-33235.png" style="max-width: 302px; max-height: 400px;" />

---

# 球谐函数的可视化

$Y_{l}^{m}(\theta, \varphi)=\frac{(-1)^{l}}{2^{l} l !} \sqrt{\frac{(2 l+1)(l+m) !}{4 \pi(l-m) !}} e^{i m \varphi}(\sin \theta)^{-m} \frac{d^{l-m}}{d(\cos \theta)^{l-m}}(\sin \theta)^{2 l}$

---

# 球谐函数的可视化

$Y_{1}^{1}(\theta, \varphi)=-\sqrt{\frac{3}{8 \pi}} e^{i \varphi} \sin \theta=-\sqrt{\frac{3}{8 \pi}} \cos \varphi \sin \theta-i \sqrt{\frac{3}{8 \pi}} \sin \varphi \sin \theta$

<img src="/images/Screen Shot 2022-04-06 at 23.35.54-33035.png" style="max-width: 428px; max-height: 400px;" />

<img src="/images/Screen Shot 2022-04-07 at 00.18.15-33355.png" style="max-width: 260px; max-height: 400px;" />

---

# 球谐函数的可视化（一）

$rY$

等高线图,颜色表示大小，计算￼

<video controls style="max-width: 445px;">
  <source src="/images/Rotating_spherical_harmonics-26522.gif" />
</video>

<video controls style="max-width: 500px;">
  <source src="/images/τÉâΦ░Éσç╜µò░-σ╝òσè¢σ£║-26829.mp4" />
</video>

---

# 球谐函数的可视化（二）

$x=|Y| \cos \varphi \sin \theta$

<img src="/images/Sphericalfunctions.svg-2-26756.png" style="max-width: 500px; max-height: 400px;" />

---

# 球谐函数的可视化（三）

$(r+|Y|)Y$

等高线图的基础上变化半径，计算￼

Earth Syst. Sci. Data, 11, 647–674, 2019

<img src="/images/ICGEM_-15_years_of_successful_collection_and_distr-26851.jpg" style="max-width: 500px; max-height: 400px;" />

<img src="/images/ICGEM_-15_years_of_successful_collection_and_distr-26872.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 量子角动量

$\begin{aligned}

& \hat{L}_x=\mathrm{i} \hbar\left(\sin \varphi \frac{\partial}{\partial \vartheta}+\operatorname{cotan} \vartheta \cos \varphi \frac{\partial}{\partial \varphi}\right) \\

& \hat{L}_y=\mathrm{i} \hbar\left(-\cos \varphi \frac{\partial}{\partial \vartheta}+\operatorname{cotan} \vartheta \sin \varphi \frac{\partial}{\partial \varphi}\right) \\

& \hat{L}_z=-\mathrm{i} \hbar \frac{\partial}{\partial \varphi}

\end{aligned}$

已知

以及

---

# 量子角动量

$\hat{L}^{2} Y_{l}^{m}(\theta, \varphi)=l(l+1) \hbar^{2} Y_{l}^{m}(\theta, \varphi)$

我们又知道 $\hat{L}^{2} \psi(r,\theta,\phi) = ?$

那么当 $\begin{aligned}

\hat{L}^2 \psi & =\hat{L}^2\left(R(r) Y_l^m(\vartheta, \varphi)=R(r) \hat{L}^2 Y_l^m(\vartheta, \varphi)\right. \\

& =R(r) l(l+1) \hbar^2 Y_l^m(\vartheta, \varphi)=l(l+1) \hbar^2 \psi

\end{aligned}$

期望值为

绝对值为

---

# 量子角动量

$\hat{L}_x \psi = ?$

那么 $\hat{L}_x \psi \neq m_x \psi$

但是我们知道 $L_x^2+L_y^2=L^2 - L^2_z$

---

# 薛定谔方程的解

$\frac{1}{R} \frac{d}{d r}\left(r^{2} \frac{d R}{d r}\right)-\frac{2 m_e r^{2}}{\hbar^{2}}[U(r)-E]=\ell(\ell+1)$

注意径向波函数与能量都不依赖于 $\frac{1}{Y}\left\{\frac{1}{\hbar^2}\hat{L}^2Y\right\}=\ell(\ell+1)$

---

# 径向薛定谔方程的解

$\left[-\frac{\hbar^{2}}{2 \mu} \frac{1}{r} \frac{d^{2}}{d r^{2}} r+\frac{l(l+1) \hbar^{2}}{2 \mu r^{2}}-\frac{1}{4 \pi \epsilon_{0}} \frac{e^{2}}{r}\right] R_{k l}(r)=E_{k l} R_{k l}(r)$

令 $R_{k l}(r)=\frac{1}{r} u_{k l}(r)$ ，则

已知 $\left[-\frac{\hbar^{2}}{2 \mu} \frac{d^{2}}{d r^{2}}+\frac{l(l+1) \hbar^{2}}{2 \mu r^{2}}-\frac{1}{4 \pi \varepsilon_{0}} \frac{e^{2}}{r}\right] u_{k l}(r)=E_{k l} u_{k l}(r)$ ，则 $u_{k l}(r)=r R_{k l}(r)$

---

# 径向薛定谔方程的解

$\left[-\frac{\hbar^{2}}{2 \mu} \frac{d^{2}}{d r^{2}}+\frac{l(l+1) \hbar^{2}}{2 \mu r^{2}}-\frac{1}{4 \pi \varepsilon_{0}} \frac{e^{2}}{r}\right] u_{k l}(r)=E_{k l} u_{k l}(r)$

束缚态

离散能级

波函数平方可积

---

# 径向薛定谔方程的解

$\left[-\frac{\hbar^{2}}{2 \mu} \frac{d^{2}}{d r^{2}}+\frac{l(l+1) \hbar^{2}}{2 \mu r^{2}}-\frac{1}{4 \pi \varepsilon_{0}} \frac{e^{2}}{r}\right] u_{k l}(r)=E_{k l} u_{k l}(r)$

“玻尔半径”

“里德伯能量”

---

# 径向薛定谔方程的解

$E_{kl} < 0$

令

---

# 径向薛定谔方程的解

$\left[\frac{d^{2}}{d \rho^{2}}-\frac{l(l+1)}{\rho^{2}}+\frac{2}{\rho}-\lambda_{k l}^{2}\right] u_{k l}(\rho)=0$

当 $\rho \longrightarrow \infty$ 时

当 $\left[\frac{d^{2}}{d \rho^{2}}-\lambda_{k l}^{2}\right] u_{k l}(\rho)=0$ 时

方程的解为

当 $\rho \longrightarrow \infty$ 时，Ansatz方程的解为

---

# 径向薛定谔方程的解

$\frac{d^{2}}{d \rho^{2}}\left[e^{-\lambda_{k l} \rho} v_{k l}(\rho)\right]=\left(\frac{d^{2}}{d \rho^{2}} e^{-\lambda_{k l} \rho}\right) v_{k l}(\rho)+2\left(\frac{d}{d \rho} e^{-\lambda_{k l} \rho}\right)\left(\frac{d}{d \rho} v_{k l}(\rho)\right)+e^{-\lambda_{k l} \rho} \frac{d^{2}}{d \rho^{2}} v_{k l}(\rho)$

代入上式可得

---

# 径向薛定谔方程的解

$\left[\frac{d^{2}}{d \rho^{2}}-2 \lambda_{k l} \frac{d}{d \rho}+\frac{2}{\rho}-\frac{l(l+1)}{\rho^{2}}\right] v_{k l}(\rho)=0$

---

# 径向薛定谔方程的解

$c_{0} \neq 0$

---

# 径向薛定谔方程的解

$\left[\frac{d^{2}}{d \rho^{2}}-2 \lambda_{k l} \frac{d}{d \rho}+\frac{2}{\rho}-\frac{l(l+1)}{\rho^{2}}\right] v_{k l}(\rho)=0$

---

# 径向薛定谔方程的解

$(q+l+1)(q+l)-l(l+1)=q^{2}+q l+q(l+1)+l(l+1)-l(l+1)$

…

---

# 径向薛定谔方程的解

$\left[\frac{d^{2}}{d \rho^{2}}-2 \lambda_{k l} \frac{d}{d \rho}+\frac{2}{\rho}-\frac{l(l+1)}{\rho^{2}}\right] v_{k l}(\rho)=0$

通过波函数的归一化确定 $v_{k l}(0) = 0$

考虑收敛性条件 $v_{k l}(\rho)=\sum_{q=0}^{\infty} c_{q} \rho^{q+s}$ 时 $\frac{c_{q}}{c_{q-1}}=\frac{2\left(\lambda_{k l}(q+l)-1\right)}{q(q+2 l+1)} \quad c_{0} \neq 0$ （当 $c_{q} \propto c_{0} \ \ \Longrightarrow \ \  v_{k l}(\rho) \propto c_{0}$ ），可得

能级与玻尔模型一致

---

# 径向薛定谔方程的解

$\frac{c_{q}}{c_{q-1}}=\frac{2\left(\lambda_{k l}(q+l)-1\right)}{q(q+2 l+1)}$

---

# 径向薛定谔方程的解

$\frac{c_{q}}{c_{q-1}}=-\frac{2(j-q)}{q(q+2 l+1)(j+l)}$

---

# 薛定谔方程的解

$\hat{H} \psi_{k l m_{l}}(\vec{r})=E_{k l} \psi_{k l m_{l}}(\vec{r})$

---

# 薛定谔方程的解

$n$

当 $E_{k l}=-E_{0} \lambda_{k l}^{2}=-\frac{E_{0}}{(j+l)^{2}}=-\frac{E_0}{n^2}$ 确定时，能量 $l$ 确定，但是 $N=\left(Z / n a_0\right)^{3 / 2}$ 不确定

<img src="/images/Screen Shot 2023-04-10 at 19.59.32-36094.png" style="max-width: 500px; max-height: 400px;" />

---

# 薛定谔方程的解

<img src="/images/Screen Shot 2023-04-10 at 20.27.27-36168.png" style="max-width: 500px; max-height: 400px;" />

---

# 薛定谔方程的解

径向波函数

<img src="/images/Screen Shot 2023-04-10 at 20.31.01-36187.png" style="max-width: 500px; max-height: 400px;" />

---

# 薛定谔方程的解

$2s$

$2p$

$m=0$

<img src="/images/Screen Shot 2023-04-10 at 20.35.10-36204.png" style="max-width: 500px; max-height: 400px;" />

---

# 薛定谔方程的解

<img src="/images/Screen Shot 2023-04-10 at 20.41.04-36228.png" style="max-width: 500px; max-height: 400px;" />

---

# 薛定谔方程的解

$P(r) \mathrm{d} r=\int_{\vartheta=0}^\pi \int_{\varphi=0}^{2 \pi}|\psi(r, \vartheta, \varphi)|^2 r^2 \mathrm{~d} r \sin \vartheta \mathrm{d} \vartheta \mathrm{d} \varphi$

氢原子中电子的概率

对于基态，即 $n=1, \ \ell =0,\  m=0$

电子和原子核之间平均距离 $P(r) \mathrm{d} r=\frac{4 Z^3}{a_0^3} r^2 \mathrm{e}^{-2 Z r / a_0} \mathrm{~d} r$

---

# 薛定谔方程的解

$\langle r \rangle$

电子和原子核之间平均距离 $\langle r\rangle=\int_{r=0}^{\infty} \int_{\vartheta=0}^\pi \int_{\varphi=0}^{2 \pi} r|\psi(r, \vartheta, \varphi)|^2 r^2 \sin \vartheta \mathrm{d} \vartheta \mathrm{d} \varphi \mathrm{d} r$

即

不同于玻尔半径

<img src="/images/Screen Shot 2023-04-10 at 21.03.06-36315.png" style="max-width: 500px; max-height: 400px;" />

---

# 主量子数，角动量量子数，磁量子数

$n$

主量子数 $\ell$ 表示能级，也表示电子到原子核的平均距离

角动量量子数 $\ell$ ，代表轨道的形状， $\ell = 0,1,2,...,(n-1)$ 的取值范围为 $m$

磁量子数 $m$ ，表示轨道的方向， $m=-\ell, (-\ell+1),...,0,...,(\ell-1),\ell$ 的取值范围为 $\ell =0$

$m=0$ ， ￼

<img src="/images/The-Shape-of-s-Orbitals-700x327-27596.png" style="max-width: 500px; max-height: 400px;" />

---

# 主量子数，角动量量子数，磁量子数

$n$

主量子数 $\ell$ 表示能级，也表示电子到原子核的平均距离

角动量量子数 $\ell$ ，代表轨道的形状， $\ell = 0,1,2,...,(n-1)$ 的取值范围为 $m$

磁量子数 $m$ ，表示轨道的方向， $m=-\ell, (-\ell+1),...,0,...,(\ell-1),\ell$ 的取值范围为 $\ell =1$

$m=-1,0,1$ ，  $m=1$

<img src="/images/CNX_UPhysics_41_01_EOrbitals-1-27608.jpg" style="max-width: 500px; max-height: 400px;" />

---

# §18 原子中电子轨道运动的磁矩（半经典）

需要掌握的知识点：

解释为什么氢原子具有磁性

使用量子数计算氢原子轨道磁偶极矩的大小

---

# 氢原子的磁矩

$$\mu=I A$$

一个载流回圈的磁偶极矩 $I$ ，其中 $A$ 为电流， $$I=\frac{e}{T}$$ 为面积

如果我们假设电子在一个完美的圆形轨道上运行，那么轨道周期是

<img src="/images/CNX_UPhysics_41_02_AtomicLoop-1-27950.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 氢原子的磁矩

$$\mu=I A=\frac{e}{\left(\frac{2 \pi r}{v}\right)} \pi r^{2}=\frac{e v r}{2}$$

玻尔的氢原子模型中磁偶极矩为

同时 $\mu$ 也可以用角动量 $\overrightarrow{\mathbf{L}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}$ 来描述

比较两式可得

写成矢量形式

负号：电子带负电

---

# 氢原子的磁矩

$$\mu=I A=\frac{e}{\left(\frac{2 \pi r}{v}\right)} \pi r^{2}=\frac{e v r}{2}$$

玻尔的氢原子模型中磁偶极矩为

同时 $\mu$ 也可以用角动量 $\overrightarrow{\mathbf{L}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}$ 来描述

比较两式可得

写成矢量形式

负号：电子带负电

<img src="/images/CNX_UPhysics_41_02_AtomicLoop-1-27950.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 氢原子的磁矩（半经典）

$\mu$

磁矩 $\ell$ 也可以用轨道角量子数 $\mu=-\left(\frac{e}{2 m_{e}}\right) L=-\left(\frac{e}{2 m_{e}}\right) \sqrt{l(l+1)} \hbar=-\mu_{\mathrm{B}} \sqrt{l(l+1)}$ 表示

$\mu_B$ 玻尔磁子

磁矩在 $z$ 方向的投影 $\mu_z$ 为

---

# 习题

$s$

(a) $p$ 态、(b) $d$ 态和 (c) $\mu$ 态的氢原子中电子的磁矩 $\mu=-\left(\frac{e}{2 m_{e}}\right) L=-\left(\frac{e}{2 m_{e}}\right) \sqrt{l(l+1)} \hbar=-\mu_{\mathrm{B}} \sqrt{l(l+1)}$ 的大小是多少？

对于 $s$ 态,  $\ell=0$ ， 于是 $\mu=0$ 和 $\mu_z=0$

对于 $p$ 态,  $\ell=1$ ，我们有

$\begin{aligned}

&\mu=-\mu_{\mathrm{B}} \sqrt{1(1+1)}=-\sqrt{2} \mu_{\mathrm{B}} \\

&\mu_{z}=-\mu_{\mathrm{B}} m, \text { where } m=(-1,0,1), \text { so } \\

&\mu_{z}=\mu_{\mathrm{B}}, 0,-\mu_{\mathrm{B}} .

\end{aligned}$

对于 $d$ 态,  $\ell=2$ ，我们有

$\begin{aligned}

&\mu=-\mu_{\mathrm{B}} \sqrt{2(2+1)}=-\sqrt{6} \mu_{\mathrm{B}} \\

&\mu_{z}=-\mu_{\mathrm{B}} m, \text { where } m=(-2,-1,0,1,2), \text { so } \\

&\mu_{z}=2 \mu_{\mathrm{B}}, \mu_{\mathrm{B}}, 0,-\mu_{\mathrm{B}},-2 \mu_{\mathrm{B}} .

\end{aligned}$

---

# §19 施特恩—盖拉赫(Stern-Gerlach)实验

Stern-Gerlach 1921年首次对原子在磁场中（角动量/磁矩）的空间量子化进行了实验观察，1943年Nobel奖

---

# 原子在磁场中的受力

$\vec{\tau}=\vec{\mu} \times \vec{B}$

原子在磁场中的力矩与势能

如果外部磁场指向正 $U=-\int_{\frac{\pi}{2}}^{\theta} \vec{\tau} d \vec{\theta}=\int_{\frac{\pi}{2}}^{\theta} \tau d \theta=\int_{\frac{\pi}{2}}^{\theta} \mu B \sin \theta d \theta=-\vec{\mu} \cdot \vec{B}$ 方向，则与轨道磁偶极矩相关的势能为

所受力为

---

# 施特恩—盖拉赫(Stern-Gerlach)实验

$\mu$

目的：证明原子在外磁场中的空间量子化。

原理：磁矩为￼的小磁体，在横向非均匀磁场中受到的合力不为零：

<video controls style="max-width: 500px;">
  <source src="/images/spin-28555.mp4" />
</video>

---

# 实验说明

$\mu_z$

方法：基态银原子束以相同的速度方向通过与速度方向垂直的不均匀磁场，不同 $\mu_z$ 的原子受力不同，因而落在照相底片上位置不同。由底片上银原子的分布情况可以判断 $\mu_z=\mu_B$ 的分布情况。

结果：相片上有两条黑斑，两者对称分布，表明Ag原子经不均匀磁场时分为两束。

结论：

基态银原子有磁矩，且￼;

磁矩相对于磁场的取向有两种可能

<img src="/images/showOpenGraphArticleImage-28714.gif" style="max-width: 500px; max-height: 400px;" />

---

# 实验分析

$S=\frac{1}{2} a t^{2}=\frac{1}{2} \frac{f}{m}\left(\frac{L}{v}\right)^{2}=\frac{1}{2 m} \frac{d B}{d Z}\left(\frac{L}{v}\right)^{2} \mu_{Z}=-\frac{1}{2 m} \frac{d B}{d Z}\left(\frac{L}{v}\right)^{2} \mu_B m$

Ag原子的运动类似平抛运动，偏转距离为:

实验中两条黑斑，表明有两个 $S$ ，原子束分为两条，而上式中除 $m$ 外都是常数，说明：Ag原子在磁场中只有两个取向，原子在磁场中的空间取向是量子化的

存在问题：理论上预言应分为 $2\ell +1$ 束, 即奇数束。实验上是两束，为偶数?!

---

# §20 电子的自旋

需要掌握的知识点：

用五个量子数表示氢原子中电子的状态

使用量子数计算电子自旋和磁矩的大小

用氢原子内部的磁相互作用来解释氢谱的精细结构

---

# 自旋假设

$\begin{aligned}

&S=\sqrt{s(s+1) }\hbar \\

&S_{z}=m_{s} \hbar

\end{aligned}$

1925年乌仑贝克—古兹米特(G.E.Ulenbeck&S.Goudsmit)

假设

类似于轨道角动量

$m_s$ 的取值范围为

对于电子 $m_{s}=-s,-s+1, \ldots, 0, \ldots,+s-1, s$

类似 $s=\frac{1}{2}$ 有 $m_l$ 种取法 $2l+1$ 应有 $m_s$ 种取法

<img src="/images/CNX_UPhysics_41_03_SpinDir-1-28845.jpg" style="max-width: 380px; max-height: 400px;" />

---

# 氢原子中电子的状态

---

# 自旋磁矩与朗德g因子

$\begin{aligned}

&\mu_{s}=-\hat{S} g_{s} \mu_{B}=-\sqrt{s(s+1)} g_{s} \mu_{B} \\

&\mu_{s, z}=-m_{s} g_{s} \mu_{B}

\end{aligned}$

电子的磁矩

对于电子 $g_s \approx 2$

实际上g因子可以表示为

---

# 电子的总角动量

$L = \sqrt{\ell(\ell+1)} \hbar$

电子的运动=轨道运动+自旋运动

轨道角动量：

自旋角动量：

总角动量：

量子数 $\ell = 0, 1, 2, ..., n-1$

其中总角动量量子数： $S = \sqrt{s(s+1)} \hbar$

当 $s=\frac{1}{2}$ 时，共 $\vec{J} = \vec{L} + \vec{S}$ 个值

当 $J = \sqrt{j(j+1)}\hbar$ 时，共 $\geq 0$ 个值

<img src="/images/Screen Shot 2022-02-21 at 13.00.33-29150.png" style="max-width: 346px; max-height: 400px;" />

---

# 电子的总磁矩

$\vec{\mu} =  \vec{\mu}_s + \vec{\mu}_l$

$\vec{J} = \vec{L} + \vec{S}$ 在 $\vec{\mu}$ 方向的分量 $\vec{J}$ 叫原子的总磁矩

其中 $\vec{\mu}_j$

<img src="/images/WechatIMG1114-29260.png" style="max-width: 220px; max-height: 400px;" />

---

# §21 自旋轨道相互作用

$\begin{aligned}

\boldsymbol{B}_{l} &=\frac{\mu_{0} Z e}{4 \pi r^{3}}(\boldsymbol{v} \times(-\boldsymbol{r}))=-\frac{\mu_{0} Z e}{4 \pi r^{3}}(\boldsymbol{v} \times \boldsymbol{r}) \\

&=+\frac{\mu_{0} Z e}{4 \pi r^{3} m_{\mathrm{e}}} \boldsymbol{L}

\end{aligned}$

电子的轨道运动会在原子内产生一个内磁场，引入自旋后，电子具有的内禀自旋磁矩与原子内磁场的磁相互作用会引起能量改变， 产生能级级分裂。

这种作用较弱，由它引起的能级和光谱的移动和分裂称作精细结构。

经典图像

在相对电子静止的坐标系中，

电流在电子处产生磁场

<img src="/images/Screen Shot 2022-02-21 at 21.43.00-29299.png" style="max-width: 500px; max-height: 400px;" />

---

# 自旋轨道相互作用

$\begin{aligned}

\Delta E &=-\mu_{s} \cdot \boldsymbol{B}_{l}=g_{s} \mu_{\mathrm{B}} \frac{\mu_{0} Z e}{4 \pi r^{3} m_{\mathrm{e}} \hbar}(\boldsymbol{L} \cdot \boldsymbol{S}) \\

& \approx \frac{\mu_{0} Z e^{2}}{4 \pi m_{\mathrm{e}}^{2} r^{3}}(\boldsymbol{L} \cdot \boldsymbol{S})

\end{aligned}$

电子的自旋磁矩在该磁场下有以下的势能

相对电子静止的坐标系中导出的结果需要变换到相对于原子核静止的坐标系 1926年托马斯(L.H. Thomas)给出了相应的洛仑兹变换

课外阅读

<img src="/images/37_622fa36000641da57a5bc7b17af7039c-29565.png" style="max-width: 500px; max-height: 400px;" />

---

# 自旋轨道相互作用对氢原子能级的影响

$E_{n}=-E_0 \frac{1}{n^2}$

当氢原子能级 $E_{n, l, s}=E_{n}-\boldsymbol{\mu}_{s} \cdot \boldsymbol{B}_{l}=E_{n}+\frac{\mu_{0} Z e^{2}}{8 \pi m_{\mathrm{e}}^{2} r^{3}}(\boldsymbol{L} \cdot \boldsymbol{S})$ ，考虑自旋轨道作用时

总角动量 $\vec{J} = \vec{L} + \vec{S}$ 以及 $J = \sqrt{j(j+1)} \hbar$

其中

因此

---

# 能级分裂

$s$

精细结构的能级分裂不适用于 $\ell \geq 1$ 轨道，只适用于 $\Delta E =\frac{a}{2}[j(j+1)-l(l+1)-s(s+1)]$

量子力学中只有本征态下的平均值才有意义

精细结构常数

<img src="/images/Screen Shot 2022-02-22 at 15.13.53-29676.png" style="max-width: 500px; max-height: 400px;" />

---

# 分裂能级差

$(n, l, j=l+1 / 2)$

精细结构通常有两个能级 $(n, l, j=l-1 / 2)$ 和 $\begin{aligned}

E_{n, l, s} \uparrow -  E_{n, l, s} \downarrow  &=\langle a\rangle\left(l+\frac{1}{2}\right)=-E_{n} \frac{Z^{2} \alpha^{2}}{n l(l+1)} \\

& \approx-5.3 \times 10^{-5} E_{n} \frac{Z^{2}}{n l(l+1)}

\end{aligned}$

已知 $E_{n} \propto Z^{2} / n^{2}$

---

# §22 塞曼效应

$\vec{\mu} = - \frac{e}{2m_e} \vec{L}$

原子能级在外磁场中发生分裂的现象,称为塞曼效应：无外磁场时的一根光谱线，加上外磁场时分裂成多条，且分裂后的谱线成分是偏振的。

磁矩 $\vec{B}$ 在外磁场 $-\vec{\mu}\cdot \vec{B}$ 中具有势能 $\vec{L}$ 。角动量 $m_\ell$ 沿外磁场的分量量子数 $(2\ell +1)$ 有 $\vec{\mu}$ 个值， $(2\ell + 1)$ 就有 $(2\ell +1 )$ 个取向，所以一个能级在外磁场中将分裂成￼

<img src="/images/Screen Shot 2022-02-23 at 14.02.48-29868.png" style="max-width: 500px; max-height: 400px;" />

---

# 塞曼效应

$n=2$

例如: 氢灯（观察氢光的光谱仪）放在足够强的外磁场中时，有些谱线(如 $l=1$ ,  $\vec{\mu} = - \frac{e}{2m_e} \vec{L}$ 对应的谱线)会分裂为三条：

磁矩 $\vec{B}$ 在外磁场 $-\vec{\mu}\cdot \vec{B}$ 中具有势能 $\vec{L}$ 。角动量 $m_\ell$ 沿外磁场的分量量子数 $(2\ell +1)$ 有 $\vec{\mu}$ 个值， $(2\ell + 1)$ 就有 $(2\ell +1 )$ 个取向，所以一个能级在外磁场中将分裂成￼

<img src="/images/pasted-image-35639.png" style="max-width: 500px; max-height: 400px;" />

---

<!-- 此页内容待补充 -->

---

<!-- 此页内容待补充 -->
