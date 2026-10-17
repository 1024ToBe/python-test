#多态：#一种行为，多种状态
#1.带继承关系
'''
class Animal:
    def speak(self):
        print("动物叫")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()

animal = Animal()
dog = Dog()
cat = Cat()

#根据传入参数不同，执行不同状态
make_noise(animal)
make_noise(dog)
make_noise(cat)

'''
'''
Python 是**鸭子类型**：不看类型，只要这个对象拥有这个方法，就能调用，不在乎它属于哪个类。
鸭子类型通俗解释：
如果一个东西，走起路像鸭子、叫起来像鸭子，那我们就把它当成鸭子。
不需要它必须继承鸭子类。

## 对比：Java / C++ 的多态
Java：必须**父类引用指向子类对象**，严格继承，类型检查严格。
Python：不需要强制继承！只要有同名方法，就支持多态。
'''

#多态：不带继承关系
class Cat:
    def speak(self):
        print("喵喵喵")

class Dog:
    def speak(self):
        print("汪汪汪")

# 定义统一的函数，接收任意对象，调用speak方法
def make_speak(animal):
    animal.speak()

# 同一个函数，传入不同对象，行为不一样
cat = Cat()
dog = Dog()
make_speak(cat)  # 喵喵喵
make_speak(dog)  # 汪汪汪