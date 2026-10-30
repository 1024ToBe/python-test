import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print('数组a：',a)
print('数组b：',b)

# 算数运算
print('加法：\n',a+b)
print('减法：\n',a-b)
print('乘法：\n',a*b)
print('除法：\n',a/b)
print('幂运算：\n',a**2)

# 比较
print('大于比较：\n',a>b)
print('小于于比较：\n',a<b)

# 矩阵乘法(点积)      点积和模长是计算余弦相似度的基础算术计算
arr1 = np.array([
    [1,2],
    [3,4]
])
arr2 = np.array([
    [5,6],
    [7,8]
])
res = np.dot(arr1,arr2)
print(res)
# arr1第一行*arr2第一列：1*5+2*7=19
# arr1第一行*arr2第二列：1*6+2*8=22
# arr1第二行*arr2第一列：3*5+4*7=43
# arr1第二行*arr2第二列：3*6+4*8=50
# [[19 22]
#  [43 50]]

# 广播机制
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]           # 3X3
])
b = np.array([10,20,30]) # 1X1

print('数组a：\n',a)
print('数组b：\n',b)
print('广播加法：\n',a+b)  #b被广播到a的每一行

c = np.array([
    [1],
    [2],
    [3]
])  #3x1  每一行，广播给对方的每一行， 1给了a里面的[1, 2, 3]  2给了a里面的[4, 5, 6]
print("广播乘法：\n", a * c)

# 统计计算
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print('数组：\n',arr)
print('总和：\n',np.sum(arr))
print('每列总和：\n',np.sum(arr,axis=0))
print('每行总和：\n',np.sum(arr,axis=1))

print('平均值：\n',np.mean(arr))
print('标准差：\n',np.std(arr))
print('方值：\n',np.var(arr))

print('最大：\n',np.max(arr))
print('最大值的索引：\n',np.argmax(arr))
print('最小：\n',np.min(arr))
print('最小值的索引：\n',np.argmin(arr))