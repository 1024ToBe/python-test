#打包 创建非空容器的过程就叫做打包
#打包元组
def func (*nums):
    print(nums,type(nums))
func(1,2,3,4)

#普通变量打包
a, *res, b = 1,2,3,4,5
print(res)

#拆包 作用：把容器里元素**打散成独立单个值**取出
lst = [10,20,30]
print(*lst)

tp = (11,22,33)
print(*tp)

s = {6,7,8}
print(*s)

str ='abc'
print(*str)

#变量拆包 元素数量必须匹配，除非用`*`接收剩余
a,b,c = [9,8,7]
print(a,b,c)

a, *res = [1,2,3,4]
print(a,res,type(res))

#字典拆包 把字典的键值对拆开，一般用在函数传参
d = {'张三':18, '李四':20}
def say (name,age):
    print(name,age)
say(*d) #拆包 只拿到key

#合并多个容器
l1 = [1,2]
l2 = [3,4]




