#传统
def get_sum(a, b):
    print(a+b)
    return a+b
get_sum(1,2)

#打印函数地址
f1 = get_sum
print(f1,get_sum)

#匿名函数
'''
lambda表达式:简单函数的简洁写法，它又叫匿名函数。
语法形式: lambda 形参1, 形参2, ... : 单行表达式 或 函数调用

注意点：
1）匿名函数中不能使用 while 循环、for 循环，只能编写单行的表达式，或函数调用
2）匿名函数中返回结果不需要使用 return，表达式的运行结果就是返回结果
3）匿名函数中也可以不返回结果。例如: lambda : print('hello world')

'''
f2 = lambda a,b:a+b
#打印函数地址
print((lambda a,b:a+b),f2)
#匿名函数调用1
print(f2(1,3))
#匿名函数调用2
print((lambda a,b:a+b)(1,4))

#函数地址作为参数传递
def show(func,a,b):
    func(a,b)
show(get_sum,1,2)

