'''
- df.head(n) 查看前n行
- df.tail(n) 查看尾n行
- df.loc[行索引] 取某一行用行索引
- df.loc[[行索引, 行索引, ..]]   # 取指定的多个行
- df.loc[行索引:行索引]   切片，从start行索引到stop行索引结束（包含尾巴）
- df.iloc[0|1|2|...] 用行自带的012索引取行
  - df.iloc[0] 取第一行
- df.iloc[[0, 2]]    # 取指定的0和2行即：第一行和第三行
- df.iloc[x:y]       # x和y是0123的数字行索引， 从x开始到y结束（不含尾巴）
- df[列索引]   # 取某个列
- df[[列索引, 列索引, ...]]   # 取指定的多个列
'''

import pandas as pd

# 创建示例DataFrame
data_list = [
    ['张三', 25,'北京',5000],
    ['张三1', 30, '上海', 7000],
    ['张三2', 35, '广州', 6000],
    ['张三3', 28, '深圳', 8000],
]

# 手动指定行列索引的名字（默认都是0、1、2、...）   column列 row行
df = pd.DataFrame(
    data_list,
    columns=['姓名','年龄','地址','薪资'],   # 手动提供列索引
    index=['row1','row2','row3','row4']   # 手动提供行索引
)

print(df)
print('='*20)

# 选择行
# 查看前2行
print('前两行：\n',df.head(2))
print('='*20)

# 查看尾2行
print('尾两行：\n',df.tail(2))
print('='*20)

# 查看df整体的描述信息
print('df信息：\n',df.describe()) # 类似sql： desc 表;
print('='*20)

# 选择列
# select 列, 列
# 单独看姓名列： select 姓名 from 表;
# df[列索引]   df[3]  df['姓名']
print('姓名列：\n',df['姓名'])
print('列类型：\n',type(df['姓名']))
print('='*20)

# 看姓名和年龄列
# select 姓名, 年龄 from 表;
# 语法： df[[列索引, 列索引, ...]]
print('姓名、年龄列：\n',df[['姓名','年龄']])
print('='*20)

# 通过行索引选择
# df.loc[行索引]
# df.loc[[行索引, 行索引, ...]]
print('第一行：\n',df.loc['row1'])
print('='*20)
print('第一行和第三行：\n',df.loc[['row1','row3']])

# 切片
print('切片：\n',df['row1':'row3'])  # 切片尾巴是包含

# 行索引默认0123...是一直存在，如果你手动设置了行索引，那么0123也存在，还是可以用
# df.iloc  可以用0123
# df.loc 用行索引名
print('第一行：\n',df.iloc[0])
print('第一行第三行：\n',df.iloc[[0,2]])
print('第三行：\n',df.iloc[0:2])# 不包含尾巴