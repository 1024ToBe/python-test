import random
# sjs = random.randint(1,10)
# print(f'生成的随机数是{sjs}')
# i = 0
# while i<3:
#     guess = int(input('请输入你猜的数字:'))
#     if guess > sjs:
#         print('猜大了')
#     elif guess < sjs:
#         print('猜小了')
#     else:
#         print('猜对了 请退出')
#         break
#     i += 1
# print('循环已结束')

#猜 1-100数字 统计第几次猜对的
# sjs1 = random.randint(1,100)
# print(f'随机数是{sjs1}')
# j = 0
# while True:
#     guess1 = int(input('请输入你要猜的随机数:'))
#     j += 1
#     if guess1 != sjs1:
#         print('猜错了 继续')
#     else:
#         break
# print(f'循环结束,总共猜了{j}次')


#猜 1-100加和
# k = 0
# l = 0
# while l<100:
#     l+=1
#     k+=l
# print(f'最后算出的得数是{k}')

#打印 9*9乘法表
i2 = 1
j2 = 1
while i2<=9 and j2<=9:
    k2 = i2 * j2
    if i2 == j2:
        print(f'{i2}*{j2}={k2}\n')
        i2 = 1
        j2 += 1
    else:
        print(f'{i2}*{j2}={k2}',end='\t')
        i2 += 1
