import socket
#1.创建服务器对象
server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
#2.选择IP和端口
server.bind(
    ('127.0.0.1',8888)
)

#3.监听服务器，被客户端连接
server.listen()

while True:
    #4.等待客户端接入
    client,client_info =  server.accept()
    print(f'客户端{client_info}已经接入')

    #5.给客户端发消息
    client.send('你好,我是服务端'.encode('UTF-8'))

    #6.接收客户端信息
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
        # client.close()
        print('hi')
