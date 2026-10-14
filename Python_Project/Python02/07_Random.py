import  random
sjs = random.randint(1, 10)
print(f'获取的随机数是：{sjs}')

#闰年判断
year =  int (input('请输入年份:'))
if (year%400 == 0) or (year%4 == 0 and year%100 !=0):
    print(f'{year}年是闰年')
else:
    print(f'{year}年不是闰年')