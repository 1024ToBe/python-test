'''
1.有嵌套
2.内层引用外层变量(局部变量、形参)
3.外层返回内层函数
4.在内层函数内，对原有函数做功能增强(即提供不存在的能力)
5.被修饰函数在外部做为形参传入
用法：
def 外层(fn):				# fn被修饰函数传入
    def 内层():
        修饰代码
        fn()
        修饰代码
    return 内层

@外层函数
def 被修饰函数():
    ...
被修饰函数()
'''

def check(fn):#被修饰函数在外部做为形参传入
    def inner():   #1.有嵌套
        print('已经登录,可以评论了')
        fn()  #2.外层有使用内层变量 fn就是被装饰的函数本身
    return inner

def comment():
    print('可以开始评论了')
# comment()
#调用方法
comment = check(comment) #comment本质就是内层函数 inner
comment() #本质就是调用inner：先打印--再调用原来被修饰函数comment
