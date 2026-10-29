import redis
r = redis.Redis(
    host='127.0.0.1',        # redis服务器
    port=6379,               # redis服务器端口
    db=0,                    # 数据库编号，默认0
    password=None,           # 密码，如果没设置则为 None
    decode_responses=True    # 自动解码，返回字符串而不是字节
)


r.set('num',0)
r.incr('num')
print('自增后：',r.get('num'))

r.incrby('num',5)
print('自增后5之后：',r.get('num'))

r.decr('num')
print('自减后：',r.get('num'))

r.decrby('num',3)
print('自减3后：',r.get('num'))

# 如果是复杂计算，就取出来，自己算，算完存回去
num = int(r.get('num'))
num = num*10+2
r.set('num',num)
print('计算后：',r.get('num'))

r.close()