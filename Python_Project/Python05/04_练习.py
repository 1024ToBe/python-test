#1.交换
a = 10
b = 20
#传统
c = a
a = b
b = c
print(a,b)
#打包
a,b = 10,20
a,b = b,a
print(a,b)

"""
7. 列表读取
班级中有 3 名学生，需要把他们的姓名保存起来并输出。
要求：

使用列表保存姓名：'张三'、'李四'、'王五'
使用 for 循环逐个输出姓名
"""
name = ['张三','李四','王五']
for i in name:
    print('学生姓名：',i)


#1.单行注释
print('#:代表单行注释')

"""
2.1 3个双引号
多行注释
"""
print('首尾""":代表单行注释')

'''
2.2 3个单引号
多行注释
'''
print('首尾\'\'\':代表单行注释')

a = 1
print(type(a))

b = 1.1
print(type(b))

c = True
print(type(c))

d = '12345'
print(type(d))

# float(x)没有学过，动动你的小手，打开百度，自己查一查这个知识点，锻炼一下动手能力。
e = float(d)
print(type(e))

"""
9. 字符串遍历
要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则终止循环。
"""
# str = input('请输入一个随机字符串:')
# for s in str:
#     if s=='q':
#         break
#     else:
#         print(s)

"""
10. 题干
假设我们有一个存储商品价格的列表 prices，每个元素代表一个商品的价格。现在需要完成以下任务：

将价格列表按升序排序。
将价格列表反转，以得到降序排序的列表。
找到最高价格和最低价格。
计算所有商品的平均价格。
"""
prices = [50,20,30,70,90]
prices.sort()
print('升序排序:',prices)

prices.sort(reverse=True)
print('降序排序:',prices)

print('最大值:',max(prices),'最小值:',min(prices))
print('平均值:',sum(prices)/len(prices))

'''
11. 题干
假设你正在开发一个在线商店的购物车功能，需要编写 Python 代码来处理购物车内的商品。请完成以下要求：

已知有一个购物车商品列表 cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]，其中每个元组表示一种商品及其数量。请编写代码，实现以下功能：

创建一个新列表 cart_items，其中仅包含购物车中的商品名称（即去除商品数量信息）。
创建一个新列表 expensive_items，其中仅包含购物车商品数量>=3的商品名称。
将购物车中每个商品的数量加倍，并创建一个新的购物车列表 cart_doubled。
请编写上述要求的代码，并输出最终的列表 cart_items、expensive_items 和 cart_doubled。

'''
cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]
cart_items = [name for name, num in cart]
print('所有商品的名称列表：',cart_items)

expensive_items = [name for name, num in cart if num >= 3]
print('商品数量>=3的商品名称列表：',expensive_items)

cart_doubled = [(name,num*2) for name, num in cart]
print('每个商品的数量加倍后,新的购物列表：',cart_doubled)

'''

12. 题干
考试成绩的问题：提示用户输入成绩，判断是属于哪个水平，将结果打印到控制台。
60以下不及格，60分以上为及格，
70分至80分为合格，
80分至90分为良好，
90分以上为优秀。
例如：请输入考试成绩：85，打印“你的成绩是良好”
'''
score = int(input('请输入考试成绩(满分100）：'))
if score<0 or score>100:
    print('成绩无效')
else:
    if score<60:
        print('你的成绩等级：不合格')
    elif 60<=score<70:
        print('你的成绩等级：一般')
    elif 70<=score<80:
        print('你的成绩等级：合格')
    elif 80<=score<90:
        print('你的成绩等级：良好')
    elif 90<=score:
        print('你的成绩等级：优秀')

'''
13. 题干
统计字符串中，各个字符的个数，"hello world" 字符串统计的结果为： 
h:1 e:1 l:3 o:2 d:1 r:1 w:1，使用程序实现。
'''

'''
s = "hello world"
word_lst = s.split(' ')
word_lst[1] = word_lst[1][::-1]
res = ' '.join(word_lst)
print(res,word_lst,type(word_lst),len(word_lst))
dict = {}
for ch in res:
    if ch==' ':
        continue
    else:
        if ch in dict:
            dict[ch]+=1
        else:
            dict[ch]=1
print(dict)
'''

'''
6. 两数求和
程序需要接收用户输入的两个数字，并计算它们的和。
要求：

定义函数 add(a, b)
函数返回两个数的和
调用函数并输出结果
'''
def add(a,b):
    return a+b

a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
print('求和结果=',add(a,b))
