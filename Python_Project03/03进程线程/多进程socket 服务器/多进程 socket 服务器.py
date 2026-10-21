import socket
import multiprocessing as mp

def work(client,client_info):
    name = mp.current_process().name
    print(f'子进程{name}接入客户端{client_info}')

    while True:
        recv_data = client.recv(1024)
        try:
            new_data = recv_data.decode('UTF-8')
        except:
            new_data = recv_data.decode('gbk')

        if not new_data:
            client.close()
            break
        else:
            print(f"收到客户端的数据：{new_data}")

        if new_data == 'bye':
            print(f'子进程{name}关闭客户端{client_info}连接')
            client.close
            break
    print(f'子进程{name}结束')



if __name__ == '__main__':
    # 1.创建
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.选择 IP 和端口
    server.bind(('127.0.0.1', 10002))
    # 3.开启监听
    server.listen()
    while True:
        # 4.等待客户端接入
        client, client_info = server.accept()

        #每接入一个新客户端，就创建一个子进程，和客户端玩去
        mp.Process(target=work,args=(client,client_info)).start()

