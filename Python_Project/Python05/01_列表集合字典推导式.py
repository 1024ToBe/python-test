"""
三目运算：真值放前面，if 条件，else 后面放假值
"""
a = 10
b = 20
res = a  if a>b else b
print(f'三元计算后结果{res}')

# 推导式：先for生成变量，然后把生成的i放到列表[]里)
# 需求: 生成存储了1-10的列表
# 方式1: 原始方式
# 1.定义空列表
nums1 = []
# 2.循环依次生成1-10,依次放到列表中
for i in range(1, 11):
    # i依次代表1-10,然后依次放到列表中
    nums1.append(i)

# 3.使用列表
print(nums1)

# 方式2: 推导式
nums2 = [i for i in range(1, 11)]
print(nums2)
print('---------------------------------------------')
# 需求: 生成一个存储了1-10中偶数的列表
# 方式1: 原始方式
# 1.定义空列表
nums1 = []
# 2.循环依次生成1-10,依次放到列表中
for i in range(1, 11):
    # 如果是偶数放到列表中
    if i % 2 == 0:
        # i依次代表1-10,然后依次放到列表中
        nums1.append(i)

# 3.使用列表
print(nums1)

# 方式2: 推导式
nums2 = [i for i in range(1, 11) if i % 2 == 0]
print(nums2)
