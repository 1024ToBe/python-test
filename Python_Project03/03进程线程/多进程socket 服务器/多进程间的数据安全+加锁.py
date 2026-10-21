import multiprocessing as mp
from multiprocessing.synchronize import Lock
import time
#im

def w1(v: mp.Value,lock: Lock):
    for _ in range(10000):
        lock.acquire() #上锁
        v.value+=1
        lock.release() #解锁

def w2(v: mp.Value,lock: Lock):
    for _ in range(10000):
        lock.acquire()  # 上锁
        v.value+=1
        lock.release()  # 解锁

if __name__ == '__main__':
    v = mp.Value('i',0)

    #解决方法 1：加锁
    lock = mp.Lock()

    w1_process = mp.Process(target=w1,args=(v,lock))
    w2_process = mp.Process(target=w1, args=(v,lock))

    s = time.time()
    w1_process.start()
    w2_process.start()

    #等待(join）这两个进程结束,运行不结束就卡在这里
    w1_process.join()
    w2_process.join()

    e = time.time()
    # 2个子进程结束，下面代码才会执行
    print(f"期望：20000")
    print(f"实际：{v.value}") #10040
    print(f"耗时：{e - s}")

