import redis
r = redis.Redis(
    host='127.0.0.1',        # redis服务器
    port=6379,               # redis服务器端口
    db=0,                    # 数据库编号，默认0
    password=None,           # 密码，如果没设置则为 None
    decode_responses=True    # 自动解码，返回字符串而不是字节
)

# 检查K是否存在
print('hobby key存在？',r.exists('hobby'))
print('hobby222 key存在？',r.exists('hobby222'))

# TTL（Time To Live 剩余生存时间）设置
# hobby 5秒后删除
r.expire('hobby',5)

#r.expire("num", 300)
# 查看TTL
num_ttl = r.ttl('num')
print('key num ttl:',num_ttl)

# 取消TTL   persist(持久化)
r.persist('num')
# TTL为-1表示永久
print("key num ttl: ", r.ttl("num"))

# 查看redis全部key
keys = r.keys('*')
print(keys)

# 查看全部user开头的key
user_keys = r.keys('user*')  # 等同于linux * 通配符写法
print(user_keys)

# 彻底删除key
r.delete('user小曹')






r.close()