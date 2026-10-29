#list操作
import redis
r = redis.Redis(
    host='127.0.0.1',        # redis服务器
    port=6379,               # redis服务器端口
    db=0,                    # 数据库编号，默认0
    password=None,           # 密码，如果没设置则为 None
    decode_responses=True    # 自动解码，返回字符串而不是字节
)

# 从左侧插入数据
r.lpush('lst1','t1','t2','t3')
# # 从右侧插入数据
r.rpush('lst1','t4','t5','t6')

# # 获取长度
len = r.llen('lst1')
print(f'列表长度{len}')
#
# 获取下标范围的元素
all_ele = r.lrange('lst1',0,-1) # -1代表：从0到尾部全部
print(f'全部内容：{all_ele}')

# 获取前三的元素
three_ele = r.lrange('lst1',0,2)
print(f'前三内容：{three_ele}')

#取出元素
first_l = r.lpop('lst1',1)
first_r = r.rpop('lst1',2)
print(f'左边弹出的第一个元素：{first_l},右边弹出的第一个元素：{first_r}')
r.close()