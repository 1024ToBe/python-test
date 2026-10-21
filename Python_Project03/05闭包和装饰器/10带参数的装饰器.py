'''
def 装饰器函数名(装饰器参数):
    def 中间层(被修饰函数):

        def 内层(被修饰函数的参数):
            修饰代码
            r = 被修饰函数(被修饰函数的参数)
            修饰代码
            return r

        return 内层

    return 中间层
'''
def outer(operator):
    def middle(fn):
        def inner(*args, **kwargs):
            if operator == '+':
                print('正在做加法运算')
            else:
                print('正在做减法运算')


            r = fn(*args, **kwargs)
            print('运算结束')
            return r
        return inner
    return middle


@outer('+')
def add(a,b):
    print(f'a+b={a+b}')


@outer('-')
def sub(a, b):
    print(f'a-b={a-b}')

add(1,2)
sub(5,1)
