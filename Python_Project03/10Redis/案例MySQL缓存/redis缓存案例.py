import redis
import pymysql

class MySQLService:
    def __init__(self,
                host='127.0.0.1',
                port=3306,
                user='root',
                pwd='123456',
                charset='utf8',
                db='my_db'):
        try:
            self.conn = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=pwd,
                charset=charset,
                database=db
            )
            # 创建游标
            self.cursor = self.conn.cursor()
            print("MySQL连接成功")
        except Exception as e:
            print("MySQL连接失败：", e)


    def __del__(self):
        self.cursor.close()
        self.conn.close()


    def get_user_info(self,username):
        sql = "SELECT * FROM userinfo WHERE name=%s"
        self.cursor.execute(sql, [username])

        #获取结果
        return self.cursor.fetchall()

class RedisService:
    def __init__(self,ms:MySQLService, host='127.0.0.1',
                port=6379,
                pwd=None,
                db=0):
        try:
            self.r = redis.Redis(
                host=host,
                port=port,
                password=pwd,
                decode_responses=True,
                db=db
            )
            print("Redis连接成功")
            self.ms = ms

        except Exception as e:
            print('Redis 连接失败：',e)

    def __del__(self):
        self.r.close()

    def __ttl_reset(self,key,ttl_time=15): #私有保护
        #设置ttl
        self.r.expire(key,ttl_time)

    def __save_user_info(self,username,infos):
        for info in infos:
            msg = ",".join([str(col) for col in info])
            self.r.lpush(username,msg)

        #首次-设置过期时间
        self.__ttl_reset(username)

    def get_user_info(self, username):
        #redis有没有？
        if self.r.exists(username):
            # 找到缓存
            print(f"查询{username}，缓存命中，重设TTL")
            # 重设TTL
            self.__ttl_reset(username)
            #
            return self.redis_conn.lrange(username, 0, -1)

        print(f"查询{username}，缓存未命中，跳转MySQL查询")

        infos = self.ms.get_user_info(username)  # ((), ())
        if infos:  # 空元组是False，非空是True
            print(f"查询{username}，缓存未命中，从MySQL中查询得到信息，同检索到{len(infos)}条信息")
            self.__save_user_info(username, infos)
        else:
            print(f"查询{username}，缓存未命中，MySQL也没查到，没有此用户")

        return infos

if __name__ == '__main__':
    ms = MySQLService()
    rs = RedisService(ms)
    while True:
        username = input("输入要查询的姓名，要退出输入exit")
        if username=='exit':
            break
        infos = rs.get_user_info(username)
        print(infos)
        
