#yield关键字需要搭配函数使用,替代函数的return
#函数的return一次性返回全部结果
#yield是返回一个数据,在函数中,yield可以重复使用

def num_gen():   #yield就别写return
    print('lalala')
    yield 1
    print('lilili')  #yield对外生成1条数据，生成后代码暂停，直到对方需要下一个数据代码继续向下
    yield 3
    print('huhuhuhu')
    yield 5
    print('eeeeeeee')
    yield 7
#yield执行几次就生成几个数据

print(next(num_gen()))  #只打印1条

for num in num_gen():
    print(num,end = ' ')


def num_gen2(max_num,flag):
    if flag == 1:
        for i in range(1,max_num):  #生成偶数
            if i%2==0:
                yield i
    else:
        for i in range(1, max_num): #生成奇数
            if i % 2 != 0:
                yield i

# gen2 = num_gen2(21,1)
gen2 = num_gen2(21,0)
for num in gen2:
    print(num,end = ' ')
