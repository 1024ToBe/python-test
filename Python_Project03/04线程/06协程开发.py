'''
协程和线程一样（在Python），都是可以利用单核CPU，进行多个任务的交替（并发）
线程的交替，是CPU的调度，由操作系统决定。
协程的交替，当不需要CPU的时候，可以主动拒绝，让CPU去干别的事情
'''

"""
开发的步骤：

1. 给需要交替运行的任务（函数），带上`async`前缀
   1. 在需要移交CPU的地方，调用`await`前缀
2. 创建一个注册函数，在注册函数内，创建协程任务
3. 通过`asyncio.run`启动注册函数即可

"""
import asyncio

#1.创建交替运行的任务
async def eat():
    print('我要吃饭了')
    await asyncio.sleep(1)  #主动移交 CPU
    print('吃完了')


async def sleep(): # async开头表示此函数内部，有移交CPU的动作（即这个是协程函数）
    print('我要睡觉了')
    await asyncio.sleep(5)   #主动移交 CPU
    print('睡醒了')

# 2.注册任务函数
async def main():
    task1 = asyncio.create_task(eat()) #带括号调用函数
    task2 = asyncio.create_task(sleep())

    #启动任务
    await task1
    await task2

#3.通过`asyncio.run`启动注册函数即可
asyncio.run(main())



