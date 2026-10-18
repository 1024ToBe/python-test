import multiprocessing as mp
import time

def eat(num):
    for i in range(1,num+1):
        print(f'我吃第{i}次饭')
        time.sleep(1)

def sleep(num,sec):
    for i in range(1,num+1):
        print(f'我睡觉第{i}次')
        time.sleep(sec)


if __name__ == '__main__':
    #第一种传参：元组
    # process_eat = mp.Process(target=eat,name='吃饭程',args=(10,))
    # process_sleep = mp.Process(target=sleep, name='睡觉进程',args=(20,2))

    #第二种传参样式 字典
    process_eat = mp.Process(target=eat,name='吃饭程',kwargs={'num':10})
    process_sleep = mp.Process(target=sleep, name='睡觉进程',kwargs={'num':20,'sec':2})

    process_eat.start()                                                                                                                                                                                                                                                                                     
    process_sleep.start()
