class Worker():
    def __init__(self,name,work_id):
        self.name = name
        self.work_id = work_id
        self.__salary = 0

    def __increamnt_salary(self,num):
        self.__salary+=num

    def __decrement_salary(self,num):
        self.__salary-=num

    def work_oneday(self):
        print('工作一天了')
        self.__increamnt_salary(1000)

    def work_late(self):
        print('工作迟到了')
        self.__decrement_salary(300)

    def get_salary(self):
        return self.__salary

worker = Worker('张三','1000')
print(f'{worker.name}当前的薪资是{worker.get_salary()}')
worker.work_oneday()
print(f'{worker.name}当前的薪资是{worker.get_salary()}')
worker.work_late()
print(f'{worker.name}当前的薪资是{worker.get_salary()}')

#类外无法访问私有变量
#worker.__salary
#类外无法访问私有方法
#worker.__decrement_salary
