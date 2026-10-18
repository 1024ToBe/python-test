import multiprocessing as mp
import time
import os

def num_print(num):
    pid = os.getpid()
    ppid = os.getppid()
    print(f'当前进程的pid是{pid},ppid是:{ppid}')

    for i in range(1,num+1):
        print(f'{i}')
        time.sleep(1)
def name_print(num,name):
    pid = os.getpid()
    ppid = os.getppid()
    print(f'当前进程的pid是{pid},ppid是:{ppid}')

    for i in range(1,num+1):
        print(f'{i}+{name}')

if __name__ == '__main__':
    pid = os.getpid()
    ppid = os.getppid()
    print(f'主进程的pid是{pid},ppid是:{ppid}')

    process_numprint = mp.Process(target=num_print,name='打印数字',args=(1000,))
    process_namerint = mp.Process(target=name_print, name='打印名字',kwargs={'num':1000,'name':'李四'})

    process_numprint.start()
    process_namerint.start()