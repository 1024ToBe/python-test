#继承的传承
class Animal(object):
    def eat(self):
        print('吃东西')


class Person(Animal):
    def sleep(self):
        print('睡觉')

class Worker(object):
    def work(self):
        print('工作')

class Student(Worker):
    def study(self):
        print('学习')

# st = Student()
# st.eat()
# st.sleep()
# st.work()
# st.study()

'''
==============================================================
多继承：一个类可以继承多个父类
'''
#如果Me同时继承Person 和 Worker，而Worker又继承 Person，继承顺序冲突！
#class Me(Person,Worker):
class Me(Animal, Worker):
    def test(self):
        #子类调用父类方法 要在子类方法中调用
        #1 super().父类方法
        super().eat()
        # 2 父类.父类方法
        Worker.work(self)
        print('搞钱')

me = Me()
me.test()

class Parent(Animal,Worker):
    pass
## MRO

#全称：Method Resolution Order
#中文：方法解析顺序；方法查找排队表，从左向右挨个找
#Parent → Animal → Worker → object
print(Parent.__mro__)

