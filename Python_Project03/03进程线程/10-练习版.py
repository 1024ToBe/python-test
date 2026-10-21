# 1.2个进程,进程1 负责向队列内每隔1秒放入一个随机数字
# 2.进程2从队列取出，*10之后打印

import multiprocessing as mp
import queue
import random
import time


def w1(q):
    for _ in range(10):
        num = random.randint(1, 1000)
        q.put(num)
        print(f'放入数字{num}')
        time.sleep(1)


def w2(q):
    time.sleep(1)
    while True:
        num = q.get()
        print(f'处理后的数字={num * 10}')


if __name__ == '__main__':
    mp.set_start_method("fork")  # Mac关键代码
    q = mp.Queue(maxsize=1)
    mp.Process(target=w1, args=(q,)).start()
    mp.Process(target=w2, args=(q,)).start()
