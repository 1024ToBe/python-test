def show1():
    print('1111111')
def show2():
    print('22222222')
    show1()

if __name__ == '__main__':
    print('main 开始')
    show2()
    print('main 结束')