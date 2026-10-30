import pandas as pd
'''
orders = [
    {"category": "图书", "price": 30, "count": 4},
    {"category": "文具", "price": 5, "count": 20},
    {"category": "图书", "price": 45, "count": 2},
    {"category": "数码", "price": 300, "count": 1},
    {"category": "文具", "price": 8, "count": 10}
]

# 1.创建 DataFrame
df = pd.DataFrame(orders)
# 2.新增一列 amount，表示 price * count
df['amount'] = df['price'] * df['count']
print('新增一列amount后\n',df)

# 3.按 category 分组统计销售总额。
result = df.groupby("category")["amount"].sum()
print(result)

# 4.按销售总额从高到低排序。
result1 = result.sort_values(ascending=False)
print(result1)
'''

data = {
    "name": ["张三", "李四", "王五", "赵六"],
    "late_count": [2, None, 0, None]
}
df = pd.DataFrame(data)
# 筛选迟到次数不为空的数据
# res = df[df["late_count"] != None]   bug
res = df[df["late_count"].notna()]
print(res)