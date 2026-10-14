#1.定义一个求和的函数 无参无返回
"""
def 函数名称 （）
   函数体
   return
"""
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print(f'sum={sum}')
get_sum()

#2.有参数无返回
def get_diff(a,b):
  diff = a-b
  print(f'diff= {diff}')
get_diff(30,15)

#2.有参数有返回
def get_multify(a, b):
 multify = a * b
 return  multify

print(f'multify = {get_multify(3,4)}')


#2.none
def test ():
 print('just test none')
a = test()
print(f'{a}')