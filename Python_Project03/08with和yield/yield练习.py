r'''
12.文本清洗：
提取邮箱和编号
背景：
客服系统导出的留言中，经常同时包含邮箱和工单编号。运营同学希望程序能从一段文本中自动提取这些关键信息，减少人工复制。
问题：
给定文本：
text = "用户 zhangsan@example.com 提交了工单 NO1001，备用邮箱 service_01@test.cn，关联工单 NO1002。"

请使用正则表达式完成：

提取所有邮箱地址。(4分)
提取所有工单编号，编号格式为 NO 后跟 4 位数字。(4分)
分别打印两个列表。(2分)
【提交运行截图和代码】

'''
r'''
import re
def handle_text():
    text = "用户 zhangsan@example.com 提交了工单 NO1001，备用邮箱 service_01@test.cn，关联工单 NO1002。"
    #1.提取所有邮箱地址
    email_p = r'\w+@\w+\.\w+'
    email_lst = re.findall(email_p,text)
    print('邮箱列表：',email_lst)

    #2.提取所有工单编号
    order_p = r'NO\d{4}'
    order_lst = re.findall(order_p,text)
    print('工单编号列表：', order_lst)
handle_text()
'''

r'''
13. 库存扣减
使用互斥锁保护共享数据
背景：
电商系统中多个用户可能同时购买同一种商品。如果多个线程同时扣减库存，库存结果可能不准确。下面用简单代码模拟两个线程同时扣库存的场景。
题目：
编写程序模拟两个线程扣减库存，要求：

初始库存 stock = 10。(1分)
定义函数 buy(name, count)，表示某个用户购买 count 件商品。(3分)
使用互斥锁保护库存判断和扣减过程。(3分)
创建三个线程，分别模拟用户购买 3 件、4 件、5 件商品。(2分)
线程结束后打印剩余库存。(1分)
'''
'''
import threading
# 初始库存
stock = 10
# 创建互斥锁
lock = threading.Lock()

def buy(name, count):
    global stock
    with lock:
        if stock >= count:
            stock -= count
            print(f'{name}购买{count}件，购买成功，当前库存{stock}')
        else:
            print(f'{name}购买{count}件，库存不够，购买失败，当前库存{stock}')


if __name__ == '__main__':
    t1 = threading.Thread(target=buy, args=('张三', 3))
    t2 = threading.Thread(target=buy, args=('李四', 4))
    t3 = threading.Thread(target=buy, args=('王五', 5))

    t1.start()
    t2.start()
    t3.start()

    # 等待线程执行完成
    t1.join()
    t2.join()
    t3.join()
    print(f'最终库存{stock}')
'''

r'''
14. 协程任务
统计多个接口耗时
背景：
数据平台需要同时请求多个接口，并在所有接口完成后汇总结果。如果一个接口完成后再请求下一个，整体等待时间会比较长。
题目：
使用 asyncio 编写程序，要求：

定义协程函数 request_api(name, delay)，模拟请求接口
函数开始时输出 开始请求：接口名
使用 await asyncio.sleep(delay) 模拟等待
函数结束时返回字符串：接口名完成
在 main() 中同时执行 3 个接口请求
打印所有接口返回结果
'''
r'''
import asyncio
import time

#1.创建交替运行的任务
async def request_api(name, delay):
    s = time.time()
    print(f'开始请求{name}')
    await asyncio.sleep(delay)  #主动移交 CPU
    print(f'{name}完成')
    e = time.time()
    print(f'{name}耗时{e-s}')


# 2.注册任务函数
async def main():
    task1 = asyncio.create_task(request_api('接口A',1)) #带括号调用函数
    task2 = asyncio.create_task(request_api('接口B',3))
    task3 = asyncio.create_task(request_api('接口C', 5))

    #启动任务
    await task1
    await task2
    await task3

#3.通过`asyncio.run`启动注册函数即可
asyncio.run(main())
'''

r'''
15. Bug 修复
正则完整匹配
背景：
小王正在写邮箱格式校验功能，希望只有完整邮箱格式才算通过。但下面代码把一段包含邮箱的普通文本也判断成了通过，需要找出问题并修复。
题目：
请阅读下面代码，判断代码是否有问题。如果有问题，请说明问题原因，并写出修复后的代码。
'''
import re

text = "我的邮箱是 test@example.com"
result = re.match(r"^\w+@\w+\.\w+$", text)

if result:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")





