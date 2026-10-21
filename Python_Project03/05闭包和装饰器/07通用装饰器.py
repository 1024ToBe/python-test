#装饰器，统计一个函数的执行时长
import time
def time_cal(fn):
    def inner(*args,**kwargs): # 怎么填，都能收
        start_time = time.time()
        # *args ==> 元组
        # **kwargs ==> 字典
        r = fn(*args,**kwargs)
        end_time = time.time()
        print(f'函数用时{end_time-start_time}')
        return r

    return inner

@time_cal
def fun1(num):
    for i in range(1,num+1):
        print(f'打印数字{i}')


@time_cal
def fun2(name,age,gender):
    print(f'我的名字:{name},年龄:{age},性别:{gender}')

@time_cal
def fun3(num):
    sum = 0
    for i in range(1,num+1):
        sum+=i
    return sum

fun1(100)
fun2('张三',22,'男')
r = fun3(50)
print(r)

