import pandas as pd
import matplotlib.pyplot as plt  # plot 画板画画
import matplotlib

orders = [
    {"category": "图书", "amount": 120},
    {"category": "文具", "amount": 80},
    {"category": "图书", "amount": 200},
    {"category": "数码", "amount": 500},
    {"category": "文具", "amount": 150}
]

#Mac 直接用 macosx 后端（原生，不需要tkinter）
matplotlib.use('macosx')
# Mac自带中文字体：Arial Unicode MS / STHeiti
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 1.创建 DataFrame
df = pd.DataFrame(orders)

# ---- 3. 分类总销售额，柱状图 ----
cat_total = df.groupby("category")["amount"].sum()
print("各分类销售总额：")
print(cat_total)

res = cat_total[cat_total>200]
print('销售总额大于 200 的分类：\n', res)


plt.figure(figsize=(6,4))
plt.bar(cat_total.index,cat_total.values)
plt.title("各分类销售总额柱状图")
plt.xlabel("商品分类")
plt.ylabel("销售总额")
plt.show()




