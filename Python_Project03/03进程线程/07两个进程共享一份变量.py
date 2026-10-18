import multiprocessing as mp
mp.set_start_method('fork', force=True)

import time

def increment(num):
    for i in range(100):
        num.value -= 1
        print('list1:',num.value)
        time.sleep(1)

def print1(num):
    for _ in range(100):
        print('list2:',num.value)
        time.sleep(2)

if __name__ == '__main__':
    num = mp.Value('i', 100) #i:int, f:float d:double b:bool
    #两个进程各自独享一份新的data_list数据
    mp.Process(target=increment,args=(num,)).start()
    mp.Process(target=print1,args=(num,)).start()




