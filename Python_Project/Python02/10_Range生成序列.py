for i in range(0,10,1):
    print(f'{i}',end='\t')

#换行
print('\n')

for i in range(0,11,2):
    print(f'{i}',end='\t')

#for 循环实现九九乘法表
print('\n')

for j in range(1,10):
    for i in range(1,10):
        if i == j:
            print(f'{i}*{j}={i*j}\n')
            break
        else:
            print(f'{i}*{j}={i*j}',end='\t')
