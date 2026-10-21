#Python线程没有提供terminate()、kill()的方法，如果要停止一个无限循环的线程，可以通过标志位执行。
"""
Python没有提供线程的terminate()方法
一般通过标志位完成
"""
import time
import threading

#标志位：决定是否执行子线程
# flag = True
#
# def work():
#     while flag:
#         print("我爱工作，工作使我强大，让我成为牛马!!!")
#         time.sleep(1)
#     print("work线程停止")

#方法2，通过设置TTL停止线程；TTL：Time To Live：剩余存活时间
# 1. 线程：作为计时器
# 2. 其它线程读取计时器的值，超时自我了结
time_counter = 0

def work():
    start_time = time.time()

    while True:
        print("我爱工作。")
        time.sleep(1)
        if time.time() - start_time > 5:
            print("工作结束回家睡觉")
            break

if __name__ == '__main__':

    t1 = threading.Thread(target=work)
    t1.start()

    # time.sleep(5)
    # print("公司黄了，你别干活了")
    # flag = False
