'''
需求背景：
某系统需要统一处理接口返回的英文提示信息，为了不修改原函数代码，希望通过装饰器把函数返回的字符串统一转换为大写。
要求：
定义一个装饰器 uppercase，要求：
1.被装饰函数返回字符串后，将结果转换为大写。(2分)
2.定义函数 get_message()，返回字符串 "hello python"。(2分)
3.使用 @uppercase 装饰 get_message。(2分)
4.在主程序中打印 get_message() 的返回值。(2分)
'''

def uppercase(fn):
    def inner(s):
        upper_s = s.upper()
        fn(upper_s)
    return inner

@uppercase
def get_message(str):
    print(str)

if __name__ == '__main__':
    get_message('hello python')



