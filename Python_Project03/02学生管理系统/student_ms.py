from student import Student
class StudentMS():
    def __init__(self,file_path):
        #用于存储学生信息{'张三'：男，18，132，学习好}{'张三'：男，18，132，学习好}
        self.data_dic = {}
        #1.读取学生内容的文件存储到data_dic
        with open(file_path,'r', encoding='utf8') as fr:
            all_line = fr.readlines()
            for line in all_line:
                # 去掉空格和换行符
                line = line.strip()

                stu = Student.generate(line)
                self.data_dic[stu.name] = stu
        # try:
        #     self.fr = open(file_path, 'r', encoding='utf8')
        # except Exception as e:
        #     print('文件读取失败，原因：', e)


    def read_info(self):
        pass

    def add_info(self):
        print('=====准备添加学生信息=====')
        name = input('请输入学生姓名：')

        #判断学生信息是否已存在
        if name in self.data_dic:
            print(f'学生{name}信息已添加过,若继续添加会覆盖信息，是否继续')
            is_continue = input('继续请输入y， 否则请输入其他信息：')
            if is_continue !='y':
                return None

        gender = input('请输入学生性别：')
        age = int(input('请输入学生年龄：'))
        phone = input('输入学生联系方式：')
        des = input('请输入学生其他信息：')
        stu = Student(name, gender, age, phone, des)

        #将学生信息添加到数据字典中
        self.data_dic[name] = stu
        print(f'学生{name}信息添加完毕')

    def update_info(self):
        print('=====准备修改学生信息======')
        name = input('请输入要修改的学生姓名：')
        stu = self.data_dic[name]
        if name not in self.data_dic:
            print(f'学生{name}信息不存在')
            return None

        print('1.修改学生性别')
        print('2:修改学生年龄')
        print('3:修改学生联系方式')
        print('4:修改学生其它信息')

        num = int(input('请输入对应数字：'))
        if num == 1:
          gender = input('请输入新的性别：')
          stu.gender = gender
        elif num == 2:
          age = int(input('请输入新的年龄：'))
          stu.age = age
        elif num == 3:
          phone = input('请输入新的联系方式：')
          stu.phone = phone
        else:
            des = input('请输入新的其它信息：')
            stu.des = des

        print(f'学生{name}信息修改成功')


    def del_info(self):
        print('=====准备删除学生信息======')
        name = input('请输入要删除的学生姓名：')
        if name not in self.data_dic:
            print(f'学生{name}信息不存在')
            return None

        del self.data_dic[name]
        print(f'学生{name}信息删除成功')

    def search_one(self):
        print('=====准备查询学生信息======')
        name = input('请输入你要查询的学生姓名：')
        if name not in self.data_dic:
            print(f'学生{name}不存在')
        else:
            print(f'学生{name}信息：{self.data_dic[name]}')


    def search_all(self):
        print('=====准备查询所有学生信息======')
        print(self.data_dic)

    def save(self,file_path):
        with open(file_path,'w',encoding='utf8') as fw:
            for name,stu in self.data_dic.items():
                fw.write(str(stu))
                fw.write('\n')
            #print(f"保存完成，本次保存{len(self.data_dic)}条学生信息")

    @staticmethod #必须缩进和def同级，不然报错
    def print_info() ->int:
        print('=====以下是你可选择的操作类型=====')
        print('1.增加学生信息')
        print('2:修改学生信息')
        print('3:删除学生联系方式')
        print('4:查看学生其它信息')
        print('5:查询所有学生其它信息')
        print('6:存储学生信息到文件')
        print('7:退出系统')

        num = int(input('请输入对应数字：'))
        return num

if __name__ == '__main__':
    # stu_ms = StudentMS('student.txt')
    # stu_ms.save('student.txt')

    StudentMS.print_info()











