
lst = [2, 4, 2, 6, 2, 8, 10]

#查询
print(lst[2])
print(lst[-1])
print(lst.index(8))
#查询9是否在列表中
print(9 in lst)
print(lst.count(2))
print('长度：',len(lst))

#增加
lst.append(12)
lst.insert(1,99)
lst.extend([14,16])
print(lst)

#改
lst[0] = 100
print('改完之后lst:',lst)

#删除
#删除匹配到的第一个元素
lst.remove(2)
print('删除之后lst:',lst)
del lst[2]
print('删除之后lst:',lst)

pop_val = lst.pop(3)
print(pop_val,lst)
lst.clear()
print('清空之后lst:',lst)

#5 综合
lst = [11,22,33,44,55]
lst.reverse()
print("反转", lst)
lst.sort(reverse=True)
print("降序", lst)

#遍历
lst = [11,22,33,44,55,66]
i=0
print('while循环遍历:')
while i < len(lst):
    print(lst[i])
    i+=1

print('for循环遍历:')
for item in lst:
    print(item)
