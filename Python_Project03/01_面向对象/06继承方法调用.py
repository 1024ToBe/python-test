class Animal(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color
        print('Animal的初始化方法被调用了')

    def eat(self):
        print('吃东西')


class Dog(Animal):
    def __init__(self, name, color, age):
        self.age = age
        super().__init__(name, color)

dog = Dog("小黄", "黑", 11)
print(dog.name)
print(dog.color)
print(dog.age)


class Cat(Animal):
    pass

#会报错，因为继承Animal
#在MRO顺序下，创建了Dog类对象后，还要创建Animal类对象，但是没有给相应的name和color实参
#所以报错，报错就是说 没给实参
#cat = Cat()
cat = Cat('小黑','白色')

#子类和父类都有 init 方法


class A:
    def __init__(self, name):
        self.name = name
        print("A init")

class B(A):
    def __init__(self, name, age):
        print("B init")
        self.age = age
        super().__init__(name)

class C(B):
    def __init__(self, name, age):
        print("C init")
        super().__init__(name, age)

class Dog(C):
    def __init__(self, name, age):
        print("Dog init")
        super().__init__(name, age)

# print(Dog.__mro__)      Dog -> C -> B -> A -> object
dog1 = Dog("大黄", 11)
print(f'名字:{dog1.name},年龄:{dog1.age}')