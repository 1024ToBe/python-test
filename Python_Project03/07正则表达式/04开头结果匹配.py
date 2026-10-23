import re
import inspect

'''
^:字符串头
$:字符串尾部

[^]:[]内部代表取反，单独用^是限制开头
'''

def print_result(funcname,result):
    if result:
        print(f'方法{funcname},匹配成功，结果：',result.group())
    else:
        print('匹配失败')

def demo04():
    '''
    #匹配密码，必须 6 位纯数字
    '''
    funcname = inspect.currentframe().f_code.co_name
    print(f'方法{funcname}开始执行')
    s = input('请输入内容：')
    p = r"^\d{6}$"  #锁定头尾，如果不锁定头尾：12345678符合，锁定头尾就必须有且只有 6 位

    result = re.match(p,s)
    print_result(funcname,result)
demo04()