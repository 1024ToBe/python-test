num = 100
#global num  只能写在函数内部 写在外面报错
def show1():
    global num
    num = 50
    print('===',num)

def show2():
    print('===', num)   #50

show1()
show2()

