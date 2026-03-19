# AI Workshop 作业：玻尔模型——从1913年的量子化轨道到2024年的量子计算机

**本作业鼓励使用 AI 辅助完成。** 你可以借助 DeepSeek、豆包、Kimi、Qwen 等 AI 工具来帮助编写代码、调试程序、理解物理概念，甚至辅助阅读英文论文。AI 是强大的学习伙伴——关键在于你需要理解 AI 给出的每一步推导和每一行代码，能够独立解释其物理含义，并对结果做出批判性判断。提交的 PDF 文档中请注明使用了哪些 AI 工具。

本作业不需要量子力学基础。你只需要掌握课堂上学过的玻尔模型（三条假设、能级公式、玻尔半径）、氢原子光谱的基本知识，以及基本的 Python 编程能力。作业将带你从1913年玻尔的大胆假设出发，经过元素周期表的规律，到达2024年Rydberg原子量子计算的最前沿。

物理常数供参考：$h = 6.626 \times 10^{-34}$ J$\cdot$s，$\hbar = 1.055 \times 10^{-34}$ J$\cdot$s，$c = 2.998 \times 10^{8}$ m/s，$e = 1.602 \times 10^{-19}$ C，$m_e = 9.109 \times 10^{-31}$ kg，$a_0 = 0.529 \times 10^{-10}$ m（玻尔半径），$E_0 = 13.6$ eV（氢原子基态电离能），$k_B = 1.381 \times 10^{-23}$ J/K（玻尔兹曼常数），$k_e = 8.988 \times 10^{9}$ N$\cdot$m²/C²（库仑常数）。

**工具安装**：`pip install scikit-learn matplotlib numpy`

## 读题前先记住：这份作业真正想让你学会什么

玻尔模型是物理学史上最美丽的"错误"之一——它的基本图像（电子绕核做圆周运动）是错的，但它做出的预测（能级公式、玻尔半径）却惊人地准确。更令人意外的是，这个1913年的"粗糙"模型，在2024年的量子计算前沿竟然"复活"了：当原子被激发到极高能级（$n \sim 50 \text{--} 100$）时，电子的行为反而越来越像玻尔描述的经典轨道。这种被称为 Rydberg 原子的奇特状态，正是当今最热门的量子计算平台之一。

整份作业围绕两条主线展开：

1. **从个体到规律**：玻尔模型精确描述了氢原子，但周期表上有一百多种元素。AI 能不能从元素的基本属性出发，预测它们的电离能？在这个过程中，玻尔模型的物理直觉和 AI 的数据驱动方法各自扮演什么角色？
2. **从"错误"到前沿**：玻尔模型在低量子数时"错"，在高量子数时却越来越"对"——对应原理保证了这一点。Rydberg 原子就是这个极限的实验实现，而它正在被用来构建量子计算机。

做题时请始终把下面三件事分开：

1. **数据和计算告诉了你什么**：图像、拟合、误差、趋势。
2. **AI 找到了什么**：模型、预测、特征重要性。
3. **物理解释说了什么**：为什么会这样，玻尔模型能解释什么，不能解释什么。

## 建议完成顺序

1. 先完成第一题 1.1–1.2，建立对电离能周期性的数据直觉。
2. 再做 1.3–1.5，体验 ML 能学到什么、学不到什么。
3. 然后做第二题 2.1，亲手算一算 Rydberg 原子有多大、多慢。
4. 再做 2.2–2.3，通过 AI 辅助阅读了解量子计算前沿。
5. 最后做 2.4 的综合讨论，把两条线串起来。

---

## 第一题：机器学习预测电离能——从玻尔模型到元素周期律（50 分）

### 背景

玻尔模型告诉我们，氢原子的电离能是 $E_0 = 13.6$ eV。对于类氢离子（只有一个电子），电离能是 $Z^2 E_0$，其中 $Z$ 是核电荷数。但真实原子有很多电子，它们之间的屏蔽和关联效应使得电离能不再是简单的 $Z^2$ 关系。

然而，第一电离能 $I_E$（从中性原子中移走最外层一个电子所需的最小能量）的变化规律并非杂乱无章——它呈现出惊人的**周期性**，这正是元素周期表的物理基础。碱金属（Li, Na, K...）的电离能最低，因为最外层只有一个 $s$ 电子，受到内层电子的强烈屏蔽；稀有气体（He, Ne, Ar...）的电离能最高，因为满壳层结构特别稳定。

玻尔模型虽然不能精确计算多电子原子的电离能，但它提供了关键的物理直觉：如果用"有效核电荷" $Z_{\text{eff}}$ 替代 $Z$，则 $I_E \approx Z_{\text{eff}}^2 \times 13.6 / n^2$ eV 仍然是一个不错的近似。这种"屏蔽"思想（Slater规则）正是从玻尔模型出发的。

本题要求你：先用数据探索电离能的周期性规律，然后训练机器学习模型来预测电离能，最后讨论 AI 预测与物理理解之间的关系。

### 本题你真正要回答的问题

1. 电离能的周期性变化背后，隐藏着什么物理规律？
2. 在只知道元素的基本属性时，ML 能预测电离能到什么精度？
3. ML 模型的"特征重要性"与玻尔模型的物理直觉一致吗？

### 元素数据集

以下数据包含前54种元素（氢到氙）的第一电离能及其基本特征。所有特征都可以从元素周期表中查到，不需要量子力学计算。

```python
import numpy as np

# 前54种元素的数据
# 列：元素符号, 原子序数Z, 周期, 族(IUPAC), 电负性χ(Pauling), 原子半径r(pm),
#      最外层电子数n_val, 最外层主量子数n, 第一电离能IE(eV)
#
# 电负性：衡量原子吸引电子的能力（稀有气体无Pauling电负性，用0标记）
# 原子半径：经验共价半径
# 最外层电子数：价电子数（简化处理）
#   注意：过渡金属计入所有 d+s 电子（如 Fe = 3d⁶4s² → 8），
#   而主族元素只计 s+p 电子（如 Ga = 4s²4p¹ → 3）。
#   这导致 Zn(12) → Ga(3) 的跳变，反映了 d 电子在主族中变为"内层"的物理事实。

elements_data = [
    # 第1周期
    ('H',   1, 1,  1, 2.20,  25, 1, 1,  13.60),
    ('He',  2, 1, 18, 0.00,  31, 2, 1,  24.59),
    # 第2周期
    ('Li',  3, 2,  1, 0.98, 145, 1, 2,   5.39),
    ('Be',  4, 2,  2, 1.57, 105, 2, 2,   9.32),
    ('B',   5, 2, 13, 2.04,  85, 3, 2,   8.30),
    ('C',   6, 2, 14, 2.55,  70, 4, 2,  11.26),
    ('N',   7, 2, 15, 3.04,  65, 5, 2,  14.53),
    ('O',   8, 2, 16, 3.44,  60, 6, 2,  13.62),
    ('F',   9, 2, 17, 3.98,  50, 7, 2,  17.42),
    ('Ne', 10, 2, 18, 0.00,  38, 8, 2,  21.56),
    # 第3周期
    ('Na', 11, 3,  1, 0.93, 180, 1, 3,   5.14),
    ('Mg', 12, 3,  2, 1.31, 150, 2, 3,   7.65),
    ('Al', 13, 3, 13, 1.61, 125, 3, 3,   5.99),
    ('Si', 14, 3, 14, 1.90, 110, 4, 3,   8.15),
    ('P',  15, 3, 15, 2.19, 100, 5, 3,  10.49),
    ('S',  16, 3, 16, 2.58, 100, 6, 3,  10.36),
    ('Cl', 17, 3, 17, 3.16,  79, 7, 3,  12.97),
    ('Ar', 18, 3, 18, 0.00,  71, 8, 3,  15.76),
    # 第4周期
    ('K',  19, 4,  1, 0.82, 220, 1, 4,   4.34),
    ('Ca', 20, 4,  2, 1.00, 180, 2, 4,   6.11),
    ('Sc', 21, 4,  3, 1.36, 160, 3, 4,   6.56),
    ('Ti', 22, 4,  4, 1.54, 140, 4, 4,   6.83),
    ('V',  23, 4,  5, 1.63, 135, 5, 4,   6.75),
    ('Cr', 24, 4,  6, 1.66, 140, 6, 4,   6.77),
    ('Mn', 25, 4,  7, 1.55, 140, 7, 4,   7.43),
    ('Fe', 26, 4,  8, 1.83, 140, 8, 4,   7.90),
    ('Co', 27, 4,  9, 1.88, 135, 9, 4,   7.88),
    ('Ni', 28, 4, 10, 1.91, 135, 10, 4,  7.64),
    ('Cu', 29, 4, 11, 1.90, 135, 11, 4,  7.73),
    ('Zn', 30, 4, 12, 1.65, 135, 12, 4,  9.39),
    ('Ga', 31, 4, 13, 1.81, 130, 3, 4,   5.99),
    ('Ge', 32, 4, 14, 2.01, 125, 4, 4,   7.90),
    ('As', 33, 4, 15, 2.18, 115, 5, 4,   9.79),
    ('Se', 34, 4, 16, 2.55, 115, 6, 4,   9.75),
    ('Br', 35, 4, 17, 2.96, 115, 7, 4,  11.81),
    ('Kr', 36, 4, 18, 3.00,  88, 8, 4,  14.00),
    # 第5周期
    ('Rb', 37, 5,  1, 0.82, 235, 1, 5,   4.18),
    ('Sr', 38, 5,  2, 0.95, 200, 2, 5,   5.69),
    ('Y',  39, 5,  3, 1.22, 180, 3, 5,   6.22),
    ('Zr', 40, 5,  4, 1.33, 155, 4, 5,   6.63),
    ('Nb', 41, 5,  5, 1.60, 145, 5, 5,   6.76),
    ('Mo', 42, 5,  6, 2.16, 145, 6, 5,   7.09),
    ('Tc', 43, 5,  7, 1.90, 135, 7, 5,   7.28),
    ('Ru', 44, 5,  8, 2.20, 130, 8, 5,   7.36),
    ('Rh', 45, 5,  9, 2.28, 135, 9, 5,   7.46),
    ('Pd', 46, 5, 10, 2.20, 140, 10, 5,  8.34),
    ('Ag', 47, 5, 11, 1.93, 160, 11, 5,  7.58),
    ('Cd', 48, 5, 12, 1.69, 155, 12, 5,  8.99),
    ('In', 49, 5, 13, 1.78, 155, 3, 5,   5.79),
    ('Sn', 50, 5, 14, 1.96, 145, 4, 5,   7.34),
    ('Sb', 51, 5, 15, 2.05, 145, 5, 5,   8.61),
    ('Te', 52, 5, 16, 2.10, 140, 6, 5,   9.01),
    ('I',  53, 5, 17, 2.66, 140, 7, 5,  10.45),
    ('Xe', 54, 5, 18, 2.60, 108, 8, 5,  12.13),
]

# 转为 numpy 数组
names   = [e[0] for e in elements_data]
Z       = np.array([e[1] for e in elements_data], dtype=float)
period  = np.array([e[2] for e in elements_data], dtype=float)
group   = np.array([e[3] for e in elements_data], dtype=float)
chi     = np.array([e[4] for e in elements_data])  # 电负性
r_atom  = np.array([e[5] for e in elements_data])  # 原子半径 (pm)
n_val   = np.array([e[6] for e in elements_data], dtype=float)  # 最外层电子数
n_main  = np.array([e[7] for e in elements_data], dtype=float)  # 主量子数
IE      = np.array([e[8] for e in elements_data])  # 第一电离能 (eV)
```

### 1.1 电离能的周期性（8 分）

**要求：**

(a) 绘制第一电离能 $I_E$ 随原子序数 $Z$ 的变化曲线。用**不同颜色**标出碱金属（Li, Na, K, Rb）和稀有气体（He, Ne, Ar, Kr, Xe），并在图中标注它们的元素符号。

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))
plt.plot(Z, IE, 'o-', color='steelblue', markersize=4, label='所有元素')

# 标出碱金属和稀有气体
alkali_idx = [i for i, n in enumerate(names) if n in ['Li', 'Na', 'K', 'Rb']]
noble_idx  = [i for i, n in enumerate(names) if n in ['He', 'Ne', 'Ar', 'Kr', 'Xe']]

plt.scatter(Z[alkali_idx], IE[alkali_idx], c='red', s=80, zorder=5, label='碱金属')
plt.scatter(Z[noble_idx], IE[noble_idx], c='gold', s=80, zorder=5, label='稀有气体')

for i in alkali_idx + noble_idx:
    plt.annotate(names[i], (Z[i], IE[i]), textcoords="offset points",
                 xytext=(5, 5), fontsize=8)

plt.xlabel('原子序数 Z')
plt.ylabel('第一电离能 (eV)')
plt.legend()
plt.title('元素的第一电离能')
plt.tight_layout()
plt.show()
```

(b) 从图中观察：
- 电离能的整体趋势是什么？（是随 $Z$ 单调增大吗？）
- 每个周期的"山谷"（最低点）和"山峰"（最高点）分别对应什么元素？
- 在同一周期内，电离能从碱金属到稀有气体大致如何变化？有没有"反常"的地方（比如 B < Be，O < N）？

(c) **用玻尔模型的语言解释**：为什么碱金属的电离能最低？提示：碱金属的最外层只有一个 $s$ 电子，它"看到"的有效核电荷 $Z_{\text{eff}}$ 很小（大部分正电荷被内层电子屏蔽了），而它的主量子数 $n$ 又比上一个稀有气体大了1。用 $I_E \approx Z_{\text{eff}}^2 \times 13.6 / n^2$ 的思路，定性解释为什么从 Li 到 Rb 电离能逐渐降低。

### 1.2 数据探索与特征相关性（8 分）

**要求：**

(a) 绘制电离能 $I_E$ 与以下特征的散点图（6张子图）：原子序数 $Z$、电负性 $\chi$、原子半径 $r$、最外层电子数 $n_{\text{val}}$、主量子数 $n$、族序号。

```python
# 注意：电负性为0的元素（稀有气体）需要特殊处理
# 计算相关系数时可以排除 χ=0 的数据点，或单独标注

features = {
    'Z (原子序数)': Z,
    'χ (电负性)': chi,
    'r (原子半径/pm)': r_atom,
    'n_val (价电子数)': n_val,
    'n (主量子数)': n_main,
    '族序号': group,
}

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
alkali = [i for i, n in enumerate(names) if n in ['Li', 'Na', 'K', 'Rb']]

for ax, (label, feat) in zip(axes.flat, features.items()):
    ax.scatter(feat, IE, c='steelblue', s=20, label='其他')
    ax.scatter(feat[alkali], IE[alkali], c='red', s=60, label='碱金属')
    ax.set_xlabel(label)
    ax.set_ylabel('IE (eV)')
    ax.legend(fontsize=7)

plt.tight_layout()
plt.show()
```

(b) 计算 $I_E$ 与每个特征的 Pearson 相关系数（对电负性，排除 $\chi = 0$ 的数据点）。哪个特征与电离能的线性相关性最强？哪些特征的关系看起来不是简单的线性？

```python
for label, feat in features.items():
    if label.startswith('χ'):
        mask = feat > 0  # 排除稀有气体的 χ=0
        r = np.corrcoef(feat[mask], IE[mask])[0, 1]
        print(f'{label}: r = {r:.3f} (排除稀有气体)')
    else:
        r = np.corrcoef(feat, IE)[0, 1]
        print(f'{label}: r = {r:.3f}')
```

(c) **物理直觉与数据的对话**：电离能本质上是"把最外层电子拉走需要的能量"。不需要量子力学，仅凭玻尔模型的直觉回答：
- 为什么原子半径越大，电离能往往越小？（外层电子离核远，束缚弱。）
- 为什么电负性与电离能正相关？（越"贪"电子的原子，越不愿放手。）
- 为什么主量子数 $n$ 本身不是一个好的预测特征？（同一个 $n$ 值下，$I_E$ 从碱金属到稀有气体变化很大。）

### 1.3 训练机器学习模型（15 分）

现在让 AI 来预测电离能。

**要求：**

(a) 准备特征矩阵，将数据分为训练集（75%）和测试集（25%）：

```python
from sklearn.model_selection import train_test_split

# 7个特征：Z, 周期, 族, 电负性, 原子半径, 价电子数, 主量子数
X = np.column_stack([Z, period, group, chi, r_atom, n_val, n_main])
y = IE

X_train, X_test, y_train, y_test, names_train, names_test = train_test_split(
    X, y, names, test_size=0.25, random_state=42
)
print(f'训练集: {len(X_train)} 种元素, 测试集: {len(X_test)} 种元素')
print(f'测试集元素: {names_test}')
```

(b) 训练三种模型并比较效果：

```python
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

models = {
    '线性回归': LinearRegression(),
    '随机森林': RandomForestRegressor(n_estimators=200, random_state=42),
    '梯度提升': GradientBoostingRegressor(n_estimators=200, random_state=42),
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test  = model.predict(X_test)
    mae_train = mean_absolute_error(y_train, y_pred_train)
    mae_test  = mean_absolute_error(y_test, y_pred_test)
    r2_test   = r2_score(y_test, y_pred_test)
    results[name] = (mae_train, mae_test, r2_test)
    print(f'{name}:')
    print(f'  训练集 MAE = {mae_train:.3f} eV')
    print(f'  测试集 MAE = {mae_test:.3f} eV')
    print(f'  测试集 R²  = {r2_test:.3f}')
```

制作表格汇总三种模型的结果。哪个模型在测试集上表现最好？线性模型是否已经抓住了主要趋势？非线性模型带来了多少改进？

(c) 特征重要性分析：

```python
rf = models['随机森林']
importances = rf.feature_importances_
feature_names = ['Z', '周期', '族', 'χ', 'r', 'n_val', 'n']

plt.figure(figsize=(8, 4))
plt.bar(feature_names, importances, color='steelblue')
plt.ylabel('特征重要性')
plt.title('随机森林：哪些特征对预测电离能最重要？')
plt.tight_layout()
plt.show()
```

结果与 1.2(b) 中的相关系数一致吗？如果不一致，讨论可能的原因。（提示：相关系数只衡量线性关系，而随机森林可以捕捉非线性关系。）

(d) 绘制"预测值 vs 真实值"散点图（对角线 = 完美预测），对测试集中预测误差最大的3个元素，标注其名称。这些元素为什么难以预测？（提示：想想它们在周期表中的位置、电子构型是否有特殊之处。可以问 AI 了解更多。）

**结果自检：**
- 线性回归的测试集 MAE 应在 **1.0–2.0 eV** 左右——线性模型只能抓住大趋势。
- 梯度提升的测试集 MAE 应在 **0.3–0.8 eV** 左右——非线性模型能学到周期性的细节。
- 如果你的 $R^2 > 0.95$，说明模型效果不错。

### 1.4 玻尔模型 vs 机器学习（12 分）

现在让我们比较两种"预测"电离能的方式：玻尔模型的物理推导 vs 机器学习的数据拟合。

**要求：**

(a) **有效核电荷估算**：对于碱金属（Li, Na, K, Rb），用 Slater 规则的简化版本估算有效核电荷。Slater 规则的基本思想是：内层电子对外层电子产生屏蔽，使外层电子"看到"的核电荷减小为 $Z_{\text{eff}} = Z - \sigma$，其中 $\sigma$ 是屏蔽常数。

对碱金属，一个粗略但有用的近似是：$Z_{\text{eff}} \approx Z - (Z - 1) \times f$，其中 $f$ 是屏蔽因子（对碱金属大约取 $f \approx 0.95$，即内层电子屏蔽了约95%的核电荷）。然后用玻尔公式

$$
I_E^{\text{Bohr}} = \frac{Z_{\text{eff}}^2 \times 13.6}{n^2} \quad (\text{eV})
$$

预测电离能。

```python
# 碱金属数据
alkali_metals = {
    'Li': {'Z': 3,  'n': 2, 'IE_exp': 5.39},
    'Na': {'Z': 11, 'n': 3, 'IE_exp': 5.14},
    'K':  {'Z': 19, 'n': 4, 'IE_exp': 4.34},
    'Rb': {'Z': 37, 'n': 5, 'IE_exp': 4.18},
}

f = 0.95  # 屏蔽因子（粗略近似）
print(f"{'元素':<5} {'Z':>3} {'n':>2} {'Z_eff':>6} {'IE_Bohr':>8} {'IE_exp':>7} {'误差':>7}")
for name, d in alkali_metals.items():
    Z_eff = d['Z'] - (d['Z'] - 1) * f
    IE_bohr = Z_eff**2 * 13.6 / d['n']**2
    error = IE_bohr - d['IE_exp']
    print(f"{name:<5} {d['Z']:>3} {d['n']:>2} {Z_eff:>6.2f} {IE_bohr:>8.2f} {d['IE_exp']:>7.2f} {error:>+7.2f}")
```

(b) 比较三种方法对碱金属电离能的预测：
1. 纯玻尔模型（$Z_{\text{eff}} = 1$，即假设完全屏蔽）：$I_E = 13.6/n^2$
2. 玻尔+Slater屏蔽（上面的计算）
3. 你训练的最佳 ML 模型

制作表格，列出三种方法的预测值和误差。哪种方法最准确？

(c) **讨论**（不少于150字）：ML 模型预测得更准，但它"理解"电离能吗？具体来说：
- 如果有一种新元素（比如119号元素，超重碱金属），ML 模型和玻尔模型哪个更可能给出合理的预测？为什么？
- ML 模型能告诉你"电离能为什么呈周期性变化"吗？玻尔模型（加上屏蔽概念）能吗？
- 什么时候应该用物理模型，什么时候应该用数据驱动的 ML？

### 1.5 交叉验证与模型可靠性（7 分）

54个数据点其实不算多。

**要求：**

(a) 用留一交叉验证（LOOCV）评估梯度提升模型：

```python
from sklearn.model_selection import LeaveOneOut, cross_val_predict

loo = LeaveOneOut()
y_pred_loo = cross_val_predict(
    GradientBoostingRegressor(n_estimators=200, random_state=42),
    X, y, cv=loo
)
mae_loo = mean_absolute_error(y, y_pred_loo)
r2_loo  = r2_score(y, y_pred_loo)
print(f'LOOCV MAE = {mae_loo:.3f} eV')
print(f'LOOCV R²  = {r2_loo:.3f}')
```

(b) 绘制每个元素的 LOOCV 预测误差 $|I_E^{\text{pred}} - I_E^{\text{exp}}|$ 的柱状图，按原子序数排列。哪些元素的预测误差最大？它们有什么共同特点？

(c) LOOCV 的 MAE 比简单 train/test split 的结果更大还是更小？为什么 LOOCV 是更可靠的评估方式？（提示：54个元素中拿出25%做测试集，只有13–14个数据点，结果可能受随机划分的影响很大。）

---

## 第二题：Rydberg 原子——玻尔模型在量子计算前沿的"复活"（50 分）

### 背景

课堂上我们学了玻尔模型的三条假设，也知道这个模型最终被量子力学取代了：电子并不沿着确定的轨道运动，而是以概率云的形式分布在原子核周围。

但这里有一个深刻的物理原理——**玻尔对应原理**：当量子数 $n$ 趋向无穷大时，量子力学的预测必须过渡到经典力学。换句话说，对于极高激发态的原子（$n \gg 1$），电子的行为**确实**越来越像沿着经典轨道运动的粒子。

这种高激发态原子被称为 **Rydberg 原子**，以瑞典光谱学家 Johannes Rydberg 命名。当 $n \sim 50\text{--}100$ 时，Rydberg 原子有一些令人震惊的性质：
- 原子半径 $\sim n^2 a_0$，可以达到**微米量级**——比普通原子大数千倍
- 轨道周期 $\sim n^3$，电子运动变得极其缓慢
- 相邻 Rydberg 原子之间存在极强的**偶极-偶极相互作用**，作用距离可达微米量级

正是最后一条性质，使得 Rydberg 原子成为当今**量子计算**最热门的实验平台之一。2023年，Harvard/MIT 的 Lukin 团队在 *Nature* 上报道，他们用 Rydberg 原子阵列实现了包含48个逻辑量子比特的容错量子计算——这项工作被 *Physics World* 评为2024年度物理学突破。

### 本题你真正要回答的问题

1. Rydberg 原子有多"大"、多"慢"？玻尔模型能给出多准确的估计？
2. 为什么一个1913年的"错误"模型在2024年的量子计算前沿仍然有用？
3. AI 在 Rydberg 原子量子计算中扮演什么角色？

### 2.1 Rydberg 原子有多大？——用玻尔模型算一算（15 分）

**要求：**

(a) 用玻尔模型的公式，计算以下物理量随主量子数 $n$ 的变化，并绘图：

- **轨道半径**：$r_n = a_0 n^2$
- **轨道速度**：$v_n = \frac{e^2}{4\pi\varepsilon_0 \hbar} \cdot \frac{1}{n} = \frac{\alpha c}{n}$（其中 $\alpha \approx 1/137$ 是精细结构常数）
- **轨道周期**：$T_n = \frac{2\pi r_n}{v_n} = \frac{2\pi a_0}{\alpha c} \cdot n^3$
- **结合能**：$E_n = -\frac{13.6}{n^2}$ eV

```python
import numpy as np
import matplotlib.pyplot as plt

a0 = 0.529e-10   # 玻尔半径 (m)
alpha = 1/137.036 # 精细结构常数
c = 2.998e8       # 光速 (m/s)
E0 = 13.6         # eV

n = np.arange(1, 101)

r_n = a0 * n**2                      # 轨道半径 (m)
v_n = alpha * c / n                   # 轨道速度 (m/s)
T_n = 2 * np.pi * a0 / (alpha * c) * n**3  # 轨道周期 (s)
E_n = -E0 / n**2                      # 结合能 (eV)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0,0].semilogy(n, r_n * 1e6)  # 转为 μm
axes[0,0].set_ylabel('轨道半径 (μm)')
axes[0,0].axhline(y=0.5, color='r', ls='--', label='细菌大小 (~0.5 μm)')
axes[0,0].axhline(y=1e-4, color='g', ls='--', label='普通原子 (~0.1 nm)')
axes[0,0].legend(fontsize=8)

axes[0,1].semilogy(n, v_n / c)
axes[0,1].set_ylabel('轨道速度 (v/c)')

axes[1,0].semilogy(n, T_n)
axes[1,0].set_ylabel('轨道周期 (s)')
axes[1,0].set_xlabel('主量子数 n')

axes[1,1].plot(n, E_n)
axes[1,1].set_ylabel('结合能 (eV)')
axes[1,1].set_xlabel('主量子数 n')

for ax in axes.flat:
    ax.set_xlabel('主量子数 n')
    ax.grid(True, alpha=0.3)

plt.suptitle('玻尔模型预测的 Rydberg 原子性质')
plt.tight_layout()
plt.show()
```

(b) 填写下表——对比不同 $n$ 值下的原子性质：

| 性质 | $n = 1$（基态） | $n = 10$ | $n = 50$ | $n = 100$ |
|------|:---:|:---:|:---:|:---:|
| 轨道半径 | 0.053 nm | ? nm | ? μm | ? μm |
| 轨道速度 | $\alpha c$ | ? m/s | ? m/s | ? m/s |
| 轨道周期 | $1.5 \times 10^{-16}$ s | ? s | ? s | ? s |
| 结合能 | $-13.6$ eV | ? eV | ? eV | ? eV |

(c) **尺度感**：当 $n = 50$ 时，轨道半径大约是多少微米？找一个日常物体做比较（比如细菌约 $0.5\text{--}5\,\mu$m，红细胞约 $7\,\mu$m，头发丝直径约 $70\,\mu$m）。当 $n = 100$ 时，结合能只有多少 meV？与室温热能 $k_B T \approx 26$ meV 比较——这意味着什么？（提示：Rydberg 原子极其脆弱，必须在超低温下才能存活。）

(d) **对应原理的体现**：当 $n = 100$ 时，轨道速度只有光速的多少分之一？与经典理论中宏观带电粒子的速度比较。讨论：为什么说 $n$ 越大，玻尔模型的描述越接近"真实"？（提示：不确定度原理 $\Delta x \cdot \Delta p \geq \hbar/2$ 意味着，当轨道半径很大时，位置的相对不确定度 $\Delta x / r_n$ 变得越来越小。）

**结果自检：**
- $n = 50$ 时，轨道半径应约为 **0.13 μm** = 130 nm——比细菌小，但已接近大型病毒的尺度，远大于普通原子（~0.1 nm）。
- $n = 100$ 时，结合能应约为 **$-1.4$ meV**——比室温热能小得多，所以实验需要超冷原子。
- $n = 100$ 时，轨道速度约为 $2.2 \times 10^4$ m/s，远小于光速。

### 2.2 Rydberg 原子之间的相互作用——量子计算的物理基础（15 分）

Rydberg 原子之所以能用来做量子计算，关键在于一个叫做 **Rydberg 阻塞**（Rydberg blockade）的效应：当两个原子靠得很近时，如果一个原子已经被激发到 Rydberg 态，另一个原子就**无法**同时被激发——因为两个 Rydberg 原子之间的相互作用能会使第二个原子的能级发生偏移，偏离激光的共振频率。

这种"一个被激发了，邻居就不能被激发"的效应，天然地实现了量子计算中的"受控操作"——这正是量子逻辑门的基础。

**要求：**

(a) **van der Waals 相互作用的估算**：两个相距 $d$ 的 Rydberg 原子之间的相互作用能大致为

$$
V(d) = \frac{C_6}{d^6}
$$

其中 $C_6$ 系数与 $n$ 的关系为 $C_6 \propto n^{11}$（这个惊人的高次幂来自 Rydberg 原子的极大极化率）。对于铷原子（$^{87}$Rb，实验中最常用的 Rydberg 原子），当 $n = 60$ 时，实验和理论给出 $C_6 \approx 140 \text{ GHz} \cdot \mu\text{m}^6$（参见 Saffman 等人 2010 年综述）。这个单位的含义很直接：如果两个原子相距 $d$（单位 μm），则它们之间的相互作用频率为 $V/(2\pi) = C_6 / (2\pi d^6)$，单位是 GHz 或 MHz。

计算两个 $n = 60$ 的 Rydberg 铷原子在以下距离上的相互作用频率：

```python
# Rydberg 相互作用计算
# C6/(2π) = 140 GHz·μm^6，即 V/(2π) = 140 / d^6 GHz（d 的单位是 μm）
C6_over_2pi = 140  # GHz·μm^6, Rb |60S⟩ 态

distances_um = np.array([1, 3, 5, 7, 10, 15])  # 微米
V_GHz = C6_over_2pi / distances_um**6  # 相互作用频率 (GHz)

print(f"{'距离 (μm)':>10} {'V/2π (GHz)':>12} {'V/2π (MHz)':>12}")
for d, v in zip(distances_um, V_GHz):
    if v >= 1:
        print(f"{d:>10} {v:>12.2f} {v*1000:>12.0f}")
    else:
        print(f"{d:>10} {v:>12.2e} {v*1000:>12.2f}")
```

从结果中观察：相互作用随距离的衰减有多剧烈？（$1/d^6$ 意味着距离翻倍，相互作用减弱64倍！）在什么距离上，相互作用从 GHz 量级降到 MHz 量级？

(b) **Rydberg 阻塞半径**：激光激发 Rydberg 原子时，激光与原子的耦合强度用 **Rabi 频率** $\Omega$ 描述——它决定了原子被激发的速率。典型的实验参数为 $\Omega/(2\pi) \sim 1$ MHz。当两个原子之间的相互作用频率 $V/(2\pi)$ 大于 Rabi 频率 $\Omega/(2\pi)$ 时，Rydberg 阻塞生效。定义阻塞半径为相互作用恰好等于 Rabi 频率的距离：

$$
R_b = \left(\frac{C_6/(2\pi)}{\Omega/(2\pi)}\right)^{1/6}
$$

计算 $\Omega/(2\pi) = 1$ MHz 时的阻塞半径（单位：μm）。这个距离在原子物理实验中意味着什么？（提示：光镊阵列中原子的间距通常在 $3\text{--}5\,\mu$m 量级。）

```python
Omega_over_2pi = 1e-3  # Rabi 频率: 1 MHz = 0.001 GHz
R_b = (C6_over_2pi / Omega_over_2pi) ** (1/6)
print(f'阻塞半径 R_b = {R_b:.1f} μm')
```

(c) **量子数的魔力**：$C_6 \propto n^{11}$ 意味着阻塞半径 $R_b \propto n^{11/6}$。计算并绘制 $R_b$ 随 $n$ 的变化（从 $n = 20$ 到 $n = 100$）。在同一张图上标出典型的原子间距（$\sim 3\text{--}5\,\mu$m）。讨论：为什么实验上通常选择 $n \sim 50\text{--}70$ 的 Rydberg 态？太低或太高有什么问题？

```python
# C6 ∝ n^11，以 n=60 为参考点
n_range = np.arange(20, 101)
C6_n = C6_over_2pi * (n_range / 60)**11  # GHz·μm^6
R_b_n = (C6_n / Omega_over_2pi) ** (1/6)  # μm

plt.figure(figsize=(8, 5))
plt.plot(n_range, R_b_n, 'b-', lw=2)
plt.axhspan(3, 5, alpha=0.2, color='orange', label='典型原子间距 3–5 μm')
plt.xlabel('主量子数 n')
plt.ylabel('阻塞半径 (μm)')
plt.title('Rydberg 阻塞半径随量子数的变化')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

(d) **物理讨论**：用你自己的话解释（5–8句话）：为什么 Rydberg 原子适合做量子计算？你的解释应该包含以下要素：
- Rydberg 原子的"大"（高极化率，强相互作用）
- Rydberg 阻塞如何实现"受控操作"
- 为什么激光可以精确控制哪些原子被激发

### 2.3 AI 辅助论文解读：Rydberg 原子量子计算的里程碑（12 分）

2024年，Harvard/MIT 的 Lukin 团队在 *Nature* 上报道了一项突破性实验：他们用约280个物理量子比特（Rydberg 原子）实现了48个逻辑量子比特的容错量子计算，这是中性原子量子计算的里程碑。

**论文信息**：D. Bluvstein et al., "Logical quantum processor based on reconfigurable atom arrays", [*Nature* 626, 58–65 (2024)](https://doi.org/10.1038/s41586-023-06927-3)

你不需要完全读懂这篇论文——它涉及量子纠错等高级概念。但你可以借助 AI 工具来帮助理解。

**要求：**

(a) 在网上找到这篇论文的摘要（Abstract）。把摘要**原文**贴入你常用的 AI 工具（DeepSeek、Kimi 等），让 AI 用**中文**把摘要翻译成你能理解的版本，并要求它"面向只学过玻尔模型、没学过量子力学的大二学生解释"。把 AI 的翻译/解释附在作业中。

建议你给 AI 的提示词明确要求区分：
- 哪些是**实验事实**（做了什么、测到了什么）；
- 哪些是**技术术语**（逻辑量子比特、纠错码等），AI 应给出简明解释；
- 哪些是**意义评价**（为什么重要），AI 应说明评价的依据。

(b) 基于 AI 的解释，用**你自己的语言**回答以下问题（每个问题3–5句话）：
- 实验用的是什么原子？它们是如何被排列和操控的？（提示：光镊阵列）
- 什么是"物理量子比特"和"逻辑量子比特"？为什么需要用多个物理比特来编码一个逻辑比特？（提示：纠错）
- 这个实验与我们在 2.1–2.2 中讨论的 Rydberg 原子性质有什么关系？（提示：Rydberg 阻塞 → 受控门操作）
- 为什么这项工作被认为是量子计算的重要里程碑？

(c) **批判性评估 AI**：AI 的解释中，有没有你觉得**过于简化**或**可能不准确**的地方？如果 AI 提到了你不认识的术语（比如"表面码"、"transversal gate"），请用 AI 进一步追问，然后用你自己的话总结。诚实地标注你**确实理解**的部分和**仍然困惑**的部分——标注"不懂"不会扣分。

### 2.4 综合讨论（8 分）

(a) **从"错误"到"有用"**：玻尔模型在描述基态氢原子时就已经与量子力学的精确解吻合，但对于更复杂的原子（多电子、角动量等）却无能为力。然而在 Rydberg 原子的极端情况下，玻尔模型又"复活"了。用你的理解解释：一个"错误的"物理模型为什么仍然有价值？在科学研究中，"近似正确"和"精确正确"各自有什么用处？

(b) **连接两道题**：回顾第一题，你用 ML 预测了54种元素的电离能——这些是基态原子（$n = 1$ 或更一般地，最低能态）的性质。如果要预测 Rydberg 原子（$n = 50$）的性质（比如能级间距、极化率、寿命），你觉得 ML 方法还有效吗？它需要什么样的训练数据？玻尔模型在这种情况下是更好的选择还是更差的选择？

(c) **展望**：2024年是量子计算的一个重要年份——Rydberg 原子量子计算机的能力在快速增长。同时，AI 在物理学研究中的作用也在迅速扩大（你在第一题中已经体验过）。设想一下：AI 有可能帮助设计更好的 Rydberg 原子量子计算方案吗？比如，AI 能否帮助选择最优的量子数 $n$、原子间距、激光参数？这与第一题中 AI 预测电离能的思路有何相似之处？（自由发挥，鼓励大胆想象。）

---

## 提交要求

1. 提交 **PDF 文档**，包含完整的计算过程说明、结果图表和物理讨论
2. 不需要提交代码文件，但文档中需展示关键代码片段和运行结果
3. 所有图表必须有标题、轴标签和图例
4. 讨论题要求有独立思考，不要照搬 AI 的回答——如果用了 AI 辅助，请说明你做了哪些修改和补充
5. 请在文档开头注明你使用了哪些 AI 工具

## 评分标准

| 项目 | 分值 |
|------|------|
| 第一题：ML预测电离能——从玻尔模型到元素周期律 | 50 |
| 第二题：Rydberg原子——玻尔模型在量子计算前沿的"复活" | 50 |
| **总计** | **100** |

---

## 参考文献与资源

### 论文

1. D. Bluvstein et al., "Logical quantum processor based on reconfigurable atom arrays", [*Nature* 626, 58–65 (2024)](https://doi.org/10.1038/s41586-023-06927-3) — Harvard/MIT 团队用 Rydberg 原子阵列实现48个逻辑量子比特
2. D. Bluvstein et al., "A quantum processor based on coherent transport of entangled atom arrays", [*Nature* 604, 451–456 (2022)](https://doi.org/10.1038/s41586-022-04592-6) — 早期工作：可移动的 Rydberg 原子量子门
3. D. Pfau et al., "Ab-initio solution of the many-electron Schrödinger equation with deep neural networks", [*Phys. Rev. Research* 2, 033429 (2020)](https://doi.org/10.1103/PhysRevResearch.2.033429) — DeepMind FermiNet：用神经网络求解薛定谔方程
4. M. Cranmer, "Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl", [arXiv:2305.01582 (2023)](https://arxiv.org/abs/2305.01582) — 符号回归用于科学发现

### 教科书与综述

5. T.F. Gallagher, *Rydberg Atoms*, Cambridge University Press (1994) — Rydberg 原子的经典教科书
6. M. Saffman, T.G. Walker, K. Mølmer, "Quantum information with Rydberg atoms", [*Rev. Mod. Phys.* 82, 2313 (2010)](https://doi.org/10.1103/RevModPhys.82.2313) — Rydberg 量子信息综述

### 科普资源

7. [Physics World: 2024 Breakthrough of the Year — quantum error correction](https://physicsworld.com/a/two-advances-in-quantum-error-correction-share-the-physics-world-2024-breakthrough-of-the-year/) — Rydberg 原子量子纠错入选年度突破
8. [DeepMind Blog: FermiNet](https://deepmind.google/discover/blog/ferminet-quantum-physics-and-chemistry-from-first-principles/) — 神经网络求解量子化学

### 工具

- [scikit-learn：机器学习 Python 库](https://scikit-learn.org/)（`pip install scikit-learn`）
- [matplotlib：Python 绘图库](https://matplotlib.org/)（`pip install matplotlib`）
