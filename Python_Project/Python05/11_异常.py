'''
系统默认处理异常的方式: 就是在异常位置直接中断程序,后面的代码就无法执行了
'''

# print('程序开始~')
#
# # NameError异常: 变量名没有提前定义过
# print(a)
# # FileNotFoundError异常: 打开文件的时候,模式如果是r,此文件不存在就报错
# f = open('a.txt', 'r')
# # ZeroDivisionError异常: 除法运算的时候,0不能作为除数,否则报错
# print(1/0)
#
# print('程序结束~')

#try_except处理异常方式
'''
方式 1
try:
   可能出现异常的代码
except Exception as e:
   出现异常要执行的代码
'''
# print('程序开始~')
# try:
#     print(a)
#     print(1 / 0)
# except:
#     print('报错了吧,下回注意啊~')
# print('程序结束~')
#
# print('程序开始~')

print('程序开始~')
try:
    print(a)
    print(1 / 0)
except Exception as e:
    print(f'报错了吧:{e},下回注意啊~')
print('程序结束~')

'''
方式 2 
try_except_else_finally处理异常
try:
    可能出现异常的代码
except Exception as e:
    出现异常要执行的代码
else:
    没有异常执行的代码
finally:
    不管有没有异常都要执行的代码
'''
print('程序开始~')
try:
    print(a)
    print(1 / 0)
except Exception as e:
    print(f'报错了吧:{e},下回注意啊~')
else:
    print('没有捕获异常，继续工作吧')
finally:
    print('finally中是不管有没有异常都执行的代码')
print('程序结束~')