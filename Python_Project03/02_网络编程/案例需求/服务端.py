'''
可以接收任意数量客户端接入,每一次只服务1个客户端
和被服务的客户端沟通的时候,可以无限接收客户端发来的消息
直到客户端发来`bye`,服务器断开和这个客户端的连接
'''

import socket
server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(
    ('127.0.0.1',10003)
)

server.listen()

while True:
    print('等待客户端接入')
    client, client_info = server.accept()
    print(f'客户端{client_info}已经接入')

    while True:
        receive_data = client.recv(1024)
        try:
            msg = receive_data.decode("utf-8")
        except UnicodeDecodeError:
            # utf8解码报错，说明不是utf8，换成gbk
            msg = receive_data.decode("gbk")

        print(f'收到客户端的信息：{msg}')
        if msg == 'bye':
            client.close()
            print(f'关闭和客户端{client_info}的连接')
            break




