'''
项目工程路径下有一个python.txt的文件，
请读取其中内容，并打印文件中的每一行数据。

'''

with open('python.txt','r',encoding='utf8') as file_in:
    for line in file_in:
        print(line)

'''
请编写一个函数 print_info，接受以下参数：

name：表示一个人的姓名（必须）
age：表示一个人的年龄（必须）
city：表示一个人所在的城市（可选，默认值为 "未知"）
gender：表示一个人的性别（可选，默认值为 "未知"）
函数内部根据提供的参数打印人物信息，输出格式如下：
姓名：xxx
年龄：xxx
城市：xxx
性别：xxx
'''

def print_info(name,age,city='未知',gender='未知'):
    print(f'姓名：{name}')
    print(f'年龄：{age}')
    print(f'城市：{city}')
    print(f'性别：{gender}')
print_info('张三','18','北京','男')
print('=================================')
print_info('李四','19')

'''
写一个 lambda 表达式，用于将字符串列表中的字符串都转换为大写
'''
def f1(str):
    str1 = str.upper()
    print(str1)
f1('qazwsx')


print((lambda str: str.upper()) ('abcdefg'))

'''
11. 异常捕获
请编写一个程序，接受用户输入一个整数，并进行相应的处理。

首先，程序需要提示用户输入一个整数。
然后，程序尝试将用户输入的内容转换为整数类型，并计算它的平方。
如果用户输入的内容无法转换为整数类型，程序将捕获异常，并输出错误信息："输入无效，请输入一个有效的整数！"。
否则，在else逻辑块中将程序输出计算得到的平方结果。
'''

# def js():
#     str = input('请输入一个整数：')
#     try:
#         num = int(str)
#     except:
#         print('输入无效，请输入一个有效的整数！')
#     else:
#         print('你输入的数字平方=',num**2)
#
# js()

'''
我们需要统计一个源文本文件中每个单词出现的次数，并将结果写入另一个目标文件。
源文件python.txt内容如下：
'''

def jswords():
    with open('input.txt','r',encoding='utf8') as file_in,open('output.txt','w',encoding='utf8') as file_out:
        str = file_in.read().replace('\n', ' ')
        l1 = str.split(' ')
        dict = {}
        print(str,str,l1)
        for ch in l1:
            if ch == ' ' or ch == '':
                continue
            else:
                if ch in dict:
                    dict[ch] += 1
                else:
                    dict[ch] = 1
        print(dict)

        for k, v in dict.items():
            file_out.write(f"{k}:{v}\n")

jswords()

'''
13. 题干
定义函数findall，要求返回符合要求的所有位置的起始下标，
如字符串"helloworldhellopythonhelloc++hellojava"
需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)
'''

def findall(main_str,sub_str):
    index_list = []
    start = 0
    while True:
        pos = main_str.find(sub_str,start)
        if pos == -1:
            break
        index_list.append(pos)
        start = pos + len(sub_str)
    return tuple(index_list)

str = 'helloworldhellopythonhelloc++hellojava'
res = findall(str,'hello')
print(res)

