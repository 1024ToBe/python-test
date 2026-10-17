'''
类属性：基于类创建的全部对象共享的属性
类方法：基于类创建的全部对象共享的方法，方便与对类属性进行操作
class 类:
    name = "联想"			  # 类属性

1.在方法中，自动传入的是cls
2.类方法，需要在方法名上面带上@classmethod装饰器
3.cls 表示类本身
4.self表示基于这个类，创建出来的对象本身

    @classmethod
    def set_name(cls, newname):		# 类方法
        cls.name = newname

    def __init__(self):		# 成员方法
        self.age = 10		# 成员属性

    def say_hi(self):		# 成员方法
        print(...)

'''
'''
class Phone():
    brand = '联想'
    @classmethod
    def set_new_brand(cls,new_brand):
        cls.brand = new_brand

#修改类属性
Phone.set_new_brand('苹果')
print(Phone.brand)
'''

'''
静态方法
写一个方法，不需要self也不需要cls，要求写在类里面，可以用静态

方法名上带有@staticmethod关键字，表示这是个静态方法
方法形参中，不写self cls
class 类:
    @staticmethod
    def 方法():
        pass
'''
class TextFileService():
    def __init__(self,file_path):
        self.fr = open(file_path,'r',encoding='utf8')
        self.fw = open(file_path,'a',encoding='uft8')

    def write_oneline(self,context:str)->bool:
        try:
            self.fw.seek(0)
            self.fw.write(context + '\n')
            return True
        except Exception:
            return False

    def print_all(self)->str:
        self.fr.seek(0)
        print(self.fr.read())

    def read_all(self):
        self.fr.seek(0)
        return self.fr.read()

    @staticmethod
    def print_info():
        print("======欢迎使用黑马程序员文件服务======")
        print("======您可以使用如下方法：======")
        print("1. write_oneline,写入一行数据")
        print("2. print_all,打印全部信息")
        print("3. read_all,读取全部信息")
        print("======祝您用的爽歪歪======")
        print("BBBBBBBBBBBBBBBBBBBBBBBB")


def print_info():
    print("======欢迎使用黑马程序员文件服务======")
    print("======您可以使用如下方法：======")
    print("1. write_oneline,写入一行数据")
    print("2. print_all,打印全部信息")
    print("3. read_all,读取全部信息")
    print("======祝您用的爽歪歪======")
    print("AAAAAAAAAAAAAAAAAAAA")

#调用函数
print_info()

#调用静态方法
#唯一的作用就是：让使用者知道，这个方法和类有关
TextFileService.print_info()

class Person():
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('人不吃饭会噶')

    def sleep(self):
        print('人不睡觉会噶')




