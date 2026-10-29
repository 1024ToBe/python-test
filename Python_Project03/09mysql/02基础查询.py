# 1.导入模块
import pymysql

# 2.创建连接类的对象(TCP三次握手，保持了TCP 连接到MySQl服务器) --接通电话线
conn = pymysql.connect(
    host='127.0.0.1',  # 指定 mysql 服务器地址
    port=3306,         # 默认在 3306端口
    user='root',       # 指定用户名
    password='123456', # 指定密码
    charset='utf8',    #指定编码集，避免中文乱码问题
    database='jing_dong'
)
#3.创建干活小弟游标对象cursor  --派出跑腿小弟【游标】
# 干活的是游标对象
# conn是负责整个网络的连接通畅
cursor = conn.cursor()

#4.指向sql查询,execute执行  --给小弟一张纸条（SQL语句），让他去数据库查询
cursor.execute('select name,brand_name,price from goods where price>5000')
# cursor.execute('select * from goods')

#4.1小弟执行完 sql 后，cursor小弟会保存结果，可以取出   --小弟把查到的数据带回来
#fetchone 是抓取一行结果，格式是元组(列，列，列...)
# r1 = cursor.fetchone()
# print(r1)
# r2 = cursor.fetchone()
# print(r2)

#4.2抓取全部
#返回结果是元组套元组((列，列，列......),(),......)
all_result = cursor.fetchall()
# print(all)
for row in all_result:
    name = row[0]
    brand_name = row[1]
    price = row[2]
    print(f'商品名称：{name},商品品牌：{brand_name},商品价格：{price}')

#干完活，收尾
#5.关闭游标
cursor.close()  # --打发小弟下班
#6.关闭连接(断网）(TCP四次挥手)
conn.close()    # --挂断电话线