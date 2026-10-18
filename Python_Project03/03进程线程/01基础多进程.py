#1.导入进程工具包
import multiprocessing
import time


def eat():
    for i in range(1000):
        print('吃吃吃')
        time.sleep(1)

def sleep():
    for i in range(100):
        print('睡睡睡')
        time.sleep(1)


#多进程代码需要写到 main 函数里面 用于区分子进程和主进程
if __name__ == '__main__':
    process_eat = multiprocessing.Process(
        group=None,  #group固定为None(Python官方预留的参数,以后可能)更新)
        target=eat,  #target目标,这个进程要执行什么代码,传入一个函数名
        name='吃货'    #给创建的这个进程起个名字
    )

    process_sleep = multiprocessing.Process(target=sleep,name='懒货')

    process_eat.start()   #创建此进程开始干活
    process_sleep.start() #创建此进程开始干活


#2.通过进程类 实例化进程 对象

#3.启动进程 执行任务