import copy

l1 = [1,2,3]

#直接赋值，那么两个变量操作完全同步。一块区域
l2 = l1
l2.append(4)
print(l1,l2)

#浅拷贝，
# 没有嵌套情况下实现两块区域分离，有嵌套不行
l3 = l1.copy()
l3.append(5)
print(l3,l1)

#深拷贝
#无论嵌套不嵌套都可以实现完全分离
l4 = [1,2,['a','b','c']]
l5 = l4.copy()
l5.append(3)
print(l5,l4)  #此时 l5和l4是完全分开的

# l5[2].append('d')
# print(l5,l4)  #此时 l5，l4又混在一起了，都增加了 d [1, 2, ['a', 'b', 'c', 'd'], 3] [1, 2, ['a', 'b', 'c', 'd']]

l5 = copy.deepcopy(l4)
l5[2].append('d')
print(l5,l4)   #此时l5，l4也是完全独立开的


