import numpy as np

# numpy的核心对象是ndarray对象，需要将数据对象如list、元组等转换为ndarray
# -> 从列表创建 -> ndarray
arr1: np.ndarray = np.array([1,3,5,7,9])
print('一维数组arr1：',arr1,type(arr1))

arr2 = np.array([ [1,2,3],[4,5,6] ])
print('二维数组arr2：\n',arr2)

# 创建特殊数组
# 全是0的数组
zeros_arr = np.zeros((3,4))     # 传入元组，3和4,3行4列，二维
print('全0数组：\n',zeros_arr)

# 全是1的数组
one_arr = np.ones((5,6))
print('全1数组：\n',one_arr)

# 创建序列数组，包头，不包尾巴，类似python range
range_arr: np.ndarray = np.arange(0,10,2)
print('序列数组：\n',range_arr,type(range_arr))

# 等分数组
linspace_arr = np.linspace(0,12,6)
print('等分数组：\n',linspace_arr)

# 随机数组
range_arr = np.random.rand(3,3)
print('随机数组：\n',range_arr)

# 标准正态分布数组
randn_arr = np.random.randn(3,3)
print('正态数组：\n',randn_arr)


# 查看ndarray对象的属性
# [   [],[]   ] 二维数组
# a = [
#     [
#         [],
#         [],
#     ],
#     [
#         [],
#         [],
#     ],
# ]   三维数组

#创建示例的数组
arr: np.ndarray = np.array([
    [1,2,3],
    [4,5,6]
])

# 属性，ndarray是一个class的类对象，类里面有方法也有变量（属性）
print('数组：',arr)
print('数组维度：',arr.ndim)      # 访问ndim成员属性
print('数组形状：',arr.shape)     # 形状（行数、列数）
print('数组大小：',arr.size)      # 元素总数
print('数据类型：',arr.dtype)     # 存的数据类型

# 数组int默认存储为int64（8字节 8bytes）
# python的int默认存储为int32（4字节 4bytes）


# ndarray的索引和切片
# arr[下标]
# arr[x, y]		# x为行下标, y列下标
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print('原始数组：\n',arr)

# 索引
print('第一个元素：',arr[0,0])
print('最后一行：',arr[-1])
print('第二列：',arr[:,1])  # 不关心行只关心列，行用:代替  [:, 列] 取指定列   [:数字]切片


# 切片
# arr[a: b]				    # a起始 b结束（不含），和列表一样
# arr[a1: b1, a2: b2]		# a1:b1 控制行   a2:b2控制列

print('前两行',arr[0: 2])
print('前两行两列',arr[:2, :2])
print('每隔一个元素要一个(行和列都隔)',arr[::2, ::2]) #[起始 : 结束 : 步长] ::2--起始省略、结束省略、步长=2

# 布尔索引
bool_arr = arr > 5
print('布尔结果：\n',bool_arr)
# 布尔结果：
#  [[False False False False]
#  [False  True  True  True]
#  [ True  True  True  True]]

# 练习
'''
1. 创建1个二维 内容不限，结构3x4
2. 取出 第二行第三列
3. 取出第二第三行，第二第三列
4. 创建1个1维数组内容不限，元素数量15个
5. 将其重塑为 3x5的二维
6. 转换为5x3的二维
7. 将5x3的二维摊平得到1维
'''
arr = np.array([
    [11,12,13,14],
    [15,16,17,18],
    [19,20,21,22]
])
print('3x4数组',arr)
print('第二行第三列',arr[1][2])
print('第二、三行',arr[1:3])
print('第二、三列',arr[:,1:3])

arr1 = np.arange(15) # 0~14，正好15个
print("一维数组：\n", arr1)

# 也可以用 np.linspace(0,10,15) 或者 np.random.randint(1,20,15)
arr1_1 = arr1.reshape(3,5)
print("重塑后3×5二维：\n", arr1_1)

arr1_2 = arr1_1.reshape(5,3)
print("重塑后5×3二维：\n", arr1_2)

arr1_0 = arr1_2.flatten()
print("将5x3的二维摊平得到1维：\n", arr1_0)


