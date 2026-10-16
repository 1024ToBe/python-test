#多态：一种行为，多种状态

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

