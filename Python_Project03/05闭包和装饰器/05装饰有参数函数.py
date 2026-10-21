'''
def 外层(fn):		   # fn被修饰函数传入
    def 内层(形参): 	   # 内层的传入参数，用于被修饰函数
        修饰代码
        fn(形参)
        修饰代码
    return 内层
'''
def print_info(fn):
    def inner(x,y):
        print('开始装饰')
        fn(x,y)
        print('装饰完成')
    return inner

@print_info  #add函数此时就=inner函数了
def add(x,y):
    print(f'x+y={x+y}')

add(3,5) #若函数inner没写参数会报错错误，因为此时add=inner函数，函数inner没办法接参数