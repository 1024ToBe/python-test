'''
需求:根据操作流程以及系统需求,完成面向对象版学生管理系统项目开发
a.可以显示基本的版本信息和操作界面;
b.可以通过键盘输入信息来完成基本功能,例如选择序号、确认退出、添加学生、修改信息等;
c.学生属性信息有姓名、性别、年龄、联系方式、描述信息等等;
d.使用系统可对学生信息进行添加、修改、删除、查询等操作年;
e.可以使用文件对学生信息进行加载、保存等;
f.可重复对学生进行增删查改操作,当确认退出系统后,则直直接退出系统;
g.请使用面向对象的编程思想完成项目的升级处理。
'''

from student_ms import StudentMS

def manage():
    print('=====欢迎进入黑马学生管理系统=====')
    stu_ms = StudentMS('student.txt')

    while True:
        num = stu_ms.print_info()
        if num == 1:
            stu_ms.add_info()
        elif num == 2:
            stu_ms.update_info()
        elif num == 3:
            stu_ms.del_info()
        elif num == 4:
            stu_ms.search_one()
        elif num == 5:
            stu_ms.search_all()
        elif num == 6:
            stu_ms.save('student.txt')
        elif num == 6:
            print('=====您已退出学生管理系统，欢迎下次光临=====')
            break
        else:
            print('=====输入错误，请重新输入=====')
            break


if __name__ == '__main__':
    manage()
