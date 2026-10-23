import time
class MyClass:
    #实现了上下文协议方法的类，就可以用 with
    def __enter__(self):
        print('我进来了')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('我出去了')

with MyClass() as mc:
    print(mc)
    time.sleep(5)


