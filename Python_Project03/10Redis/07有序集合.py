#有序集合操作
import redis
r = redis.Redis(
    host='127.0.0.1',        # redis服务器
    port=6379,               # redis服务器端口
    db=0,                    # 数据库编号，默认0
    password=None,           # 密码，如果没设置则为 None
    decode_responses=True    # 自动解码，返回字符串而不是字节
)

# zadd 添加有序集合
r.zadd('leaderboard',{
    '小曹':2000, # k->v 信息->分数
    '小花':5000,
    '小旺':6000,
    '小翠':1000
})
asc_names = r.zrange('leaderboard',0,-1)
print(asc_names)

# 升序
asc_names = r.zrange('leaderboard',0,-1,withscores=True)
print(asc_names)

# 降序
desc_names = r.zrevrange('leaderboard',0,-1,withscores=True)
print(desc_names)

#增加分数
r.zincrby('leaderboard',1000,'小曹')
print('小曹分数：',r.zscore('leaderboard','小曹'))

# 得到排名从高到低  从0开始排名
print('小曹排名：',r.zrevrank('leaderboard','小旺'))

# 按分数范围获取
scores = r.zrangebyscore('leaderboard', 1000, 5000, withscores=True)
print(scores)

r.close()