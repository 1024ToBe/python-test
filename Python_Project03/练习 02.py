class Person:
    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print(f'Hello, {self.name}!')


class Rectangle:
    def __init__(self,width: float,height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height


if __name__ == '__main__':
    rec = Rectangle(3,5)
    print('面积是：',rec.area())

