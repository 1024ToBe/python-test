age = 22
if age >= 18:
    print('我成年了')
    print('我可以去上大学了')

age1 = input('请输入你的年龄:')
if int(age1) >= 18:
    print('我成年了哦')
else:
    print('我还小')

#账密
name = '张三'
pwd = '123456'
name_input = input('请输入你的用户名:')
pwd_input = input('请输入你的密码：')
if name_input == name and pwd_input == pwd:
    print('登录成功')
else:
    print('登录失败')

# 学习等级  if - elif -else
score = int(input('请输入你的成绩'))
if 90 < score <= 100:
    print('学习等级为优')
elif 80 < score <= 90:
    print('学习等级为良')
elif 70 < score <= 80:
    print('学习合格')
else:
    print('不合格')

#嵌套if
