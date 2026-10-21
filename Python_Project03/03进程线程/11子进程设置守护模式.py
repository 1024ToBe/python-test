import multiprocessing as mp
import time


def w1():
    for i in range(1, 11):
        print("w1:", i)
        time.sleep(1)


def w2():
    for i in range(100, 111):
        print("w2:", i)
        time.sleep(1)


if __name__ == '__main__':
    '''
    主进程现在没代码了，没事干了。
    w1: 6
    w1: 7
    w1: 8
    w1: 9
    w1: 10
    '''
    # mp.Process(target=w1).start() #即便主线程结束了 子线程没干完 还继续干


    mp.Process(target=w1, daemon=True).start() #主线程结束 子线程就陪葬一块儿结束
    mp.Process(target=w2, daemon=True).start()
    '''
    w1: 3
    w2: 102
    w2: w1:103 
    4
    w2: 104
    w1: 5
    主进程现在没代码了，没事干了。
    '''

    time.sleep(5)
    print("主进程现在没代码了，没事干了。")


