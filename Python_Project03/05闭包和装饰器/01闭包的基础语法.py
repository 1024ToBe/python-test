'''
1.函数有嵌套（外层函数内写内层函数）
2.内层函数使用外层函数的局部变量（形参、定义好的）
3.外层函数要返回内层函数本身

'''

#Global：函数内部修改全局变量
#nonlocal：内层函数修改外层函数局部变量

def outer():
    num = 100  #外层函数的局部变量

    def inner(): #1.有嵌套函数-内层函数
        nonlocal num  #2.内层用外层的变量 内层函数想要改变外层函数变量，必须加nonlocal修饰
        num+=1
        print(num)

    return inner #3.外层函数返回内层函数本身

#这里执行完，out函数就出栈，被销毁了
f1 = outer()
f2 = outer()

#f1、f2是变量，本身就是inner函数。因为inner函数调用了变量num，f1、f2把num 的值要保存下来。放在__closure__闭包列表里
f1() #101
f1() #102
f2() #101
f1()

# num = f1.__closure__[0].cell_contents
print('单独取出闭包变量',f1.__closure__[0].cell_contents)

