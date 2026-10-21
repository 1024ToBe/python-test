import socket
# 1. 创建socket对象（IP4、TCP）
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 发起连接（客户端是主动方）（服务器需要提前运行好）
client.connect(             # 背后就是三次握手
    ("127.0.0.1", 10002)     # IP和端口都要指定服务器的，不要乱填
)

# 3. 发送或接收 （send、recv）
# 接收服务端发来的数据
# 如果接收不到服务端发送来的数据，会卡住
# recv_data = client.recv(1024)
# print(f"收到服务器的回复：{recv_data.decode('utf-8')}")

# 再发一条
while True:
    str = input('请输入你要发送的数据：')
    client.send(str.encode("UTF-8"))

# 4. 关闭
client.close()      # 背后就是四次挥手
