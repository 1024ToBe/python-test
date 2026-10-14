#1
'''
def fun(*args,**kwargs):
    total = 0
    for i in args:
        total+=i

    for v in  kwargs.values():
        total+=int(v)
    return total
total = fun(*[1,2,3],**{"张三":18,'李四':'20','王五':25})
print('总和==',total)
'''

#2
'''
import  random
def fun1(s):
    code = ''
    for i in range(4):
        ch = random.choice(s)
        code+=ch
    print('随机码:', code)
    return code
str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
fun1(str)
'''

#3
'''
def func3(word):
    if word.isupper() or word.islower() or word.istitle():
        print('true')
    else:
        print('false')

func3('USA')
func3('FlaG')
func3('Google')
func3('Hello World')
'''

#4
'''
def fun4(s):
    if s.count('A')<2 and 'LLL' not in s:
        print('true')
    else:
        print('false')
fun4('PPALLP')
fun4('PPALLL')
fun4('AAPPP')
'''

#5
'''
def fun5(words):
    line1 = 'qwertyuiop'
    line2 = 'asdfghjkl'
    line3 = 'zxcvbnm'
    lst = []
    for word in words:
        group1 = False
        group2 = False
        group3 = False
        for ch in word.lower():
            if ch in line1:
                group1 = True
            elif ch in line2:
                group2 = True
            else:
                group3 = True
        total = group1 + group2 + group3
        if total == 1:
            lst.append(word)
    print(lst)


fun5(["Hello","Alaska","Dad","Peace"])
fun5(["omk"])
fun5(["adsdf",'sfd'])
'''

#6
book_list = []

def add_info():
    book_id = len(book_list) + 1
    book_name = input('请输入书籍名称：')
    price_input = float(input('请输入书籍价格：'))
    if price_input == '':
        book_price = 0.0
    else:
        book_price = float(price_input)

    rent_input = bool(input('是否已出租？是输入True，否输入False，回车默认否：'))
    if rent_input == '':
        book_rent = False
    else:
        book_rent = bool(rent_input)
    book_info = {
        "编号": book_id,
        "书名": book_name,
        "价格": book_price,
        "出租状态": book_rent
    }
    book_list.append(book_info)
    print('书籍信息',book_info)
#add_info()

def delete_info():
    del_id = int(input("请输入要删除书籍的编号："))
    find = False
    for book in book_list:
        if book['编号'] == del_id:
            book_list.remove(book)
            find = True
            print(f"编号{del_id}的书籍删除成功！")
            break
        if not find:
            print(f"没有找到编号为{del_id}的书籍，删除失败！")

# delete_info()
# print('删除后图书信息', book_list)

def update_info():
    update_id = int(input("请输入要修改书籍的编号："))
    target_book = None
    for book in book_list:
        if book['编号'] == update_id:
            target_book = book
            break
        if target_book is None:
            print(f"未找到编号{update_id}的书籍，修改失败！")


    print('请输入你要修改的字段：')
    print("1. 书名")
    print("2. 价格")
    print("3. 书籍出租状态")
    choice = input("输入序号(1/2/3): ")

    if choice == '1':
        new_name = input('请输入新的书名：')
        target_book['书名'] = new_name
        print('书名修改完成！')
    elif choice == '2':
        new_price = float(input("请输入新的价格："))
        target_book['价格'] = new_price
        print("价格修改完成！")
    elif choice == '3':
        new_price = bool(input("请输入新的出租状态："))
        target_book['出租状态'] = new_price
        print("出租状态修改完成！")
    else:
        print("输入序号错误！")
# update_info()
# print('书籍信息',book_list)

def search_info():
    find_name = input("请输入要查询的书籍名称：")

    if len(book_list) == 0:
        print("暂无任何书籍信息！")
        return

    find = False
    for book in book_list:
        if book['书名'] == find_name:
            print("====书籍信息====")
            print("书籍编号：%d" % book["编号"])
            print("书籍名称：%s" % book["书名"])
            print("书籍价格：%.2f" % book["价格"])
            print("出租状态：%s" % book["出租状态"])
            find = True
            break
    if not find:
        print("没有找到该书籍！")

# search_info()
# print('书籍信息',book_list)


def search_all():
    if len(book_list) == 0:
        print("暂无任何书籍信息！")
        return

    print("====所有书籍信息====")
    for book in book_list:
        print("书籍编号：%d，书名：%s，价格：%.2f，出租状态：%s"
              % (book["编号"], book["书名"], book["价格"], book["出租状态"]))

# search_all()
# print('书籍信息',book_list)

def print_info():
    print("\n========图书管理系统========")
    print("输入1:  添加书籍(书籍编号,  书籍名，书籍价格，书籍出租状态【是/否】).")
    print("输入2: 删除书籍(根据编号删除，删除时，需要判断书籍出租状态，如果书籍未出租，则删除书籍；如果书籍已出租，则打印“书籍已出租，暂无法删除”)")
    print("输入3: 修改书籍信息(只能改书籍名，书籍出租状态)")
    print("输入4: 查询单个书籍信息(根据书籍名查)")
    print("输入5: 查询所有书籍信息")
    print("输入6: 退出系统")
    print("============================")


def login():
    user_name = 'admin'
    pwd = '123456'
    for i in range(3):
        username = input("请输入管理员账号：")
        password = input("请输入管理员密码：")
        if username == user_name and password == pwd:
            print("登录成功！")
            return True
        else:
            print("账号或密码错误，请重试")

    # 循环结束，3次全部失败
    print("错误次数达上限")
    return False

def read_book():
    with open('book.txt','r',encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            name,price_str,rent_str = line.split('，')
            book_name = str(name)
            price = float(price_str)
            rent = bool(rent_str)
            book_id = len(book_list)+1
            book_dict = {
                "编号": book_id,
                "书名": book_name,
                "价格": price,
                "出租状态": rent
            }
            book_list.append(book_dict)
print("文件读取完成！")

# read_book()
# print('书籍信息',book_list)

def main():
    # 启动读取文件
    read_book()
    # 登录校验
    ret = login()
    if not ret:
        return
    while True:
        print_info()
        op = input("请输入1-6的数字选择操作：")
        if op == "1":
            add_info()
        elif op == "2":
            delete_info()
        elif op == "3":
            update_info()
        elif op == "4":
            search_info()
        elif op == "5":
            search_all()
        elif op == "6":
            print("退出系统，程序结束！")
            break
        else:
            #非法输入处理
            print("输入非法！请输入1~6之间的数字！")


if __name__ == '__main__':
    main()