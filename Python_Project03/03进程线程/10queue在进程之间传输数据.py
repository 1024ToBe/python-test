'''
进程1,每隔1秒生成一个随机数
进程2,得到进程1生成的随机数,判断是奇数还是偶数输出
'''
import multiprocessing as mp
import queue
import time
import random

def w1(q):
    for _ in range(100):
        num = random.randint(1,1000)
        q.put(num)
        print(f'放入数据：{num}')
        time.sleep(1)


def w2(q):
    time.sleep(1)
    while True:
        num = q.get()
        if num % 2 == 0:
            print('偶数')
        else:
            print('奇数')


if __name__ == '__main__':
    #不报错方式1 添加 mp.set_start_method("fork")
    # mp.set_start_method("fork")  # Mac关键代码
    # 不是Python内置 queue包，而是用multiprocessing包内的Queue
    # q = mp.Queue(maxsize=1) #这样就可以保证w1放入一个数据，卡住， 然后等w2取完数据，W1才能放；放一取一；

    # mp.Process(target=w1, args=(q,)).start()
    # mp.Process(target=w2, args=(q,)).start()

    #方式2
    manager = mp.Manager()
    q = manager.Queue(maxsize=1)

    # ❌不要 mp.Process(...).start() 链式写法！
    p1 = mp.Process(target=w1, args=(q,))
    p2 = mp.Process(target=w2, args=(q,))
    p1.start()
    p2.start()

    # 等待两个子进程全部执行完毕
    p1.join()
    p2.join()
    # 所有子进程结束之后，再关闭manager
    manager.shutdown()
