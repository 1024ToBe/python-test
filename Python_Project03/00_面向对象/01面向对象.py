class Student:
   def __init__(self,name,age,address):
       self.name = name
       self.age = age
       self.address = address
   def __str__(self):
       return f'信息为：学生姓名：{self.name}，学生年龄：{self.age}，学生地址：{self.address}】'

st1 = Student('张三','20','北京')
st2 = Student('王丽','22','上海')

for i in range(10):
    print('当前录入第%d位学生信息 总共需要录入10位学生信息' %(i+1))
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    address = input('请输入学生地址：')
    st = Student(name,age,address)
    #print('学生%d信息录入完成， 信息为：【学生姓名：%s 学生年龄：%d 学生地址：%s】' %((i+1),name,age,address))
    print('学生%d信息录入完成， 信息为：' %(i + 1), str(st))

