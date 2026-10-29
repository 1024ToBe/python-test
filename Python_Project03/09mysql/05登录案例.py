import pymysql
import random
import time

user = input('请输入用户名：')
pwd = input('请输入密码：')

#1.建立连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    database='jing_dong'
)
#2.创建干活小弟游标
cursor = conn.cursor()

#3.小弟开始干活
# sql = f"select * from user where user='{user}' and pwd ='{pwd}'"
# cursor.execute(sql)

#使用占位符
sql = f"select * from user where user=%s and pwd=%s"
cursor.execute(sql,(user,pwd))

all_result = cursor.fetchall()
# for row in all_result:
#     print(row)
if len(all_result)>0:
    print('认证通过')
else:
    print('认证失败')

#4.下班，关闭连接
cursor.close()
conn.close()