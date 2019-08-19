import serial
import serial.tools.list_ports


import sys
import os
import time
import re


sPort = 'COM37'
sBaudRate = 115200
sTimeOut = 1

port_list = list(serial.tools.list_ports.comports())
if len(port_list) == 0:
    print('找不到串口')
else:
    for i in range(0, len(port_list)):
        print(port_list[i])


str_com = list(port_list[1])  # 串口信息列表 此处修改串口序号


# str_com = port_list[2]
# str_com = str(str_com)
# sPort = (str_com[0:5])
# sPort.strip()

# sPort = 'COM3'

sPort = str_com[0]  # 获取串口号 字符形式

print("现在打开的串口是", sPort)


try:
    myserial = serial.Serial(port=sPort, baudrate=sBaudRate, timeout=sTimeOut)
    print('open serial ok')
except:
    print('open serial error')

try:
    serial_read_data = myserial.readline()
    print(serial_read_data)
    # snum = int(serial_read_data)
    # print(snum)

except:
    print('serial_read_data error')

serial_format_string = (
    "this is a format test ,int %d float %2.1f  string %s") % (1, 3.14, "string")
myserial.write(serial_format_string.encode('utf-8'))
# 通过串口写入ser.write(b'')，参数需要使用字节bytes类型，如果是str类型，则可以使用encode('utf-8')的方式进行转换
myserial.write(b"123456\r\n")
myserial.write("123456\r\n".encode('GB2312'))


# print(myserial.read(6))
