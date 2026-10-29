#集合操作
import redis
r = redis.Redis(
    host='127.0.0.1',        # redis服务器
    port=6379,               # redis服务器端口
    db=0,                    # 数据库编号，默认0
    password=None,           # 密码，如果没设置则为 None
    decode_responses=True    # 自动解码，返回字符串而不是字节
)

'''
# 存入集合（去重）
r.sadd('set1','python','itheima','itcast','python')
# 获取全部
all_tags: set = r.smembers('set1')
print(all_tags)

#判断元素是否有
is_memeber = r.sismember('set1','python')
print('是否有python元素结果：',is_memeber)

# 弹出元素（集合没下标）
tag = r.spop('set1')
print('弹出：',tag)

# 指定弹出（删除）元素
r.srem('set1','itheima')
print('删除后：',r.smembers('set1'))

r.sadd('seta','a','b','c')
r.sadd('setb','d','b','c')

# 交集
interset = r.sinter('seta','setb')
print('交集',interset)

# 并集
union = r.sunion('seta','setb')
print('并集',union)

# 差集
diff = r.sdiff('seta','setb')
print('差集',diff)
'''

#test
r.lpush('lst2','a1','a2','a3')
r.rpush('lst3','a4','a5','a6')
all_ele = r.lrange('lst3',0,-1)
print('列表2的全部内容：',all_ele)

r.sadd('set2','b1','b2','b3')
r.sadd('set3','b4','b5','b6')
s_ele = r.spop('set2')
print('随机删除的集合元素是：',s_ele)
r.srem('set3','b4')
print('删除指定元素后：',r.smembers('set3'))

print('集合2所有元素：',r.smembers('set2'))


r.close()