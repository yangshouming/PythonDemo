'''
Descripttion: 
version: v0.0.1
Author: Stream
Date: 2020-08-15 14:12:32
LastEditors: Stream
LastEditTime: 2020-08-15 16:54:08
'''
import os
import socket
import sys
import time

host = socket.gethostname()
port = 5555

print(host)
print(port)

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
mysocket.connect((host, port))

for i in range(10):
    print(mysocket.recv(1000))
    time.sleep(1)
mysocket.close()

print("close")
