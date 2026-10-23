#1.字符串必须包含test(用match)
#2.匹配IP格式xxxx.xxx.xxx.xxx xxx是纯数字数量1-3
#3.匹配网址 http://www.itheima.com或https://www.itheima.com
#4.匹配手机号,必须是1开头,其余纯数字数量11位١٤٣
import re
import inspect

def print_result(funcname,result):
    if result:
        print(f'方法{funcname},匹配成功，结果：',result.group())
    else:
        print('匹配失败')
def demo01():
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r".*test.*"
    result = re.match(p,s)
    print_result(funcname,result)
# demo01()

def demo02():
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    result = re.match(p,s)
    print_result(funcname,result)
# demo02()


def demo03():
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r"https?://www.itheima.com"

    result = re.match(p,s)
    print_result(funcname,result)
# demo03()

def demo04():
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r"1\d{10}"

    result = re.match(p,s)
    print_result(funcname,result)
# demo04()

def demo05():
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r"1\d{10}"

    result = re.match(p,s)
    print_result(funcname,result)
# demo05()

def demo06():
    # 1.将手机号替换为1★★★★★★★★★★1,中间9个数字为*
    s = input('请输入手机号：')
    p = r"(\d{1})\d{9}(\d{1})"

    result = re.sub(p,r'\1*********\1',s)
    print('替换之后：',result)
# demo06()


def demo07():
    # 2.微博超话#....#,抽取2个#的内容输出
    s = input('请输入内容：')
    p = r"#(\w+)#"

    result = re.search(p,s)
    print(result.group(1))
# demo07()

def demo08():
    # IP地址xxx.xxx.xxx.xxx,输出中间第二个xxx和第三xxx,分开输出
    s = input('请输入内容：')
    p = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"

    result = re.search(p,s)
    print(result.group(2))
    print(result.group(3))
# demo08()

def demo09():
    r"""
    网址:http://www.qq.com,分别输出
    协议,即http或https
    域名,即qq.com
    协议http或https
    域名支持qq.com sina.com itheima.com itcast.cn
    """
    s = input('请输入内容：')
    p = r"(https?)://www\.(qq\.com|itheima\.com|itcast\.cn)"

    result = re.search(p,s)
    print('协议：',result.group(1))
    print('域名：',result.group(2))
# demo09()

'''
背景：
小红正在开发一个简单的用户注册功能。为了避免用户填写错误手机号，系统需要在提交注册信息前先校验手机号格式。只有手机号格式正确，才允许继续注册。
问题:
请使用正则表达式完成手机号格式校验。
已知待校验手机号：phone = "13812345678"
要求:
1.手机号必须以 1 开头
2.手机号总长度必须是 11 位
3.除第一位外，后 10 位必须都是数字
4.如果格式正确，输出 手机号格式正确
5.如果格式错误，输出 手机号格式错误
'''

def demo10():
    phone = "13812345678"
    p = r'^1\d{10}$'
    r = re.match(p,phone)
    if r:
        print('手机号格式正确')
    else:
        print('手机号格式错误')

demo10()
