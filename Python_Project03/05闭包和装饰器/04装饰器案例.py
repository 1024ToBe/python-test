'''
def 外层(fn):    # fn被修饰函数传入
    def 内层():
        修饰代码
        fn()
        修饰代码
    return 内层

@外层函数名
def 被修饰函数():
    ...
'''
#写一个装饰器,被装饰的函数能够输出执行时间(秒)
import time
def time_clac(fn):
    count = 0
    def inner():
        #用来统计函数被执行次数
        nonlocal count
        count+=1
        print(count)

        #统计函数执行时间
        s = time.time()
        fn()
        e = time.time()
        print(f'时间：{e-s}')

    return inner

@time_clac
def js1():
    for _ in range(100000):
        1+1  #单纯用来占用时间用

@time_clac
def js2():
    for _ in range(100000):
        100*100

js2()
js1()
js2()
js1()
