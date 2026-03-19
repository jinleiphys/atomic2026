---
title: "AI Workshop：Vibe Coding 与物理学"
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
.slidev-layout.two-columns .col-right img {
  max-height: 380px !important;
  margin: 0 auto !important;
  object-fit: contain;
}
.timeline-box {
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
  border-radius: 12px;
  padding: 1.2rem;
  border-left: 4px solid #C71585;
  margin: 0.5rem 0;
}
.highlight-box {
  background: #fff3f8;
  border: 2px solid #C71585;
  border-radius: 10px;
  padding: 1rem 1.2rem;
  margin: 0.8rem 0;
}
.code-block {
  background: #1e1e2e;
  color: #cdd6f4;
  border-radius: 8px;
  padding: 1rem;
  font-family: "JetBrains Mono", "Fira Code", monospace !important;
  font-size: 0.85rem;
  line-height: 1.6;
}
.code-block .comment { color: #6c7086; }
.code-block .keyword { color: #cba6f7; }
.code-block .string { color: #a6e3a1; }
.code-block .function { color: #89b4fa; }
.emoji-large { font-size: 2rem; }
.workflow-step {
  background: white;
  border-radius: 8px;
  padding: 0.6rem 1rem;
  margin: 0.3rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.08);
  display: flex;
  align-items: center;
  gap: 0.8rem;
}
.workflow-step .step-num {
  background: #C71585;
  color: white;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.9rem;
  flex-shrink: 0;
}
</style>

# AI Workshop

<br>

## <span class="kaiti-accent">Vibe Coding 与物理学作业</span>

<br>

<div class="text-center">

**金 磊**

原子物理学 2026

</div>

---

# 编程方法的演变——<span class="kaiti-accent">抽象层不断上移</span>

70年来，编程的核心趋势：**把人从底层细节中解放出来**

<div class="grid grid-cols-4 gap-3 mt-4">

<div class="timeline-box text-center" style="font-size: 0.85rem;">
<div class="emoji-large">🔧</div>
<b>1950s</b><br>
机器码 / 汇编<br>
<span style="color:#666;">手动管理每个寄存器</span>
</div>

<div class="timeline-box text-center" style="font-size: 0.85rem;">
<div class="emoji-large">📐</div>
<b>1968</b><br>
结构化编程<br>
<span style="color:#666;">Dijkstra：消灭 goto</span>
</div>

<div class="timeline-box text-center" style="font-size: 0.85rem;">
<div class="emoji-large">🧩</div>
<b>1970s–90s</b><br>
面向对象 / 函数式<br>
<span style="color:#666;">封装、模块、可复用</span>
</div>

<div class="timeline-box text-center" style="font-size: 0.85rem;">
<div class="emoji-large">💬</div>
<b>2025</b><br>
<span class="kaiti-accent">Vibe Coding</span><br>
<span style="color:#666;">用自然语言驱动AI写代码</span>
</div>

</div>

<v-click>

<div class="highlight-box mt-4" style="font-size: 1.05rem;">

每次范式转移的本质都一样：**人关注"做什么"，机器负责"怎么做"**

Vibe Coding 把这个推到了极致——你的"编程语言"变成了中文/英文

</div>

</v-click>

---

# 什么是 Vibe Coding？

<div class="highlight-box">

**Vibe Coding**（氛围编程）：用自然语言指令驱动 AI 生成代码，以"跑通为准、快速迭代"的方式推进开发。

—— Andrej Karpathy（前特斯拉AI总监），2025年2月

</div>

<v-click>

Karpathy 的原话（大意）：

> "我开始了一种新的编程方式，我称之为 vibe coding——你完全沉浸在氛围中，拥抱指数级的增长，**忘掉代码的存在**。看到报错就把错误信息复制给AI，让它修复……关键是你不去读代码，**它就是能跑**。"

</v-click>

<v-click>

<div style="font-size: 1.1rem; margin-top: 1rem;">

Collins 词典将 **vibe coding** 评为 <span class="kaiti-accent">2025年度词汇</span>

Merriam-Webster 将其收入为流行语条目

</div>

</v-click>

---

# Vibe Coding ≠ 不严谨

Simon Willison（著名程序员博主）的重要澄清：

<div class="highlight-box">

"如果你认真审查、测试并理解了AI生成的每一行代码，那不算 vibe coding——那是**把AI当打字员**。"

</div>

<v-click>

所以 vibe coding 的核心争议是：<span class="kaiti-accent">把质量控制放在哪里？</span>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="timeline-box">
<b>传统编程</b><br>
质量控制在<b>写之前</b><br>
设计 → 编码 → 测试<br>
<span style="color:#666;">你理解每一行代码</span>
</div>

<div class="timeline-box">
<b>Vibe Coding</b><br>
质量控制在<b>写之后</b><br>
描述意图 → AI生成 → 运行/测试 → 迭代<br>
<span style="color:#666;">你理解<b>目标和结果</b></span>
</div>

</div>

</v-click>

<v-click>

对物理学研究和学习而言——结果是否正确，**物理规律**本身就是最好的检验标准！

</v-click>

---

# 科研中的"受控 Vibe Coding"

<div style="font-size: 1.05rem;">

对科研团队而言，vibe coding 的价值不在于"替代严谨的工程"，而在于：

</div>

<v-click>

<div class="highlight-box">

**把探索性研究中的大量"胶水工作"与原型构建加速到小时级**，将你的注意力重新聚焦到<span class="kaiti-accent">科学问题、实验设计、数据质量与结果解释</span>上。

</div>

</v-click>

<v-click>

但它也会放大风险——所以我们需要**护栏**：

<div class="grid grid-cols-3 gap-3 mt-3" style="font-size: 0.9rem;">

<div class="workflow-step" style="flex-direction: column; align-items: flex-start;">
<b>🎯 物理直觉是指南针</b><br>
AI找到的公式/结果必须通过物理检验
</div>

<div class="workflow-step" style="flex-direction: column; align-items: flex-start;">
<b>🧪 数据是裁判</b><br>
实验数据和已知结果验证AI输出
</div>

<div class="workflow-step" style="flex-direction: column; align-items: flex-start;">
<b>🧠 理解是底线</b><br>
"AI给了答案但你说不清物理含义，题没做完"
</div>

</div>

</v-click>

---
layout: two-cols
---

# AI Workshop 的设计理念

我们的作业 = <span class="kaiti-accent">受控的 Vibe Coding 实践</span>

<v-click>

**三层结构（每一份作业）：**

1️⃣ **经典物理计算**
用已学的公式动手算——建立直觉

2️⃣ **AI / ML 方法**
符号回归、机器学习——让AI"重新发现"物理规律

3️⃣ **前沿论文解读**
AI辅助阅读Nature/Science——连接课堂与前沿

</v-click>

<v-click>

**贯穿始终的核心问题：**

<span class="kaiti-accent">AI能找到什么？不能找到什么？</span>

"找到公式"和"理解公式"的区别是什么？

</v-click>

::right::

<v-click>

<div style="margin-top: 2rem; display: flex; flex-direction: column; align-items: center; gap: 0.6rem;">

<div style="background: #e8f5e9; border: 2px solid #4caf50; border-radius: 10px; padding: 0.8rem 1.5rem; text-align: center; font-size: 1rem; width: 80%;">
<b>经典物理计算</b><br><span style="font-size:0.8rem; color:#666;">建立直觉</span>
</div>

<div style="font-size: 1.5rem; color: #999;">↓</div>

<div style="background: #fff3e0; border: 2px solid #ff9800; border-radius: 10px; padding: 0.8rem 1.5rem; text-align: center; font-size: 1rem; width: 80%;">
<b>AI / ML 方法</b><br><span style="font-size:0.8rem; color:#666;">发现 vs 理解</span>
</div>

<div style="font-size: 1.5rem; color: #999;">↓</div>

<div style="background: #fce4ec; border: 2px solid #e91e63; border-radius: 10px; padding: 0.8rem 1.5rem; text-align: center; font-size: 1rem; width: 80%;">
<b>前沿论文解读</b><br><span style="font-size:0.8rem; color:#666;">课堂 → 前沿</span>
</div>

<div style="font-size: 1.5rem; color: #999;">↓</div>

<div style="background: #f3e5f5; border: 2px solid #9c27b0; border-radius: 10px; padding: 0.8rem 1.5rem; text-align: center; font-size: 1rem; width: 80%;">
<b>综合讨论</b><br><span style="font-size:0.8rem; color:#666;">AI能做什么？不能做什么？</span>
</div>

</div>

</v-click>

---

# Vibe Coding 工具——<span class="kaiti-accent">AI 编程神器一览</span>

<div class="grid grid-cols-2 gap-4 mt-2" style="font-size: 0.88rem;">

<div>

### AI IDE（图形界面）

<div class="workflow-step">
<div style="font-size:1.3rem; flex-shrink:0;">🖥️</div>
<div><b>Cursor</b><br>最流行的 AI-first IDE，内置 Agent 模式，"描述需求 → 自动改代码"<br><span style="color:#666;">cursor.com · 付费 · 目前最强编辑器体验</span></div>
</div>

<div class="workflow-step">
<div style="font-size:1.3rem; flex-shrink:0;">🌊</div>
<div><b>TRAE（字节跳动）</b><br>免费 AI IDE，内置豆包大模型，对中文支持好<br><span style="color:#666;">trae.ai · 免费 · 国内可直接使用</span></div>
</div>

<div class="workflow-step">
<div style="font-size:1.3rem; flex-shrink:0;">🆚</div>
<div><b>VS Code + Copilot</b><br>GitHub Copilot 插件，代码补全 + Chat<br><span style="color:#666;">学生免费 · 最普及的 AI 编程助手</span></div>
</div>

</div>

<div>

### AI CLI（命令行工具）

<div class="workflow-step">
<div style="font-size:1.3rem; flex-shrink:0;">🟠</div>
<div><b>Claude Code（Anthropic）</b><br>终端里的 AI 程序员，直接读写文件、运行命令<br><span style="color:#666;">claude.ai/code · 本课件就是用它做的！</span></div>
</div>

<div class="workflow-step">
<div style="font-size:1.3rem; flex-shrink:0;">💎</div>
<div><b>Gemini CLI（Google）</b><br>Google 的命令行 AI 编程工具，Gemini 驱动<br><span style="color:#666;">开源 · 免费额度充足</span></div>
</div>

<div class="workflow-step">
<div style="font-size:1.3rem; flex-shrink:0;">🧬</div>
<div><b>OpenAI Codex CLI</b><br>OpenAI 的终端 Agent，擅长多步骤自动化任务<br><span style="color:#666;">开源 · GPT-4o 驱动</span></div>
</div>

</div>

</div>

---

# CLI 工具演示——<span class="kaiti-accent">这份slides是怎么做的？</span>

<div class="grid grid-cols-2 gap-4 mt-2">

<div>

<div style="font-size: 1rem; line-height: 1.8;">

这份 Slidev 演示文稿的制作过程：

<v-click>

**1.** 我用自然语言告诉 Claude Code：

> "新建一个Slidev文件夹，介绍 vibe coding 和 AI 作业"

</v-click>

<v-click>

**2.** Claude Code 自动完成了：
- 创建 `package.json`
- 生成完整的 `slides.md`
- 配置楷体字体、强调色
- 安装依赖并测试运行

</v-click>

<v-click>

**3.** 我审查内容 → 提出修改 → AI 迭代

> "第6页有问题" → 自动修复

> "作业相关的删掉" → 自动删除

</v-click>

</div>

</div>

<div>

<v-click>

<div style="background: #1e1e2e; border-radius: 10px; padding: 1rem; color: #cdd6f4; font-family: monospace; font-size: 0.75rem; line-height: 1.7;">
<span style="color:#6c7086;"># 终端里的对话（真实过程）</span><br><br>
<span style="color:#a6e3a1;">$ claude</span><br><br>
<span style="color:#89b4fa;">我：</span>新建一个slide，用Slidev，<br>
&nbsp;&nbsp;&nbsp;&nbsp;介绍vibe coding<br>
&nbsp;&nbsp;&nbsp;&nbsp;和AI在作业中的应用<br><br>
<span style="color:#cba6f7;">Claude Code：</span><br>
&nbsp;&nbsp;创建 AI-workshop-slides/<br>
&nbsp;&nbsp;写入 package.json...<br>
&nbsp;&nbsp;写入 slides.md (11页)...<br>
&nbsp;&nbsp;npm install...<br>
&nbsp;&nbsp;✅ Slidev 启动成功<br><br>
<span style="color:#89b4fa;">我：</span>6页有问题<br><br>
<span style="color:#cba6f7;">Claude Code：</span><br>
&nbsp;&nbsp;问题是mermaid在v-click中<br>
&nbsp;&nbsp;渲染出错，已替换为HTML<br>
&nbsp;&nbsp;✅ 修复完成
</div>

</v-click>

</div>

</div>

<v-click>

<div class="highlight-box mt-2" style="text-align: center; font-size: 1rem;">
从零到完整slides：<span class="kaiti-accent">约15分钟</span>——这就是 Vibe Coding
</div>

</v-click>

---

# 总结

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Vibe Coding 的启示

<div style="font-size: 1rem; line-height: 1.8;">

- 编程的趋势是**抽象不断上移**
- 2025年：自然语言成为新的"编程语言"
- 对物理学生而言：**代码能力不再是门槛**
- 你的注意力可以回归到<span class="kaiti-accent">物理本身</span>

</div>

</div>

<div>

### 但物理理解不能外包

<div style="font-size: 1rem; line-height: 1.8;">

- AI 可以从数据中**找到** $V_s = a\nu + b$
- 但它不知道 $a = h/e$ 意味着**光是一份一份的**
- AI 可以**预测**电离能到 0.5 eV 精度
- 但它不知道**为什么**碱金属电离能最低
- <span class="kaiti-accent">找到公式 ≠ 理解公式</span>

</div>

</div>

</div>

<v-click>

<div class="highlight-box mt-6" style="text-align: center; font-size: 1.15rem;">

**核心态度**：AI 是强大的学习伙伴——但<span class="kaiti-accent">物理理解不能外包</span>

使用 AI 不丢人，不理解才丢人

</div>

</v-click>

---
layout: center
---

# <span class="kaiti-accent">Vibe Coding 时代已经到来</span>

<br>

<div style="font-size: 1.2rem; text-align: center;">

自然语言是新的编程语言

物理直觉是你的核心竞争力

</div>

<br>

<div style="text-align: center; font-size: 1rem; color: #666;">

拥抱 AI，但永远追问：**为什么？**

</div>
