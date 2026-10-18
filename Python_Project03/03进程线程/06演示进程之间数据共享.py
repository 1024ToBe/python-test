import multiprocessing as mp
import time

data_list = []
def increment():
    for i in range(10):
        data_list.append(i)
        print('list1:',data_list)
        time.sleep(1)

def print1():
    for _ in range(10):
        print('list2:',data_list)

if __name__ == '__main__':
    #两个进程各自独享一份新的data_list数据
    mp.Process(target=increment).start()
    mp.Process(target=print1).start()
