'''
1.计数器作为全局变量，虽然可以随意访问，但是，也可以随意修改

'''
#1.全局变量的方法
# count1 = 0
# count2 = 0

#2.闭包方法,使用变量count
def counter():
    count = 0
    def inner():
        nonlocal count
        count+=1
        print(f'计件数量：{count}')
    return inner


def w1(f):
    # global count1
    # print('我爱工作,请计件')
    # count1+=1
    # print(f'我爱工作,计件数量：{count1}')
    print('我爱工作,请计件')
    f()


def w2(f):
    #global count2
    #print('黑马工作,请计件')
    #count2 += 1
    #print(f'黑马工作,计件数量：{count2}')

    print('黑马工作,请计件')
    f()

print('开始招水军干活')
# w1()
# w2()
# #安全隐患：随时可以被人修改
# count1 = 0
# count2 = 0
# w1()
# w2()

f1 = counter()
f2 = counter()

w1(f1)
w2(f2)
w1(f1)
w2(f2)


