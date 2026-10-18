import multiprocessing as mp
import time
def num_print(num):
    for i in range(1,num+1):
        print(f'{i}')
        time.sleep(1)
def name_print(num,name):
    for i in range(1,num+1):
        print(f'{i}+{name}')

if __name__ == '__main__':
    process_numprint = mp.Process(target=num_print,name='打印数字',args=(10,))
    process_namerint = mp.Process(target=name_print, name='打印名字',kwargs={'num':10,'name':'李四'})

    process_numprint.start()
    process_namerint.start()