import multiprocessing as mp
import time


def w1():
    self_process = mp.current_process()
    for i in range(1, 11):
        print("w1:", i)
        time.sleep(1)
        #方式2（进程自杀）
        #**Mac + fork 模式**下，子进程内部拿到的进程对象，它内部的 `_popen` 属性是 `None`，直接调用 `.terminate()` 就会报这个 `NoneType` 错误。
        #self_process.terminate()

def w2():
    for i in range(100, 111):
        print("w2:", i)



if __name__ == '__main__':
    mp1 = mp.Process(target=w1, daemon=True)
    mp2 = mp.Process(target=w2, daemon=True)
    mp1.start()
    mp2.start()

    #1.主进程中杀死子进程
   #mp1.terminate()


    #mp1 和 mp2没有先后顺序，但可以确保一个进程结束再执行另一个进程
    mp1.join()  # 卡住，直到mp1子进程执行结束
    print("w1结束")
    mp1.join()  # 卡住，直到mp2子进程执行结束
    print("w2结束")

    print("主进程没代码啦")



