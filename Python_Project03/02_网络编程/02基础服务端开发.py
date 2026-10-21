# 服务端（被动方），需要选择一个运行端口
import socket       # 导入包（Python内置）

# 1. 创建socket对象（类对象）
# 使用IP4版本地址，+TCP协议构建网络通讯
server = socket.socket(
    socket.AF_INET,      # 本质就是数字2， AF_INET IPv4地址（xxx.xxx.xxx.xxx）
    socket.SOCK_STREAM   # 本质就是数字1， 代表TCP协议
)

# 2. 选择IP地址和端口（IP地址就是自己电脑，端口随意，自定）
# socket对象的bind方法
#相当于租好门面、挂上门牌（IP + 端口）
server.bind(
    # (IP, 端口)
    # 127.0.0.1 表示自己电脑
    # 在自己电脑的8888端口上运行，客户端通过8888端口接入服务器
    # 8888随意，自己定
    ("127.0.0.1", 8888)
)

# 3. 启动服务器，被客户端连接
# socket对象的listen()方法
# 启动后，服务器就默默藏着8888端口后，接收数据，不阻塞
# 相当于开门、摆好等候座椅，告诉系统：我是服务端，有人来敲门（客户端连接）帮我排好队，我准备接待
server.listen()
print("服务器当前运行在8888端口")

# 4. 等待客户端接入
# socket对象的accept方法
# accept()方法返回一个元组，内含2个元素。
# 元素1：客户端连接对象。此对象记录了客户端的一切特征，和客户端通讯使用这个对象
# 元素2：记录了客户端的IP和端口，可以自行取用
# accept()方法是阻塞式， 如果客户端不接入，代码就卡在这里
#亲自开门，接待第一个排队的客人
client, client_info = server.accept()
print(f"客户端{client_info}已经接入")

# 5. 给客户端发消息
# 客户端连接对象的send方法
# 发送和接收都是二进制
# 服务器向客户端发
client.send("我是帅哥来了".encode("UTF-8"))

# 6. 接收客户端的消息
recv_data = client.recv(1024)       # 阻塞方法，不收到消息就不向下执行
print(f"收到客户端的数据：{recv_data.decode('UTF-8')}")

# 7. 主动关闭连接
# 客户端连接对象的recv方法
# 接收的也是二进制
# 1024，表示一次最多接收多少字节（byte），1024表示1024Byte == 1KB
# close方法
client.close()
