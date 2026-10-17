#学生属性信息有姓名、性别、年龄、联系方式、描述信息等等;
class Student():
    def __init__(self,name,gender,age,phone,des):
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.des = des

    def __str__(self):
        return f"{self.name},{self.gender},{self.age},{self.phone},{self.des}"
        #return ','.join([self.name,self.gender,str(self.age),self.phone,self.des])


    def __repr__(self):
        return f"{self.name},{self.gender},{self.age},{self.phone},{self.des}"

    #方便后续写文件，传入字符串得到对象
    #静态方法，因为不依赖 self 和 cls
    @staticmethod
    def generate(stu_str:str):
        arr = stu_str.split(',')
        stu = Student(arr[0],arr[1],int(arr[2]),arr[3],arr[4])
        return stu

