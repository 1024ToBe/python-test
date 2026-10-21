'''
list = []
for i in range(10):
    list.append(i)
    print('===',i)

for _ in len(list):
    num = list.pop(0)
    print(f'删除的元素:{num},列表:{list}')
'''
import queue
q = queue.Queue(10) #参数表示最多容纳多少元素，如果不填，基本无限（看你内存）

#放入数据，尾部入列
for i in range(1,11):
    q.put(i)
    print(f'放入数据{i}')

#取出数据（头部出列）
for i in range(1,11):
   num = q.get(i)
   print(f'取出数据：{num}')

#判断队列大小    
print(q.qsize())
