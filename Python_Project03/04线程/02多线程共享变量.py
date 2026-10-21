
import threading
import time

g_list = []

def w1():
    for i in range(10000):
        i+=1
        g_list.append(i)
        print('w1',g_list)
        time.sleep(1)

def w2():
    for i in range(1000,2000):
        i+=1
        g_list.append(i)
        print('w2',g_list)
        time.sleep(1)

threading.Thread(target=w1).start()
threading.Thread(target=w2).start()