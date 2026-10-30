import pandas as pd

# 基于字典
data = {
    '姓名':['张三','张三1','张三2','张三3'],
    '年龄':[25,30,35,28],
    '城市':['北京','上海','广州','深圳'],
    '工资':[5000,7000,6000,8000]
}  # key就是列名，value是列表，当前列的每一行数据

df1 = pd.DataFrame(data)
print(df1)
print(type(df1))
print('='*20)

# 基于列表
data_list = [
    ['张三', 25,'北京',5000],
    ['张三1', 30, '上海', 7000],
    ['张三2', 35, '广州', 6000],
    ['张三3', 28, '深圳', 8000],
]

df2 = pd.DataFrame(data_list)  # 没有列名，列默认0 -> 1 -> 2 -> ...
print(df2)
print('='*20)

# 查看DataFrame的基本信息
print('形状：',df1.shape)
print('列名：',df1.columns)        # 列索引
print('索引：',df1.index)          # 行索引
print('数据类型：',df1.dtypes)      # 每个列的类型



#test 使用 Pandas 创建学生成绩数据，包含 name 和 score 两列，输出分数大于 80 的学生。
student_info = pd.DataFrame({
    'name':['张三','张三1','张三2','张三3','张三4','张三5'],
    'score':[75,80,85,68,90,88]
})
print("分数大于 80 的学生：\n", student_info[student_info['score'] > 80])