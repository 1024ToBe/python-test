def check1(fn):
    def inner():
        print('请输入账密')
        fn()
    return inner

def check2(fn):
    def inner():
        print('请输入验证码')
        fn()
    return inner

#多装饰器顺序：从上到下
@check2
@check1
def comment():
    print('可以发表评论了')

comment()
