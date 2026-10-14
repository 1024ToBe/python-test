'''
6. 图书租借管理系统
项目背景：
你是云飞软件科技有限公司的一名AI开发工程师，现在公司要为蓝天社区的图书馆开发一个图书管理系统。
蓝天社区图书馆需要数字化管理其图书租借业务，蓝天社区的图书馆现在的图书管理方式均为纸质记录方式，该方式效率低下且容易出错。
为此，需要开发一个图书租借管理系统，帮助图书管理员高效管理馆藏图书和租借业务。现在公司把部分开发任务分配给了你。
开发需求如下：

'''

'''
1、自定义函数 add_info()
功能: 添加书籍，让用户输入要添加的书籍的书名、价格，书籍出租状态，并将这本书的信息添加到存储图书信息的列表中。
注意事项：
编号：设置为int类型，编号必须唯一；
书名：设置为str类型；
价格：设置为float类型，默认为0；
书籍出租状态：设置为bool类型，默认为【否】。
'''
#1.添加书籍
# 存储图书的列表
book_list = []
def add_info():
    # 生成唯一编号：列表现有数量+1，int类型
    book_id = len(book_list) + 1
    # 用户输入书名
    book_name = input("请输入书籍书名：")
    # 输入价格，默认0
    price_input = input("请输入书籍价格（回车默认为0）：")
    if price_input == "":
        price = 0.0
    else:
        price = float(price_input)
    # 输入出租状态，默认False（否）
    rent_input = input("是否已出租？是输入True，否输入False，回车默认否：")
    if rent_input == "":
        rent_status = False
    else:
        rent_status = bool(rent_input)
    # 组装单本书籍信息字典
    book_info = {
        "编号": book_id,
        "书名": book_name,
        "价格": price,
        "出租状态": rent_status
    }
    # 添加到列表
    book_list.append(book_info)
    print("书籍添加成功！")


'''
2、自定义函数 delete_info()。
功能: 根据编号删除书籍。
让用户输入要删除的书籍的编号，并根据编号从存储图书信息的列表中，删除这本书。
'''
#2.按编号删除书籍
def delete_info():
    # 用户输入要删除的编号
    del_id = int(input("请输入要删除书籍的编号："))
    # 标记是否找到
    find_flag = False
    for book in book_list:
        if book["编号"] == del_id:
            book_list.remove(book)
            find_flag = True
            print(f"编号{del_id}的书籍删除成功！")
            break
    if not find_flag:
        print(f"没有找到编号为{del_id}的书籍，删除失败！")




'''
3、自定义函数 update_info()。
功能: 修改书籍信息。让用户输入要修改的书籍的编号，
再让用户选择要修改的字段，并输入修改的信息，然后根据编号从存储图书信息的列表中修改这本书的信息。
注意事项：
根据编号修改, 只能修改: 书籍名，价格，书籍出租状态.
'''
#3.按编号修改书籍
def update_info():
    # 输入要修改的图书编号
    edit_id = int(input("请输入要修改书籍的编号："))
    # 查找这本书
    target_book = None
    for book in book_list:
        if book["编号"] == edit_id:
            target_book = book
            break
    # 判断有没有找到
    if target_book is None:
        print(f"未找到编号{edit_id}的书籍，修改失败！")
        return

    # 选择要修改的字段，只能修改 书名/价格/出租状态
    print("请选择要修改的字段：")
    print("1. 书名")
    print("2. 价格")
    print("3. 书籍出租状态")
    choice = input("输入序号(1/2/3): ")

    if choice == "1":
        new_name = input("请输入新的书名：")
        target_book["书名"] = new_name
        print("书名修改完成！")
    elif choice == "2":
        new_price = float(input("请输入新的价格："))
        target_book["价格"] = new_price
        print("价格修改完成！")
    elif choice == "3":
        new_rent = bool(input("请输入出租状态（True/False）："))
        target_book["出租状态"] = new_rent
        print("出租状态修改完成！")
    else:
        print("输入序号错误！")

'''
4、自定义函数 search_info()。
功能: 查询某个书籍信息.
注意事项: 根据书籍名查询，使用占位符格式化输出书籍信息
'''
#4.查询书籍
def search_info():
    # 用户输入要查询的书名
    search_name = input("请输入要查询的书籍名称：")
    find_flag = False
    for book in book_list:
        if book["书名"] == search_name:
            # 使用 % 占位符格式化输出
            print("====书籍信息====")
            print("书籍编号：%d" % book["编号"])
            print("书籍名称：%s" % book["书名"])
            print("书籍价格：%.2f" % book["价格"])
            print("出租状态：%s" % book["出租状态"])
            find_flag = True
            break
    if not find_flag:
        print("没有找到该书籍！")

'''
5、自定义函数 search_all()。
功能: 查询所有书籍的信息，并使用占位符格式化分别输出每一本书的书籍信息。
'''
#5.查询所有书籍
def search_all():
    # 判断列表是否为空
    if len(book_list) == 0:
        print("暂无任何书籍信息！")
        return
    print("====所有书籍信息====")
    # 循环遍历每一本书，%占位符输出
    for book in book_list:
        print("书籍编号：%d，书名：%s，价格：%.2f，出租状态：%s"
              % (book["编号"], book["书名"], book["价格"], book["出租状态"]))


'''
6、定义函数 print_info() ，打印提示信息。
功能：打印提示界面(1-6的数字)，以及1-6个数字分别代表的操作，如下：
①输入1:  添加书籍(书籍编号,  书籍名，书籍价格，书籍出租状态【是/否】).
②输入2: 删除书籍(根据编号删除）
【删除时，需要判断书籍出租状态，如果书籍未出租，则删除书籍；如果书籍已出租，则打印“书籍已出租，暂无法删除”】)
③输入3: 修改书籍信息(只能改书籍名，书籍出租状态)
④当管理员选择4的时候, 实现操作: 查询单个书籍信息(根据书籍名查)
⑤输入5: 查询所有书籍信息
⑥输入6: 退出系统
'''
#6.打印提示信息
def print_info():
    print("\n========图书管理系统========")
    print("输入1:  添加书籍(书籍编号,  书籍名，书籍价格，书籍出租状态【是/否】).")
    print("输入2: 删除书籍(根据编号删除，删除时，需要判断书籍出租状态，如果书籍未出租，则删除书籍；如果书籍已出租，则打印“书籍已出租，暂无法删除”)")
    print("输入3: 修改书籍信息(只能改书籍名，书籍出租状态)")
    print("输入4: 查询单个书籍信息(根据书籍名查)")
    print("输入5: 查询所有书籍信息")
    print("输入6: 退出系统")
    print("============================")

'''

7、打印提示界面, 让管理员登录账号和密码。
功能:自定义for循环, 让用户输入用户名和密码，并验证输入是否正确。
注意事项：
如果账号密码正确，打印“登陆成功！”
如果账号密码错误，打印“账号或密码错误，请重试”
三次机会，三次都登录失败，提示【错误次数达上限】，并退出系统.
'''
#7.登录
def login():
    # 预设正确账号密码
    user_name = "admin"
    pwd = "123456"
    # for循环，总共3次机会
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

#8.读取书籍
'''
功能:文件“book.txt”中存储的是现有图书的信息，
书籍信息包括【书名，价格，书籍出租状态(是否已经出租)】。
读取文件中图书信息，并使用列表(list)存放所有书籍，
每本书都用一个字典(dict)来存储书籍信息。
'''
def read_book():
    global book_list
    book_list = []
    # with打开book.txt，r读取
    with open("book.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
    # 遍历每一行，生成书籍字典
    for line in lines:
        line = line.strip()  # 去掉换行、空格
        if not line:
            continue
        # 分割：书名，价格，出租状态
        name, price_str, rent_str = line.split(",")
        book_name = str(name)
        price = float(price_str)
        # 字符串转布尔
        rent_status = rent_str.strip() == "True"
        # 自动生成唯一编号
        book_id = len(book_list) + 1
        book_dict = {
            "编号": book_id,
            "书名": book_name,
            "价格": price,
            "出租状态": rent_status
        }
        book_list.append(book_dict)
    print("文件读取完成！")

'''
9、自定义while True循环逻辑， 实现用户录入什么选项, 就进行相应的操作
9.1、 调用函数print_info()， 打印提示界面(1-6的数字)。
9.2 、使用输入函数，提示让管理员输入1-6的数字，选择他/她要进行的操作【注意事项: 处理一下非法值】。
①当管理员选择1的时候, 调用 add_info()函数，实现添加书籍。
②当管理员选择2的时候, 调用 delete_info() 函数，实现删除书籍。
③当管理员选择3的时候, 调用 update_info() 函数，实现修改书籍信息。
④当管理员选择4的时候, 调用 search_info() 函数，实现 查询单个书籍信息。
⑤当管理员选择5的时候, 调用 search_all() 函数，实现查询所有书籍信息。
⑥当管理员选择6的时候, 退出循环，结束程序。）
'''
#9、主函数 while True循环菜单
def main():
    #启动读取文件
    read_book()
    #登录校验
    ret = login()
    if not ret:
        return

    #9.1 +9.2 while循环主菜单
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

