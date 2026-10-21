import threading
import  time

def eat(sec):
    print('开吃')
    time.sleep(sec)
    print('吃完了')

def sleep(sec,name):
    print('睡')
    time.sleep(sec)
    print(f'{name}睡够了')

#if __name__ == '__main__': # 多线程，不需要写if __name__ == '__main__':
t_eat = threading.Thread(target=eat,name='吃线程',args=(5,))
t_sleep = threading.Thread(target=sleep, name='睡线程',args=(7,'小王八'))
t_eat.start()
t_sleep.start()

    # 多进程： eat和sleep是可以并行（同时）的（真的是2个CPU核心可以同时跑）
    # 多线程：1个进程不管多少线程，只能同时用1个核心，所以eat和sleep是并发执行（交替） 1个 cpu 纳秒级交替执行线程，减少为所谓等待
