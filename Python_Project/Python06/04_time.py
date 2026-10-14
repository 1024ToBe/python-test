import  pg

#1.倒包
import time

#2.获取开始时间
start = time.time()
print('开始时间',start)

# 3.执行程序:累加计算1到1亿的数字之和
sum = 0
for i in range(1, 100000001):
    sum += i
print(f"总和:{sum}")
# 4.获取结束时间
end = time.time()
print("结束时间：", end)
# 5.计算差值
print("程序运行时间：", end - start)

pg.tes

