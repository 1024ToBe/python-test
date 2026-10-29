import redis
r = redis.Redis(
    host='127.0.0.1',        # redis服务器
    port=6379,               # redis服务器端口
    db=0,                    # 数据库编号，默认0
    password=None,           # 密码，如果没设置则为 None
    decode_responses=True    # 自动解码，返回字符串而不是字节
)

'''
#哈希操作
r.hset('user小曹','age',21)
r.hset('user小曹','hobby','写代码')
r.hset('user小曹','height',187)

#取出
# r.hget(k1, k2)
hobby = r.hget('user小曹','hobby')
print(hobby)

#取出全部字段
userdic:dict = r.hgetall('user小曹')
# print(userdic)
print("--------------------")

# 过期方法
# r.hmset(
#     'user小曹',{
#         'name':'王小锤',
#         'age':11,
#         'gender':'男'
#     }
# )


# 新方法
r.hset('user小曹',mapping={'name':'王锤锤','age':22,'gender':'女'})
print( r.hgetall('user小曹'))

keys = r.hkeys('user小曹')
print('小曹的keys:',keys)

values = r.hvals('user小曹')
print('小曹的values:',values)
'''

#test
r.hset('user1001',mapping={'name':'赵哈哈','age':23,'gender':'女'})
values = r.hvals('user1001')
print(values)


#删除 指定 key 键，在哈希 `user1001` 里面，删除字段 `name`
# r.hdel('user1001','name')
r.hdel('user1001', 'name', 'age')
print(r.hgetall('user1001'))

r.close()