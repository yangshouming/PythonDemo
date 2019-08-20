import serial
import serial.tools.list_ports


import sys
import os
import time
import re

import binascii

sPort = 'COM37'
sBaudRate = 115200
sTimeOut = 1

port_list = list(serial.tools.list_ports.comports())
if len(port_list) == 0:
    print('找不到串口')
else:
    for i in range(0, len(port_list)):
        print('序号%d :' % (i+1), port_list[i])

# serial_index = input("请输入串口序号")
serial_index = '2'

serial_index = int(serial_index)
str_com = list(port_list[serial_index-1])  # 串口信息列表 此处修改串口序号
sPort = str_com[0]  # 获取串口号 字符形式

print("现在打开的串口是", sPort)


try:
    myserial = serial.Serial(port=sPort, baudrate=sBaudRate, timeout=sTimeOut)
    # myserial.setPort('COM37')
    print('open serial ok')
except:
    print('open serial error')


# 通过串口写入ser.write(b'')，参数需要使用字节bytes类型，如果是str类型，则可以使用encode('utf-8')的方式进行转换
# 串口发送格式化的字符串------------------------------------------------------------------------------------------
print('serial write')
serial_format_string = (
    "是的 This is a format test, int %d;float %2.1f;string %s \r\n") % (1, 3.14, "string")
myserial.write(serial_format_string.encode('utf-8'))
myserial.write(serial_format_string.encode('GB2312'))
myserial.write(b"123456\r\n")

# 串口发送格式化的16进制数------------------------------------------------------------------------------------------
hex_string_num1 = 1
hex_string_num2 = 2
hex_string_num3 = 3
hex_string_num4 = 4
hex_string_num5 = 5

hex_string = ('%02x%02x%02x%02x' %
              (hex_string_num1, hex_string_num2, hex_string_num3, hex_string_num4))  # 将数据以16进制方式转成字符串

hex_str = binascii.a2b_hex(hex_string)  # 将字符串(ascii)转成byte类型
myserial.write(hex_str)  # 串口发送


# 串口读取------------------------------------------------------------------------------------------
print('serial read test')
# 结束符 16进制 数字 04(0x04) LF(0X0A) CR (0X0D)
serial_read_data = myserial.read_until(binascii.a2b_hex('04'))
print(serial_read_data)
serial_read_data = myserial.read_until(binascii.a2b_hex('0203'))
print(serial_read_data)

serial_read_data = myserial.readline()
print(serial_read_data)
serial_read_data = myserial.read(8)
print(serial_read_data)
