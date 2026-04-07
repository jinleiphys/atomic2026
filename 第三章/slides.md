---
title: "第三章 量子力学导论"
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
  font-size: 1.2rem;
  line-height: 1.5;
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
  max-height: 380px !important;
  margin: 0 auto !important;
  object-fit: contain;
}
</style>

# 第三章 量子力学导论

金 磊

办公室：瑞安楼703B

邮箱：jinl@tongji.edu.cn

---

<style scoped>
.slidev-layout { font-size: 1.35rem; line-height: 1.8; }
</style>

# §12 波粒二象性

需要掌握的知识点：

（1）了解哪些现象电磁波显示粒子性，哪些现象粒子显示波动性

（2）理解德布罗意物质波的假设

（3）解释德布罗意假设如何给出玻尔氢原子量子理论中角动量量子化的基本原理

（4）了解戴维孙-革末实验

（5）使用德布罗意假设解释电子衍射现象

---
layout: two-cols
---

<style scoped>
.prop-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-bottom: 0.6em; border-left: 3px solid #C71585; }
.prop-card h4 { color: #C71585; margin: 0 0 0.2em 0; font-size: 1em; }
.prop-card p { margin: 0.15em 0; font-size: 0.95em; }
</style>

# 什么是粒子性？

<div class="prop-card">
<h4>动量</h4>

$\vec{p} = m \vec{v}$

</div>

<div class="prop-card">
<h4>角动量</h4>

$\vec{\ell} = \vec{r} \times \vec{p}$，$|\ell| = |r||p|\sin\theta$

</div>

<div class="prop-card">
<h4>动能</h4>

$T = \frac{1}{2}mv^2$

</div>

<div class="prop-card">
<h4>势能</h4>

$V_P = -\int_R^P F(x)\,dx$

</div>

::right::

<img src="/images/Screen Shot 2022-03-09 at 12.24.21-26215.png" style="max-width: 100%; max-height: 200px; object-fit: contain;" />

<img src="/images/Screen Shot 2022-03-09 at 12.35.38-26277.png" style="max-width: 100%; max-height: 200px; object-fit: contain;" />

---
layout: two-cols
---

<style scoped>
.wave-card { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-bottom: 0.6em; border-left: 3px solid #5856d6; }
.wave-card h4 { color: #5856d6; margin: 0 0 0.2em 0; font-size: 1em; }
.wave-summary { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-top: 0.6em; border-left: 3px solid #C71585; }
</style>

# 什么是波动性？

<div class="wave-card">

**基本参量**

谐波：$\lambda = vT$，频率：$\nu = 1/T$，波速：$\lambda\nu = v$

</div>

<div class="wave-card">

**波数与角频率**

波数：$k = \frac{2\pi}{\lambda}$，角频率：$\omega = \frac{2\pi}{T} = 2\pi\nu$

</div>

<div class="wave-summary">

<span style="color: #C71585; font-weight: bold;">谐波方程</span>

$y(x,t) = A\sin[2\pi(x/\lambda - t/T)] = A\sin(kx - \omega t)$

</div>

::right::

<img src="/images/Screen Shot 2022-03-09 at 12.47.48-26290.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

<style scoped>
.standing-card { background: rgba(48,209,88,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-bottom: 0.6em; border-left: 3px solid #30d158; }
.standing-result { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-top: 0.6em; border-left: 3px solid #C71585; }
</style>

# 驻波：波的叠加/相干

<div class="standing-card">

**叠加原理**：$y(x,t) = y_1(x,t) + y_2(x,t)$

</div>

<div class="standing-card">

**向右传播**：$y_1 = A\sin(kx - \omega t)$

**向左传播**：$y_2 = A\sin(kx + \omega t)$

</div>

<div class="standing-result">

<span style="color:#C71585;font-weight:bold;">驻波方程</span>

$y(x,t) = 2A\sin(kx)\cos(\omega t)$

节点条件：$\sin(kx) = 0$，即 $x = n\frac{\lambda}{2}$

</div>

::right::

<img src="/images/Waventerference-28289.gif" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

<style scoped>
.timeline { position: relative; padding-left: 1.5em; }
.timeline::before { content: ''; position: absolute; left: 0.35em; top: 0.2em; bottom: 0.2em; width: 2px; background: linear-gradient(to bottom, #C71585, #5856d6); }
.timeline .era { position: relative; margin-bottom: 1em; }
.timeline .era::before { content: ''; position: absolute; left: -1.28em; top: 0.45em; width: 10px; height: 10px; border-radius: 50%; background: #C71585; }
.slidev-layout { font-size: 1.3rem; }
.timeline .era h3 { font-size: 1.3em; color: #C71585; margin-bottom: 0.2em; }
.timeline .era p { margin: 0.15em 0; font-size: 1.1em; line-height: 1.5; }
.vs-box { display: flex; gap: 1em; margin: 0.3em 0; }
.vs-box .side { flex: 1; padding: 0.4em 0.6em; border-radius: 8px; font-size: 0.9em; }
.vs-box .side.newton { background: rgba(199,21,133,0.08); border-left: 3px solid #C71585; }
.vs-box .side.huygens { background: rgba(88,86,214,0.08); border-left: 3px solid #5856d6; }
</style>

# 光的波粒二象性

<div class="timeline">
<div class="era">
<h3>17世纪 — 两大学说之争</h3>
<div class="vs-box">
<div class="side newton"><b>牛顿：微粒说</b><br>解释反射、直线传播</div>
<div class="side huygens"><b>惠更斯：波动说</b><br>解释折射、衍射</div>
</div>
</div>

<div class="era">
<h3>19世纪 — 波动说的胜利</h3>
<p>杨氏、菲涅尔、夫琅禾费：光的<b>干涉与衍射</b>实验</p>
<p>麦克斯韦 & 赫兹：光是<b>电磁波</b> → 确立波动说</p>
</div>
</div>

---

<style scoped>
.timeline { position: relative; padding-left: 1.5em; }
.timeline::before { content: ''; position: absolute; left: 0.35em; top: 0.2em; bottom: 0.2em; width: 2px; background: linear-gradient(to bottom, #C71585, #ff9f0a); }
.timeline .era { position: relative; margin-bottom: 0.8em; }
.timeline .era::before { content: ''; position: absolute; left: -1.28em; top: 0.45em; width: 10px; height: 10px; border-radius: 50%; background: #C71585; }
.slidev-layout { font-size: 1.3rem; }
.timeline .era h3 { font-size: 1.3em; color: #C71585; margin-bottom: 0.2em; }
.timeline .era p { margin: 0.15em 0; font-size: 1.1em; line-height: 1.5; }
.formula-box { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-top: 0.6em; border-left: 3px solid #C71585; font-size: 1.1em; }
.duality-box { display: flex; gap: 0.8em; margin-top: 0.6em; }
.duality-box .side { flex: 1; padding: 0.5em 0.6em; border-radius: 8px; text-align: center; font-size: 1.1em; }
.duality-box .wave { background: rgba(88,86,214,0.08); border: 1px solid rgba(88,86,214,0.2); }
.duality-box .particle { background: rgba(199,21,133,0.08); border: 1px solid rgba(199,21,133,0.2); }
</style>

# 光的波粒二象性

<div class="timeline">
<div class="era">
<h3>20世纪 — 粒子性的回归</h3>
<p><b>光电效应</b>：光的能量是量子化的</p>
<p><b>康普顿散射</b>：光子具有动量</p>
</div>
</div>

<div class="formula-box">

**光量子关系**：$E = h\nu = pc$，$p = \frac{h}{\lambda}$

</div>

<div class="duality-box">
<div class="side wave">🌊 <b>传播</b>时显示<b>波动性</b></div>
<div class="side particle">⚛ <b>能量转移</b>时显示<b>粒子性</b></div>
</div>

---
layout: two-cols
---

<style scoped>
.bio-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; }
.bio-card h3 { color: #C71585; margin: 0 0 0.3em 0; font-size: 1.2em; }
.bio-card p { margin: 0.2em 0; font-size: 1.05em; line-height: 1.6; }
.quote-box { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-top: 0.8em; border-left: 3px solid #5856d6; font-style: italic; font-size: 1.05em; line-height: 1.5; }
</style>

# 德布罗意假设（1923年提出，1929年获诺奖）

<div class="bio-card">
<h3>L.V. de Broglie（法，1892—1987）</h3>
<p>从辩证思维出发：既然光具有粒子性，实物粒子如电子是否也应当具有波动性？</p>
<p>1924.11.29 博士论文"量子理论的研究"提交巴黎大学</p>
</div>

<div class="quote-box">
"每一个运动的物体都伴随着一个波，而且不可能将物体的运动和波的传播分开。"
</div>

::right::

<img src="/images/de-broglie-portrait.png" style="max-width: 100%; max-height: 400px; object-fit: contain; border-radius: 10px;" />

---

# 德布罗意假设（1923年提出，1929年获诺奖）

<!-- TODO: 缺失图片 pasted-image-28355.tiff，需从Keynote重新导出 -->

<img src="/images/WeChatc972adbd697068c605064e09c291962c-28365.png" style="max-width: 500px; max-height: 400px;" />

<!-- TODO: 缺失图片 pasted-image-28373.tiff，需从Keynote重新导出 -->

---

# 德布罗意假设（1923年提出，1929年获诺奖）

<img src="/images/1_340818701_171_85_3_672765207_5951e9c80a09ad1f8d1a6d3eb395360a-28382.png" style="max-width: 400px; max-height: 400px;" />

---

<style scoped>
.slidev-layout { font-size: 1.2rem; }
.core-box { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-bottom: 0.6em; border-left: 3px solid #C71585; }
.alt-box { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-top: 0.6em; border-left: 3px solid #5856d6; }
.note { font-size: 0.95em; color: #555; margin-top: 0.5em; }
</style>

# 德布罗意假设（1923年提出，1929年获诺奖）

任何具有能量和动量的粒子都伴随着频率为 $\nu$、波长为 $\lambda$ 的**德布罗意波**

<div class="core-box">

**德布罗意关系**

$$E = h\nu \qquad \lambda = \frac{h}{p}$$

</div>

<div class="alt-box">

**等价形式**（$\hbar = h/2\pi$）

$$E = \hbar\omega \qquad \vec{p} = \hbar\vec{k}$$

</div>

<p class="note">德布罗意物质波的群速率等于粒子的速率</p>

---
layout: two-cols
---

# 习题

计算一下物体的德布罗意物质波波长

（a）以10 m/s飞行的质量为0.65 kg的篮球；

（b）动能为1.0 eV的电子；

（c）动能为108 keV的电子

::right::

<img src="/images/400px-Wavelet-22901.gif" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

<style scoped>
.step { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-bottom: 0.5em; border-left: 3px solid #C71585; font-size: 0.95em; }
.result { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-top: 0.5em; border-left: 3px solid #5856d6; font-size: 0.95em; }
</style>

# 习题 (a) 篮球的德布罗意波长

<div class="step">

**篮球动能**：$K = \frac{1}{2}m_0 u^2 = (0.65~\mathrm{kg})(10~\mathrm{m/s})^2/2 = 32.5~\mathrm{J}$

</div>

<div class="step">

**静止质能**：$E_0 = m_0 c^2 = (0.65~\mathrm{kg})(2.998\times10^8~\mathrm{m/s})^2 = 5.84\times10^{16}~\mathrm{J}$

</div>

<div class="step">

$K/(K+E_0) \ll 1$，非相对论近似成立，动量 $p = m_0 u = 6.5~\mathrm{kg \cdot m/s}$

</div>

<div class="result">

**篮球的德布罗意波长**：$\lambda = \frac{h}{p} = \frac{6.626\times10^{-34}~\mathrm{J\cdot s}}{6.5~\mathrm{kg\cdot m/s}} = 1.02\times10^{-34}~\mathrm{m}$

</div>

---

<style scoped>
.step { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-bottom: 0.5em; border-left: 3px solid #C71585; font-size: 0.95em; }
.tip { background: rgba(48,209,88,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-top: 0.5em; border-left: 3px solid #30d158; font-size: 0.9em; }
.result { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-top: 0.5em; border-left: 3px solid #5856d6; font-size: 0.95em; }
</style>

# 习题 (b) 动能 $K=1.0~\mathrm{eV}$ 的电子

<div class="step">

**电子静止质能**：$E_0 = m_0 c^2 = 511~\mathrm{keV}$

</div>

<div class="step">

$K/(K+E_0) \ll 1$，但方便起见仍采用相对论公式 $E^2 = p^2c^2 + E_0^2$

</div>

<div class="tip">

**TIPS**：相对论动量 $p = \sqrt{K(K+2E_0)}/c$

</div>

<div class="result">

**德布罗意波长**：$\lambda = \frac{hc}{\sqrt{K(K+2E_0)}} = \frac{1.241~\mathrm{eV\cdot\mu m}}{\sqrt{1.0~\mathrm{eV}\times[1.0~\mathrm{eV}+2(511~\mathrm{keV})]}} = 1.23~\mathrm{nm}$

</div>

---

<style scoped>
.step { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-bottom: 0.5em; border-left: 3px solid #C71585; font-size: 0.95em; }
.result { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-top: 0.5em; border-left: 3px solid #5856d6; font-size: 0.95em; }
</style>

# 习题 (c) 动能 $K=108~\mathrm{keV}$ 的电子

<div class="step">

$K/(K+E_0) = 108/619$，**相对论效应不能忽略**

</div>

<div class="result">

**德布罗意波长**：$\lambda = \frac{hc}{\sqrt{K(K+2E_0)}} = \frac{1.241~\mathrm{eV\cdot m}}{\sqrt{108~\mathrm{keV}\times[108~\mathrm{keV}+2(511~\mathrm{keV})]}} = 3.55~\mathrm{pm}$

</div>
---

<style scoped>
.slidev-layout { display: flex; flex-direction: column; align-items: center; justify-content: center; }
</style>

# 戴维孙-革末实验

<img src="/images/Screen Shot 2023-03-15 at 19.29.55-28397.png" style="max-width: 85%; max-height: 75vh; object-fit: contain;" />

---
layout: two-cols
---

<style scoped>
.timeline { position: relative; padding-left: 1.5em; margin-top: 0.5em; }
.timeline::before { content: ''; position: absolute; left: 0.35em; top: 0.2em; bottom: 0.2em; width: 2px; background: linear-gradient(to bottom, #5856d6, #C71585); }
.timeline .era { position: relative; margin-bottom: 1em; }
.timeline .era::before { content: ''; position: absolute; left: -1.28em; top: 0.45em; width: 10px; height: 10px; border-radius: 50%; background: #5856d6; }
.slidev-layout { font-size: 1.3rem; }
.timeline .era p { margin: 0.15em 0; font-size: 1.2em; line-height: 1.6; }
.highlight { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.6em 0.8em; margin-top: 0.8em; border-left: 3px solid #C71585; font-size: 1.2em; }
</style>

# 戴维孙-革末实验

<div class="timeline">
<div class="era">
<p><b>1924年</b>：德布罗意提出物质波假设</p>
</div>
<div class="era">
<p><b>1926年</b>：戴维孙、革末了解到德布罗意假设</p>
</div>
<div class="era" style="margin-bottom:0;">
<p><b>1927年</b>：观察到电子衍射现象</p>
</div>
</div>

<div class="highlight">

历史上**第一次**实验证实电子具有波动性

</div>

::right::

<img src="/images/pasted-image-26569.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 戴维孙-革末实验

<img src="/images/Screen Shot 2023-03-15 at 19.33.01-28427.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Screen Shot 2023-03-15 at 19.42.00-28451.png" style="max-width: 500px; max-height: 400px;" />

---
layout: two-cols
---

<style scoped>
.slidev-layout { font-size: 1.2rem; }
.formula-box { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-bottom: 0.6em; border-left: 3px solid #5856d6; }
.obs-card { background: rgba(199,21,133,0.04); border-radius: 10px; padding: 0.5em 0.8em; margin-bottom: 0.5em; border-left: 3px solid #C71585; font-size: 1.05em; line-height: 1.5; }
.result-box { background: rgba(48,209,88,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-top: 0.5em; border-left: 3px solid #30d158; font-size: 1.05em; }
</style>

# 戴维孙-革末实验

<div class="formula-box">

$e\Delta V = K = \frac{p^2}{2m} \Rightarrow p = \sqrt{2me\Delta V}$

</div>

<div class="obs-card">

**随机晶体**：散射电子束强度在各方向大致相同

</div>

<div class="obs-card">

**规则晶体**：特定角度出现明显最大值，呈现清晰的**衍射图案**

</div>

<div class="result-box">

$\Delta V = 54~\mathrm{eV}$，$\varphi = 50°$ 时衍射极大

</div>

::right::

<img src="/images/CNX_UPhysics_39_05_davisson-1-23088.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

<style scoped>
.slidev-layout { font-size: 1.2rem; }
.paper-caption { text-align: center; font-size: 0.85em; color: #666; margin-top: 0.3em; }
</style>

# 戴维孙-革末实验

<img src="/images/davisson-germer-nature-1927.jpg" style="max-width: 100%; max-height: 380px; object-fit: contain; border-radius: 6px; box-shadow: 0 2px 12px rgba(0,0,0,0.1);" />

<p class="paper-caption">C. Davisson & L.H. Germer, <i>Nature</i>, 1927</p>

::right::

<img src="/images/CNX_UPhysics_39_05_davisson2-1-23136.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

<style scoped>
.slidev-layout { font-size: 1.05rem; }
.step { background: rgba(88,86,214,0.06); border-radius: 8px; padding: 0.4em 0.7em; margin-bottom: 0.5em; border-left: 3px solid #5856d6; }
.step-result { background: rgba(48,209,88,0.06); border-radius: 8px; padding: 0.4em 0.7em; margin-bottom: 0.5em; border-left: 3px solid #30d158; }
.step-final { background: rgba(199,21,133,0.06); border-radius: 8px; padding: 0.4em 0.7em; border-left: 3px solid #C71585; font-size: 1.1em; }
</style>

# 戴维孙-革末实验：数值验证

<img src="/images/CNX_UPhysics_39_05_bragg-1-23265.jpg" style="max-width: 90%; max-height: 200px; object-fit: contain; margin-bottom: 0.3em;" />

<div class="step">

**电子动量**：$p = \sqrt{2me\Delta V} = 2.478 \times 10^{-5}~\mathrm{eV \cdot s/m}$

</div>

<v-click>
<div class="step">

**德布罗意波长**：$\lambda = \dfrac{h}{p} = \dfrac{4.136 \times 10^{-15}~\mathrm{eV \cdot s}}{2.478 \times 10^{-5}~\mathrm{eV \cdot s/m}} = 1.67~\mathrm{\AA}$

</div>
</v-click>

::right::

<v-click>
<div class="step-result">

**晶面间距**：$a = 2.15~\mathrm{\AA}$（镍晶体）

**衍射条件**：$n\lambda = a \sin\varphi$

$\Rightarrow \sin\varphi = \dfrac{n\lambda}{a} = 0.776\,n$

</div>
</v-click>

<v-click>
<div class="step-final">

$n=1$：$\varphi \approx 50°$ ✓ 与实验完全吻合！

</div>
</v-click>

---

# 戴维孙-革末实验

<video controls style="width: 95%; max-height: 85vh;">
  <source src="/images/videoplayback-29034.mp4" />
</video>

---

# 汤姆逊衍射实验

同年，英国的汤姆逊用多晶体做电子衍射实验,也得到了电子衍射照片。

<div style="text-align: center; margin-top: 1em;">
<img src="/images/Screen Shot 2023-03-15 at 20.04.58-28471.png" style="max-width: 70%; object-fit: contain;" />
</div>

---

# 汤姆逊衍射实验

同年，英国的汤姆逊用多晶体做电子衍射实验,也得到了电子衍射照片。

十年后，戴维逊、汤姆逊因电子衍射实验的成果共获1937年度诺贝尔物理奖。

<div style="text-align: center; margin-top: 1em;">
<img src="/images/Screen Shot 2022-03-09 at 16.19.29-26625.png" style="max-width: 70%; object-fit: contain;" />
</div>

---

<style scoped>
.slidev-layout { font-size: 1.4rem; }
table { font-size: 1.3em; margin: 0.8em auto; }
th, td { padding: 0.4em 1.2em !important; }
</style>

# 德布罗意波长 $\lambda=1~\AA$ 时各粒子动能

| 光子 | 电子 | 中子 | 氦原子 |
|:---:|:---:|:---:|:---:|
| 12.4 keV | 150 eV | 81 meV | 20 meV |

单原子气体（monatomic gas）在室温下的动能为

$K_{T}=\frac{3}{2} k_{B} T=\frac{3}{2}\left(8.62 \times 10^{-5}~\mathrm{eV/K}\right)(300~\mathrm{K})=38.8~\mathrm{meV}$

---

<style scoped>
.slidev-layout { font-size: 1.3rem; }
.concept { color: #1e90ff; font-size: 1.2em; font-weight: bold; margin-bottom: 0.3em; }
.formula-row { display: flex; align-items: center; gap: 0.8em; margin-top: 0.5em; flex-wrap: wrap; }
.formula-row .arrow { color: #C71585; font-size: 1.5em; }
.bohr { color: #C71585; font-weight: bold; font-size: 1.1em; text-align: right; }
</style>

# 德布罗意波和量子态

<p class="concept">定态 ⟺ 驻波</p>

<img src="/images/CNX_UPhysics_39_05_string-1-23413.jpg" style="width: 95%; object-fit: contain;" />

<div class="formula-row">

$l = n\lambda/2$

<span style="width: 2em;"></span>

电子绕一周之后相位不变，圆周长是波长的整数倍

</div>

<div class="formula-row">

$2\pi r_n = n\lambda = n\dfrac{h}{p}$

<span class="arrow">➡</span>

$L_n = pr_n = n\dfrac{h}{2\pi} = n\hbar$

</div>

<p class="bohr">玻尔量子化条件</p>

---

<style scoped>
.slidev-layout { font-size: 1.4rem; }
</style>

# 波粒二象性（电子散射实验）

1961年，Claus Jönsson在德国进行了第一个电子束双缝实验，证明电子束确实形成了干涉图案，这意味着电子集体表现为波。

<div style="display: flex; justify-content: center; margin-top: 1em;">
<img src="/images/Screen Shot 2023-03-15 at 23.04.28-28494.png" style="width: 85%; object-fit: contain;" />
</div>

---

<style scoped>
.slidev-layout { font-size: 1.4rem; }
</style>

# 波粒二象性（电子散射实验）

1961年，Claus Jönsson在德国进行了第一个电子束双缝实验，证明电子束确实形成了干涉图案，这意味着电子集体表现为波。

<div style="display: flex; flex-direction: column; align-items: center; gap: 0.5em; margin-top: 0.5em;">
<img src="/images/Wave-particle_duality-24264.gif" style="width: 55%; object-fit: contain;" />
<img src="/images/CNX_UPhysics_39_06_duality-1-24258.jpg" style="width: 85%; object-fit: contain;" />
</div>

---

<style scoped>
.slidev-layout { font-size: 1.4rem; }
</style>

# 波粒二象性（电子散射实验）

1974 年意大利的Giulio Pozzi和1989年日本的Akira Tonomura进行了第一个单电子通过狭缝的双缝实验。他们表明，即使电子单独通过狭缝，干涉条纹也会逐渐形成。这最终证明了电子衍射图像是由于电子的波动性而形成的。

<div style="display: flex; justify-content: center; margin-top: 1em;">
<img src="/images/4e86ca73913ca43ca418deaf3e209739_1440w-26675.png" style="width: 70%; object-fit: contain;" />
</div>

---

<style scoped>
table { border-collapse: collapse; width: 95%; margin: 0 auto; }
td { padding: 0.3em; border: none; width: 50%; }
td img { width: 85%; }
.caption { margin-top: 0.5em; font-size: 2rem; text-align: center; }
</style>

# 波粒二象性（电子散射实验）

| | |
|---|---|
| ![](/images/9e67b1b3aaf9576626f97f20e055da11_1440w-26683.png) | ![](/images/14677f39105af01a5a05e422c912ae59_1440w-26691.png) |
| ![](/images/99380bf24481838b19a0e60b1ffcb2e3_1440w-26699.png) | ![](/images/300db4aa0a9cc4ccd804cae19213610c_1440w-26705.png) |

<p class=”caption”>电子不是每次只是随机通过其中的一条缝，而是”同时”通过了两条缝，并和”自己”发生了干涉。</p>

---

# 波粒二象性（电子散射实验）

<img src="/images/Screen Shot 2023-03-15 at 23.21.35-28505.png" style="max-width: 70%;" />

<img src="/images/1_340818701_171_85_3_673605011_57003a3890cf1f96ae77fb258dad939c-28511.png" style="width: 280px; position: absolute; right: 2em; bottom: 2em;" />

---

# 波粒二象性

<div style="display: flex; justify-content: center;">
<img src="/images/23722e3c2ff6ac38e138ab4aba38c01a_1440w-2-26732.png" style="width: 80%;" />
</div>

---

# 波粒二象性

<div style="display: flex; justify-content: center;">
<img src="/images/2aab38f5e9704e365ecf9e118ee0306e_1440w-2-26738.png" style="width: 80%;" />
</div>

---

# 波粒二象性

<div style="display: flex; justify-content: center;">
<video controls style="width: 95%; max-height: 85vh;">
  <source src="/images/Wave-28480-h264.mp4" type="video/mp4" />
</video>
</div>

---

<style scoped>
.slidev-layout { font-size: 1.2rem; }
.frontier { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.5em 0; border-left: 3px solid #5856d6; line-height: 1.7; }
.question { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.5em 0; border-left: 3px solid #C71585; line-height: 1.7; font-size: 1.1em; }
</style>

# 🔬 前沿：量子世界的边界在哪里？

<div class="frontier">

**2019年**：维也纳大学Arndt团队让含 **~2000个原子** 的有机大分子（25,000道尔顿）产生了干涉条纹，德布罗意波长仅 **53飞米**——比氢原子直径小1000倍

</div>

<v-click>
<div class="frontier">

**2026年1月**（*Nature*）：同一团队将记录推至含 **7000+原子的钠纳米粒子**（170,000道尔顿，直径~8nm），质量已接近小型**病毒**！

</div>
</v-click>

<v-click>
<div class="frontier">

**2020年**：天然抗生素多肽**短杆菌肽**（gramicidin，15个氨基酸）也展示了物质波干涉——这是**活细胞产生的分子**

</div>
</v-click>

<v-click>
<div class="question">

**思考**：量子力学有尺寸上限吗？是什么阻止我们看到篮球的干涉条纹？

</div>
</v-click>

<v-click>
<div class="frontier">

**估算**：一个篮球（$m=0.65~\mathrm{kg}$，$v=10~\mathrm{m/s}$）的德布罗意波长 $\lambda = h/mv \approx 10^{-34}~\mathrm{m}$，比质子直径还小 $10^{19}$ 倍——根本不存在这么小的"狭缝"。而且篮球每时每刻都在与 $10^{23}$ 量级的空气分子和热光子碰撞，每次碰撞都会泄露位置信息，在 $10^{-30}~\mathrm{s}$ 内就彻底**退相干**。量子力学本身没有尺寸上限，是**环境**消灭了宏观物体的量子行为。

</div>
</v-click>

---

<style scoped>
.slidev-layout { font-size: 1.2rem; }
.exp-box { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.5em 0; border-left: 3px solid #5856d6; line-height: 1.7; }
.mind-blow { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.5em 0; border-left: 3px solid #C71585; line-height: 1.7; font-size: 1.1em; }
</style>

# 🧪 思考实验：现在的决定能改变过去吗？

<div class="exp-box">

**Wheeler延迟选择实验**：粒子**已经通过了双缝**之后，你再决定是观测"干涉图案"（波）还是"经过哪条缝"（粒子）——结果取决于你**之后**的选择！

</div>

<v-click>
<div class="exp-box">

**2015年实验验证**：澳大利亚国立大学用**单个氦原子**在Mach-Zehnder干涉仪中实现了这一实验。原子进入装置后，实验者才随机决定是否插入第二个分束器。结果完美符合量子力学预言。

</div>
</v-click>

<v-click>
<div class="mind-blow">

**物理学家的解释**：不是"现在改变了过去"，而是**在你测量之前，粒子的"过去"根本就没有确定的状态**。"粒子走了哪条路？"——这个问题在测量之前没有答案，甚至没有意义。

</div>
</v-click>

---

<style scoped>
.slidev-layout { font-size: 1.2rem; }
.item { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.5em 0; border-left: 3px solid #5856d6; line-height: 1.7; }
.highlight-item { background: rgba(48,209,88,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.5em 0; border-left: 3px solid #30d158; line-height: 1.7; }
</style>

# 🌌 前沿：物质波的新应用

<div class="item">

**反物质也是波**：2025年，东京大学首次观测到**正电子偶素**（电子-正电子束缚态）通过石墨烯膜的物质波衍射，证实德布罗意假设对反物质同样成立

</div>

<v-click>
<div class="item">

**太空中的物质波**：2024年，NASA在国际空间站的冷原子实验室（CAL）实现了首次**太空原子干涉**，微重力下原子可自由漂浮150ms以上，灵敏度远超地面实验

</div>
</v-click>

<v-click>
<div class="item">

**中子量子弹跳球**：在法国ILL实验室，超冷中子在镜面上方的引力场中形成**离散的量子能级**——这是引力与量子力学直接交汇的罕见实验

</div>
</v-click>

<v-click>
<div class="highlight-item">

**未来**：全球正在建造百米级原子干涉仪（MAGIS-100@费米实验室、ZAIGA@中国），用物质波探测**暗物质**和**引力波**——德布罗意假设正在成为探索宇宙的工具

</div>
</v-click>

---

<style scoped>
.slidev-layout { font-size: 1.4rem; }
.highlight { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.6em 0; border-left: 3px solid #5856d6; line-height: 1.8; }
.key-point { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.6em 0; border-left: 3px solid #C71585; line-height: 1.8; }
</style>

# 电子显微镜

<div class="highlight">

第一台电子显微镜是由德国鲁斯卡（E·Ruska）研制成功，荣获**1986年诺贝尔物理奖**。

</div>

<div class="highlight">

从波动光学可知，由于显微镜的分辨本领与波长成反比，光学显微镜的最大分辨距离大于 $0.2~\mu\mathrm{m}$，最大放大倍数也只有1000倍左右。

</div>

<div class="key-point">

自从发现电子有波动性后，电子束德布罗意波长比光波波长短得多，而且极方便改变电子波的波长。这样就能制造出用**电子波代替光波**的电子显微镜。

</div>

---

<div style="display: flex; justify-content: center;">
<video controls style="width: 95%; max-height: 85vh;">
  <source src="/images/Untitled-26745.mp4" type="video/mp4" />
</video>
</div>

---

<style scoped>
.slidev-layout { font-size: 1.4rem; }
.summary-item { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin: 0.7em 0; border-left: 3px solid #5856d6; line-height: 1.8; }
</style>

# 小结

<div class="summary-item">

**德布罗意物质波假设**：任何具有动量的粒子也是波。波长与粒子的动量大小成反比。物质波的速度就是粒子的速度。

</div>

<div class="summary-item">

**玻尔模型的解释**：德布罗意物质波概念为玻尔氢原子模型中电子角动量的量化提供了基本原理。

</div>

<div class="summary-item">

**戴维孙-革末实验**：电子从结晶镍表面散射，观察到电子物质波的衍射图案。它们是物质波存在的证据。在各种粒子的衍射实验中观察到物质波。

</div>

---


# §13 不确定关系

需要掌握的知识点：

（1）描述位置-动量不确定关系的物理意义

（2）解释量子理论中不确定性原理的起源

（3）描述能量-时间不确定性关系的物理意义

---
layout: two-cols
---

# 观测效应（Observer Effect）

测量本身会干扰被测量的对象，这在经典物理中也存在。

<br>

**例：测胎压**

用气压表测轮胎胎压时，必须放出少量气体，导致轮胎内气压改变，无法精确测量原始胎压。

<div v-click>

<br>

**微观世界更极端：**

要"看见"电子的位置，至少需要一个光子去照亮它。但光子与电子的能量和动量可比拟，观测必然带来显著扰动。

</div>

::right::

<img src="/images/aid120258-v4-728px-Check-Air-Pressure-in-Tires-Step-10-Version-2.jpg.webp-28524.jpeg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 海森堡显微镜思想实验

用波长为 $\lambda$ 的光子去测量电子的位置：

- **位置的不确定性**取决于光的波长：$\Delta x \sim \lambda$

  波长越短，"分辨率"越高，位置测得越准

<div v-click>

- **动量的不确定性**取决于光子的动量：$\Delta p \sim \frac{h}{\lambda}$

  光子波长越短，光子动量越大，对电子的"踢"越猛

</div>

<div v-click>

<div style="border: 2px solid #C71585; border-radius: 8px; padding: 12px 16px; margin-top: 16px; background: #fef0f5;">

**两者此消彼长**：$\Delta x \cdot \Delta p \sim h$

位置测得越准确，动量就变得越不确定，反之亦然。

</div>

</div>

---
layout: two-cols
---

# 单缝衍射验证不确定关系

电子束通过宽度为 $a$ 的单缝：

**1）位置的不确定度**

电子通过缝隙，其 $x$ 方向位置被限制为：

$$\Delta x = a$$

<div v-click>

**2）动量的不确定度**

电子通过缝后发生衍射，$x$ 方向获得动量分量。忽略次级极大，认为电子主要落在中央亮纹内：

$$\Delta p_x = p\sin\theta_1$$

</div>

::right::

<img src="/images/pasted-image-26779.png" style="max-width: 95%; max-height: 160px; object-fit: contain; margin-bottom: 0.5rem;" />

<img src="/images/pasted-image-26793.png" style="max-width: 95%; max-height: 260px; object-fit: contain;" />

---

# 单缝衍射验证（续）

考虑到衍射条纹有次级极大，更一般地：$\Delta p_x \geq p\sin\theta_1$

<div v-click>

**利用衍射条件和德布罗意关系：**

一级极小的衍射角：$\sin\theta_1 = \dfrac{\lambda}{\Delta x}$

德布罗意关系：$\lambda = \dfrac{h}{p}$

</div>

<div v-click>

代入得：

$$\sin\theta_1 = \frac{h}{p \cdot \Delta x} \quad \Longrightarrow \quad \Delta p_x \geq \frac{h}{\Delta x}$$

即 $\boxed{\Delta x \cdot \Delta p_x \geq h}$

缝越窄（ $\Delta x$ 越小），衍射越宽（ $\Delta p_x$ 越大），<span class="kaiti-accent">不确定关系得到验证！</span>

</div>

---

# 单缝衍射实验演示

<video controls style="max-width: 80%; max-height: 400px; margin: 10px auto; display: block;">
  <source src="/images/ΦºúΘçèµ╡╖µú«σáíτÜäΣ╕ìτí«σ«ÜµÇºσÄƒτÉå-28705.mp4" />
</video>

缝宽减小 → 衍射图样展宽 → 动量不确定度增大

---

# 从"测不准"到"不确定"

前面的思想实验和单缝衍射似乎在说：**测量行为扰动了粒子**，所以"测不准"。

<div v-click>

但这只是故事的一半。更深刻的问题是：

**如果我们不去测量，电子是否同时拥有确定的位置和动量？**

</div>

<div v-click>

答案是**否**。不确定性源于波粒二象性的数学本质，与是否有人观测无关。

</div>

<div v-click>

<span class="kaiti-accent">不确定性不是测量的缺陷，而是微观粒子的本性。</span>

海森堡最初称其为"测不准关系"（Unschärferelation），后来物理学界逐渐认识到：这不是"测不准"，而是"本来就不确定"。

</div>

---
layout: two-cols
---

# 什么是波包？

§12 中德布罗意告诉我们：动量为 $p$ 的粒子对应波长 $\lambda = h/p$，即平面波 $\psi = Ae^{i(kx-\omega t)}$，其中 $k = p/\hbar$。

但平面波在空间中**无限延伸**，粒子的位置完全不确定！

<div v-click>

**波包**：将多个不同 $k$（不同动量）的德布罗意波叠加，构造出局域化的波形：

$$\psi(x) = \int_{-\infty}^{\infty} \phi(k) \, e^{ikx} \, dk$$

- 波包内部的振荡 → 对应粒子的德布罗意波长（中心动量 $p_0 = \hbar k_0$）
- 波包的包络宽度 → 对应粒子位置的不确定范围

</div>

<div v-click>

$\phi(k)$ 是各动量成分的权重，叠加的动量越多，波包越窄，位置越确定。

</div>

::right::

<img src="/images/Sequential_superposition_of_plane_waves-25514.gif" style="max-width: 95%; max-height: 240px; object-fit: contain; margin-top: 2rem;" />

<div style="text-align: center; font-size: 0.85em; color: #888; margin-top: 0.5rem;">

逐步叠加德布罗意平面波 → 形成局域波包

</div>

---

# 波包的位置与频率：此消彼长

<div style="background: #1a1a2e; border-radius: 8px; padding: 10px 16px 8px;">
<div style="display: flex; gap: 12px; justify-content: center;">
  <div style="text-align: center;">
    <div style="color: #ccc; font-size: 0.8em; margin-bottom: 4px;">位置空间 ψ(x)</div>
    <canvas id="posC" width="380" height="200" style="background: #0d0d1a; border-radius: 6px;"></canvas>
  </div>
  <div style="text-align: center;">
    <div style="color: #ccc; font-size: 0.8em; margin-bottom: 4px;">频率（动量）空间 φ(k)</div>
    <canvas id="momC" width="380" height="200" style="background: #0d0d1a; border-radius: 6px;"></canvas>
  </div>
</div>
<div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin: 8px 0 2px; color: #ccc; font-size: 0.85em;">
  <span>波包宽度：</span>
  <span style="color:#888; font-size:0.8em;">窄</span>
  <input type="range" id="sigSlider" min="0.3" max="4.0" step="0.01" value="1.5" style="width: 240px; accent-color: #C71585;">
  <span style="color:#888; font-size:0.8em;">宽</span>
  <span id="obsT" style="color: #f0c040; font-size: 0.85em; min-width: 200px;"></span>
</div>
<div style="text-align: center; color: #888; font-size: 0.75em; margin-top: 2px;">
  思考：这个"一窄一宽"是波的数学性质，和有没有人去测量无关。对微观粒子意味着什么？
</div>
</div>

<script setup>
import { onMounted } from 'vue'
onMounted(() => {
  const posC = document.getElementById('posC')
  const momC = document.getElementById('momC')
  if (!posC || !momC) return
  const pCtx = posC.getContext('2d')
  const mCtx = momC.getContext('2d')
  const slider = document.getElementById('sigSlider')
  const obsT = document.getElementById('obsT')
  const G = (x, s) => Math.exp(-x*x/(2*s*s))

  function drawAxis(ctx, W, H, label) {
    ctx.strokeStyle = '#444'; ctx.lineWidth = 1
    ctx.beginPath(); ctx.moveTo(0, H/2); ctx.lineTo(W, H/2); ctx.stroke()
    ctx.fillStyle = '#666'; ctx.font = 'italic 12px serif'
    ctx.fillText(label, W-14, H/2-6)
  }

  function draw() {
    const sx = parseFloat(slider.value), sk = 1/(2*sx), k0 = 8, N = 600
    const W = posC.width, H = posC.height, a = H/2-18

    pCtx.clearRect(0,0,W,H); drawAxis(pCtx,W,H,'x')
    const xR = 10
    // envelope fill
    pCtx.fillStyle = 'rgba(240,101,149,0.08)'
    pCtx.beginPath()
    for(let i=0;i<=N;i++){const x=-xR+2*xR*i/N; const px=i/N*W; const py=H/2-G(x,sx)*a; i?pCtx.lineTo(px,py):pCtx.moveTo(px,py)}
    pCtx.lineTo(W,H/2); pCtx.lineTo(0,H/2); pCtx.fill()
    // envelope
    pCtx.strokeStyle='rgba(240,101,149,0.3)'; pCtx.lineWidth=1; pCtx.beginPath()
    for(let i=0;i<=N;i++){const x=-xR+2*xR*i/N; const px=i/N*W; const py=H/2-G(x,sx)*a; i?pCtx.lineTo(px,py):pCtx.moveTo(px,py)}
    pCtx.stroke()
    // wave
    pCtx.strokeStyle='#4dabf7'; pCtx.lineWidth=1.5; pCtx.beginPath()
    for(let i=0;i<=N;i++){const x=-xR+2*xR*i/N; const px=i/N*W; const py=H/2-G(x,sx)*Math.cos(k0*x)*a; i?pCtx.lineTo(px,py):pCtx.moveTo(px,py)}
    pCtx.stroke()
    // Δx lines
    const xc=W/2, dxP=sx/xR*(W/2)
    pCtx.strokeStyle='rgba(240,192,64,0.5)'; pCtx.lineWidth=1; pCtx.setLineDash([4,3])
    ;[xc-dxP,xc+dxP].forEach(x=>{pCtx.beginPath();pCtx.moveTo(x,8);pCtx.lineTo(x,H-6);pCtx.stroke()})
    pCtx.setLineDash([])

    // momentum
    const MW=momC.width, MH=momC.height, kR=20
    mCtx.clearRect(0,0,MW,MH); drawAxis(mCtx,MW,MH,'k')
    mCtx.fillStyle='rgba(81,207,102,0.1)'; mCtx.beginPath()
    for(let i=0;i<=N;i++){const k=-kR+2*kR*i/N; const px=i/N*MW; const py=MH/2-G(k-k0,sk)*a; i?mCtx.lineTo(px,py):mCtx.moveTo(px,py)}
    mCtx.lineTo(MW,MH/2); mCtx.lineTo(0,MH/2); mCtx.fill()
    mCtx.strokeStyle='#51cf66'; mCtx.lineWidth=2; mCtx.beginPath()
    for(let i=0;i<=N;i++){const k=-kR+2*kR*i/N; const px=i/N*MW; const py=MH/2-G(k-k0,sk)*a; i?mCtx.lineTo(px,py):mCtx.moveTo(px,py)}
    mCtx.stroke()
    const kc=(k0+kR)/(2*kR)*MW, dkP=sk/kR*(MW/2)
    mCtx.strokeStyle='rgba(240,192,64,0.5)'; mCtx.lineWidth=1; mCtx.setLineDash([4,3])
    ;[kc-dkP,kc+dkP].forEach(x=>{mCtx.beginPath();mCtx.moveTo(x,8);mCtx.lineTo(x,MH-6);mCtx.stroke()})
    mCtx.setLineDash([])

    const r=sx/1.5
    obsT.textContent = r<0.5?'位置窄 → 频率宽':r<0.85?'位置较窄 → 频率较宽':r<1.2?'两边宽度适中':r<2?'位置较宽 → 频率较窄':'位置宽 → 频率窄'
  }
  slider.addEventListener('input', draw)
  draw()
})
</script>

---

# 宏观物体也有不确定性吗？

**问题**：如果动量确定就意味着位置不确定，那宏观物体呢？一个棒球的动量和位置不是都确定的吗？

<div v-click>

**算一算**：一个棒球（$m = 0.145$ kg，$v = 40$ m/s）

$$\lambda_{\text{dB}} = \frac{h}{mv} = \frac{6.63 \times 10^{-34}}{0.145 \times 40} \approx 10^{-34} \text{ m}$$

</div>

<div v-click>

即使 $\Delta x$ 小到 $10^{-20}$ m（比原子核还小一万倍），$\Delta p$ 也只有 $\sim 10^{-15}$ kg·m/s，对宏观运动完全可忽略。

</div>

<div v-click>

<span class="kaiti-accent">宏观物体不是没有不确定性，而是 $\hbar$ 太小，Δx 和 Δp 可以同时小到无法察觉。</span>

量子效应只在微观尺度显著，原因正在于此：只有当德布罗意波长 $\lambda_{\text{dB}}$ 与物体尺寸可比拟时，波动性才会显现。

</div>

---

# 海森堡不确定性原理（1927）

<div style="border: 2px solid #C71585; border-radius: 10px; padding: 16px 20px; margin: 8px 0; background: #fef0f5; text-align: center; font-size: 1.3em;">

$$\Delta x \cdot \Delta p_{x} \geq \frac{\hbar}{2}$$

</div>

| 年份 | 里程碑 |
|------|--------|
| 1924 | 德布罗意提出物质波假说 |
| 1925 | 海森堡建立矩阵力学 |
| 1926 | 薛定谔建立波动方程 |
| 1927 | 海森堡提出不确定性原理（基于对易关系 $[\hat{x}, \hat{p}] = i\hbar$） |
| 1927 | 肯纳德（Kennard）用标准差严格推导 $\sigma_x \sigma_p \geq \hbar/2$ |
| 1929 | 罗伯逊（Robertson）推广到一般共轭变量 |

---
layout: two-cols
---

# 海森堡不确定性原理

<img src="/images/Screenshot 2023-03-20 at 14.44.08-28558.png" style="max-width: 100%; max-height: 380px; object-fit: contain;" />

::right::

<img src="/images/Screenshot 2023-03-20 at 14.49.01-28573.png" style="max-width: 100%; max-height: 380px; object-fit: contain;" />

---
layout: two-cols
---

# 海森堡不确定性原理

<img src="/images/Screenshot 2023-03-20 at 15.04.55-28623.png" style="max-width: 100%; max-height: 380px; object-fit: contain;" />

::right::

<img src="/images/Screenshot 2023-03-20 at 15.05.03-28617.png" style="max-width: 100%; max-height: 380px; object-fit: contain;" />

---
layout: two-cols
---

# 海森堡不确定性原理

<img src="/images/Screenshot 2023-03-20 at 15.29.00-28662.png" style="max-width: 100%; max-height: 380px; object-fit: contain;" />

::right::

<img src="/images/Screenshot 2023-03-20 at 15.30.38-28670.png" style="max-width: 100%; max-height: 380px; object-fit: contain;" />

---

# 思考：原子为什么不会坍缩？

经典电动力学预言：电子绕核做加速运动，会不断辐射能量，应该在 $\sim 10^{-11}$ s 内螺旋坠入原子核。

**问题**：用不确定性原理解释为什么原子是稳定的，并估算氢原子的大小。

<div v-click>

**解**：设电子被限制在半径 $r$ 的范围内，$\Delta x \sim r$

由 $\Delta x \cdot \Delta p \geq \hbar/2$，得 $\Delta p \geq \dfrac{\hbar}{2r}$

动能的最小估算：$K \sim \dfrac{(\Delta p)^2}{2m} \sim \dfrac{\hbar^2}{8mr^2}$

</div>

<div v-click>

总能量：$E(r) = \dfrac{\hbar^2}{8mr^2} - \dfrac{e^2}{4\pi\varepsilon_0 r}$

- $r$ 很大：势能项主导，$E < 0$，电子被束缚
- $r$ 很小：动能项（$\propto 1/r^2$）增长更快，能量反而升高

</div>

<div v-click>

对 $r$ 求极小：$\dfrac{dE}{dr} = 0 \Rightarrow r_{\min} \sim \dfrac{4\pi\varepsilon_0 \hbar^2}{me^2} \sim 0.05~\text{nm}$

与玻尔半径 $a_0 = 0.053$ nm 量级一致！$E_{\min} \sim -13.6$ eV

<span class="kaiti-accent">不确定性原理提供了"零点能"，阻止电子坍缩到原子核上。</span>

</div>

---

# 能量-时间不确定性关系

由相对论能量-动量关系：$p^{2} c^{2}=E^{2}-m_{0}^{2} c^{4}$

两边微分：$2pc^2 \, dp = 2E \, dE$，即 $\Delta p = \dfrac{E}{pc^2} \Delta E$

<div v-click>

粒子位移的不确定度：$\Delta x = v \Delta t = \dfrac{p}{m} \Delta t$（其中 $v = p/m$, $E = mc^2$）

</div>

<div v-click>

将 $\Delta x$ 和 $\Delta p$ 代入 $\Delta x \cdot \Delta p \geq \dfrac{\hbar}{2}$：

$$\frac{p}{m}\Delta t \cdot \frac{E}{pc^2}\Delta E = \frac{E}{mc^2}\Delta E \cdot \Delta t = \Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

</div>

<div v-click>

<div style="border: 2px solid #C71585; border-radius: 10px; padding: 16px 20px; margin-top: 12px; background: #fef0f5; text-align: center; font-size: 1.3em;">

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

</div>

**物理意义**：存在时间越短的量子态（$\Delta t$ 小），其能量越不确定（$\Delta E$ 大）。

</div>

---

# 能量-时间不确定性：谱线的自然宽度

**问题**：激发态不是哈密顿量的本征态吗？本征值怎么会有宽度？

<div v-click>

理想的氢原子（纯库仑势 $H_0$）确实有精确的激发态能级，它们是永远稳定的定态。

但现实中，电磁场无处不在。即使没有外加光源，真空中也存在电磁场的零点涨落。原子始终处在与辐射场的耦合之中：$H = H_0 + H_{\text{int}}$

</div>

<div v-click>

因此：

- **有激发，就有辐射场**：激发态会通过自发辐射衰变，不再是完整 $H$ 的本征态
- **基态不会衰变**（没有更低的态），寿命 $\tau \to \infty$，能量严格确定

</div>

<div v-click>

寿命为 $\tau$ 的激发态，其能级具有自然宽度：

$$\Gamma = \frac{\hbar}{\tau}$$

$\tau$ 越短，谱线越宽。这在实验中可以直接观测到。

</div>

---

# 思考：电子能不能住在原子核里？

早期 β 衰变实验中，原子核释放出电子。物理学家曾争论：电子是本来就住在原子核里，还是衰变时新产生的？

**问题**：用不确定性原理判断电子能否被限制在原子核内（核半径 $r \sim 1~\text{fm} = 10^{-15}~\text{m}$）。

<div v-click>

**解**：若电子被限制在 $\Delta x \sim 10^{-15}$ m 的范围内：

$$\Delta p \geq \frac{\hbar}{2\Delta x} = \frac{1.055 \times 10^{-34}}{2 \times 10^{-15}} \approx 5.3 \times 10^{-20}~\mathrm{kg \cdot m/s}$$

</div>

<div v-click>

对应的动能（需要用相对论）：

$$K = \sqrt{(pc)^2 + (m_ec^2)^2} - m_ec^2 \approx pc \approx 100~\text{MeV}$$

这远远超过核力的典型束缚能（$\sim$几 MeV）。

</div>

<div v-click>

<span class="kaiti-accent">电子不可能被束缚在原子核内。β 衰变中的电子是在衰变过程中新产生的（中子→质子+电子+反中微子）。</span>

对比：质子质量是电子的 1836 倍，$K \sim 0.05$ MeV，可以被核力束缚。

</div>

---

# 练习：激发态的频率不确定性

原子激发态的典型寿命 $\Delta t = 10^{-8}$ s，发射光子的平均频率 $\nu = 7.1 \times 10^{14}$ Hz。

**问题**：发射光子的频率不确定性是多少？辐射是单色的吗？

<div v-click>

**解**：由能量-时间不确定性关系 $\Delta E \geq \dfrac{\hbar}{2\Delta t}$

又 $\Delta E = h \Delta f$，因此：

$$\Delta f \geq \frac{1}{4\pi \Delta t} = \frac{1}{4\pi \times 10^{-8}} \approx 8.0 \times 10^{6} ~\text{Hz}$$

</div>

<div v-click>

**分析**：$\dfrac{\Delta f}{\nu} = \dfrac{8.0 \times 10^6}{7.1 \times 10^{14}} \approx 1.1 \times 10^{-8}$

频率展宽仅约 $10^{-8}$，辐射近似单色，但**严格意义上不存在完美单色光**。

</div>

---

# 爱因斯坦 vs 玻尔：光子箱思想实验

爱因斯坦不接受不确定性原理，在1930年索尔维会议上提出了精巧的**光子箱**思想实验：

一个箱子里装满光子，箱壁有一个由时钟控制的快门。在精确时刻 $t$ 打开快门，放出一个光子。称量箱子的质量变化 $\Delta m$，由 $E = mc^2$ 得到光子能量。

**挑战**：这样不是可以同时精确测量 $E$ 和 $t$，违反 $\Delta E \cdot \Delta t \geq \hbar/2$ 吗？

<div v-click>

**玻尔的反驳**（用爱因斯坦自己的广义相对论！）：

称量质量需要在引力场中测量箱子的位移 $\Delta x$。根据广义相对论，引力场中不同高度的时钟走速不同（引力红移）：

$$\Delta t = \frac{g \Delta x}{c^2} \cdot t$$

</div>

<div v-click>

箱子位置的不确定性 $\Delta x$ 导致时钟读数的不确定性 $\Delta t$，代入计算后恰好满足：

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

<span class="kaiti-accent">爱因斯坦被自己创立的理论击败了。此后他不再试图推翻不确定性原理，转而质疑量子力学的完备性（EPR佯谬）。</span>

</div>

---

# 前沿：能否"绕过"不确定性原理？

<div style="font-size: 0.95em;">

**2025年，Science Advances**：悉尼大学 Valahu、Tan 等人用囚禁离子实现了**同时**精确测量位置和动量，精度超越"标准量子极限"。

<div v-click>

**方法**：将离子制备在量子纠错中发展出的**网格态**（grid states）。不确定性并没有消失，而是被"挤"到了粗粒度的大尺度跳跃上，在精细尺度上实现了超越经典极限的测量精度。

**应用前景**：无 GPS 环境的量子导航（潜艇、地下、太空）、生物医学成像、引力探测。

</div>

</div>

<div v-click style="font-size: 0.95em; margin-top: 0.8rem;">

**2026年，Physical Review Research**：维也纳工业大学 Sponar 等人用中子自旋实验发现了新的不确定性关系：

$$\text{correlation}^2 + \text{disturbance}^2 \leq 1$$

测量的**关联度**与**扰动度**之间存在圆形约束，实验数据完美落在理论预言的圆上。为量子测量设备的校准提供了新工具。

</div>

<div style="font-size: 0.7em; color: #888; margin-top: 0.8rem; line-height: 1.5;">

[1] C.H. Valahu et al., "Quantum-enhanced multiparameter sensing in a single mode," *Science Advances* **11**, eadw9757 (2025). DOI: 10.1126/sciadv.adw9757

[2] A. Asadian, F. Gams, S. Sponar, "Covariant correlation-disturbance relation and its experimental realization with spin-1/2 particles," *Phys. Rev. Research* **8** (2026). DOI: 10.1103/llgb-gql9

</div>

---

# 前沿：不确定性原理本身需要修正吗？

所有量子引力理论（弦论、圈量子引力、黑洞物理）都预言：存在一个**最小可测长度**，约为普朗克长度 $\ell_P = \sqrt{\hbar G/c^3} \approx 1.6 \times 10^{-35}$ m。

<div v-click>

这意味着海森堡不确定性原理可能需要修正为**广义不确定性原理**（GUP）：

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}\left(1 + \beta \frac{(\Delta p)^2}{M_P^2 c^2}\right)$$

当 $\Delta p$ 接近普朗克尺度时，$\Delta x$ 存在下界，不能无限小！

</div>

<div v-click style="font-size: 0.95em;">

**实验探索**：

- **LIGO 引力波探测器**（2023，*Phys. Rev. X*）：利用量子压缩光突破标准量子极限，灵敏度已接近可能探测到普朗克尺度修正的区域
- **AURIGA 引力波棒探测器**（Marin et al., *Nature Physics* 2013）：将吨级机械振子冷却到亚毫开尔文，对宏观物体的基态能量的普朗克尺度修正给出了实验上限

</div>

<div v-click style="font-size: 0.95em;">

如果 GUP 被实验证实，将是**量子力学建立百年以来最深刻的修正**，意味着时空本身在最小尺度上是离散的。

</div>

<div style="font-size: 0.7em; color: #888; margin-top: 0.5rem; line-height: 1.5;">

[3] LIGO et al., "Broadband quantum enhancement of the LIGO detectors with frequency-dependent squeezing," *Phys. Rev. X* **13**, 041021 (2023)

[4] F. Marin et al., "Gravitational bar detectors set limits to Planck-scale physics on macroscopic variables," *Nature Phys.* **9**, 71 (2013)

</div>

---

# 如果 $h = 1$……

<div style="display: flex; gap: 1.5rem; align-items: center; margin-top: 0.5rem;">
<img src="/images/tompkins-cover.png" style="max-height: 360px; object-fit: contain; flex-shrink: 0;" />
<div>
<img src="/images/tompkins-billiards.jpg" style="max-width: 100%; max-height: 280px; object-fit: contain;" />
<div style="font-size: 0.95em; margin-top: 0.8rem;">

如果普朗克常数和日常尺度可比拟，不确定性效应将无处不在：把台球限定在三角框里，它就会剧烈抖动！

</div>
<div style="font-size: 0.8em; color: #888; margin-top: 0.3rem;">

乔治·伽莫夫《物理世界奇遇记》：汤普金斯先生在一个 $h$ 很大的世界里打台球

</div>
</div>
</div>

---

# 课外阅读

<img src="/images/1_799760234_171_85_3_675143862_bd7c9602dcfebe6ce1c760938b27cecb-28678.png" style="max-width: 400px; max-height: 400px;" />

推荐阅读：关于不确定性原理的深入讨论与思考


---

# §14 波函数

需要掌握的知识点：

（1）描述波函数的统计解释

（2）使用波函数来确定概率

（3）计算位置的期望值

---

# 波粒二象性如何统一？

<img src="/images/pasted-image-27189.jpeg" style="max-width: 90%; max-height: 180px; object-fit: contain; margin: 0 auto; display: block;" />

<div style="display: flex; gap: 1.5rem; align-items: center; margin-top: 1rem;">
<div style="flex: 1;">

粒子性和波动性这两个完全不同的性质，如何统一到微观粒子上？

<div v-click>

费曼设计了一组理想实验来回答这个问题：用**子弹、水波、电子**分别通过双缝，比较它们在屏上的分布。

</div>

</div>
<div style="flex-shrink: 0; text-align: center;">
<img src="/images/pasted-image-27196.jpeg" style="max-height: 200px; object-fit: contain;" />
<div style="font-size: 0.75em; color: #888;">

费曼（1918–1988）

1965年诺贝尔物理学奖

</div>
</div>
</div>

---
layout: two-cols
---

# 子弹的双缝实验

开单缝：子弹密度分布为 $P_1$ 或 $P_2$

开双缝：分布为 $P_{12} = P_1 + P_2$

<div v-click>

子弹是经典粒子，概率直接相加，**没有干涉**。

这是"非相干叠加"，体现的是**粒子性**。

</div>

::right::

<img src="/images/pasted-image-27233.jpeg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 水波的双缝实验

水波通过双缝后在屏上的分布与子弹相同吗？

<div v-click>

不同！水波通过双缝时分为两个相干的次波源，在空间进行**相干叠加**，屏上呈现**干涉图样**。

强度：$I_{12} \neq I_1 + I_2$（有交叉项）

</div>

::right::

<img src="/images/pasted-image-27271.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 电子的双缝实验

**关键问题**：电子的双缝实验结果像子弹还是像水波？

<div v-click>

实验结果：屏上出现了**干涉条纹**！

但每个电子到达屏时都是一个**亮点**（粒子性）。

</div>

<div v-click>

**矛盾**：

- 如果电子是粒子，过缝时走一条缝，就不该有干涉
- 如果电子是波，过缝时弥散开来，就不该打出一个点

经典物理无法调和这个矛盾。

</div>

::right::

<img src="/images/pasted-image-27296.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 概率波

在量子力学建立的初期，人们对德布罗意波的含义提出过各种猜测：

- 电子波是代表电子实体的波包？
- 电子本身是弥散于空间的物质波动？
- 电子的波动性是大量电子之间的相互作用？

<div v-click>

这些猜测最终都因不能圆满解释实验现象而被放弃。

</div>

<div v-click>

1926年，玻恩（M. Born）提出了**统计诠释** ：

<div style="border: 2px solid #C71585; border-radius: 8px; padding: 12px 16px; margin-top: 8px; background: #fef0f5;">

德布罗意波是**概率波**：波函数的模方 $|\Psi|^2$ 代表在该处找到粒子的概率密度。

</div>

</div>

---
layout: two-cols
---

# 什么是波函数

宏观的波需要：振幅、波长、相位、含时演化。

物质波也是波，也应该具备这些信息。

<div v-click>

量子力学的平面波波函数写为复数形式：

$$\Psi(x, t) = A e^{i(kx - \omega t)}$$

- $k = p/\hbar$（德布罗意关系）
- $\omega = E/\hbar$（普朗克关系）

</div>

<div v-click>

为什么用复数？因为波函数本身**不可直接测量**，可测量的是概率密度 $|\Psi|^2 = \Psi^* \Psi$。

</div>

::right::

<img src="/images/600px-Wave_Sinusoidal_Cosine_wave_sine_Blue.svg-2-24291.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/AC_wave_Positive_direction-2-24272.gif" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/Plane_Wave_3D_Animation_300x216_255Colors-2-24278.gif" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

---
layout: two-cols
---

# 光的波函数与概率

对于光（电磁波）：

- 波函数是电场 $E(x,t)$
- 能量密度正比于 $|E|^2$
- 单个光子的能量 $\varepsilon = h\nu$

<div v-click>

因此 $|E|^2$ 正比于光子数密度，也就是光子打在屏幕上某点的**概率**。

爱因斯坦的洞见：光的振幅的平方是光子出现概率的量度。

</div>

<div v-click>

玻恩将同样的逻辑推广到物质波：

$|\Psi(x,t)|^2$ 就是粒子出现在 $x$ 处的概率密度。

</div>

::right::

<img src="/images/CNX_UPhysics_40_01_TwoSlit-1-24365.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 波函数的统计解释（M. Born, 1926）

波函数 $\Psi(x,t)$ 的模方 $|\Psi(x,t)|^2$ 是**概率密度**：

在 $t$ 时刻，粒子出现在 $x$ 到 $x+dx$ 区间内的概率为：

$$P(x, x+dx) = |\Psi(x,t)|^2 \, dx$$

<div v-click>

**波恩的概率解释**是量子力学的基本原理之一：

- $\Psi$ 是概率幅（不可直接测量）
- $|\Psi|^2$ 是概率密度（可测量）
- 1954年诺贝尔物理学奖

</div>

::right::

<video controls style="max-width: 100%; max-height: 400px; object-fit: contain;">
  <source src="/images/1-24677.mp4" />
</video>

---

# 波函数的统计解释（M. Born, 1926）

<img src="/images/CNX_UPhysics_40_01_Prob_Square-1-24588.jpg" style="max-width: 70%; max-height: 350px; margin: 10px auto; display: block;" />

<div v-click>

**波函数坍缩**：当不被观测时，粒子处于各位置的叠加态。一旦测量，波函数"坍缩"到某个确定位置，概率由 $|\Psi|^2$ 给出。

</div>

---

# 爱因斯坦 vs 玻恩："上帝掷骰子吗？"

In a letter to Born on 4 December 1926, Einstein made his famous remark:

<div style="border-left: 3px solid #C71585; padding-left: 16px; margin: 12px 0; font-style: italic; font-size: 0.95em;">

"Quantum mechanics is certainly imposing. But an inner voice tells me that it is not yet the real thing. The theory says a lot, but does not really bring us any closer to the secret of the 'old one'. I, at any rate, am convinced that He is not playing at dice."

</div>

<div v-click>

This quotation is often paraphrased as **"God does not play dice"**.

Niels Bohr reportedly replied: **"Stop telling God what to do."**

</div>

---

# 哥本哈根解释

哥本哈根解释是量子力学最主流的诠释框架，其核心要点：

<div v-click>

**量子态的叠加**：观测之前，量子系统可以同时处于多个可能状态的叠加。

</div>

<div v-click>

**波函数坍缩**：测量时，波函数"坍缩"到某个确定状态，这个过程是不可逆的。

</div>

<div v-click>

**互补性原理**（玻尔）：波动性和粒子性是量子现象的两个互补方面，只能在不同的实验安排中分别观察到。

</div>

<div v-click>

**不确定性原理**（海森堡）：位置和动量不能同时被精确确定，这是自然界的基本性质。

</div>

---

# 量子力学的其他解释：多世界解释

<div style="display: flex; gap: 2rem; align-items: flex-start;">
<div style="flex: 1;">

**多世界解释**（休·埃弗雷特，1957）

<div v-click>

波函数**从不坍缩**。每次量子测量时，宇宙"分裂"为所有可能结果对应的分支，每个分支中的观测者只看到一个结果。

</div>

<div v-click>

薛定谔的猫不再是悖论：宇宙分裂成两个分支，一个分支中猫活着，另一个中猫死了。

</div>

<div v-click>

数学上最简洁（无额外假设），但无法实验验证其他"世界"的存在。近年来在量子计算领域越来越受欢迎。

</div>

</div>
<div style="flex-shrink: 0; width: 280px; text-align: center;">

<img src="/images/Schroedingers_cat_film.svg-29098.png" style="max-width: 100%; max-height: 120px; object-fit: contain;" />

<img src="/images/9780691645926.jpg-29105.jpeg" style="max-width: 80%; max-height: 150px; object-fit: contain; margin-top: 0.5rem;" />

<img src="/images/1_340818701_171_85_3_824378794_c0eab89545593cfdca20f31f5498b98c-29121.png" style="max-width: 90%; max-height: 90px; object-fit: contain; margin-top: 0.5rem;" />

</div>
</div>

---
layout: two-cols
---

# 量子力学的其他解释

**隐变量理论**（德布罗意-玻姆理论，1952）

<div v-click>

核心思想：粒子在任何时刻都有**确定的位置和轨迹**，但受到一个"导航波"（pilot wave）的引导。波函数是真实存在的物理场，引导粒子运动。

</div>

<div v-click>

与哥本哈根解释的根本区别：概率不是内禀的，而是**认识论**上的。粒子始终有确定轨迹，量子力学的随机性仅仅来自我们不知道初始位置，类似经典统计力学。

</div>

<div v-click>

1964年，贝尔（J. Bell）证明了著名的**贝尔不等式**，对隐变量理论提出了关键判据。

</div>

::right::

<img src="/images/Screen Shot 2024-03-27 at 21.37.11-29145.png" style="max-width: 100%; max-height: 350px; object-fit: contain;" />

<img src="/images/Screen Shot 2024-03-27 at 21.37.19-29152.png" style="max-width: 100%; max-height: 350px; object-fit: contain;" />

---

# 贝尔不等式与非定域性

<div v-click>

**什么是"定域性"？** 物理学中一个基本假设：对一个粒子的操作，不能**瞬时**影响远处另一个粒子的状态。也就是说，物理影响的传递不能超过光速。爱因斯坦称之为"不存在超距的幽灵作用"（no spooky action at a distance）。

</div>

<div v-click>

**贝尔不等式**（1964）：贝尔不等式本身是数学定理，但它的前提是两个**物理假设**：① 粒子在测量前就有确定属性（实在性）；② 一边的测量不影响远处另一边（定域性）。从这两个假设出发，可以严格推出纠缠粒子测量关联度的一个**数学上限**。贝尔证明：量子力学的预言**超过**这个上限。

</div>

<div v-click>

**实验判决**：Aspect（1982）等人的实验明确证实，自然界**违反**贝尔不等式，量子力学正确。这意味着"定域性"和"隐变量"不可兼得。贝尔不等式的深刻意义在于：**把爱因斯坦与玻尔之间的哲学争论变成了可以用实验判决的科学问题**。

</div>

<div v-click>

**什么是"非定域性"？** 纠缠粒子之间存在超越空间距离的关联，对一个粒子的测量结果会瞬时确定另一个粒子的状态，无论它们相距多远。这不能用于超光速通信，但这种关联是真实的。玻姆理论正是一种**非定域**隐变量理论，放弃了定域性假设，因此不受贝尔不等式限制。

</div>

---
layout: two-cols
---

# 量子力学的其他解释

**客观坍缩理论**（GRW / Penrose）

<div v-click>

核心思想：波函数坍缩是一个**真实的物理过程**，不需要观测者介入。当量子叠加涉及的质量或能量差异达到某个阈值时，坍缩会自发发生。

</div>

<div v-click>

**GRW理论**（1986）：波函数会以极低的概率自发坍缩到某个位置。对单个粒子几乎不影响，但宏观物体包含 $\sim 10^{23}$ 个粒子，叠加态在极短时间内就会坍缩，这就解释了为什么我们看不到宏观叠加态。

</div>

<div v-click>

**彭罗斯方案**：引力是坍缩的根源。两个叠加态对应不同的质量分布，产生不同的时空弯曲，当时空曲率差异达到阈值时触发坍缩。这是少数可以实验检验的量子引力效应之一。

</div>

::right::

<img src="/images/Screen Shot 2024-03-27 at 21.57.51-29187.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 波函数的性质

波函数 $\Psi(x,t)$ 必须满足以下条件：

- **单值**：空间每一点只对应一个概率值
- **有限**：概率密度不能为无穷大
- **连续可导**：概率密度一般不发生突变

<div v-click>

**归一化条件**：粒子一定在空间某处出现，在整个空间的总概率为 1：

$$\int_{-\infty}^{+\infty} |\Psi(x, t)|^{2} \, dx = 1$$

若 $\phi$ 是未归一化的波函数，令 $\Psi = A\phi$，由归一化条件可确定 $A$。

</div>

<div v-click>

**注意**：$\Psi$ 和 $e^{i\alpha}\Psi$（$\alpha$ 为实数）描述同一个量子态，概率密度相同。

</div>

---

# 例题：波函数的归一化

设粒子的波函数为 $\phi(x) = A e^{-\alpha |x|}$（$\alpha > 0$），求归一化常数 $A$。

<div v-click>

由归一化条件：

$$\int_{-\infty}^{+\infty} |A|^2 e^{-2\alpha |x|} \, dx = 2|A|^2 \int_0^{\infty} e^{-2\alpha x} \, dx = 2|A|^2 \cdot \frac{1}{2\alpha} = \frac{|A|^2}{\alpha} = 1$$

</div>

<div v-click>

因此 $A = \sqrt{\alpha}$，归一化波函数为：

$$\Psi(x) = \sqrt{\alpha} \, e^{-\alpha |x|}$$

</div>

<div v-click>

粒子出现在 $[-a, a]$ 区间内的概率：

$$P = \int_{-a}^{a} \alpha e^{-2\alpha |x|} dx = 1 - e^{-2\alpha a}$$

当 $a = 1/\alpha$ 时，$P = 1 - e^{-2} \approx 86.5\%$。

</div>

---

# 波函数的物理意义

$|\Psi(x,y,z,t)|^2$ 是概率密度：

<div v-click>

$t$ 时刻，粒子出现在 $(x,y,z)$ 点附近体积元 $dV = dx\,dy\,dz$ 内的概率为：

$$dP = |\Psi|^2 \, dV$$

</div>

<div v-click>

$t$ 时刻，粒子出现在体积 $V$ 内的概率为：

$$P = \int_V |\Psi|^2 \, dV$$

</div>

<div v-click>

在球坐标下（原子物理中最常用），$dV = r^2 \sin\theta \, dr \, d\theta \, d\phi$，归一化条件变为：

$$\int_0^{\infty} \int_0^{\pi} \int_0^{2\pi} |\Psi(r,\theta,\phi)|^2 \, r^2 \sin\theta \, dr \, d\theta \, d\phi = 1$$

这就是我们后面求解氢原子波函数时使用的形式。

</div>

---

# 电子双缝干涉的统计学解释

从 A、B 两缝通过的电子波函数为 $\psi_A$ 和 $\psi_B$。两缝同时开启时：$\psi = \psi_A + \psi_B$

<div v-click>

屏上电子的概率分布：

$$|\psi|^2 = \underbrace{|\psi_A|^2}_{\text{只开A缝}} + \underbrace{|\psi_B|^2}_{\text{只开B缝}} + \underbrace{\psi_A^* \psi_B + \psi_B^* \psi_A}_{\text{干涉项：产生条纹的原因}}$$

</div>

<div v-click>

<div style="border: 2px solid #C71585; border-radius: 8px; padding: 10px 16px; margin-top: 12px; background: #fef0f5; text-align: center;">

玻恩用概率解释把波动性和粒子性统一起来：粒子逐个到达屏幕（**粒子性**），大量粒子的统计分布呈现干涉图样（**波动性**）。

</div>

</div>

---
layout: two-cols
---

# 电子云

用疏密表示空间各处概率密度的大小，很像在原子核外有一层疏密不等的"云"，形象地称为**电子云**。

- 密处：$|\Psi|^2$ 大，电子出现概率高
- 疏处：$|\Psi|^2$ 小，电子出现概率低

<div v-click>

电子云的形状由量子数 $(n, l, m)$ 决定：

- $l=0$（s 态）：球对称
- $l=1$（p 态）：哑铃形
- $l=2$（d 态）：花瓣形

这些形状就是化学中熟悉的**原子轨道**。

</div>

::right::

<img src="/images/pasted-image-27530.jpeg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 态叠加原理

考虑一个粒子可以在 $x_1$ 或 $x_2$ 处：

- 宏观上，粒子不是在 $x_1$ 就是在 $x_2$
- 量子力学中，未测量时粒子处于**叠加态**：$\Psi = c_1\psi_1 + c_2\psi_2$

<div v-click>

测量时，粒子以概率 $|c_1|^2$ 出现在 $x_1$，以概率 $|c_2|^2$ 出现在 $x_2$。

这就是薛定谔的猫的量子力学基础。

</div>

::right::

<img src="/images/CNX_UPhysics_40_01_Two_State-1-25192.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# Schrödinger's Cat

<img src="/images/Screen Shot 2024-03-27 at 22.05.33-29212.png" style="max-width: 500px; max-height: 300px; margin: 10px auto; display: block;" />

<div v-click>

薛定谔（1935）提出这个思想实验，本意是**嘲讽**哥本哈根解释的荒谬：如果量子叠加可以通过放大机制传递到宏观世界，那么一只猫就可以处于"既死又活"的叠加态，这显然违背常识。

</div>

<div v-click>

现代物理的回答：**退相干**（decoherence）。宏观物体与环境的相互作用会在极短时间内（$\sim 10^{-20}$ s）破坏量子相干性，使叠加态表现为经典的确定态。猫永远不会真正处于叠加态。

</div>

---

# 期望值计算

在经典力学中，位置 $x(t)$ 是确定的函数。

在量子力学中，只能知道概率密度 $|\Psi(x,t)|^2$，因此位置的**期望值**为：

$$\langle x \rangle = \int_{-\infty}^{\infty} x \, |\Psi(x,t)|^2 \, dx = \int_{-\infty}^{\infty} \Psi^* \, x \, \Psi \, dx$$

<div v-click>

一般地，任何物理量 $Q$ 的期望值：

$$\langle Q \rangle = \int_{-\infty}^{\infty} \Psi^* \, \hat{Q} \, \Psi \, dx$$

其中 $\hat{Q}$ 是 $Q$ 对应的算符。

</div>

---

# 不确定性原理的统计学解释

用标准差代替不确定度：$\Delta x \to \sigma_x$

$$\sigma_x^2 = \langle x^2 \rangle - \langle x \rangle^2, \quad \sigma_p^2 = \langle p^2 \rangle - \langle p \rangle^2$$

<img src="/images/Standard_deviation_diagram.svg-25326.png" style="max-width: 60%; max-height: 250px; margin: 10px auto; display: block;" />

<div v-click>

不确定性原理的严格表述：$\sigma_x \cdot \sigma_p \geq \dfrac{\hbar}{2}$

高斯波包取等号（**最小不确定态**）。

</div>

---
layout: two-cols
---

# 习题：估算氢原子基态能量

利用不确定性原理估算氢原子基态能量。

设电子被限制在半径 $a$ 的范围内，$\sigma_x \approx a$。

<div v-click>

由 $\sigma_x \sigma_p = \dfrac{\hbar}{2}$ 得 $\sigma_p = \dfrac{\hbar}{2a}$

电子来回运动，$\bar{p} = 0$，因此 $\langle p^2 \rangle = \sigma_p^2 = \dfrac{\hbar^2}{4a^2}$

</div>

<div v-click>

总能量：$E(a) = \dfrac{\langle p^2 \rangle}{2m} - \dfrac{e^2}{4\pi\varepsilon_0 a} = \dfrac{\hbar^2}{8ma^2} - \dfrac{e^2}{4\pi\varepsilon_0 a}$

对 $a$ 求极小值，可得基态能量估算值 $E \sim -13.6$ eV，与精确解一致！

</div>

::right::

<img src="/images/CNX_UPhysics_40_01_Cosine_Wave-1-24711.jpg" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/v2-4fcebba5e210f33cd800759166c495fe_720w.webp-24870.gif" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

---

# 思考：双缝实验中"偷看"会怎样？

在电子双缝实验中，如果我们在缝旁放一个探测器，试图确定电子究竟通过了哪条缝，干涉条纹会发生什么？

<div v-click>

**答**：干涉条纹**消失**！一旦确定电子走哪条缝，波函数就"坍缩"到 $\psi_A$ 或 $\psi_B$，不再是叠加态 $\psi_A + \psi_B$，干涉项 $\psi_A^*\psi_B + \psi_B^*\psi_A = 0$。

</div>

<div v-click>

这不是探测器"打扰"了电子那么简单。即使用极弱的光去探测，只要获取了"哪条路径"的信息，干涉就消失。

</div>

<div v-click>

<span class="kaiti-accent">量子力学中，获取信息本身就会改变系统的状态。互补性原理：路径信息和干涉条纹不可兼得。</span>

</div>

---

# 思考：概率幅 vs 概率

经典概率论中，两个互斥事件的概率直接相加：$P = P_1 + P_2$。量子力学中为什么不能这样做？

<div v-click>

**答**：量子力学中相加的不是概率，而是**概率幅**（波函数）：

$$\psi = \psi_1 + \psi_2, \quad P = |\psi_1 + \psi_2|^2 \neq |\psi_1|^2 + |\psi_2|^2$$

</div>

<div v-click>

"先加概率幅，再取模方"与"先取模方，再加概率"，结果不同！差别正是干涉项。

| | 经典概率 | 量子概率 |
|---|---|---|
| **相加对象** | 概率 $P$ | 概率幅 $\psi$ |
| **计算** | $P = P_1 + P_2$ | $P = |\psi_1 + \psi_2|^2$ |
| **干涉** | 无 | 有 |

</div>

<div v-click>

<span class="kaiti-accent">这是量子力学与经典物理最本质的区别：自然界的基本规律是概率幅叠加，不是概率叠加。</span>

</div>

---

# 思考：波函数是"真实"的吗？

波函数 $\Psi$ 是一个复数，不可直接测量。它只是方便计算的数学工具，还是代表了某种物理实在？

<div v-click>

**观点一（工具论）**：$\Psi$ 只是编码我们对系统知识的工具，真正有物理意义的只有 $|\Psi|^2$。

**观点二（实在论）**：$\Psi$ 代表真实的物理场。2012年 Pusey 等人 [5] 从数学上证明：如果量子力学的预测正确，波函数不可能只是"知识的编码"，它必须反映物理实在。

</div>

<div v-click>

**想一想**：如果波函数只是数学工具，如何解释干涉实验中 $\psi_A$ 和 $\psi_B$ 的叠加产生了可观测的条纹？纯粹的"知识"怎么会发生干涉？

</div>

<div v-click>

<span class="kaiti-accent">这个问题至今没有定论，是量子力学基础研究的前沿课题。不同的量子力学诠释给出不同的回答。</span>

</div>

---

# 前沿：2022年诺贝尔物理学奖

<div style="display: flex; gap: 2rem; align-items: flex-start;">
<div style="flex: 1;">

Aspect、Clauser、Zeilinger 因**纠缠光子实验、验证贝尔不等式的违反以及开创量子信息科学**获2022年诺贝尔物理学奖 [6]。

<div v-click>

**贝尔不等式**（1964）：如果存在定域隐变量，实验中纠缠粒子的关联度有一个上限。量子力学预言这个上限会被突破。

</div>

<div v-click>

三位科学家先后用越来越严格的实验堵住了所有漏洞，明确证实：**自然界违反贝尔不等式**，定域隐变量理论被实验排除。

</div>

<div v-click>

<span class="kaiti-accent">这是20世纪物理学最深刻的实验之一：量子力学的非定域性不是理论假设，而是实验事实。</span>

</div>

</div>
</div>

---

# 前沿：Born规则能被实验检验吗？

Born规则（$P = |\Psi|^2$）是量子力学的基本公设。能否设计实验来检验它？

<div v-click>

**Sorkin（1994）[7] 的方案**：在双缝实验中，$P_{12} = P_1 + P_2 +$ 干涉项。但如果 Born 规则有偏差，**三缝**实验会出现额外的高阶干涉项。

定义 Sorkin 参数：$\kappa = P_{123} - P_{12} - P_{13} - P_{23} + P_1 + P_2 + P_3$

Born 规则预言 $\kappa = 0$，任何偏差都意味着量子力学不完备。

</div>

<div v-click>

实验结果 [8]：多个独立实验验证 $\kappa$ 在 $10^{-4}$ 精度内为零，Born 规则经受住了考验。

</div>

<div v-click>

<span class="kaiti-accent">"概率等于振幅的模方"不是不可检验的信条，而是经过精密实验验证的物理规律。</span>

</div>

---

# §14 小结

- 量子力学中，系统的状态由**波函数** $\Psi(x,t)$ 表示

- 玻恩的统计解释：$|\Psi|^2$ 表示粒子出现的概率密度

- 波函数必须满足归一化条件 $\int |\Psi|^2 dx = 1$

- 期望值：$\langle Q \rangle = \int \Psi^* \hat{Q} \Psi \, dx$

- 态叠加原理：未测量时，粒子可以同时处于多个态的叠加

---

# §14 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] M. Born, "Zur Quantenmechanik der Stoßvorgänge," *Z. Phys.* **37**, 863 (1926). — 波函数的统计解释（1954年诺贝尔物理学奖）

[2] J. S. Bell, "On the Einstein Podolsky Rosen paradox," *Physics Physique Физика* **1**, 195 (1964). — 贝尔不等式

[3] D. Bohm, "A Suggested Interpretation of the Quantum Theory in Terms of 'Hidden' Variables," *Phys. Rev.* **85**, 166 (1952). — 德布罗意-玻姆导航波理论

[4] G. C. Ghirardi, A. Rimini, T. Weber, "Unified dynamics for microscopic and macroscopic systems," *Phys. Rev. D* **34**, 470 (1986). — GRW 客观坍缩理论

[5] M. F. Pusey, J. Barrett, T. Rudolph, "On the reality of the quantum state," *Nature Phys.* **8**, 475 (2012). — 波函数实在性定理

[6] A. Aspect, J. Clauser, A. Zeilinger, **2022年诺贝尔物理学奖**："纠缠光子实验，建立贝尔不等式的违反，开创量子信息科学"

[7] R. D. Sorkin, "Quantum mechanics as quantum measure theory," *Mod. Phys. Lett. A* **9**, 3119 (1994). — Born 规则三缝检验方案

[8] U. Sinha et al., "Ruling Out Multi-Order Interference in Quantum Mechanics," *Science* **329**, 418 (2010). — Born 规则实验检验

[9] S. Gerlich et al., "Probing quantum mechanics with nanoparticle matter-wave interferometry," *Nature* (2026). — 17万道尔顿纳米粒子量子干涉

</div>

---

# §15 薛定谔方程

需要掌握的知识点：

（1）理解薛定谔方程作为量子力学**基本公设**的地位（不是从经典力学"推导"出来的）

（2）掌握"算符替换"的启发式构造思路：从经典 $E = \dfrac{p^2}{2m} + V$ 到量子方程

（3）区分含时薛定谔方程与定态薛定谔方程

（4）理解定态、本征值方程、概率守恒、态叠加原理

（5）了解波动力学、矩阵力学、路径积分三种等价表述

---
layout: two-cols
---

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 0.9em; margin-bottom: 0.6em; border-left: 3px solid #C71585; }
.q-card h4 { color: #C71585; margin: 0 0 0.3em 0; font-size: 1.05em; }
.w-card { background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.7em 0.9em; margin-bottom: 0.6em; border-left: 3px solid #5856d6; }
.w-card h4 { color: #5856d6; margin: 0 0 0.3em 0; font-size: 1.05em; }
.qm-card { background: rgba(255,165,0,0.10); border-radius: 10px; padding: 0.7em 0.9em; margin-bottom: 0.6em; border-left: 3px solid #ff8c00; text-align: center; }
.qm-card h4 { color: #ff8c00; margin: 0 0 0.3em 0; font-size: 1.05em; }
</style>

# 第一幕：量子世界需要新方程

经典物理已有两套完整的运动方程：

<div class="q-card">
<h4>经典粒子（牛顿，1687）</h4>

$$\vec{F} = m\dfrac{d^2 \vec{r}}{dt^2}$$

状态 = 一条确定轨迹 $\vec{r}(t), \vec{p}(t)$
</div>

<div class="w-card">
<h4>经典波（达朗贝尔，1747）</h4>

$$\dfrac{\partial^2 \phi}{\partial t^2} = c^2 \nabla^2 \phi$$

状态 = 弥散的波场 $\phi(\vec{r}, t)$
</div>

::right::

<div style="margin-top: 5em;">

<div class="qm-card">
<h4>量子粒子（既是粒子又是波）</h4>

$$\Large\boldsymbol{?}$$

状态 = ？？？

满足 = ？？？
</div>

<p style="text-align: center; color: #555; font-size: 0.95em; margin-top: 1em;">这就是 1925 年量子物理面对的<br/>最深的空白。</p>

</div>

---

# 1925 年圣诞节，阿尔卑斯山阿罗萨

1925 年秋，苏黎世大学的物理讨论班上，薛定谔被指派讲解德布罗意的论文。会后，物理化学家德拜（P. Debye）当面提了一句：

<div style="border-left: 3px solid #C71585; padding-left: 16px; margin: 12px 0; font-style: italic; font-size: 1.05em;">

"对于波，应该有一个波动方程。"

</div>

<div v-click>

这句话像一根刺一样扎在薛定谔心里。1925 年圣诞，他带着一位"红颜知己"来到瑞士阿罗萨（Arosa）的滑雪小镇度假两周。两周后他下山时，量子力学的波动方程已经在脑子里成型。

1926 年 1 月起，薛定谔以《作为本征值问题的量子化》（*Quantisierung als Eigenwertproblem*）为题，半年内连续发表四篇论文，**波动力学**就此诞生。

</div>

<div v-click>

**他自己也无法严格"推导"出这个方程。** 他做的是一件更深刻的事，为量子世界**发明**一个新方程，然后让实验来检验它。

下面我们一起重走他当年的思路。

</div>

---

# 第二幕之 ①：自由粒子的平面波

回顾 §12，德布罗意告诉我们：动量为 $p$、能量为 $E$ 的自由粒子，其物质波是平面波

$$\Psi(x, t) = A\, e^{i(kx - \omega t)}$$

加上德布罗意–爱因斯坦关系：

$$E = \hbar \omega, \qquad p = \hbar k$$

<div v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-top: 1em;">

**关键问题**：这个 $\Psi(x, t)$ 满足什么微分方程？

</div>

我们尝试**对它求偏导**，看看会发生什么……

</div>

---

# 第二幕之 ②：算符替换的诞生

对平面波 $\Psi = A\, e^{i(kx - \omega t)}$ 直接求偏导：

<div v-click>

$$\dfrac{\partial \Psi}{\partial x} = ik\, \Psi \quad\Longrightarrow\quad \boxed{\;-i\hbar \dfrac{\partial}{\partial x}\,\Psi = \hbar k \, \Psi = p \, \Psi\;}$$

</div>

<div v-click>

$$\dfrac{\partial \Psi}{\partial t} = -i\omega\, \Psi \quad\Longrightarrow\quad \boxed{\;i\hbar \dfrac{\partial}{\partial t}\,\Psi = \hbar \omega \, \Psi = E \, \Psi\;}$$

</div>

<div v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #ff8c00; margin-top: 1em;">

**惊人的事实**：动量 $p$ 和能量 $E$ 竟然可以表示成**作用在波函数上的微分算符**！

$$\hat{p} \;\equiv\; -i\hbar \dfrac{\partial}{\partial x}, \qquad \hat{E} \;\equiv\; i\hbar \dfrac{\partial}{\partial t}$$

</div>

这就是量子力学的"**算符替换法则**"，薛定谔在 1926 年第一次系统地写下了它。

</div>

---

# 第二幕之 ③：对应原理 → 薛定谔方程

把"算符替换"应用到经典能量关系。一维粒子的经典能量：

$$E \;=\; \dfrac{p^2}{2m} + V(x)$$

<div v-click>

把 $E, p$ 同时换成算符 $\hat{E}, \hat{p}$，并让方程作用在波函数 $\Psi$ 上：

$$\hat{E}\, \Psi \;=\; \dfrac{\hat{p}^2}{2m}\, \Psi + V(x)\, \Psi$$

</div>

<div v-click>

代入算符的具体形式：

$$\boxed{\;\; i\hbar\, \dfrac{\partial \Psi}{\partial t} \;=\; -\dfrac{\hbar^2}{2m}\, \dfrac{\partial^2 \Psi}{\partial x^2} \;+\; V(x)\, \Psi \;\;}$$

</div>

<div v-click>

<p style="text-align: center; color: #C71585; font-size: 1.3em; font-weight: bold; margin-top: 0.6em;">这就是薛定谔方程！</p>

我们用三步"猜"出了一个全新的方程：① 自由粒子的平面波 → ② 算符替换 → ③ 套用经典能量关系。

</div>

---

# 第二幕之 ④：诚实的警告

我们刚才做的事其实是一种**循环论证**：

- 用平面波（自由粒子）"猜出"算符替换法则；
- 然后**强行假定**这套法则对所有粒子都成立。

<div v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-top: 0.6em;">

**薛定谔方程是量子力学的基本公设**，它不是从经典力学推导出来的。

它的地位类似于：

- 牛顿第二定律 $\vec{F} = m\vec{a}$（牛顿没有"推导"它）
- 麦克斯韦方程组（麦克斯韦没有"推导"它）

</div>

我们能做的只是给出**启发式动机**（heuristic motivation），让你明白方程为什么"长这个样子"。它的正确性由**实验**决定，不由数学证明决定。

</div>

<div v-click>

<div style="border-left: 3px solid #5856d6; padding-left: 16px; margin: 14px 0; font-style: italic; color: #333;">

"Where did we get that from? Nowhere. It is not possible to derive it from anything you know. It came out of the mind of Schrödinger." 

（R. P. Feynman, *Lectures on Physics*, Vol. III, Ch. 16）

</div>

</div>

---

# 第三幕之 ①：紧凑形式（哈密顿算符）

定义**哈密顿算符**：

$$\hat{H} \;\equiv\; \hat{T} + \hat{V} \;=\; -\dfrac{\hbar^2}{2m}\, \nabla^2 + V(\vec{r}, t)$$

<div v-click>

含时薛定谔方程的紧凑形式：

$$\boxed{\;\; i\hbar \dfrac{\partial \Psi}{\partial t} \;=\; \hat{H}\, \Psi \;\;}$$

</div>

<div v-click>

完整三维形式：

$$i\hbar \dfrac{\partial \Psi}{\partial t} \;=\; -\dfrac{\hbar^2}{2m}\!\left(\dfrac{\partial^2}{\partial x^2} + \dfrac{\partial^2}{\partial y^2} + \dfrac{\partial^2}{\partial z^2}\right) \Psi + V(\vec{r},t)\, \Psi$$

</div>

<div v-click>

**类比牛顿第二定律**：给定初始波函数 $\Psi(\vec{r}, 0)$ 和势能 $V$，薛定谔方程决定了波函数在任何后续时刻的演化。区别只在于：牛顿方程的对象是轨迹 $\vec{r}(t)$，薛定谔方程的对象是波函数 $\Psi(\vec{r}, t)$。

</div>

---

# 第三幕之 ②：经典 ↔ 量子的全面对照

<style scoped>
table { font-size: 0.92em; margin: 0.6em auto; }
th, td { padding: 0.5em 0.9em !important; }
th { color: #C71585; }
</style>

| | **经典力学** | **量子力学** |
|---|---|---|
| 状态 | 位置 $\vec{r}(t)$，动量 $\vec{p}(t)$ | 波函数 $\Psi(\vec{r}, t)$ |
| 状态空间 | $6N$ 维相空间 | 复线性空间（束缚态在 $L^2$，散射态在装备希尔伯特空间）|
| 运动方程 | $\vec{F} = m\ddot{\vec{r}}$ 或 Hamilton 方程 | $i\hbar\, \partial_t \Psi = \hat{H}\, \Psi$ |
| 可观测量 | 函数 $f(q, p)$，确定值 | 厄米算符 $\hat{Q}$，期望值 $\langle \hat{Q} \rangle$ |
| 演化 | 沿相空间一条轨迹 | 复线性空间中的幺正变换 |
| 预言 | 完全确定 | 概率分布 |
| 叠加性 | 没有 | $c_1\Psi_1 + c_2\Psi_2$ 仍是解 |

---

# 第三幕之 ③：薛定谔的四篇论文（1926）

<div class="grid grid-cols-2 gap-6">

<div>

四篇论文一起为量子力学奠定了"波动力学"的基础：

- **第一篇**（1月）：氢原子的本征值问题
- **第二篇**（2月）：与汉密尔顿光学的几何类比
- **第三篇**（5月）：含时微扰论
- **第四篇**（6月）：含时薛定谔方程

最关键的是：薛定谔在这些论文里**自己证明**了，他的"波动力学"与海森堡（1925）的"矩阵力学"在数学上完全等价。这是 20 世纪物理史上最戏剧性的事件之一：两个看似毫无关系的理论，结果是同一个东西的两副面孔。

</div>

<div>

<img src="/images/Screenshot 2023-03-29 at 10.29.30-28961.png" style="max-width: 100%; max-height: 230px; object-fit: contain;" />

<img src="/images/Screenshot 2023-03-29 at 10.32.17-28966.png" style="max-width: 100%; max-height: 230px; object-fit: contain; margin-top: 8px;" />

</div>

</div>

---

# 第四幕之 ①：当 $V$ 不显含 $t$，分离变量

绝大多数原子物理问题中，势能只与位置有关：$V = V(\vec{r})$（不显含 $t$）。

<div v-click>

尝试**分离变量法**：假设解的形式为

$$\Psi(\vec{r}, t) \;=\; \psi(\vec{r})\, f(t)$$

代入含时薛定谔方程：

$$i\hbar\, \psi(\vec{r})\, f'(t) \;=\; f(t)\, \hat{H}\psi(\vec{r})$$

两边同时除以 $\psi \cdot f$：

$$i\hbar\, \dfrac{f'(t)}{f(t)} \;=\; \dfrac{\hat{H}\psi(\vec{r})}{\psi(\vec{r})}$$

</div>

<div v-click>

**左边只依赖 $t$，右边只依赖 $\vec{r}$**。要让等式恒成立，两边必须等于同一个常数，记作 $E$。

</div>

---

# 第四幕之 ②：定态薛定谔方程

时间方程：
$$i\hbar\, \dfrac{f'(t)}{f(t)} = E \quad\Longrightarrow\quad f(t) = e^{-iEt/\hbar}$$

空间方程：
$$\dfrac{\hat{H}\psi(\vec{r})}{\psi(\vec{r})} = E \quad\Longrightarrow\quad \boxed{\;\hat{H}\, \psi(\vec{r}) \;=\; E\, \psi(\vec{r})\;}$$

<div v-click>

写开来就是：

$$-\dfrac{\hbar^2}{2m}\, \nabla^2 \psi(\vec{r}) + V(\vec{r})\, \psi(\vec{r}) \;=\; E\, \psi(\vec{r})$$

这就是**定态薛定谔方程**，一个关于空间波函数 $\psi(\vec{r})$ 的**本征值方程**。

</div>

<div v-click>

完整解：
$$\Psi(\vec{r}, t) \;=\; \psi(\vec{r})\, e^{-iEt/\hbar}$$

波函数 $\psi(\vec{r})$ 必须满足 §14 中讲的标准条件：**单值、连续、有限、可归一**。

</div>

---

# 第四幕之 ③："定态"为什么叫"定态"？

**stationary** 不是说粒子静止不动，而是说**所有可观测的统计性质都不随时间变化**。

<div v-click>

概率密度：

$$|\Psi(\vec{r}, t)|^2 \;=\; |\psi(\vec{r})|^2 \cdot |e^{-iEt/\hbar}|^2 \;=\; |\psi(\vec{r})|^2$$

**与时间无关！**

</div>

<div v-click>

任何不显含 $t$ 的物理量 $\hat{Q}$ 的期望值：

$$\langle \hat{Q} \rangle \;=\; \int \Psi^*\, \hat{Q}\, \Psi\, d^3 r \;=\; \int \psi^*\, \hat{Q}\, \psi\, d^3 r$$

**也与时间无关！**

</div>

<div v-click>

虽然波函数本身在每一点都有 $e^{-iEt/\hbar}$ 因子在不停转动，但**所有实验可观测量都是凝固的**。这正是"定态"名称的由来。

<img src="/images/pasted-image-27914.png" style="max-width: 280px; max-height: 180px; margin: 0.5em auto; display: block;" />

</div>

---

# 第四幕之 ④：什么是 Ansatz？

Ansatz（德语"开端、设想"）：对方程解的形式做一个有根据的猜测，代入方程验证并求解。

<div v-click>

**例子**：求解 $y''(x) + 2 y'(x) + 3 y(x) = x^3$

猜测 $y(x) = a x^3 + b x^2 + c x + d$，代入方程比较各次幂系数，即可确定 $a, b, c, d$。

</div>

<div v-click>

**薛定谔方程中的 Ansatz**：

我们猜测 $\Psi(\vec{r}, t) = \psi(\vec{r}) \, f(t)$（时空可分离）。这并非随意猜测，它来自对自由粒子平面波 $e^{i(kx - \omega t)}$ 的类比，平面波本身就是空间项 $e^{ikx}$ 与时间项 $e^{-i\omega t}$ 的乘积。

数学上不能解析求解的方程，物理学家常常通过 Ansatz 找到精确解或近似解。这是理论物理最常用的"工具"之一。

</div>

---

# 第四幕之 ⑤：量子化是怎样"自动"出现的

定态薛定谔方程是**本征值方程**：

$$\hat{H}\, \psi_n(\vec{r}) \;=\; E_n\, \psi_n(\vec{r})$$

<div v-click>

加上**波函数的标准条件**（§14 已讲）：单值、连续、处处有限、可归一（$\int |\psi|^2 d^3 r < \infty$）。

</div>

<div v-click>

<div style="background: rgba(255,140,0,0.10); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #ff8c00; margin-top: 0.6em;">

**关键事实**：在大多数束缚态问题中，**只有当 $E$ 取特定的离散值** $E_1, E_2, E_3, \ldots$ 时，方程才有满足上述条件的解。

→ **能量量子化是数学求解的自然结果**，不再需要像普朗克、玻尔那样人为假定！

</div>

</div>

<div v-click>

这就是薛定谔方程的革命意义：把"量子化"从一条神秘的假设，变成了一个**边值问题**的解。后面几章你将看到，氢原子、谐振子、势阱、势垒……量子化能级都从这个方程**自然涌现**。

</div>

---

# 第五幕之 ①：线性性 → 态叠加原理

薛定谔方程是**线性微分方程**：如果 $\Psi_1, \Psi_2$ 都是它的解，那么

$$\Psi \;=\; c_1\, \Psi_1 + c_2\, \Psi_2 \qquad (c_1, c_2 \in \mathbb{C})$$

**也是它的解**（直接代入即可验证）。

<div v-click>

推广：如果 $\{\psi_n\}$ 是定态方程 $\hat{H}\psi_n = E_n\psi_n$ 的所有本征解，那么含时薛定谔方程的**通解**是

$$\Psi(\vec{r}, t) \;=\; \sum_n c_n\, \psi_n(\vec{r})\, e^{-iE_n t/\hbar}$$

复系数 $c_n$ 由初始条件决定，且 $|c_n|^2$ 表示测量能量得到 $E_n$ 的概率。归一化要求 $\sum_n |c_n|^2 = 1$。

</div>

<div v-click>

<div style="background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #C71585; margin-top: 0.6em;">

**态叠加原理是量子力学最深刻的特征**。双缝干涉、薛定谔的猫、量子纠缠、量子计算的全部能力，都源于薛定谔方程的这一条线性性。

</div>

</div>

---

# 第五幕之 ②：复数为何不可或缺？

经典波动方程是**二阶**时间导数：

$$\dfrac{\partial^2 \phi}{\partial t^2} = c^2 \nabla^2 \phi$$

它有实数解（如 $\sin(kx - \omega t)$），物理量 $\phi$ 本身就可观测。

<div v-click>

但薛定谔方程是**一阶**时间导数：

$$i\hbar \dfrac{\partial \Psi}{\partial t} = \hat{H}\, \Psi$$

如果 $\Psi$ 是实函数，那么左边 $i\hbar\, \partial_t \Psi$ 是纯虚数，右边 $\hat{H}\Psi$ 是纯实数，**直接矛盾**！

→ **波函数必须是复数。**

</div>

<div v-click>

**更深的原因**：薛定谔方程的幺正性保证了概率守恒 $\frac{d}{dt}\int |\Psi|^2 d^3 r = 0$。

- 实波动方程（二阶时间导数）守恒的是**能量** $\int (\dot\phi^2 + |\nabla\phi|^2) d^3 r$；
- 薛定谔方程（一阶时间导数）守恒的是**概率** $\int |\Psi|^2 d^3 r$。

这要求 $\Psi$ 同时携带"振幅"和"相位"两个自由度，正好对应一个**复数**。

</div>

---

# 第五幕之 ③：概率守恒（连续性方程）

把薛定谔方程两边乘以 $\Psi^*$，再减去其复共轭，可以推出：

$$\dfrac{\partial}{\partial t}|\Psi|^2 + \nabla \cdot \vec{j} \;=\; 0$$

其中**概率流密度**

$$\vec{j} \;=\; \dfrac{\hbar}{2mi}\left(\Psi^* \nabla \Psi - \Psi \nabla \Psi^*\right) \;=\; \dfrac{\hbar}{m}\, \mathrm{Im}(\Psi^* \nabla \Psi)$$

<div v-click>

这是一个**连续性方程**，与流体力学、电荷守恒方程的形式完全一致：

$$\dfrac{\partial \rho}{\partial t} + \nabla \cdot \vec{j} = 0$$

只不过这里"流动"的是**概率**。它保证了概率不会"凭空消失"或"凭空出现"。

</div>

<div v-click>

**为什么重要**：这是 §14 中**玻恩概率诠释**的自洽性保证。若没有这条性质，"$|\Psi|^2$ 是概率密度"就会与时间演化矛盾。

注意：概率守恒**不是额外假设**，而是薛定谔方程的**内在数学结果**。这正是这个方程的"美"。

</div>

---

# 第六幕之 ①：薛定谔方程的"三胞胎"

20 世纪 20–40 年代，量子力学被构造了**三种数学上完全等价**的形式：

<style scoped>
.path-card { background: rgba(199,21,133,0.05); border-radius: 12px; padding: 0.8em 0.9em; border-left: 3px solid #C71585; height: 100%; }
.path-card h4 { color: #C71585; margin: 0 0 0.3em 0; font-size: 1.0em; }
.path-card .author { color: #555; font-size: 0.85em; margin-bottom: 0.4em; }
.path-card .formula { font-size: 0.9em; margin: 0.3em 0; }
.path-card .desc { font-size: 0.85em; color: #444; margin-top: 0.4em; }
</style>

<div class="grid grid-cols-3 gap-3 mt-4">

<div class="path-card">
<h4>① 波动力学</h4>
<div class="author">薛定谔 · 1926</div>

<div class="formula">

$$i\hbar\, \partial_t \Psi = \hat{H}\, \Psi$$

</div>

<div class="desc">

状态 = 复波函数 $\Psi(\vec{r}, t)$

直觉：可视化、好教学

</div>
</div>

<div class="path-card">
<h4>② 矩阵力学</h4>
<div class="author">海森堡 · 1925</div>

<div class="formula">

$$i\hbar\, \dfrac{d\hat{Q}}{dt} = [\hat{Q}, \hat{H}]$$

</div>

<div class="desc">

状态固定，**算符**演化

直觉：抽象代数、强调可观测量

</div>
</div>

<div class="path-card">
<h4>③ 路径积分</h4>
<div class="author">费曼 · 1948</div>

<div class="formula">

$$\langle x_f | x_i\rangle = \int\! \mathcal{D}[x(t)]\, e^{iS/\hbar}$$

</div>

<div class="desc">

粒子走"**所有可能路径**"的相干叠加

直觉：与最小作用量相通

</div>
</div>

</div>

<div v-click style="margin-top: 1.2em;">

三种表述给出**完全相同的物理预言**，但提供完全不同的图像和计算工具。薛定谔本人（1926）证明了 ① ↔ ②；费曼（1948）证明了 ① ↔ ③。狄拉克在 *Principles of Quantum Mechanics*（1930）中将三者统一为算符代数。

**学习量子力学的最佳方式**：先掌握波动力学（最直观），再学矩阵力学（最有力），最后理解路径积分（最深刻）。

</div>

---

# 第六幕之 ②：从对称性出发的现代视角

20 世纪后半叶发展出的**公理化量子力学**（Sakurai、Weinberg）不依赖任何经典对应，而是从最少的假设出发：

<div v-click>

<div style="background: rgba(88,86,214,0.06); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #5856d6; margin-top: 0.5em;">

**公设 1**：量子态由一个复线性空间中的矢量 $|\psi\rangle$ 描述。可归一化的束缚态构成希尔伯特空间 $L^2$，散射态（如平面波 $e^{i\vec{k}\cdot\vec{r}}$）作为**广义本征态**需要用**装备希尔伯特空间**（Rigged Hilbert Space）严格处理。

**公设 2**：时间演化是**幺正变换** $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$，且 $\hat{U}^\dagger \hat{U} = \mathbb{1}$（保持概率不变）。

**公设 3**：$\hat{U}$ 是**连续单参数群**：$\hat{U}(t_1 + t_2) = \hat{U}(t_1)\hat{U}(t_2)$。

</div>

</div>

<div v-click>

**Stone 定理**（1932）：满足上述三条的 $\hat{U}$ 必然有形式

$$\hat{U}(t) \;=\; e^{-i\hat{H}t/\hbar}$$

其中 $\hat{H}$ 是某个厄米算符（"哈密顿量"）。

</div>

<div v-click>

把 $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ 代回 $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$，再对 $t$ 求导：

$$\dfrac{d}{dt}|\psi(t)\rangle \;=\; \dfrac{d}{dt}\!\left[e^{-i\hat{H}t/\hbar}\right]|\psi(0)\rangle \;=\; -\dfrac{i}{\hbar}\hat{H}\, e^{-i\hat{H}t/\hbar}|\psi(0)\rangle \;=\; -\dfrac{i}{\hbar}\hat{H}\, |\psi(t)\rangle$$

两边乘以 $i\hbar$，立即得到：

$$\boxed{\;i\hbar\, \dfrac{d}{dt}|\psi(t)\rangle \;=\; \hat{H}\, |\psi(t)\rangle\;}$$

**薛定谔方程从对称性自动产生**，根本不需要"对应原理"或"算符替换"。这条路径揭示了它最深的本质：**薛定谔方程是连续幺正时间演化的微分形式**。

</div>

---

# §15 思考 1　<span style="color: #C71585; font-size: 0.7em;">概念</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

如果某个粒子的波函数 $\Psi$ 是**纯实函数**，它能成为薛定谔方程的解吗？为什么？这与经典波动方程有何不同？

</div>

<div v-click>

<div class="a-card">

<h4>答案</h4>

**不能**（除了完全静态的平凡情形 $\partial_t \Psi = 0$）。薛定谔方程 $i\hbar\, \partial_t \Psi = \hat{H}\Psi$ 中，左边 $i\hbar\, \partial_t \Psi$ 是纯虚数，右边 $\hat{H}\Psi$（实算符作用在实函数上）是纯实数，**直接矛盾**。

**注意**：定态空间部分 $\psi(\vec{r})$ 可以是实函数（一维谐振子基态、无限深势阱本征态都是实函数），但完整的含时波函数必然是复数：

$$\Psi(\vec{r}, t) = \psi(\vec{r})\, e^{-iEt/\hbar}$$

**与经典波的对比**：经典波动方程 $\partial_t^2 \phi = c^2 \nabla^2 \phi$ 是**二阶**时间导数，两边奇偶性一致，可以有实数解（如 $\sin(kx - \omega t)$），$\phi$ 本身就是可观测量。薛定谔方程是**一阶**时间导数，必须复函数才能让 $\frac{d}{dt}\int |\Psi|^2 d^3 r = 0$ 这条概率守恒成立。

</div>

</div>

---

# §15 思考 2　<span style="color: #C71585; font-size: 0.7em;">计算</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #30d158; font-size: 0.9em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

对自由粒子平面波 $\Psi = A\, e^{i(kx - \omega t)}$，计算概率流密度 $\vec{j}$。它的物理意义是什么？

</div>

<div v-click>

<div class="a-card">

<h4>答案</h4>

代入 $\vec{j} = \dfrac{\hbar}{m}\, \text{Im}(\Psi^* \nabla \Psi)$：

$$\Psi^* \nabla \Psi \;=\; A^*\, e^{-i(kx - \omega t)} \cdot (ik\, \hat{x})\, A\, e^{i(kx - \omega t)} \;=\; ik\, |A|^2\, \hat{x}$$

$$\vec{j} \;=\; \dfrac{\hbar}{m}\, \text{Im}(ik\, |A|^2)\, \hat{x} \;=\; \dfrac{\hbar k}{m}\, |A|^2\, \hat{x} \;=\; \dfrac{p}{m}\, |A|^2\, \hat{x} \;=\; v\, |A|^2\, \hat{x}$$

**物理意义**：

$$\boxed{\;\vec{j} \;=\; \rho\, \vec{v}\;}$$

其中 $\rho = |\Psi|^2 = |A|^2$ 是**概率密度**，$\vec{v} = p/m$ 是**经典速度**。这与流体力学中"质量流密度 = 密度 × 速度"的形式完全一致。

→ 平面波就像一束沿 $\hat{x}$ 方向均匀流动的"概率流"，每单位时间、单位面积流过 $|A|^2 \cdot v$ 个粒子。

</div>

</div>

---

# §15 思考 3　<span style="color: #C71585; font-size: 0.7em;">深入</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #30d158; font-size: 0.85em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

定态意味着 $|\Psi|^2$ 不变，但 $\Psi$ 本身在以 $e^{-iEt/\hbar}$ 转动。能否用某个实验区分一个真正的定态，和一个 $|\Psi|^2$ 恰好相同的非定态？（提示：考虑两个定态 $\psi_1, \psi_2$ 的叠加。）

</div>

<div v-click>

<div class="a-card">

<h4>答案</h4>

**单凭 $|\Psi|^2$ 测量区分不了**，但通过**辐射光谱**就能区分。

考虑两个定态的叠加：

$$\Psi(\vec{r}, t) \;=\; c_1\, \psi_1(\vec{r})\, e^{-iE_1 t/\hbar} \;+\; c_2\, \psi_2(\vec{r})\, e^{-iE_2 t/\hbar}$$

它的概率密度

$$|\Psi|^2 \;=\; |c_1\psi_1|^2 + |c_2\psi_2|^2 + 2\, \text{Re}\!\left[c_1^* c_2\, \psi_1^* \psi_2\, e^{-i(E_2 - E_1)t/\hbar}\right]$$

**最后一项以频率** $\omega_{21} = (E_2 - E_1)/\hbar$ **振荡**。这是一个有时间依赖的电荷分布，会**辐射出频率 $\omega_{21}$ 的电磁波**。

- **真正的定态**：电荷分布静止，不辐射任何光（玻尔的"稳态轨道"）
- **定态叠加**：以玻尔频率 $\omega_{21}$ 辐射光子

→ 这正是**原子光谱线**和**爱因斯坦受激/自发辐射**的微观起源。$\Delta E = \hbar \omega$ 这条玻尔 1913 年提出的"经验假设"，在 1926 年的薛定谔方程中得到了完整解释。

</div>

</div>

---

# §15 思考 4　<span style="color: #C71585; font-size: 0.7em;">前沿</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.7em 1em; border-left: 3px solid #30d158; font-size: 0.82em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.4em 0; }
</style>

<div class="q-card">

薛定谔方程是**线性**的。如果加上一个非线性项（比如 $\lambda |\Psi|^2 \Psi$），物理上会发生什么？这种"非线性量子力学"是否可能？为什么 Steven Weinberg 在 1989 年的尝试失败了？

</div>

<div v-click>

<div class="a-card">

<h4>答案</h4>

非线性项会破坏量子力学的几条核心性质：

1. **态叠加原理失效**：$\Psi_1 + \Psi_2$ 不再是解，干涉、纠缠都失去基础
2. **超光速通信**：N. Gisin（1990）证明，任何非线性量子力学都允许利用 EPR 纠缠态进行超光速信号传递，**违反相对论因果律**
3. **概率诠释失效**：归一化和全局相位不再独立，Born 规则失去意义
4. **能量本征值依赖振幅**：本征值变成 $|\Psi|^2$ 的函数，破坏线性谱

**Weinberg 1989 年的尝试**：他提出 $H = H_0 + \epsilon\, h(|\Psi|^2)$，希望实验测量 $\epsilon$ 是否严格为零。同年 Bollinger 等人立刻用 $^9$Be$^+$ 离子的核磁共振谱将 $|\epsilon|/H_0$ 限制到 $\sim 10^{-21}$ 之内。Walsworth、Chupp 等人后来又把上限再压低多个数量级。

**结论**：实验表明，量子力学**精确**地是线性的。Weinberg 自己后来也承认这条路走不通。**线性不是历史偶然，而是量子力学的根本特征**。

</div>

</div>

---

# §15 思考 5　<span style="color: #C71585; font-size: 0.7em;">哲学</span>

<style scoped>
.q-card { background: rgba(199,21,133,0.06); border-radius: 10px; padding: 0.8em 1em; border-left: 3px solid #C71585; margin-bottom: 0.8em; font-size: 1.0em; }
.a-card { background: rgba(48,209,88,0.08); border-radius: 10px; padding: 0.6em 1em; border-left: 3px solid #30d158; font-size: 0.78em; }
.a-card h4 { color: #2ea043; margin: 0 0 0.3em 0; }
</style>

<div class="q-card">

$\Psi$ 的演化是确定性的（薛定谔方程），但测量结果是概率性的（玻恩规则），这两点如何并存？这就是著名的"**量子测量问题**"。

</div>

<div v-click>

<div class="a-card">

<h4>答案：没有公认答案，五种主流解释</h4>

**① 哥本哈根解释**（Bohr, Heisenberg）：测量是一个特殊过程，导致波函数"坍缩"。问题：什么算"测量"？没有给出动力学机制。

**② 多世界解释**（Everett, 1957）：波函数从不坍缩，每次测量让宇宙"分裂"为所有可能分支，每个分支中的"你"都看到一个确定结果。问题：分支的"概率"从何而来？

**③ 退相干**（Zeh, Zurek, 1980s）：环境与系统的纠缠让宏观叠加态在极短时间内退相干，事实上变成经典混合态。退相干解释了"为什么我们看不到宏观叠加"，但不解释"为什么单次测量得到具体结果"。

**④ 客观坍缩**（GRW 1986, Penrose）：坍缩是真实的物理过程，质量越大坍缩越快，宏观物体（含 $10^{23}$ 个粒子）几乎瞬间发生。可被实验检验。

**⑤ 导航波 / Bohmian**（Bohm, 1952）：粒子始终有确定位置，波函数是真实的"导航场"。预言与标准量子力学完全等价，但物理图像完全不同。

**当前状态**：没有任何解释获得普遍接受。但实用的量子力学（薛定谔方程 + Born 规则）在**所有**已知实验中准确无误。这是物理学最深刻的未解之谜之一。

</div>

</div>

---

# §15 参考文献

<div style="font-size: 0.7em; line-height: 1.6;">

[1] E. Schrödinger, "Quantisierung als Eigenwertproblem (Erste Mitteilung)," *Ann. Phys.* **384**, 361 (1926). 波动力学第一篇论文，建立定态薛定谔方程。

[2] E. Schrödinger, "Über das Verhältnis der Heisenberg-Born-Jordanschen Quantenmechanik zu der meinen," *Ann. Phys.* **384**, 734 (1926). 证明波动力学与矩阵力学完全等价。

[3] W. Heisenberg, "Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen," *Z. Phys.* **33**, 879 (1925). 矩阵力学的奠基性论文。

[4] R. P. Feynman, "Space-Time Approach to Non-Relativistic Quantum Mechanics," *Rev. Mod. Phys.* **20**, 367 (1948). 路径积分的奠基性论文。

[5] M. H. Stone, "On One-Parameter Unitary Groups in Hilbert Space," *Ann. Math.* **33**, 643 (1932). Stone 定理，幺正演化的数学基础。

[6] R. P. Feynman, R. B. Leighton, M. Sands, *The Feynman Lectures on Physics*, Vol. III, Ch. 16 (Addison-Wesley, 1965). 经典教学："薛定谔方程从何而来"。

[7] J. J. Sakurai & J. Napolitano, *Modern Quantum Mechanics*, 3rd ed. (Cambridge Univ. Press, 2020). 现代公理化路径。

[8] D. J. Griffiths & D. F. Schroeter, *Introduction to Quantum Mechanics*, 3rd ed. (Cambridge Univ. Press, 2018). 启发式构造，本科标准教材。

[9] W. Moore, *Schrödinger: Life and Thought* (Cambridge Univ. Press, 1989). 薛定谔传记，讲述阿罗萨度假与方程诞生的故事。

[10] S. Weinberg, "Testing Quantum Mechanics," *Ann. Phys.* **194**, 336 (1989). 非线性量子力学的尝试与困难。

</div>

---

# 第三章总结（一）

- **德布罗意关系**：$E = h\nu$，$p = h/\lambda$，或 $E = \hbar\omega$，$p = \hbar k$

- **德布罗意对角动量量子化的解释**：驻波条件 $\Rightarrow$ 波长量子化 $\Rightarrow$ 角动量量子化

- **戴维孙-革末实验**：物质波的第一个实验证据

- **波函数的统计解释**（玻恩）：$|\Psi|^2$ 是概率密度

- **波包**：在有限区域之外为零（或极小）的波，描述局域化粒子

---

# 第三章总结（二）

- **波函数的性质**：单值、有限、连续，归一化 $\displaystyle\int_{\Omega}|\Psi|^{2} dV = 1$

- **不确定性关系**：$\Delta x \Delta p \geq \hbar/2$，$\Delta t \Delta E \geq \hbar/2$

- **薛定谔方程**：$i\hbar \dfrac{\partial \Psi}{\partial t} = \hat{H}\Psi$（量子力学的基本方程）

- **定态薛定谔方程**：$\hat{H}\psi = E\psi$（本征值问题）

- **经典与量子的对比**：牛顿方程 $\leftrightarrow$ 薛定谔方程，轨道 $\leftrightarrow$ 波函数，确定值 $\leftrightarrow$ 概率
