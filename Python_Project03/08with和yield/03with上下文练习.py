'''
实现1个类,内容随意,要求支持对类对象使用with
要求,with语句开始执行,自动输出开始
with语句结束,自动输出结束
with语句内部代码随意,比如print一些东西
'''
import time
class MyClass():
    def __enter__(self):
        print('开始')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('结束')

#
# mc = MyClass()
with MyClass() as mc:   #取自于enter函数的返回值，enter中没有 return self，则无法使用 with as
    print('开始执行 with 语句')
    time.sleep(3)

