'''
def 外层(被修饰函数):
    def 内层(形参):
        修饰代码
        r = 被修饰函数(形参)
        修饰代码
        return r

    return 内层
'''
def buff(fn):
    def inner(x,y,z):
        print('开始装饰')
        r = fn(x,y,z)
        print('装饰结束')
        print(f'最后计算值={r}')
        return r
    return inner

@buff
def sum(x,y,z):
    return x+y+z

sum(1,2,3)