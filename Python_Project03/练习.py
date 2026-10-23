'''
9. 商品价格管理
商品价格管理：定义商品类
背景：
商店系统中需要管理商品价格。为了后续扩展库存、折扣活动等功能，先用类保存商品名称和单价，并提供方法计算打折后的价格。
题目：
定义一个 Product 类，要求：
1.构造方法接收 name 和 price 两个参数，并保存为实例属性。 (2分)
2.实现 get_discount_price(rate) 方法，返回打折后的价格，计算公式为 price * rate。 (3分)
3.实现 str() 方法，返回格式为：商品：图书，单价：50。 (3分)
4.在主程序中创建 Product("图书", 50) 对象，打印对象，并打印 8 折后的价格。 (2分)

【提交运行截图和代码】
'''
'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discount_price(self, rate):
        return self.price * rate

    def __str__(self):
        return f'商品：{self.name}，单价：{self.price}'


if __name__ == '__main__':
    pd = Product("图书", 50)
    print('商品信息：',pd)
    print(f'打折后的价格：{pd.get_discount_price(0.8)}')
'''

'''
10. 装饰器
函数执行统计：编写带参数返回值的装饰器
背景：
后台系统中很多函数都需要记录执行日志。如果每个函数里都手动写日志代码，会重复很多。可以使用装饰器统一增加日志功能，同时不影响原函数参数和返回值。
问题：
编写一个装饰器 log_func，要求：
1.函数执行前输出：开始执行。 (1分)
2.函数执行后输出：执行结束。(1分)
3.装饰器内部需要支持任意参数。(2分)
4.定义函数 add(a, b)，返回两个数的和。(3分)
5.使用装饰器装饰 add。(2分)
6.调用 add(10, 20) 并打印返回结果。(1分)
【提交运行截图和代码】

'''
def log_func(fn):
    def inner(*args,**kwargs):
        print('开始执行')
        r = fn(*args,**kwargs)
        print('执行结束')
        return r
    return inner

@log_func
def add(a,b):
    return a+b

r = add(10, 20)
print(f'运行结果：{r}')







