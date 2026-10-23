def process(lst):
    lst.append(100)

ls1 = [1,2,3]
# process(ls1) #这种方式= ‘用=赋值’
# print(ls1)

#浅拷贝
process(ls1.copy())
print(ls1)
