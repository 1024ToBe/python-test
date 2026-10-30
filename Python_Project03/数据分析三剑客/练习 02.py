import pymysql

#1.创建连接
conn = pymysql.connect(
    host='127.0.0.1',  # 指定 mysql 服务器地址
    port=3306,         # 默认在 3306端口
    user='root',       # 指定用户名
    password='123456', # 指定密码
    charset='utf8',    #指定编码集，避免中文乱码问题
    database='zww_sql1'
)

# 2.创建游标对象
cursor = conn.cursor()

# 3.游标开始执行SQL
#
# sql = '''
# SELECT
#     s.class_name,
#     AVG(sc.score) AS avg_score
# FROM students s
#          JOIN scores sc ON s.id = sc.student_id
# GROUP BY s.class_name
# HAVING AVG(sc.score) >= 80
# ORDER BY avg_score DESC
# '''

# 1.给 t_student 表新增一个字段 phone，类型为 varchar(20)，用于保存手机号
# sql = 'alter table t_student add column phone varchar(20)'
# 2.将 age 字段类型修改为 int
# sql = 'alter table t_student modify age int'
# 3.将 name 字段名称修改为 student_name，类型为 varchar(50)
# sql = 'alter table t_student change name student_name varchar(50)'
# 4.删除 phone 字段。
# sql = 'alter table t_student drop column phone'
# 5.查询年龄大于 18 的学生姓名和年龄，并按照年龄从大到小排序
sql = 'select student_name,age from t_student where age>18 order by age desc'
cursor.execute(sql)

# 4.取出结果
all_result = cursor.fetchall()
print(all_result)

# 5.关闭
# 关闭游标
cursor.close()
# 关闭连接
conn.close()