# pandas的数据也有维度，分为1维和2维
# 一维可以看做是一个只有一个列的数据库表
# 二维可以可看做是由多个列的数据库表
import pandas as pd

# 一维Series  <class 'pandas.Series'>
# 从列表创建(默认索引是 0、1、2)
s1 = pd.Series(['a','b','c'])  # numpy纯玩数字，pandas玩的是数据（数字、字符串都支持）
print(s1)
print(type(s1))
print('-'*20) #打印20隔- 虚线分割线

# 从字典创建
# 字典key作为数据的索引，字典的value就是数据
s2 = pd.Series({'a':1,'b':2,'c':3})
print(s2)
print('-'*20)

# 指定索引
s3 = pd.Series([100,200,300],index=['x','y','z'])
print(s3)
print('-'*20)

# 取值
print('s3全部值：',s3.values,type(s3.values))
print('s3全部索引：',s3.index)



