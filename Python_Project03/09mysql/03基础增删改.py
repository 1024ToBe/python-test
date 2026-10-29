import pymysql
import random

#1.建立与MySQL服务器连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    database='jing_dong'
)

#2.创建游标，去数据库干活
cursor = conn.cursor()

#3.开始干活,执行SQL
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for data_id in range(4,10004):
    user = random.choice(names)+random.choice(names)+random.choice(names)
    password = '123456'
    # sql = f"insert into user values ({data_id},'{user}','{password}')"
    # cursor.execute(sql)

    sql = "insert into user values (%s, %s, %s)"
    cursor.execute(sql, (data_id, user, password))

#4.大哥 conn 确认提交修改
conn.commit()


#3.1 取结果


#4.下班，关闭游标、连接
cursor.close()
conn.close()