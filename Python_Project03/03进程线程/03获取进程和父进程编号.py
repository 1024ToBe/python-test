import multiprocessing as mp
import time
def num_print(num):
    process_numprint = mp.current_process()
    pid = process_numprint.pid
    name = process_numprint.name
    print(f'当前进程的pid是{pid},进程名字是:{name}')

    for i in range(1,num+1):
        print(f'{i}')
        time.sleep(1)
def name_print(num,name):
    process_namerint = mp.current_process()
    pid = process_namerint.pid
    name = process_namerint.name
    print(f'当前进程的pid是{pid},进程名字是:{name}')

    for i in range(1,num+1):
        print(f'{i}+{name}')

if __name__ == '__main__':
    process_main = mp.current_process()
    pid = process_main.pid
    name = process_main.name
    print(f'主进程的pid是{pid},进程名字是:{name}')

    process_numprint = mp.Process(target=num_print,name='打印数字',args=(10,))
    process_namerint = mp.Process(target=name_print, name='打印名字',kwargs={'num':10,'name':'李四'})

    process_numprint.start()
    process_namerint.start()