'''
# 1. 2个线程，线程1对共享变量num += 1   +10000次
# 2. 线程2同样num += 1   + 10000次
# 3. num起始是0
#
# 等待2个线程执行完成后，输出num的最终值（等待线程执行完成，使用线程对象.join()）
'''

import threading
import time
num = 0
count = 10000000
lock = threading.Lock()

def w1():
    global num
    for _ in range(100000):
        lock.acquire() #加锁
        num+=1
        lock.release() #解锁

def w2():
    lock.acquire()  # 加锁
    global num
    for _ in range(100000):
        num+=1
    lock.release()  # 解锁


t1 = threading.Thread(target=w1)
t2 = threading.Thread(target=w2)

t1.start()
t2.start()

# 等待线程执行完成
t1.join()
t2.join()
print(f'最终结果{num}')