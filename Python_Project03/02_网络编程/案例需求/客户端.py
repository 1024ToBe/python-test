'''
无限和服务器发送消息
发送的每一条消息都是input输入
当输入消息为bye的时候,结束连接
'''
import socket
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    ('127.0.0.1',10003)
)

while True:
    msg = input('发啥：')
    client.send(msg.encode('UTF-8'))

    if msg == 'bye':
        break
