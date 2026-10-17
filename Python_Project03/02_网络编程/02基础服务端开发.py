#服务端（被动放）：需要选择一个端口运行
import socket #Python自带

#1.创建 socket 对象（类对象）
server = socket.socket(
    socket.AF_INET, #AF_INET本质是数字 2，其实就是代表 IPv4地址
    socket.SOCK_STREAM #SOCK_STREAM 本字是数字1， 其实是代表 TCP 协议
    # 2,
    # 1
)
#print(server,type(server))

#2.选择IP地址和端口(IP是自己电脑地址，端口号自定义)
#socket对象的 bind方法
server.bind(
#参数-元组形式 (IP,端口)
#127.0.0.1表示自己电脑
#在自己电脑的8888端口上运行,客户端通过8888端口接入服务器
#8888随意,自己定
    ('127.0.0.1', 8888)
)

#3.启动服务器 被客户端连接
#socket对象的 listen()方法
#启动后,服务器就默默藏着8888端口后,接收数据
server.listen()

#4.等待客户端接入
#socket对象的 accept()方法
#accept()方法返回一个元组,内含2个元素。
#元素1:客户端连接对象。此对象记录了客户端的一切特征,和客户端通讯使用这个对象
#元素2:记录了客户端的IP和端口,可以自行取用
#accept()方法是阻塞式,如果客户端不接入,代码就卡在这里
client, client_info = server.accept()

#可能有多个客户端
# client1, client_info = server.accept()
# client2, client_info = server.accept()
# client3, client_info = server.accept()
print(f'客户端{client_info}已经接入')
#5.给客户端发送消息
#socket对象的 send()方法
#发送和接收都是二进制
# client：代表服务器向客户端n发！
#此处是服务端代码，所有执行者都是服务端
client.send('你好啊客户端'.encode('UTF-8'))

#6.接收客户端消息
#socket对象的 rscv()方法
#接收的也是二进制
#1024,表示一次最多接收多少字节(byte),1024表示1024kByte==1KB
receive_data = client.recv(1024)
print("原始字节：", receive_data)
# print(f'收到客户端数据：{receive_data.decode('UTF-8')}')
print(f"收到客户端的数据：{receive_data.decode('gbk')}")

#7.关闭链接
#socket对象的 close()方法
# client.close()


