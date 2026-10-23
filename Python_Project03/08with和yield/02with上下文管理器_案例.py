'''
需求:写一个class类。类提供一个random_line()方法,调用向文件内追加随机内容
'''
import random
import time


class MyClass():
    def __init__(self,path):
        self.f = open(path,'a',encoding='UTF-8')

    def __enter__(self):           #上下文管理器，with 开始执行会调用
        print('即将开始工作')

    def __exit__(self, exc_type, exc_val, exc_tb):  #上下文管理器，with结束完毕会自动调用；即便运行出现异常，也会调用。
        print('退出，关闭文件')
        self.f.flush()
        self.f.close()
        print(f'exc_type={exc_type}')  #异常类型
        print(f'exc_val={exc_val}') #异常实例（异常对象，异常消息）
        print(f'exc_tb={exc_tb}') #异常追踪对象

    def random_line(self):
        lines = [
            'abc',
            'def',
            'qaz',
            '1234',
            '5678'
        ]
        num = random.randint(1,10)
        self.f.write(random.choice(lines))
        self.f.write('\n')

mc = MyClass('data.txt')
with mc:
    for _ in range(5):
        mc.random_line()
        time.sleep(1)


