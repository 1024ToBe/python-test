#不可变 变量值相同，那么他们指向同一块内存区域
a=10
b=10
print(f'a的地址{id(a)}\nb的地址{id(b)}')

s1='i will be boss'
s2='i will be boss'
print(f'a的地址{id(s1)}\nb的地址{id(s2)}')

#打印20个虚线分割
print('-'*20)
#不可变：一旦内存内放入这个数字，不可以改变重写，只能程序停止，内存被回收清理；
# 如果变量值改变，会指向一块新内存。原地址内容不变
num1 = 10
num2 = 20
print(f'a的地址{id(num1)}\nb的地址{id(num2)}')

