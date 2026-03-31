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

**2026年1月**：同一团队将记录推至含 **7000+原子的钠纳米粒子**（170,000道尔顿，直径~8nm），质量已接近小型**病毒**！

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

1926年，玻恩（M. Born）提出了**统计诠释**：

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
layout: two-cols
---

# 量子力学的其他解释

**多世界解释**（休·埃弗雷特）

波函数从不坍缩，所有可能的量子事件都在多宇宙中实现，每个可能的历史在不同的宇宙中发生。

::right::

<img src="/images/Schroedingers_cat_film.svg-29098.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/9780691645926.jpg-29105.jpeg" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/1_340818701_171_85_3_824378794_c0eab89545593cfdca20f31f5498b98c-29121.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

---
layout: two-cols
---

# 量子力学的其他解释

**隐变量理论**（德布罗意-玻姆理论）

除了波函数之外还存在隐藏的变量决定粒子的行为，这些变量在标准量子力学中没有被考虑。

::right::

<img src="/images/Screen Shot 2024-03-27 at 21.37.11-29145.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/Screen Shot 2024-03-27 at 21.37.19-29152.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

---
layout: two-cols
---

# 量子力学的其他解释

**客观坍缩理论**（Penrose）

当量子叠加产生的时空曲率差异达到一个阈值时，会自发触发坍缩。彭罗斯认为这种坍缩与引力有关。

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

---
layout: two-cols
---

# 电子双缝干涉的统计学解释

设从 A、B 两缝通过的电子波函数分别为 $\psi_A$ 和 $\psi_B$。

双缝同时开启时：$\psi = \psi_A + \psi_B$

<div v-click>

概率密度：

$$|\psi|^2 = |\psi_A + \psi_B|^2 = |\psi_A|^2 + |\psi_B|^2 + \psi_A^* \psi_B + \psi_B^* \psi_A$$

后两项是**干涉项**，正是它产生了干涉条纹。

</div>

<div v-click>

玻恩的概率解释将粒子性和波动性统一起来：粒子逐个到达屏幕（粒子性），大量粒子的统计分布呈现干涉图样（波动性）。

</div>

::right::

<img src="/images/pasted-image-27416.png" style="max-width: 100%; max-height: 100px; object-fit: contain;" />

<img src="/images/pasted-image-27446.png" style="max-width: 100%; max-height: 100px; object-fit: contain;" />

<img src="/images/pasted-image-27453.png" style="max-width: 100%; max-height: 100px; object-fit: contain;" />

<img src="/images/pasted-image-27459.png" style="max-width: 100%; max-height: 100px; object-fit: contain;" />

---
layout: two-cols
---

# 电子云

用疏密表示空间各处概率密度的大小，很像在原子核外有一层疏密不等的"云"，形象地称为**电子云**。

- 密处：$|\Psi|^2$ 大，电子出现概率高
- 疏处：$|\Psi|^2$ 小，电子出现概率低

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

# Schrödinger's Joke

<img src="/images/Screen Shot 2024-03-27 at 22.05.33-29212.png" style="max-width: 500px; max-height: 400px; margin: 10px auto; display: block;" />

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

# 小结

- 量子力学中，系统的状态由**波函数** $\Psi(x,t)$ 表示

- 玻恩的统计解释：$|\Psi|^2$ 表示粒子出现的概率密度

- 波函数必须满足归一化条件 $\int |\Psi|^2 dx = 1$

- 期望值：$\langle Q \rangle = \int \Psi^* \hat{Q} \Psi \, dx$

- 态叠加原理：未测量时，粒子可以同时处于多个态的叠加



# §15 薛定谔方程

需要掌握的知识点：

描述薛定谔方程在量子力学中的作用

解释与时间依赖和与时间无关的薛定谔方程之间的区别

解释薛定谔方程的解

---

# 薛定谔方程

宏观上

经典的波：用波函数描述，满足经典的波动方程

经典的波、经典粒子都满足牛顿力学

那么，具有波粒二象性的粒子呢？

用什么描述？满足什么方程？

这是1925年维也纳大学的P.Debye和E.Schrodinger遇到的问题，也是玻尔的弟子们W.Heisenberg等人的问题！

---

# 问题的提出

$-\frac{\hbar^{2}}{2 m}\left(\frac{\partial^{2} \Psi}{\partial x^{2}}+\frac{\partial^{2} \Psi}{\partial y^{2}}+\frac{\partial^{2} \Psi}{\partial z^{2}}\right)+U(x, y, z, t) \Psi=i \hbar \frac{\partial \Psi}{\partial t}$

德拜:问薛定谔能不能讲一讲De Broglie的那篇学位论文呢？

德拜提醒薛定谔:“对于波，应该有一个波动方程”

薛定谔（1926）提出了非相对论性的薛定谔方程：

<img src="/images/pasted-image-27833.png" style="max-width: 500px; max-height: 400px;" />

---

# 薛定谔方程

<img src="/images/Screen Shot 2022-02-14 at 19.28.56-25712.png" style="max-width: 500px; max-height: 400px;" />

---

# 薛定谔方程

<img src="/images/Screenshot 2023-03-29 at 10.29.30-28961.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Screenshot 2023-03-29 at 10.32.17-28966.png" style="max-width: 500px; max-height: 400px;" />

---

# 自由粒子的波动方程

$\frac{\partial^{2} \Psi}{\partial x^{2}}=-k^2 \Psi(x, t), \quad \frac{\partial \Psi}{\partial t}=\frac{E}{i \hbar} \Psi(x, t)$

与经典波相似，自由粒子波函数分别对时间、空间求偏导，可以得到其满足的波动方程：

或 $E \Psi(x, t)=i \hbar \frac{\partial \Psi}{\partial t}$

考虑到： $E= \frac{(\hbar k)^2}{2m}$ ，有

---

# 非自由粒子的波函数

$\Psi(x,y,z,t)$

对非自由粒子，由于受外场作用, 其波函数与自由粒子的不同。

一般情况下，是一个坐标与时间的函数￼,  但具体形式要根据具体问题来确定。

用波函数描述微观粒子的状态，这是量子力学的基本假设之一,  这种新的描述方法, 充分体现了粒子的波粒二象性。

---

# 非自由粒子的波动方程

$\Psi(x,t)$

非自由粒子受到势场作用，其波函数 $i \hbar \frac{\partial}{\partial t} \Psi(x, t)=\left[-\frac{\hbar^{2}}{2 m} \frac{\partial^{2}}{\partial x^{2}}+U(x, t)\right] \Psi(x, t)$ 的形式与具体的势场有关，其满足的波动方程应加势能项：

三维情况下，波动方程变为：

薛定谔方程是量子力学的基本方程

类比牛顿第二定律在宏观的作用

---

# 经典力学与量子力学的对比

$\frac{d\vec{p}}{dt}=m\frac{d^2\vec{r}}{dt^2}$

---

# 定态薛定谔方程

$U$

当势能项 $\Psi(x, t)= A e^{i(kx-\omega t)}$ 不依赖于时间时，我们可以根据平面波波函数的形式 $\Psi(x, t)=\psi(x) e^{-i \omega t}$ ，猜测（ansatz）

不依赖于时间

不依赖于空间

满足定态薛定谔方程

波函数 $-\frac{\hbar^{2}}{2 m} \frac{d^{2} \psi(x)}{d x^{2}}+U(x) \psi(x)=E \psi(x)$ : 单值、有限、连续、可归一

---

# Ansatz

$y''(x) + 2 y'(x) + 3 y(x) = x^3$

is an educated guess or an additional assumption made to help solve a problem, and which may later be verified to be part of the solution by its results.

假设

代入上式求解系数 $y(x) = a x^3 + b x^2 + c x + d$

---

# 定态薛定谔方程

$\psi(x)$

解出定态波函数 $\Psi(x, t)=\psi(x) e^{-i \omega t}$ 后可得总波函数为：

概率密度为

即在定态下概率分布不随时间改变，这正是定态这一名称的由来。

<img src="/images/pasted-image-27914.png" style="max-width: 332px; max-height: 400px;" />

---

# 定态薛定谔方程的意义：

$-\frac{\hbar^{2}}{2 m} \nabla^{2} \psi+U \psi=E \psi$

对波函数进行某种运算或作用的符号称为算符。

若 $H \psi = \lambda \psi$ ，则 $\psi$ 是算符 $H$ 的本征函数，数值λ称为算符  $H$ 的本征值， $H \psi = \lambda \psi$ 称为算符 $H$ 的本征方程。因此，定态薛定谔方程也称为哈密顿算符的本征方程，或能量算符的本征方程。

利用薛定谔方程，再加上波函数标准条件，可以 “自然地” 得到微观粒子的重要特征—量子化结果, 而不须象普朗克假设那样强制假定量子化。薛定谔方程的结果，已被无数实验所证实。

---

# 态叠加原理

$\psi_1$

如果 $\psi_2$ , $\psi_n$ ,⋅⋅⋅, $\Psi=C_{1} \psi_{1}+C_{2} \psi_{2}+\cdots+C_{n} \psi_{n}$ 等都是体系的可能状态或称基矢，那么，它们的线性叠加态也是这个体系的一个可能状态。

即       $C_1,\  C_2,\ ...,\  C_n$

其中的系数 $1=\sum_{n} C_{n}^{2}$  为复数，它们模平方是在对应态粒子出现的概率。

它们满足：           
---

# 为什么波函数用复数表示

$(E-H) \Psi = 0$

考虑定态薛定谔方程 $H=T+V$ ，其中 $(E-T) \Psi = V \Psi$

通过变换可得 $E <0$

当 $\Psi = \frac{1}{E-T} V \Psi$ 时， $E >0$

当 $\Psi = \lim_{\epsilon -> 0}\frac{1}{E-T+i\epsilon} V \Psi$ 时，
---

# 总结

$E=h \nu \quad \text { and } \quad p=h / \lambda$

德布罗意关系式： $\Rightarrow$

德布罗意对角动量量子化的解释：局域内的波函数 $\Rightarrow$ 波长的量子化 $|\Psi|^{2}=$ 角动量的量子化

戴维孙-革末实验：物质波的第一个证据

波函数的统计解释： $\lambda=2 \pi / k , \quad \nu=\omega / 2 \pi=1 / T, \quad

v=\lambda \nu$ 概率密度

正弦波的参数： $\omega$

$k$ 和 $E=\hbar \omega, \quad  p=\hbar k$ 表达下的德布罗意关系：
波包：在某个有限区域之外为零（或极小）的波

---

# 总结

$\int_{\Omega}|\Psi|^{2} d V=1 \quad(\Omega-\text { 全空间 })$

波函数的性质以及归一化： $\begin{align}

& \Delta x \Delta k \geq 1 / 2, \quad \Delta t \Delta \omega \geq 1 / 2 \\

& \Delta x \Delta p \geq \hbar / 2, \quad \Delta t \Delta E \geq \hbar / 2

\end{align}$

不确定性关系： $\sigma  \equiv \sqrt{E[X^2]-(E[X])^2}$

不确定性原理的统计学解释：
经典力学与量子力学的对比：特点，状态描述，运动方程，联系

---

<!-- 此页内容待补充 -->

---

<!-- 此页内容待补充 -->

---

<!-- 此页内容待补充 -->

---

# 不确定性关系与傅里叶变换

吉他发声可以看成是主弦的频率和腔体反射声音频率的干涉叠加

因此，吉他（以及任何其他乐器，包括你的声音）发出的声音是由具有不同频率和振幅的纯正弦波组成的

<img src="/images/acoustic_guitar_techniques_article_image_2021-28709.jpg" style="max-width: 500px; max-height: 400px;" />

---

# 不确定性关系与傅里叶变换

$$$

\hat{f}(s)=\int_{-\infty}^{\infty} f(t) e^{-2 \pi i s t} d t

$$$

当我们描述这样一个复杂的信号时，我们可以选择两种相等的方式来表示它。我们可以选择用一个时间轴来描述所有产生干涉图样的波是如何同时相互作用的，或者我们可以选择用构成它的纯波的频率来描述它。这两种方式被称为双重关系（dual relationship）。

它们之间满足傅里叶变换

---

# 不确定性关系与傅里叶变换

$$$

\hat{f}(s)=\int_{-\infty}^{\infty} f(t) e^{-2 \pi i s t} d t

$$$

它们之间满足傅里叶变换

傅里叶逆变换

<img src="/images/1*ww6y2-OzmWfB5M_igMwuog-28805.gif" style="max-width: 500px;" />

---

# 不确定性关系与傅里叶变换

那么对时间的缩放会导致

<img src="/images/1*8q2WxhGVG4mKBfo_rmvD1w-28848.png" style="max-width: 500px; max-height: 400px;" />

---

# 不确定性关系与傅里叶变换

那么对时间的缩放会导致

<img src="/images/1*emjh1NtMFdAjPpKpxfaILQ-28854.png" style="max-width: 500px; max-height: 400px;" />

---

# 不确定性关系与傅里叶变换

那么对时间的缩放会导致

傅里叶变换的缩放特性意味着如果我们在时间上压缩信号，那么这对应于在频率上扩展信号，反之亦然

<img src="/images/1*0CJpPOjjAwQwbiuLKbVgEw-28863.png" style="max-width: 373px; max-height: 400px;" />
