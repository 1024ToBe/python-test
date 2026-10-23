'''
l1 = [i for i in range(1,10)]
print(l1)  #此时l1已存放好全部内容

num_generator = (i for i in range(10,20))
print(num_generator)  #这里只是一个申生成器generator
#生成器：记录生成数据的规则，即记下了：i for i in range(10,50)

print(next(num_generator)) #使用 next(生成器)，按生成规则，临时产生一条数据给你
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator)) #规则耗尽就无法得到下一个了

while True:
    try:
        print(next(num_generator))
    except StopIteration:
        print('生成器用完了')
        break



for num in num_generator:
    print(num,end=' ')
'''

num2_generator = (i for i in range(1,101) if i%2==0)
for num in  num2_generator:
    print(num, end=' ')
