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
.slidev-layout { font-size: 1.2rem; }
.diff-box { display: flex; gap: 0.8em; margin-top: 0.6em; }
.diff-box .side { flex: 1; padding: 0.5em 0.7em; border-radius: 8px; font-size: 1.05em; line-height: 1.5; }
.diff-box .xray { background: rgba(88,86,214,0.08); border-left: 3px solid #5856d6; }
.diff-box .electron { background: rgba(199,21,133,0.08); border-left: 3px solid #C71585; }
.formula-box { background: rgba(48,209,88,0.06); border-radius: 10px; padding: 0.5em 0.8em; margin-top: 0.8em; border-left: 3px solid #30d158; font-size: 1.05em; }
</style>

# 戴维孙-革末实验：电子散射 vs X射线散射

<div class="diff-box">
<div class="side xray"><b>X射线</b><br>可以穿透物体表面，发生体散射（Bragg衍射）</div>
<div class="side electron"><b>低能电子</b><br>只能与物体表面发生作用，属于表面散射</div>
</div>

<div class="formula-box">

电子动量：$p = \sqrt{2me\Delta V}$

</div>

::right::

<img src="/images/CNX_UPhysics_39_05_bragg-1-23265.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 戴维孙-革末实验

<video controls style="max-width: 400px;">
  <source src="/images/videoplayback-29034.mp4" />
</video>

---
layout: two-cols
---

# 汤姆逊衍射实验

同年，英国的汤姆逊用多晶体做电子衍射实验,也得到了电子衍射照片。

::right::

<img src="/images/Screen Shot 2023-03-15 at 20.04.58-28471.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 汤姆逊衍射实验

同年，英国的汤姆逊用多晶体做电子衍射实验,也得到了电子衍射照片。

十年后，戴维逊、汤姆逊因电子衍射实验的成果共获1937年度诺贝尔物理奖。

::right::

<img src="/images/Screen Shot 2022-03-09 at 16.19.29-26625.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 德布罗意波长 $\lambda=1 \AA$ 时各粒子动能

$K_{T}=\frac{3}{2} k_{B} T=\frac{3}{2}\left(8.6210^{-5} \mathrm{eV} / \mathrm{K}\right)(300 \mathrm{~K})=38.8~\mathrm{meV}$

单原子气体（monatomic gas）在室温下的动能为

https://en.wikipedia.org/wiki/Monatomic_gas

---
layout: two-cols
---

# 德布罗意波和量子态

$l=n \lambda / 2$

定态

驻波

电子绕一周之后相位不变

圆周长是波长的整数倍

玻尔量子化条件

::right::

<img src="/images/CNX_UPhysics_39_05_string-1-23413.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 波粒二象性（电子散射实验）

1961年，Claus Jönsson在德国进行了第一个电子束双缝实验，证明电子束确实形成了干涉图案，这意味着电子集体表现为波。

::right::

<img src="/images/Screen Shot 2023-03-15 at 23.04.28-28494.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 波粒二象性（电子散射实验）

1961年，Claus Jönsson在德国进行了第一个电子束双缝实验，证明电子束确实形成了干涉图案，这意味着电子集体表现为波。

::right::

<img src="/images/CNX_UPhysics_39_06_duality-1-24258.jpg" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/Wave-particle_duality-24264.gif" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

---
layout: two-cols
---

# 波粒二象性（电子散射实验）

1974 年意大利的Giulio Pozzi和1989年日本的Akira Tonomura进行了第一个单电子通过狭缝的双缝实验。他们表明，即使电子单独通过狭缝，干涉条纹也会逐渐形成。这最终证明了电子衍射图像是由于电子的波动性而形成的。

::right::

<img src="/images/4e86ca73913ca43ca418deaf3e209739_1440w-26675.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 波粒二象性（电子散射实验）

电子不是每次只是随机通过其中的一条缝，而是“同时”通过了两条缝，并和“自己”发生了干涉。

<img src="/images/9e67b1b3aaf9576626f97f20e055da11_1440w-26683.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/14677f39105af01a5a05e422c912ae59_1440w-26691.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

::right::

<img src="/images/99380bf24481838b19a0e60b1ffcb2e3_1440w-26699.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/300db4aa0a9cc4ccd804cae19213610c_1440w-26705.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

---

# 波粒二象性（电子散射实验）

<img src="/images/Screen Shot 2023-03-15 at 23.21.35-28505.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/1_340818701_171_85_3_673605011_57003a3890cf1f96ae77fb258dad939c-28511.png" style="max-width: 400px; max-height: 400px;" />

---

# 波粒二象性

<img src="/images/23722e3c2ff6ac38e138ab4aba38c01a_1440w-2-26732.png" style="max-width: 500px; max-height: 400px;" />

---

# 波粒二象性

<img src="/images/2aab38f5e9704e365ecf9e118ee0306e_1440w-2-26738.png" style="max-width: 500px; max-height: 400px;" />

---

# 波粒二象性

<video controls style="max-width: 500px;">
  <source src="/images/Wave-28480.mp4" />
</video>

---

# 电子显微镜

第一台电子显微镜是由德国鲁斯卡（E·Ruska）研制成功，荣获1986年诺贝尔物理奖。

从波动光学可知，由于显微镜的分辨本领与波长成反比，光学显微镜的最大分辨距离大于0.2 μm，最大放大倍数也只有1000倍左右。

自从发现电子有波动性后，电子束德布罗意波长比光波波长短得多。而且极方便改变电子波的波长。这样就能制造出用电子波代替光波的电子显微镜。

---

<video controls style="max-width: 500px;">
  <source src="/images/Untitled-26745.mp4" />
</video>

---

# 小结

德布罗意的物质波假设任何具有动量的粒子也是波。波长与粒子的动量大小成反比。物质波的速度就是粒子的速度。

德布罗意物质波概念为玻尔氢原子模型中电子角动量的量化提供了基本原理。

在戴维孙-革末实验中，电子从结晶镍表面散射。观察到电子物质波的衍射图案。它们是物质波存在的证据。在各种粒子的衍射实验中观察到物质波。

---

# §13 不确定关系

需要掌握的知识点：

（1）描述位置-动量不确定关系的物理意义

（2）解释量子理论中不确定性原理的起源

（3）描述能量-时间不确定性关系的物理意义

---
layout: two-cols
---

# 唯像的测不准关系(Observer effect)

胎压测量时会导致轮胎内部气体的溢出，无法准确的测量轮胎的胎压

::right::

<img src="/images/aid120258-v4-728px-Check-Air-Pressure-in-Tires-Step-10-Version-2.jpg.webp-28524.jpeg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 唯像的测不准关系(Observer effect)

$\Delta p \sim \frac{h}{\lambda}$

对位置的测量总是会对运动物体的速度产生干扰，根据动量守恒，粒子受光量子撞击后，它的动量会产生一种测不准性，其大小同光子的动量差不多

光子的波长

运动物体动量

的不确定性

粒子位置的测不准性取决于光量子的波长 $\Delta x \sim \lambda$

位置测定得越准确，动量就变得越测不准，反之亦然

---
layout: two-cols
---

# 测不准关系的实验验证（单缝衍射）

$\Delta x = a$

1) 位置的不确定程度

电子在单缝处的位置

不确定量为 $0 \leq p_x \leq p \sin\theta_1$

2）单缝处电子的动量的不确定程度

忽略次级极大，认为电子都落在中央亮纹内，则：

$\Delta p_x = p\sin\theta_1$      (1)

x方向上的动量不确定量为：

::right::

<img src="/images/pasted-image-26779.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/pasted-image-26786.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/pasted-image-26793.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

---

# 测不准关系的实验验证（单缝衍射）

$\Delta p_x = p\sin\theta_1$

忽略次级极大，认为电子都落在中央亮纹内，则x方向上的动量不确定量为：

考虑到衍射条纹的次级极大,可得    $\Delta p_x \geq p\sin\theta_1$   （2）

一级最小衍射角  $\sin \theta_1 =\lambda / \Delta x$ ， 以及  $\lambda = h / p$ ，可得

代入(2)式有

$\sin\theta_1 = \frac{h}{p \Delta x }$    或： $\Delta p \geq \frac{h}{\Delta x }$

---

# 测不准关系的实验验证（单缝衍射）

<video controls style="max-width: 500px;">
  <source src="/images/ΦºúΘçèµ╡╖µú«σáíτÜäΣ╕ìτí«σ«ÜµÇºσÄƒτÉå-28705.mp4" />
</video>

---

# 海森堡不确定性原理 1927

$\Delta x \Delta p_{x} \geq \frac{\hbar}{2}$

1924 波粒二象性（德布罗意物质波）

1925 海森堡建立了矩阵力学（量子力学）

1926 薛定谔建立了波动方程（量子力学）

1927 海森堡基于矩阵力学和对易关系

测不准

不确定性原理

1927 肯纳德基于标准差推导出不确定性关系

1929 罗伯逊更普遍意义的不确定性关系

---

# 海森堡不确定性原理 1927

<img src="/images/Screenshot 2023-03-20 at 14.44.08-28558.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Screenshot 2023-03-20 at 14.49.01-28573.png" style="max-width: 500px; max-height: 400px;" />

---

# 海森堡不确定性原理 1927

<img src="/images/Screenshot 2023-03-20 at 15.04.55-28623.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Screenshot 2023-03-20 at 15.05.03-28617.png" style="max-width: 500px; max-height: 400px;" />

---

# 海森堡不确定性原理 1927

<img src="/images/Screenshot 2023-03-20 at 15.29.00-28662.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Screenshot 2023-03-20 at 15.30.38-28670.png" style="max-width: 500px; max-height: 400px;" />

---

# 能量与时间的不确定性关系

$p^{2} c^{2}=E^{2}-m_{0}^{2} c^{4}$

可得 $\Delta p=\frac{E}{c^{2} p} \Delta E$

粒子可能发生的位移 $v \Delta t=\frac{p}{m} \Delta t=\Delta x$

能级自然宽度和寿命

两边微分可得

---

# 练习

$\Delta t=10^{-8}~s$

原子的激发态通常存在约 $\nu=7.1\times 10^{14} \mathrm{~Hz}$ ，估算当原子从激发态跃迁并同时发射平均频率为 $\Delta E \approx \frac{\hbar}{2 \Delta t} \Rightarrow h \Delta f \approx \frac{\hbar}{2 \Delta t} \Rightarrow \Delta f \approx \frac{1}{4 \pi \Delta t}=\frac{1}{4 \pi\left(10^{-8} \mathrm{~s}\right)}=8.0 \times 10^{6} \mathrm{~Hz}$ 的光子时，发射光子频率的不确定性, 发射的辐射是单色的吗？

能量-时间不确定性原理表达了实验观察到，仅存在很短时间的量子态不能具有确定的能量。

---

# 当h=1时

<!-- TODO: 缺失图片 pasted-image-27117.tiff，需从Keynote重新导出 -->

<img src="/images/Screen Shot 2022-03-21 at 10.23.20-27128.png" style="max-width: 500px; max-height: 400px;" />

---

# 课外阅读

<img src="/images/1_799760234_171_85_3_675143862_bd7c9602dcfebe6ce1c760938b27cecb-28678.png" style="max-width: 400px; max-height: 400px;" />

---

# §14 波函数

需要掌握的知识点：

描述波函数的统计解释

使用波函数来确定概率

计算位置的期望值

---
layout: two-cols
---

# 波函数

问题：那么，粒子性和波动性这两个完全不同的性质又是如何统一到了微观粒子上呢？

::right::

<img src="/images/img-02.proxy.5ce.com-27163.jpeg" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/pasted-image-27178.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/pasted-image-27167.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

---
layout: two-cols
---

# 子弹、水波和电子分别通过双缝的理想实验

理查德·费曼Richard Feynman（1918－1988）美国物理学家。1965年诺贝尔物理奖得主。

::right::

<img src="/images/pasted-image-27189.jpeg" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/pasted-image-27196.jpeg" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

---
layout: two-cols
---

# 子弹的双缝实验

开单缝：

子弹密度分布曲线：P1 和P2。

开双缝：

曲线P1 ＋P2。

“非相干叠加”。即主要表现了粒子性。

::right::

<img src="/images/pasted-image-27233.jpeg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 水波的双缝实验

水波的双缝实验，屏上观察到的分布是否与子弹实验结果一样？

因为水波通过双缝时被分为两个相干的次波源，它们在空间将进行相干叠加，所以在屏上将呈现出双缝干涉图样。

::right::

<img src="/images/pasted-image-27271.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 电子的双缝实验

每个电子是如何从两个缝通过的，它们又是如何逐渐形成干涉花样的?

1). 通过缝时电子是粒子？

双缝干涉花样就应该是两个单缝花样的简单叠加。存在干涉就表明每个电子似乎都是从两个缝通过的。

2). 通过缝时电子已散开成波？

不可能在到达屏的一瞬间收缩成一个亮点 。

经典物理学无法解释

经典物理学无法说明粒子性和波动性之间的关系

::right::

<img src="/images/pasted-image-27296.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 概率波

在量子力学建立的初期，人们对德布罗意波的意义曾提出过各种各样的猜测，例如:

电子波是一个代表电子实体的波包，

电子本身是弥散于空间的物质波动，

电子的波动性是大量电子之间的相互作用等。

但是，这些猜测最终都因不能圆满地解释实验现象而不得不放弃。

1926年，玻恩（M.Born）对波粒二象性给出了一种

统计诠释，他认为

德布罗意波：是概率波

---
layout: two-cols
---

# 什么是波函数

宏观上

波函数需要的信息有相位，波长，振幅，含时演化

考虑到物质波也是波的一种，也应该具备上述信息

但是位置和动量不能同时确定

::right::

<img src="/images/600px-Wave_Sinusoidal_Cosine_wave_sine_Blue.svg-2-24291.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/AC_wave_Positive_direction-2-24272.gif" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/Plane_Wave_3D_Animation_300x216_255Colors-2-24278.gif" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

---
layout: two-cols
---

# 光的波函数

$E(x,t)$

波函数 $|E|^2$

能量密度 $E$

$\varepsilon_{\text {photon }}=h \nu$ 为电场强度

单个光子的能量

$|E|^2$

￼正比于光子数量

光打在屏幕上某点的概率

正比于电场在该点的强度的平方

::right::

<img src="/images/CNX_UPhysics_40_01_TwoSlit-1-24365.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 波函数的统计解释（M.Born, 1926）

$|\Psi(x,t)|^2$

直到1926年，M.Born在认真研究波粒二象性之后，才意识到，类似于爱因斯坦“光振幅的平方为光子密度的概率量度”，波函数的模方是粒子的几率密度！

即：波函数的模方 $t$ (波在空间某点的强度)与 $x$ 时刻在空间某点 $t$ 处单位体积内发现粒子的几率成正比

或, $x$ 时刻在 $x+dx$ 到 $P(x, x+d x)$ 的区间内找到粒子的几率 $|\Psi(x,t)|^2 dx$ 与￼成正比

::right::

<video controls style="max-width: 100%; max-height: 400px; object-fit: contain;">
  <source src="/images/1-24677.mp4" />
</video>

---
layout: two-cols
---

# 波函数的统计解释（M.Born, 1926）

波恩的波函数几率解释是量子力学基本原理之一

波函数是几率幅，是不可测量，可测量是几率

1954年Nobel物理奖

::right::

<img src="/images/CNX_UPhysics_40_01_Prob_Square-1-24588.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 波函数的统计解释（M.Born, 1926）

<img src="/images/Screenshot 2023-03-27 at 11.28.58-28926.png" style="max-width: 500px; max-height: 400px;" />

---

# 波函数的统计解释（M.Born, 1926）

<img src="/images/Screenshot 2023-03-27 at 11.28.54-28919.png" style="max-width: 500px; max-height: 400px;" />

---

# 波函数的统计解释（M.Born, 1926）

In a letter to Born on 4 December 1926, Einstein made his famous remark regarding quantum mechanics:


Quantum mechanics is certainly imposing. But an inner voice tells me that it is not yet the real thing. The theory says a lot, but does not really bring us any closer to the secret of the 'old one'. I, at any rate, am convinced that He is not playing at dice.


This quotation is often paraphrased as 'God does not play dice'.

Niels Bohr reportedly replied to Einstein's later expression of this sentiment by advising him to "stop telling God what to do."

---

# 波函数的统计解释（M.Born, 1926）

课外阅读

<img src="/images/1_799760234_171_85_3_677559846_22ee4b7cb5e10a621742b2f0775f6e68-28883.png" style="max-width: 400px; max-height: 400px;" />

<img src="/images/Screenshot 2023-03-27 at 11.18.38-28895.png" style="max-width: 500px; max-height: 400px;" />

<img src="/images/Screenshot 2023-03-27 at 11.22.17-28911.png" style="max-width: 500px; max-height: 400px;" />

---

# 哥本哈根解释

量子态的叠加: 在观测之前，一个量子系统可以同时处于多个可能状态的叠加。这意味着，系统的所有可能性都是同时存在的，直到被测量。

波函数坍缩: 当对一个量子系统进行测量时，波函数会突然“坍缩”到一个特定的状态，这个过程是不可逆的，而且与测量过程本身有关。

互补性原理: 玻尔提出的互补性原理指出，波动性和粒子性是量子现象的两个互补方面，只能在不同的实验安排中分别观察到。

不确定性原理: 海森堡提出不确定性原理，指出粒子的位置和动量不能同时被精确地知道。这不是测量技术的限制，而是自然界的基本性质。

---
layout: two-cols
---

# 量子力学的其他解释

多世界解释: 由休·埃弗雷特提出，认为波函数从不坍缩，而是所有可能的量子事件都在一个广阔的多宇宙中实现，每个可能的历史都在不同的宇宙中发生。

::right::

<img src="/images/Schroedingers_cat_film.svg-29098.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/9780691645926.jpg-29105.jpeg" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

<img src="/images/1_340818701_171_85_3_824378794_c0eab89545593cfdca20f31f5498b98c-29121.png" style="max-width: 100%; max-height: 130px; object-fit: contain;" />

---
layout: two-cols
---

# 量子力学的其他解释

隐变量理论: 如德布罗意-玻姆理论，提出除了波函数之外还有隐藏的变量决定粒子的行为，这些变量在标准量子力学中没有被考虑。

::right::

<img src="/images/Screen Shot 2024-03-27 at 21.37.11-29145.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/Screen Shot 2024-03-27 at 21.37.19-29152.png" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

---
layout: two-cols
---

# 量子力学的其他解释

客观坍缩理论: 在Penrose解释中，当一个物体的量子态与不同的时空几何相互叠加时，这种叠加状态是不稳定的，会自发地坍缩到一个确定的状态。彭罗斯认为，这种坍缩与引力有关，当量子叠加产生的时空曲率差异达到一个阈值时，就会触发坍缩。

::right::

<img src="/images/Screen Shot 2024-03-27 at 21.57.51-29187.png" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# 波函数的性质

$P(-\infty,+\infty)=\int_{-\infty}^{\infty}|\Psi(x, t)|^{2} d x=1$

波函数必须单值、有限、连续可导

单值：在任何一点，几率只能有一个值。

有限：几率不能无限大。

连续可导：几率一般不发生突变。

归一化条件：由于粒子总在空间某处出现，故在整个空间出现的总几率应当为1

---

# 波函数的归一化

$\int_{\Omega}|\Psi|^{2} d V=1 \quad(\Omega-\text { 全空间 })$

由于波函数 $\psi(\vec{r}, t)$ 的概率解释, 粒子在整个空间出现的概率为1，所以 $\psi$ 应该满足波函数的归一化条件：

已知 $\phi(\vec{r}, t)$ 是未归一化的波函数，则令 $\psi=A \phi$ ，它们描述同一个状态，有

所以

---

# 波函数的物理意义

$[x, x+\Delta x]$

在空间很小的区域  $[y,y+\Delta y]$ ， $[z,z+\Delta z]$ ， $d V=d x d y d z$ 内，波函数可视为不变，粒子在 $|\Psi|^{2}$ 内出现的概率, 正比于 $dV$ 和 $|\psi|^{2}$ 。

$t$ －在 $(x,y,z)$ 时刻粒子出现在 $|\psi|^{2} d V$ 点处单位体

积内出现的概率密度。

$t$ －在 $(x,y,z)$ 时刻粒子出现在 $dV$ 点附近  $\int_{V}|\psi|^{2} d V$

体积元内出现的概率。

$t$ －在 $V$ 时刻粒子出现在 $\alpha$ 体积内的概率。

当 $\psi$ 为实数时， $e^{i\alpha}\psi$ 与￼代表同一个态

---
layout: two-cols
---

# 电子双缝干涉实验的统计学解释

$\psi_A(r,t)$

在电子双缝干涉实验中，用波函数 $\psi_B(r,t)$ 和 $\psi(r, t)=\psi_{A}(r, t)+\psi_{B}(r, t)$ 分别表示从A、B缝通过电子的状态。两缝同时开启时，电子的波函数为 $\begin{aligned}

|\psi(\mathbf{r}, t)|^{2} &=\left|\psi_{A}+\psi_{B}\right|^{2} \\

&=\left|\psi_{A}\right|^{2}+\left|\psi_{B}\right|^{2}+\psi_{A}^{*} \psi_{B}+\psi_{B}^{*} \psi_{A}

\end{aligned}$

屏上发现电子的概率分布为

玻恩用概率解释把微观粒子的波动性和粒子性统一起来，

玻恩的统计诠释成为量子力学的一个基本假设。

::right::

<img src="/images/pasted-image-27416.png" style="max-width: 100%; max-height: 90px; object-fit: contain;" />

<img src="/images/pasted-image-27446.png" style="max-width: 100%; max-height: 90px; object-fit: contain;" />

<img src="/images/pasted-image-27453.png" style="max-width: 100%; max-height: 90px; object-fit: contain;" />

<img src="/images/pasted-image-27459.png" style="max-width: 100%; max-height: 90px; object-fit: contain;" />

---

# 如何理解微观粒子的波粒二象性

1) 粒子性

•整体性

•不是经典的粒子 没有“轨道”概念

2) 波动性

•“可叠加性”

•有“干涉”“衍射”“偏振”现象

•不是经典的波 不代表实在物理量的波动

---
layout: two-cols
---

# 电子云

用密或稀表示空间各处概率密度的大小，很像在原子核外有一层疏密不等的“云”，人们把它形象地叫做“电子云”。

::right::

<img src="/images/pasted-image-27530.jpeg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 习题

$L$

球被限制在长度为 $\Psi(x, 0)=A \cos (k x)~(-L / 2<x<L / 2)$ 的管内移动，球优先位于管的中间。表示其波函数的一种方法是使用简单的余弦函数。在管子的最后四分之一处找到球的概率是多少？

波函数可以写为

$k=2\pi/\lambda$ 为波数，区间外波函数为0

应用归一化条件可得 $A \cos (k L / 2)=0$ ，可得

::right::

<img src="/images/CNX_UPhysics_40_01_Cosine_Wave-1-24711.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---
layout: two-cols
---

# 习题

$L$

球被限制在长度为 $A=\sqrt{2 / L}$ 的管内移动，球优先位于管的中间。表示其波函数的一种方法是使用简单的余弦函数。在管子的最后四分之一处找到球的概率是多少？

应用归一化条件可得 $\Psi(x, 0)=\sqrt{\frac{2}{L}} \cos (\pi x / L), \quad-L / 2<x<L / 2$ ，可得

最后四分之一处找到球的概率

小球的波长

::right::

<img src="/images/CNX_UPhysics_40_01_Cosine_Wave-1-24711.jpg" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

<img src="/images/v2-4fcebba5e210f33cd800759166c495fe_720w.webp-24870.gif" style="max-width: 100%; max-height: 180px; object-fit: contain;" />

---
layout: two-cols
---

# 态叠加原理

$x_1$

考虑一个粒子可以在盒子 $x_2$ 或 $x_1$ 处

宏观上，粒子不是在 $x_2$ 就是在 $x_1$

量子力学中，当不被测量时，粒子既在 $x_2$ ，又在 $x_1$ ，处于 $x_2$ 与￼的叠加态

薛定谔的猫

::right::

<img src="/images/CNX_UPhysics_40_01_Two_State-1-25192.jpg" style="max-width: 100%; max-height: 400px; object-fit: contain;" />

---

# Schrödinger’s Joke

<img src="/images/Screen Shot 2024-03-27 at 22.05.33-29212.png" style="max-width: 500px; max-height: 400px;" />

---

# 什么是波函数

$\Psi(x, t)=A \sin (k x-\omega t)$

量子上 $\Psi(x,t)$

一个数学函数，它可用于确定做位置测量时粒子可能在哪里。

波函数如何用于预测？如果有必要找出在某个区间内发现粒子的概率，则对波函数求平方并在感兴趣的区间上积分。

如果物质波波函数为 $(x=-\infty,+\infty)$ ，那么粒子究竟在哪？

当不被观测时，粒子无处不在 $(x, x+d x)$

当被观测时，粒子“跳入”特定的状态 $P(x, x+d x)=|\Psi(x, t)|^{2} d x$ ，概率为￼，这个过程叫做“坍缩”

---

# 波函数的复数形式

$\Psi(x, t)=A \cos (k x-\omega t)+i A \sin (k x-\omega t) = A e^{i(kx-\omega t)} = Ae^{i\phi}$

量子力学的平面波波函数可以写为

相对于宏观的机械波、声波，物质波波函数不可测，因此需要写成复数形式

用复共轭的方式计算概率

---

# 期望值计算

$x(t)$

宏观上，运动方程的解是一个可测量量的函数，例如  $x$ ，其中 $t$ 是位置， $t$ 是时间。请注意，粒子在任何时间 $\Psi(x,t)$ 都有一个位置值。

在量子力学中，运动方程的解是波函数 $t$ 。粒子在任何时间 $|\Psi(x,t)|^2$ 都有许多位置值，并且只能知道找到粒子的概率密度 $\langle x\rangle=\int_{-\infty}^{\infty} x P(x, t) d x=\int_{-\infty}^{\infty} x \Psi *(x, t) \Psi(x, t) d x$ 。粒子的位置平均值为

---

# 不确定性原理的统计学解释

$\Delta x \to \sigma_x$

使用标准差代替不确定度

<img src="/images/Standard_deviation_diagram.svg-25326.png" style="max-width: 500px; max-height: 400px;" />

---

# 习题

$\sigma_{x} \sigma_{p}=\frac{\hbar}{2}$

利用不确定性原理估算氢原子的基态能量（假设氢原子的直径为0.1 nm）

其中

电子在左右来回运动， $\sigma_{x}^{2}=x^{2}-\bar{x}^{2} \text { and } \sigma_{p}^{2}=p^{2}-\bar{p}^{2}$ ；位置的不确定性近似为原子的半径 $\bar{p}= 0$ ，因此基态能量可以估算为

为了方便计算，

---

# 波包

$\Psi(x, t)= A e^{i(kx-\omega t)}$

平面波波函数（确定动量 $p=\hbar k$ ）

确定动量时，粒子完全无法确定位置，无处不在

波包是平面波在 $|\Psi(x,t)|^2 =|A|^2$ 区间内的叠加态

<img src="/images/reality_wavepacket-25511.gif" style="max-width: 313px;" />

<img src="/images/Sequential_superposition_of_plane_waves-25514.gif" style="max-width: 360px;" />

---

# 小结

在量子力学中，系统的状态由波函数表示。

在玻恩的解释中，粒子波函数的平方表示在空间中特定位置附近找到粒子的概率密度。

在使用波函数进行预测之前，必须首先对波函数进行归一化。

期望值是一种平均值，它的计算需要波函数的形式和进行积分运算

---

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
