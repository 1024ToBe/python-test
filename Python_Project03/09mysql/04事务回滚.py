import pymysql
import random
import time

#1.建立连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    database='zww_sql2'
)
#2.创建干活小弟游标
cursor = conn.cursor()

#3.小弟开始干活
try:
    for i in range(1, 10001):
        name = f"王大锤{i}"
        age = random.choice([22, 11, 33, 21, 25, 26, 28, 20])
        gender = random.choice(["男", "女"])
        height = random.randint(160, 186)

        if i == 5001:
            #sql = f"INSERT INTO student VALUES({i}, '{name}',{age}, '{gender}', {height},  12345)"
            sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (i, name, age, gender, height,12345))
        else:
            sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (i, name, age, gender, height))
            # sql = f"INSERT INTO student VALUES({i}, '{name}', {age} '{gender}', {height})"
            # sql = f"INSERT INTO student VALUES(1,'王大厨1',22,'男',187)"

        if i % 1000 == 0:
            print(f"插入了{i}条数据")
    conn.commit()       # 确认这些操作生效
except Exception:
    time.sleep(10)
    print(f"插入数据库中途出现问题，前面全部操作撤回")
    conn.rollback()     # 撤回

#4.下班，关闭连接
cursor.close()
conn.close()