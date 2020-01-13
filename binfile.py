'''
@Author: your name
@Date: 2020-01-06 14:05:38
@LastEditTime : 2020-01-07 09:43:36
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \PythonDemo\binfile.py
'''
# https://blog.csdn.net/zw515370851/article/details/95536315
# hexdump for VSCode  插件

import struct
import os

# mlx90640 参数  参数数值个数为832个  一帧图像数值个数为834个
eep_fmt = "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
time_fmt = "I"
data_fmt = "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"

# eep_fmt = "HHHHHHHHHH"
# time_fmt = "I"
# data_fmt = "HHHHHHHHHH"

eep_number = 832  # 数据的个数 int型 总字节长度=个数*2(byte)
time_number = 1  # 数据的个数 int型 总字节长度=个数*4(byte)
data_number = 834  # 数据的个数 int型 总字节长度=个数*2(byte)


def WriteFile():
    filepath = 'mlx90640.bin'

    # binfile = open(filepath, 'wb+')  # 打开二进制文件(新建完成)
    # data1 = range(0, eep_number)
    # a = struct.pack(eep_fmt, *data1)  # EEP 传感器参数
    # binfile.write(a)
    # binfile.close()

    # n = 0
    # for n in range(1):
    # binfile = open(filepath, 'ab+')  # 打开二进制文件(追加完成)
    # data1 = 1234
    # a = struct.pack(time_fmt, data1)  # 时间戳
    # binfile.write(a)
    # binfile.close()

    # binfile = open(filepath, 'ab+')  # 打开二进制文件(追加完成)
    # data1 = range(0, data_number)
    # a = struct.pack(data_fmt, *data1)  # 图像数据
    # binfile.write(a)
    # binfile.close()

    binfile = open(filepath, 'wb+')  # 打开二进制文件(追加完成)
    data1 = range(0, data_number)
    a = struct.pack(data_fmt, *data1)  # 图像数据
    binfile.write(a)
    binfile.close()


def ReadFile():
    filepath = 'mlx90640.bin'

    binfile = open(filepath, 'rb')  # 打开二进制文件
    size = os.path.getsize(filepath)  # 获得文件大小

    print("size", size)

    data = binfile.read(eep_number*2)  #
    print("sensor parameters", struct.unpack(eep_fmt, data))  # 解析 EEP 传感器参数

    while (binfile.tell() < size):

        data = binfile.read(time_number*4)  #
        print(struct.unpack(time_fmt, data))  # 解析 时间戳

        data = binfile.read(data_number*2)  #
        print("data", struct.unpack(data_fmt, data))  # 解析 图像数据

    binfile.close()

# -------------------------------------------------------------------


WriteFile()
# ReadFile()
