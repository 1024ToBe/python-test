import pandas as pd
import matplotlib.pyplot as plt  # plot 画板画画
import matplotlib

sales = [
    {"month": "1月", "category": "图书", "amount": 1200},
    {"month": "1月", "category": "文具", "amount": 800},
    {"month": "2月", "category": "图书", "amount": 1500},
    {"month": "2月", "category": "文具", "amount": 950},
    {"month": "3月", "category": "图书", "amount": 1800},
    {"month": "3月", "category": "文具", "amount": 1100}
]



#Mac 直接用 macosx 后端（原生，不需要tkinter）
matplotlib.use('macosx')
# Mac自带中文字体：Arial Unicode MS / STHeiti
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 1.创建 DataFrame
df = pd.DataFrame(sales)

# ---- 2. 每月总销售额，折线图 ----
month_total = df.groupby("month")["amount"].sum()
# 创建画板
plt.figure(figsize=(8,4))
# 画线
plt.plot(month_total.index,month_total.values,marker='o')
plt.title("每月总销售额趋势")
plt.xlabel("月份")
plt.ylabel("销售额")
plt.show()

# ---- 3. 分类总销售额，柱状图 ----
cat_total = df.groupby("category")["amount"].sum()
plt.figure(figsize=(6,4))
plt.bar(cat_total.index,cat_total.values)
plt.title("各分类总销售额")
plt.xlabel("商品分类")
plt.ylabel("销售额")
plt.show()




