#函数参数类型
'''
1. **位置参数**：调用按顺序传参；`func(10,20)`
2. **关键字参数**：调用指定参数名；`func(a=10,b=20)`
3. **默认参数**：定义时给默认值，可传可不传；`def func(a,b=0)`
4. **可变参数**
   - `*args`：接收任意多个位置参数，存元组
   - `**kwargs`：接收任意多个关键字参数，存字典
'''
def sum(a,b,c):
    print('求和之后=',a+b+c)
#1.位置参数
sum(10,20,10)
#2.关键字参数，位置可变
sum(b=30,a=20,c=35)
#2.1关键字参数+位置参数混用，位置参数必须在前，且匹配参数顺序
sum(30,b=10,c=10)


#3.默认参数
def sum(a,b,c=5):
    print('默认参求和之后=',a+b+c)
sum(10,20)#不传，用默认值 5
sum(10,20,30)#传了C，就覆盖默认值
#4.python 不能限制变量类型，只能警告
sum('1','a','c')

#可变参数
#① `*args` 接收**多个位置实参**，打包成元组
def func(*args):
    print('可变参数：',args)
func(1,3,5,7)

#`**kwargs` 接收**多个关键字实参**，打包成字典
def func(**kwargs):
    print(kwargs)

func(name="tom", age=18)

#参数位置:** 位置参数 → 默认参数 → *args → **kwargs**
def demo(a, b=10, *args, **kwargs):
    '''
    1. `a`：**必须传**（位置参数）
    2. `b=10`：可传可不传，不传就是 10
    3. `*args`：接收**额外位置实参**，打包成元组
    4. `**kwargs`：接收**额外关键字实参（key=value）**，打包成字典
    '''
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)
    print("-" * 30)
#写法1：只传 a
demo(100)
#写法2：给 a、b 都传值
demo(100,200)
#写法3：a,b 之后，再加多个位置参数 → 进 args
demo(100, 200, 300, 400, 500)
#写法 4：a,b,args，再加关键字参数 → 进 kwargs
demo(100, 200, 300, 400, name="张三", age=20)
#写法 5：也可以用关键字传 a 和 b
#demo(a=66, b=88, 99) # ❌报错！关键字参数后面不能跟裸位置参数
#demo(66, b=88, 99)  # ✅正确
demo(5, 6, 7, 8, city="liaocheng")


#类型提示
def sum (a:int,b:int)->int:
    print(a+b)
sum(10,11)
