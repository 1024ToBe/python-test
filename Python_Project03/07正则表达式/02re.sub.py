import re
import inspect
#-----------------------------re.sub------------------------------------
'''
-
参数1:规则
参数2要替换成的
参数3被替换的字符串
参数4替换数量，要求参数4使用count=x关键字传参

-新字符串，老字符串不变
-全串匹配，替换符合规则的全部

'''
def demo13():
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input("请输入内容：")
    # p = r"\d" #把字符串中所有数字换成*
    # result = re.sub(p, '*', s)

    p = r"\." #把字符串中所有.换成#
    result = re.sub(p, '#', s)

    print(result)

# demo13()

def demo14():
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = 'www.com.myslef'
    p = r"\."
    result = re.sub(p, '#', s,1) ##仅把字符串中第一个(count =1)点换成#

    print(result)

demo14()
