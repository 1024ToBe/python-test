#字典推导式
lst = [i for i in range(0,101)]
print(lst)

lst = [i for i in range(0, 101) if i%2==0]
print(lst)

dic = {i:i*i for i in range(0, 101) if i%2==0}
print(dic)

# 生成器推导式
# 注意:以下不是元组推导式
nums = (i for i in range(1, 11))
print(nums)
# 但是如果想要变成元组,可以使用tuple()类型转换
t = tuple(nums)
print(t)

#集合借助 生成器去推导生成
lst = list(i for i in range(0,101))
print(lst,type(lst))

#借助 生成器去推导生成
se1 = set(i for i in range(0,101))
print(se1,type(se1))