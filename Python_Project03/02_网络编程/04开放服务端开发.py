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
#0.0.0.0表示自己电脑 也代表可以让任何的电脑连接我本机这个服务器
#在自己电脑的8888端口上运行,客户端通过8888端口接入服务器
#8888随意,自己定
    ('0.0.0.0', 9999)
)

#3.启动服务器 被客户端连接
#socket对象的 listen()方法
#启动后,服务器就默默藏着8888端口后,接收数据
server.listen()

while True:
    #4.等待客户端接入
    client, client_info = server.accept()
    print(f'客户端{client_info}已经接入')

    #5.给客户端发送消息
    client.send('你好啊客户端'.encode('UTF-8'))

    # 6.接收客户端消息
    try:
        receive_data = client.recv(1024)
        print("原始字节：", receive_data)
        print(f'收到客户端数据：{receive_data.decode('UTF-8')}')
    except UnicodeDecodeError:
        # utf8解码失败，换成gbk
        print(f'收到客户端数据：{receive_data.decode('gbk')}')
    except Exception as e:
        print(f'客户端{client_info}不遵守规则， 信息无效')
    finally:
        # 7.关闭链接
        #client.close()
        print('hi')









