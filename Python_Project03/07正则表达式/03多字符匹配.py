import re
import inspect

def print_result(funcname,result):
    if result:
        print(f'方法{funcname},匹配成功，结果：',result.group())
    else:
        print('匹配失败')

'''
|:匹配左右任意一个表达式，或者
():
1. 将内容作为整体
2. 将内容作为一个分组
\数字: 引用分组几的内容
'''
def demo01():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com .cn
    # 使用或关系： (x|y|z)  x或y或z， xyz就是规则
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input('请输入内容：')
    p = r"^\w{4,20}@(163|qq|sina)\.(com|cn)$"
    result = re.match(p,s)

    print_result(funcname,result)
# demo01()

def demo02():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com .cn
    # 使用或关系： (x|y|z)  x或y或z， xyz就是规则
    # ()本身也是分组

    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input('请输入内容：')
    p = r"^\w{4,20}@(163|qq|sina)\.(com|cn)$"
    r = re.match(p, s)
    if r:
        print("成功")
        print(r.group())#1234@163.com
        print(r.group(0))#1234@163.com
        print(r.group(1))#.163
        print(r.group(2))#.com
    else:
        print("匹配失败")

# demo02()

def demo03():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com .cn
    # 使用或关系： (x|y|z)  x或y或z， xyz就是规则
    # ()本身也是分组
    # 需求：输出@之前内容  输出@之后的域名  输出.后面的结尾
    # abcd@qq.com   输出 abcd   输出qq   输出com
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input('请输入内容：')
    p = r"(^\w{4,20})@(163|qq|sina)\.(com|cn)$"
    # ()也是分组，从左到右，序号是组1组2组3...
    r = re.match(p,s)
    if r:
        print("成功")
        print("@符号之前：", r.group(1))
        print("@符号之后：", r.group(2))
        print(".符号之后：", r.group(3))
    else:
        print("匹配失败")
# demo03()

def demo04():
    """
   匹配HTML标签，HTML标签规则符合如下：
   <h1>............</h1>
   <abc>............</abc>
   <ccc>............</ccc>
   """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r"^<(\w+)>.*</\1>$"
    #\w+:  \w:任意字符；+:至少出现1次   .*：.是任意字符，*是任意次数，结合就是任意个数的任意字符
    #\1：引用第一组(\w+)内容

    r = re.match(p, s)
    print_result(funcname,r)
# demo04()

def demo05():
    """
   邮箱 abcd@qq.com
   邮箱运行 @之前4-20   @之后，qq.com或sina.com 或163.com
   输入字符串是：
   abcd@qq.com 二级域名abcd 域名qq.com
   :return:
   """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r"^(\w{4,20})@(qq\.com|sina\.com|163\.com)\s二级域名\1\s域名\2$"

    r = re.match(p, s)
    if r:
        print("成功")
        print("@符号之前：", r.group())
        print("@符号之前：", r.group(1))
        print("@符号之后：", r.group(2))
    else:
        print("匹配失败")
# demo05()
def demo06():
    """
    将合规手机号，替换为185****1234
    在sub中，参数2repl，也可以用正则，可以引用规则中的分组
   """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input('请输入内容：')
    p = r"(\d{3})\d{4}(\d{4})"

    r = re.sub(p,r"\1****\2",s)
    #\1 还原继续使用第一组内容(\d{3})
    # ****：把剩余内容替换为****
    #\2 还原继续使用第一组内容(\d{4})
    if r:
        print("成功")
        print("替换后：", r)
        # print("@符号之前：", r.group(1))
        # print("@符号之后：", r.group(2))
    else:
        print("匹配失败")
# demo06()

def demo07():
    """
    将合规手机号，替换为185****1234
    在sub中，参数2repl，也可以用正则，可以引用规则中的分组
   """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input('请输入手机号：')

    #切片截取 + 拼接
    s = s[:3] + '****' +s[7:]
    print(s)

demo07()
