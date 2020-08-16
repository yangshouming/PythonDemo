'''
Descripttion: 
version: v0.0.1
Author: Stream
Date: 2020-08-15 16:24:00
LastEditors: Stream
LastEditTime: 2020-08-15 16:52:08
'''
import time
import socket

host = socket.gethostname()
port = 5555

# 创建socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
socket_server.bind((host, port))
# 设置最大监听数
socket_server.listen(5)


while (1):

    # 接受客户端连接
    socket_client, addr = socket_server.accept()
    print("addr", str(addr))
    # 发送数据
    msg = "server msg"
    socket_client.send(msg.encode('utf-8'))
    time.sleep(500)
