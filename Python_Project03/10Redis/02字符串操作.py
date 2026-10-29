import redis
r = redis.Redis(
    host='127.0.0.1',        # redis服务器
    port=6379,               # redis服务器端口
    db=0,                    # 数据库编号，默认0
    password=None,           # 密码，如果没设置则为 None
    decode_responses=True    # 自动解码，返回字符串而不是字节
)

#测试ping方法,测试通不通,通了返回True,否则False
# response = r.ping()

# redis结构是K+V
# K字符串
# V是各类类型，我们现在的V演示为字符串
# set存入  set(k, v)
# r.set('name', '周杰轮')
# r.set('age', '19')

# 取出  get取出，  v = r.get(k)
# name = r.get('name')
# age = r.get('age')
# age123 = r.get('age123')        # K不存在，结果为None
# print(f"取出name：{name}，age：{age}, {age123}")
#
# print("-----------------------------------------")

# mset multi set  批量存多个
# r.mset({k:v, k: v, K:v})
'''
r.mset({"hobby": "唱跳RAP", "money": "123456", "gender": "男"})
# r.mget([k, k, k])   返回值 -> [v, v, v]
values = r.mget(['hobby', 'money', 'gender'])
print(f"一次型取出：{values}")
'''

#test
r.set('name','赵维维')
name = r.get('name')
print(name)

r.mset({'name':'赵薇','age':'35'})
values = r.mget(['name','age'])
print(values)


r.close()