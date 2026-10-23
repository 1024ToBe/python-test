import re
import inspect
'''
match
作用：从字符串头部开始匹配，寻址符合规则的子串
找到了，返回class Match对象
获取匹配结果：match对象.group()

search
从整个字符串中搜索符合规则的子串，如果有多个，只匹配第一个出现的。

findall
全串搜索，多个匹配的都得到，组装为list返回。

sub
替换符合规则的子串
'''

def print_result(funcname,result):
    if result:
        print(f'方法{funcname},匹配成功，结果：',result.group())
    else:
        print('匹配失败')

#-------------------------------------match---------------------------------------------
'''
-参数1规则，参数2被匹配字符串
-从头匹配，取第一个
-成功，返回re.Match类对象，失败返回None
'''

def demo01():
    r"""
    匹配字符串是否是：
    - 开头有3个字符，内容随意
    - 结尾有3个字符，内容随意
    - 中间必须是itheima
    aaaitheimaaaa合格
    bbbitheimabbb合格
    aitheimab 不合格
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    # 正则中， .：代表任意字符，数量1， (\n除外)
    s = input('输入内容：')
    result = re.match(
        "...itheima...",  #参数1：规则； .*itheima.*:这个代表前后任意字符 任意个数
        s  #参数2：被匹配字符串
    )

    print_result(funcname,result)
# demo01()

def demo02():
    r"""
   字符串必须符合规则：
   - 从头开始，第一个字符是小写字母，第二个是大写字母，第三个是数字，其余随意
   [ab]        表示1个字符， 内容非a即b
   [abcde]     表示1个字符， 内容a或b或c或d或e
   第一个字符是小写字母: [abcdefghijklmnopqrstuvwxyz]        表示1个字符，内容是或a或b或c...或z
   第二个字符是大写：[ABCDEFGHIJKLMNOPQRSTUVWXYZ]       表示1个字符，内容是或A或B或C...或Z
   第三个字符是数字：[0123456789]       表示1个字符，内容是或0或1或2...或9
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('输入内容：')
    result = re.match(
         "[abcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZ][0123456789]",  # 规则
        s  # 参数2：被匹配字符串
    )

    print_result(funcname,result)

# demo02()

def demo03():
    r"""
    字符串必须符合规则：
    - 从头开始，第一个字符是小写字母，第二个是大写字母，第三个是数字，其余随意
    [ab]        表示1个字符， 内容非a即b
    [abcde]     表示1个字符， 内容a或b或c或d或e
    第一个字符是小写字母: [abcdefghijklmnopqrstuvwxyz]        表示1个字符，内容是或a或b或c...或z
    第二个字符是大写：[ABCDEFGHIJKLMNOPQRSTUVWXYZ]       表示1个字符，内容是或A或B或C...或Z
    第三个字符是数字：[0123456789]       表示1个字符，内容是或0或1或2...或9

    [abcdefghijklmnopqrstuvwxyz]  简化为：[a-z]     范围是按照ASCII
    [ABCDEFGHIJKLMNOPQRSTUVWXYZ]  简化为：[A-Z]
    [0123456789]    简化为[0-9]        -本身不算
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('输入内容：')
    result = re.match(
          "[a-z][A-Z][0-9]",   # 规则
        s  # 参数2：被匹配字符串
    )
    print_result(funcname,result)

# demo03()

def demo04():
    r"""
    第一个字符是字母（大小写都行），第二个是数字，后面随意
    [a-zA-Z]   字符数量1个，内容小写或大写
    [a-zA-Z]   等同于[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]
    [ab]
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input("输入内容：")
    p = "[a-zA-Z][0-9]"
    result = re.match(
        p,
        s
    )
    print_result(funcname,result)

# demo04()

def demo05():
    r"""
    第一个字符不能是字母和数字
    [a-zA-Z0-9]  等于 [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]
    不是字母和数字
    [^a-zA-Z0-9] 不是这些
    [^]表示取反
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input("输入内容：")
    p = "[^a-zA-Z0-9]"
    result = re.match(
        p,
        s
    )
    print_result(funcname,result)
# demo04()

def demo06():
    r"""：
    前三个字符必须是数字，后面随意
    \d 表示字符数量为1，内容，必须是数字

   `r""` 原始字符串（raw string）
    作用：让 Python 把反斜杠 `\` 当成转义字符，原样保留 `\`。
    举例：
    普通字符串
    "\d"   # Python会尝试解析 \d，它不是合法转义，容易出问题
    原始字符串
    r"\d"  # Python不处理反斜杠，交给正则表达式去解析 \d
    """
    s = input("输入内容：")
    p = r"\d\d\d"
    result = re.match(
        p,
        s
    )
    funcname = inspect.currentframe().f_code.co_name
    print_result(funcname,result)
# demo06()

def demo07():
    r"""
    前三个字符必须不是数字，后面随意
    \D 表示字符数量为1，内容，必须不是数字
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input("输入内容：")
    p = r"\D\D\D"
    result = re.match(
        p,
        s
    )
    print_result(funcname,result)
# demo07()

def demo08():
    r"""
    匹配字符串开头的是如下的IPv4地址
    xxx.xxx.xxx.xxx

    .表示任意字符，数量1
    \. 表示 . 本身
    """

    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input("输入内容：")
    p = r"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
    result = re.match(
        p,
        s
    )
    print_result(funcname,result)
# demo08()

#-----------------------------serch------------------------------------
'''
-参数1规则，参数2被匹配字符串
-全串匹配，取第一个
-成功，返回re.Match类对象，失败返回None
'''

def demo09():
    r"""
    找 字母 字母 字母的串
    要求字符串中有即可，找到出现的第一个
    \s 空白 空格、tab
    \S 非空白
    """

    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input("输入内容：")
    p = r"[a-zA-Z]\s[a-zA-Z]\s[a-zA-Z]"

    result = re.search(p, s)
    print_result(funcname,result)
# demo09()

def demo10():
    r"""
    要求字符串必须是 找到 2连字母+1个字符+2连字母   [a-zA-Z][a-zA-Z]\S[a-zA-Z][a-zA-Z]
    中间的一个字符不能是空白,从整个字符串去查找符合这样连续的字符串

    \S：非空白
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input("输入内容：")
    p = r"[a-zA-Z][a-zA-Z]\S[a-zA-Z][a-zA-Z]"

    result = re.search(p, s)
    print_result(funcname,result)
# demo10()

def demo11():
    r"""
    \w：正常字符（字母、数字、下划线，中文、韩文、阿拉伯文等），即不是符号
    匹配 xxxx xxxx
    x表示正常字符（有内容的），且不可以是符号

    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input("输入内容：")
    p = re.compile(r"\w\w\w\w\s\w\w\w\w")

    print_result(funcname,re.search(p, s))
demo11()

def demo12():
    r"""
    \W:非正常字符（符号，!@#$%等）
    用户设置密码，最少有1个特殊字符（!#!@*这些符号）
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = input("设置密码：")
    p = r"\W"

    result = re.search(p, s)
    if result:
        print("符合规则")
    else:
        print("必须有1个特殊字符")

# demo12()


#-----------------------------re.findall------------------------------------
'''
-参数1规则，参数2被匹配字符串
-全串匹配，取全部
-成功返回列表（list[str]），失败返回空列表
'''
def demo13():
    r"""
    要求字符串必须是 找到 2连字母+1个字符+2连字母   [a-zA-Z][a-zA-Z]\S[a-zA-Z][a-zA-Z]
    中间的一个字符不能是空白,从整个字符串去查找符合这样连续的字符串
    """
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')

    s = 'qa#123#erttg$12&sdd'
    p = r"[a-zA-Z][a-zA-Z]\S[a-zA-Z][a-zA-Z]"

    result = re.findall(p, s)
    print(result,type(result))

demo13()




