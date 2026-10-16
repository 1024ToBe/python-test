import random
#command+p 可以查看形参类型
#random.randint()
#类型注解  传值类型错误也可以正常运行
#1.基础数据注解
var_1: int = 10
var_2: float = 2.0
var_3: bool = False
var_4: str = 'hello'
#2.类对象类型注解
class Student():
    pass
st: Student = Student()

#3.容器类型
lst: list = [10,True,30]
tp: tuple = (21,'hi',23)
se: set = {11,'你好',13}
st: str = 'hello'
dic: dict = {'name':'张三','age':'22'}

#4.同元素类型注解
lst1: list[int] = [10,20,30]
dic1: dict[str:int] = {'name':1,'age':2}

#5.在注释中写类型描述
num = 10  #type: int