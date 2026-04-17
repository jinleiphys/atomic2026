---
title: "复习：第二、三、四章 复习要点"
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
  font-family: "Kaiti SC", "STKaiti", "KaiTi", "楷体", serif !important;
}
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
}
.slidev-layout h1 {
  font-size: 1.85em !important;
}
.slidev-layout h2 {
  font-size: 1.35em !important;
}
.kaiti-accent {
  color: #C71585 !important;
  font-weight: bold !important;
}
.box {
  border: 2px solid #C71585;
  border-radius: 0.5rem;
  padding: 0.6rem 1rem;
  margin: 0.4rem 0;
}
.box-soft {
  background: #FDF2F8;
  border-left: 4px solid #C71585;
  padding: 0.5rem 0.9rem;
  margin: 0.4rem 0;
  border-radius: 0.3rem;
}
.small {
  font-size: 0.85em;
}
table {
  font-size: 0.85em;
}
</style>

# 期末复习：第二章 / 第三章 / 第四章

<div class="text-center" style="margin-top: 2rem;">

**原子物理学 2026**

<br>

<span class="kaiti-accent">从玻尔模型 → 量子力学 → 氢原子精细结构</span>

</div>

<div class="text-center small" style="margin-top: 3rem; opacity: 0.7;">

按一下右键或空格逐步展开复习要点

</div>

---
layout: center
---

# 三章主线一图

<div class="box-soft" v-click>

**第二章：玻尔模型** —— <span class="kaiti-accent">从经验到量子化的猜想</span>

光谱 (Balmer / Rydberg) → 量子化假设 ($L = n\hbar$) → 能级 $E_n = -13.6/n^2$ eV

</div>

<div class="box-soft" v-click>

**第三章：量子力学初步** —— <span class="kaiti-accent">从猜想到方程</span>

de Broglie ($\lambda = h/p$) → 不确定性 → 波函数 $|\Psi|^2$ → Schrödinger 方程 $\hat H\psi = E\psi$

</div>

<div class="box-soft" v-click>

**第四章：氢原子 + 自旋** —— <span class="kaiti-accent">从方程到完整原子图像</span>

球坐标分离 → 三量子数 $(n,\ell,m)$ → 轨道磁矩 → Stern-Gerlach → 自旋 → 精细结构

</div>

<div class="text-center small" v-click style="margin-top: 1.5rem;">

考点不在记公式，而在<span class="kaiti-accent">能解释每一步"为什么"</span>。

</div>

---
layout: section
---

# 第一部分：第二章 玻尔模型

<div class="text-center small" style="opacity: 0.7;">

七个要点：黑体辐射 / 光电效应 / 光谱线系 / 玻尔三假设 / 能级与里德伯 / 类氢离子 / Franck-Hertz

</div>

---

# §2.1 黑体辐射 — 量子化的起点

<div v-click>

**经典困难：紫外灾难**

Rayleigh-Jeans 公式在高频端 $\rho(\nu) \to \infty$，与实验完全不符。

</div>

<div class="box" v-click>

**Planck 假设 (1900)**：振子能量只能取分立值

$$E = nh\nu, \quad n = 0, 1, 2, \ldots$$

普朗克常数 $h = 6.626 \times 10^{-34}$ J·s

</div>

<div v-click>

**经验规律要记住**：

- 斯特藩-玻尔兹曼律：$M(T) = \sigma T^4$
- 维恩位移律：$\lambda_{\max} T = b$（测恒星表面温度）

</div>

<div class="box-soft" v-click>

<span class="kaiti-accent">考点</span>：为什么经典物理在低频对、高频错？因为高频模式的"能量门槛" $h\nu \gg k_B T$ 时被冻结。

</div>

---

# §2.2 光电效应 — 光的粒子性

<div v-click>

**经典理论解释不了的三件事**：

1. 响应**瞬时**（< $10^{-9}$ s），无须能量积累
2. 最大动能**与光强无关**，只与频率有关
3. 存在**截止频率** $\nu_0$

</div>

<div class="box" v-click>

**Einstein 光量子假设 (1905)** + **光电方程**：

$$K_{\max} = h\nu - \phi, \qquad \nu_0 = \phi/h$$

$\phi$：金属脱出功；一个光子的能量一次性传给一个电子。

</div>

<div v-click>

**Millikan 1916 精密实验**：原想否证 Einstein，结果

- 不同金属的 $V_s$-$\nu$ 直线**斜率相同 = $h/e$**
- 测得 $h$ 精度 0.5%，反而成了 Einstein 公式的最强证据

</div>

<div class="box-soft" v-click>

<span class="kaiti-accent">考点</span>：能写光电方程，能从 $V_s$-$\nu$ 图读出 $h$ 和 $\phi$。

</div>

---

# §2.3 氢光谱 — Balmer 与 Rydberg

<div v-click>

**Balmer (1885)** 把氢的可见光四条线写成了一个"巧妙公式"：

$$\frac{1}{\lambda} = R_H\!\left(\frac{1}{2^2} - \frac{1}{n^2}\right), \quad n = 3, 4, 5, \ldots$$

</div>

<div class="box" v-click>

**Rydberg 推广** —— 氢原子所有谱线：

$$\frac{1}{\lambda} = R_H\!\left(\frac{1}{n^2} - \frac{1}{n'^2}\right), \quad n' > n$$

$R_H \approx 1.097 \times 10^7\ \mathrm{m^{-1}}$

</div>

<div v-click>

**线系命名**（要会区分）：

| 线系 | $n$ | 区段 |
|---|---|---|
| Lyman 莱曼 | 1 | 紫外 |
| Balmer 巴耳末 | 2 | 可见 |
| Paschen 帕邢 | 3 | 红外 |
| Brackett 布拉开 | 4 | 红外 |

</div>

---

# §2.4 玻尔三假设 (1913)

<div class="box" v-click>

**①  定态假设**：电子在特定轨道上运动，<span class="kaiti-accent">虽加速但不辐射</span>。

</div>

<div class="box" v-click>

**②  角动量量子化**：

$$L_n = m_e v_n r_n = n\hbar, \quad n = 1, 2, 3, \ldots$$

</div>

<div class="box" v-click>

**③  跃迁辐射条件**：

$$h\nu = |E_{n'} - E_n|$$

</div>

<div class="box-soft" v-click>

<span class="kaiti-accent">三假设的角色</span>：①回避了经典电动力学的死局，②给出了定量的"挑选规则"，③把光谱与能级直接连起来。

</div>

---

# §2.5 玻尔模型 — 关键结果

<div v-click>

**轨道半径**：

$$r_n = a_0 n^2, \qquad a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \approx 0.529\ \text{Å}$$

</div>

<div v-click>

**能级公式**：

$$\boxed{E_n = -\frac{E_0}{n^2}, \qquad E_0 = 13.6\ \text{eV}}$$

</div>

<div v-click>

**与 Rydberg 公式的连接**：

$$h\nu = E_0\!\left(\frac{1}{n^2} - \frac{1}{n'^2}\right) \;\Rightarrow\; R_H = \frac{E_0}{hc}$$

<span class="kaiti-accent">玻尔模型从第一性原理导出了 Rydberg 经验律 — 这是它最大的胜利。</span>

</div>

<div v-click>

**精细结构常数**（要会写）：

$$\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137}$$

</div>

---

# §2.6 类氢离子 + Franck-Hertz

<div class="box" v-click>

**类氢离子** (He⁺, Li²⁺, …) — 把 $e^2$ 换成 $Ze^2$：

$$r_n = \frac{a_0}{Z}n^2, \qquad E_n = -\frac{Z^2 E_0}{n^2}$$

</div>

<div v-click>

**约化质量修正**：考虑核动，电子质量替换为

$$m_\mu = \frac{m_e M}{m_e + M}$$

</div>

<div class="box" v-click>

**Franck-Hertz 实验 (1914)**：电子-汞蒸气碰撞，电流-电压曲线出现**周期性突降**

- 间距正好是汞的第一激发能 $\Delta E = 4.9$ eV
- <span class="kaiti-accent">这是能级离散性的"直接"证据</span>，不依赖光谱

</div>

---
layout: section
---

# 第二部分：第三章 量子力学初步

<div class="text-center small" style="opacity: 0.7;">

四个要点：物质波 / 不确定性 / 波函数 / 薛定谔方程

</div>

---

# §3.1 de Broglie 物质波

<div class="box" v-click>

**de Broglie 假设 (1923)**：所有粒子都伴随波

$$\lambda = \frac{h}{p}, \qquad \nu = \frac{E}{h}$$

等价：$\vec p = \hbar \vec k$, $E = \hbar \omega$

</div>

<div v-click>

**Davisson-Germer 实验 (1927)**：电子在镍单晶上的衍射，首次实验证实物质波。

</div>

<div class="box-soft" v-click>

**与玻尔量子化的"统一"**：电子轨道是驻波

$$2\pi r = n\lambda = n\,\frac{h}{p} \;\Longrightarrow\; L = pr = n\hbar$$

<span class="kaiti-accent">"角动量量子化"原来就是"驻波条件"。</span>

</div>

---

# §3.2 Heisenberg 不确定性原理

<div class="box" v-click>

**位置-动量**：

$$\Delta x \cdot \Delta p_x \geq \frac{\hbar}{2}$$

**能量-时间**：

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

</div>

<div v-click>

**单缝衍射估计**：缝宽 $a \to \Delta x \sim a$；衍射角 $\sim \lambda/a \to \Delta p \sim p\lambda/a$

$$\Delta x \cdot \Delta p \sim p\lambda = h \;\;\checkmark$$

</div>

<div class="box-soft" v-click>

**应用：原子稳定性的能量极小**

把电子限制在半径 $r$：$\Delta p \sim \hbar/r$

$$E(r) \sim \frac{\hbar^2}{2 m_e r^2} - \frac{e^2}{4\pi\varepsilon_0 r}$$

求极小 $\to r_{\min} = a_0$, $E_{\min} = -13.6$ eV，<span class="kaiti-accent">不需要轨道也能给出基态</span>。

</div>

---

# §3.3 波函数与统计解释

<div class="box" v-click>

**Born 解释 (1926)**：$|\Psi(\vec r, t)|^2$ 是<span class="kaiti-accent">概率密度</span>

$$P(\vec r)\, dV = |\Psi(\vec r, t)|^2\, dV$$

**归一化**：$\displaystyle \int |\Psi|^2\, dV = 1$

</div>

<div v-click>

**波函数标准条件**：单值、有限、连续、可归一化。

</div>

<div v-click>

**期望值与不确定度**：

$$\langle \hat Q\rangle = \int \Psi^* \hat Q\, \Psi\, dV, \quad \Delta Q = \sqrt{\langle Q^2\rangle - \langle Q\rangle^2}$$

</div>

<div class="box-soft" v-click>

**双缝干涉的概率叙事**：

$$|\Psi_A + \Psi_B|^2 = |\Psi_A|^2 + |\Psi_B|^2 + 2\,\mathrm{Re}(\Psi_A^*\Psi_B)$$

最后一项 = 干涉项。"哪条缝"实验关掉它，恢复粒子图像。

</div>

---

# §3.4 薛定谔方程

<div class="box" v-click>

**含时方程**：

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat H \Psi, \qquad \hat H = -\frac{\hbar^2}{2m}\nabla^2 + V(\vec r)$$

</div>

<div class="box" v-click>

**定态方程**（$V$ 不显含 $t$，分离变量 $\Psi = \psi(\vec r) e^{-iEt/\hbar}$）：

$$\boxed{\hat H\, \psi(\vec r) = E\, \psi(\vec r)}$$

这是一个<span class="kaiti-accent">本征值问题</span>：$E_n$ 是本征值，$\psi_n$ 是本征函数。

</div>

<div v-click>

**算符替换法则**：

$$\hat p \to -i\hbar\nabla, \quad \hat E \to i\hbar\frac{\partial}{\partial t}$$

</div>

<div class="box-soft" v-click>

<span class="kaiti-accent">"定态"</span>不是粒子静止，而是 $|\Psi|^2$ 与所有可观测量的统计平均不随时间变化。

</div>

---

# §3.5 量子化的"自然涌现"

<div v-click>

玻尔需要"假设" $L = n\hbar$；薛定谔不需要 — 量子化是边值问题的<span class="kaiti-accent">自然结果</span>。

</div>

<div class="box" v-click>

**叠加原理**（线性方程的直接推论）：

$$\Psi(\vec r, t) = \sum_n c_n\, \psi_n(\vec r)\, e^{-iE_n t/\hbar}$$

测得能量为 $E_n$ 的概率 $= |c_n|^2$。

</div>

<div class="box-soft" v-click>

**第三章一句话总结**：

> 玻尔说"轨道是离散的"，薛定谔说"那是边界条件 + 本征值方程的必然结果"。

</div>

---
layout: section
---

# 第三部分：第四章 氢原子 / 自旋 / 精细结构

<div class="text-center small" style="opacity: 0.7;">

八个要点：氢原子求解 / 三量子数 / 轨道磁矩 / Stern-Gerlach / 自旋 / 五量子数 / 精细结构 / 塞曼

</div>

---

# §4.1 氢原子 — 球坐标分离

<div v-click>

**库仑势** $U(r) = -\dfrac{e^2}{4\pi\varepsilon_0 r}$ 是中心势，球坐标完美分离：

$$\psi_{n\ell m}(r,\theta,\varphi) = R_{n\ell}(r)\, Y_\ell^m(\theta, \varphi)$$

</div>

<div class="box" v-click>

**角向方程的本征值**：

$$\hat L^2\, Y_\ell^m = \ell(\ell+1)\hbar^2\, Y_\ell^m, \qquad \hat L_z\, Y_\ell^m = m\hbar\, Y_\ell^m$$

- $\ell$ 整数来自 Legendre 方程的级数截断
- $m$ 整数来自 $\varphi$ 周期条件

</div>

<div v-click>

**径向方程引入有效势**（关键直觉：离心势垒）：

$$V_\text{eff}(r) = U(r) + \frac{\ell(\ell+1)\hbar^2}{2 m_e r^2}$$

</div>

---

# §4.2 三量子数与简并度

<div class="box" v-click>

**三量子数的取值规则**：

| 量子数 | 取值 | 物理意义 |
|---|---|---|
| $n$ | $1, 2, 3, \ldots$ | 主量子数 → 能量 $E_n$ |
| $\ell$ | $0, 1, \ldots, n-1$ | 轨道角动量大小 $\sqrt{\ell(\ell+1)}\hbar$ |
| $m$ | $-\ell, \ldots, +\ell$ | $L_z = m\hbar$（共 $2\ell+1$ 个） |

</div>

<div v-click>

**能级公式不变**（巧合还是必然？）：

$$E_n = -\frac{13.6\ \text{eV}}{n^2}$$

</div>

<div class="box-soft" v-click>

**简并度** $= \displaystyle\sum_{\ell=0}^{n-1}(2\ell+1) = n^2$

特殊：$\ell$ 的简并是库仑势的"偶然简并"（SO(4) 对称），其它中心势没有。

</div>

<div v-click>

**与玻尔的对比**：玻尔基态预言 $L = \hbar$，<span class="kaiti-accent">薛定谔正确给出 $L = 0$</span>（球对称 $1s$ 态）。

</div>

---

# §4.3 轨道磁矩 + 玻尔磁子

<div v-click>

电子在 $m \neq 0$ 态有<span class="kaiti-accent">环形概率流</span> → 等效电流环 → 磁矩。

</div>

<div class="box" v-click>

**轨道磁矩**：

$$\vec\mu_L = -\frac{e}{2 m_e}\, \vec L$$

(负号源自电子电荷；磁旋比 $\gamma = -e/(2m_e)$)

</div>

<div class="box" v-click>

**玻尔磁子**（原子磁性的天然单位）：

$$\boxed{\mu_B = \frac{e\hbar}{2 m_e} = 9.274 \times 10^{-24}\ \text{J/T}}$$

$$|\vec\mu_L| = \mu_B \sqrt{\ell(\ell+1)}, \quad \mu_{L,z} = -m\mu_B$$

</div>

<div v-click class="small" style="opacity: 0.85;">

注意：$|\vec\mu_L| > |\mu_{L,z}|_{\max}$ — 角动量永远不能完全"指向 z"，这是不确定性原理在角动量上的体现。

</div>

---

# §4.4 Stern-Gerlach 实验 (1922)

<div v-click>

**原理**：非均匀磁场对磁矩有力 $F_z = \mu_z\, \dfrac{\partial B_z}{\partial z}$

银原子束穿过 → 不同 $\mu_z$ 偏转角不同。

</div>

<div class="box" v-click>

**实验结果** = <span class="kaiti-accent">完全对称的 2 条痕迹</span>

</div>

<div v-click>

**这与轨道理论矛盾**：
- 银基态 $5s^1$，$\ell = 0$ → 应当 0 偏转
- 即使 $\ell \neq 0$，分裂数 $2\ell + 1$ 永远是<span class="kaiti-accent">奇数</span>，不可能等于 2

</div>

<div class="box-soft" v-click>

唯一出路：硬解 $2\ell+1 = 2 \Rightarrow \ell = 1/2$（半整数！）

→ 必有新的<span class="kaiti-accent">内禀角动量</span>：电子自旋。

</div>

---

# §4.5 电子自旋

<div v-click>

**1925 年危机的四条线索**：

1. Stern-Gerlach 的 2 条
2. 碱金属双线（如 Na D 线）
3. 反常 Zeeman 效应
4. 周期表每轨道容纳 $2(2\ell+1)$ 个电子

</div>

<div class="box" v-click>

**Uhlenbeck-Goudsmit 假设 (1925)**：电子有内禀角动量

$$s = \frac{1}{2},\quad |\vec S| = \frac{\sqrt 3}{2}\hbar,\quad S_z = m_s \hbar = \pm\frac{\hbar}{2}$$

</div>

<div class="box" v-click>

**自旋磁矩**（注意 $g_s \approx 2$，是反常的！）：

$$\vec\mu_s = -g_s\, \frac{e}{2m_e}\, \vec S, \quad g_s \approx 2$$

$$\mu_{s,z} = \mp \mu_B$$

</div>

<div v-click class="small" style="opacity: 0.85;">

$g_s = 2$ 来自 Dirac 方程 (1928) 的<span class="kaiti-accent">自动结果</span>，QED 修正给出 $g_s = 2.00231930\ldots$

</div>

---

# §4.6 完整五量子数

<div v-click>

| 量子数 | 取值 | 物理意义 |
|---|---|---|
| $n$ | $1, 2, 3, \ldots$ | 能量 |
| $\ell$ | $0, 1, \ldots, n-1$ | 轨道角动量 |
| $m_\ell$ | $-\ell, \ldots, +\ell$ | 轨道磁投影 |
| $s$ | $1/2$（电子固定） | 自旋 |
| $m_s$ | $\pm 1/2$ | 自旋投影 |

</div>

<div class="box" v-click>

**加上自旋后简并度**：$2n^2$

</div>

<div class="box-soft" v-click>

**Pauli 不相容原理** 隐含其中：每个 $(n, \ell, m_\ell, m_s)$ 一个电子 → 周期表的"行长" 2, 8, 18, ⋯ 自然涌现。

</div>

---

# §4.7 自旋-轨道耦合 + 精细结构

<div v-click>

**物理来源**（半经典）：电子坐标系下原子核运动产生 $\vec B \propto \vec L$，自旋在此磁场中有势能 $\propto \vec L \cdot \vec S$。

</div>

<div class="box" v-click>

**总角动量** $\vec J = \vec L + \vec S$，对电子 ($s=1/2$)：

$$j = \ell \pm \tfrac{1}{2}\quad(\ell \geq 1), \qquad j = \tfrac{1}{2}\quad(\ell = 0)$$

</div>

<div v-click>

**$\vec L \cdot \vec S$ 用 $\vec J^2$ 算**：

$$\langle \vec L\cdot\vec S\rangle = \frac{\hbar^2}{2}\bigl[j(j+1) - \ell(\ell+1) - s(s+1)\bigr]$$

</div>

<div class="box" v-click>

**精细结构 ~ $\alpha^2$**：能级修正 $\Delta E / E_n \sim Z^2 \alpha^2 \approx 5\times10^{-5}$（氢）

→ 钠 D 双线 ($D_1\,589.59$ nm, $D_2\,588.99$ nm) 就是 $3p_{1/2}, 3p_{3/2}$ 之差。

</div>

---

# §4.8 Zeeman 效应

<div v-click>

**正常 Zeeman**（$S = 0$，纯轨道）：

$$\Delta E = m_\ell\, \mu_B B$$

每条线分 3 条等距，间距 $\mu_B B$。

</div>

<div class="box" v-click>

**反常 Zeeman**（一般情形，弱场，$\vec L\vec S$ 耦合保持）：

$$\Delta E = g_J\, m_j\, \mu_B B$$

**Landé g 因子**：

$$\boxed{g_J = 1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2 j(j+1)}}$$

</div>

<div v-click class="small">

**几个常用 $g_J$**：
- $\ell=0,\, j=1/2$ → $g_J = 2$（纯自旋）
- $2p_{1/2}$ → $g_J = 2/3$
- $2p_{3/2}$ → $g_J = 4/3$

</div>

<div class="box-soft" v-click>

**Paschen-Back（强场）**：磁场压垮 LS 耦合，$m_\ell, m_s$ 重新成为好量子数：

$$\Delta E = (m_\ell + 2 m_s)\, \mu_B B$$

</div>

---
layout: section
---

# 公式速记 + 常见易错点

---

# 核心公式速查

<div class="small">

| 概念 | 公式 |
|---|---|
| 能级（玻尔/薛定谔同形） | $E_n = -13.6\ \text{eV}/n^2$ |
| 玻尔半径 | $a_0 = 0.529$ Å |
| Rydberg 公式 | $1/\lambda = R_H(1/n^2 - 1/n'^2)$ |
| 类氢离子 | $E_n = -Z^2 \cdot 13.6 / n^2$ eV |
| 光电方程 | $K_{\max} = h\nu - \phi$ |
| de Broglie | $\lambda = h/p$ |
| 不确定性 | $\Delta x\, \Delta p \geq \hbar/2$ |
| 定态薛定谔 | $\hat H \psi = E \psi$ |
| 角动量大小 | $\|\vec L\| = \sqrt{\ell(\ell+1)}\,\hbar$ |
| 轨道磁矩 | $\vec\mu_L = -(e/2m_e)\vec L$ |
| 玻尔磁子 | $\mu_B = e\hbar/(2m_e) = 9.274\times10^{-24}$ J/T |
| 自旋磁矩 | $\vec\mu_s = -g_s(e/2m_e)\vec S,\ g_s\approx 2$ |
| 精细结构常数 | $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137$ |
| Landé 因子 | $g_J = 1 + [j(j+1)+s(s+1)-\ell(\ell+1)]/[2j(j+1)]$ |
| 弱场 Zeeman | $\Delta E = g_J m_j \mu_B B$ |

</div>

---

# 常见易错点

<div class="box" v-click>

**①  $L \neq n\hbar$**

玻尔说 $L = n\hbar$ 是错的。薛定谔正解：$|\vec L| = \sqrt{\ell(\ell+1)}\hbar$，且基态 $\ell = 0$。

</div>

<div class="box" v-click>

**②  分清 "能级简并" 与 "态数"**

能级简并 = 同一 $E_n$ 对应的态数 = $n^2$（不含自旋）/ $2n^2$（含自旋）。

</div>

<div class="box" v-click>

**③  自旋 $g_s = 2$ 不是 $1$**

这就是反常 Zeeman 出现的根源 —— 总磁矩不平行于 $\vec J$。

</div>

<div class="box" v-click>

**④  $s$ 态没有自旋-轨道耦合分裂**

$\ell = 0 \Rightarrow \vec L = 0 \Rightarrow \vec L\cdot\vec S = 0$。所以 $1s, 2s, 3s$ 都不分裂。

</div>

<div class="box" v-click>

**⑤  Stern-Gerlach 银 vs. 氢的差异**

银 $5s^1$ 外层 $\ell=0$，2 条裂分 = 纯自旋；氢 $1s$ 同理。但若实验用 $\ell\neq 0$ 原子，会同时看到轨道与自旋贡献。

</div>

---
layout: center
---

# 一句话历史脉络

<div class="box-soft" v-click>

**1900 Planck** 引入 $h$ → **1905 Einstein** 光子 → **1913 Bohr** 量子化原子
</div>

<div class="box-soft" v-click>

**1923 de Broglie** 物质波 → **1925 Heisenberg / 1926 Schrödinger** 量子力学方程
</div>

<div class="box-soft" v-click>

**1925 Uhlenbeck-Goudsmit** 自旋 → **1928 Dirac** 方程统一相对论与自旋
</div>

<div class="text-center" v-click style="margin-top: 2.5rem;">

<span class="kaiti-accent">考前回顾这条时间线，每个名字对应的关键公式都能默写，就稳了。</span>

</div>

---
layout: center
---

# 祝考试顺利！

<div class="text-center" style="margin-top: 2rem; font-size: 1.3em;">

<span class="kaiti-accent">理解 > 记忆</span>

每个公式都能讲出"为什么"，比死记十个公式更有用。

</div>
