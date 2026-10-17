class Animal(object):
    color = '黄'
    def __init__(self):
        self.name = '二狗'
        self.__nickname = '傻狗'
    def __eat_fish(self):
        print('偷偷地说 我喜欢吃鱼 哈哈')

    def eat(self):
        print('吃东西')
    def sleep(self):
        print('睡觉')

class Dog(Animal):
    def work(self):
        print('看家护院')

class Cat(Animal):
    def work(self):
        print('被撸')


dog = Dog()
dog.work()
dog.eat()
dog.sleep()
print(f'我的名字：{dog.name}')
#我的昵称:{dog.__nickname}

cat = Cat()
cat.work()
#print('私有方法',dog.__eat_fish())
