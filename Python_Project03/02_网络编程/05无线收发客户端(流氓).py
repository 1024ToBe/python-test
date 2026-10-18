import socket
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    ('127.0.0.1',8888)
)

resv_data = client.recv(1024)
print(f'接收到的数据是{resv_data.decode('UTF-8')}')

count = 1
while True:
    client.send(f'你好服务端,我是流氓客户端{count}'.encode('UTF-8'))
    count+=1

# client.close()