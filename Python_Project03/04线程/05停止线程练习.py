#写1个线程,无限循环每隔1秒输出信息(内容随意),要求,主线程内无限循环得到随机数,如果随机数是5,则停止线程
import threading
import time
import random

flag = True
def work():
    while flag:
        print('不受坏情绪影响')
        time.sleep(1)
    print('坏情绪消失了')


if __name__ == '__main__':
    threading.Thread(target=work).start()

    while True:
        num = random.randint(1, 100)
        print(f'num=={num}')
        if num == 5:
            flag = False
            print('该结束了')
            break
        time.sleep(0.5)





