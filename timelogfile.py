# coding=utf-8
'''
@Description: 
1.创建带时间的文件
2.文件名带重名检测
@Author: Stream
@Version: V0.0.1
@Date: 2020-07-02 09:49:12
@LastEditors: Stream
@LastEditTime: 2020-07-02 11:01:39
@FilePath: \timelogfile.py
@ChangeLog: ChangeLog
'''
import sys
import os
import time


def creat_time_file_name():
    '''
    1.创建带时间的文件名
    2.文件名带重名检测
    '''
    # 获取当前系统时间
    time_str = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    print(time_str)

    # 获取当前文件夹所有文件名
    dir_ls = os.listdir()
    print(dir_ls)

    # 文件名合成及编号累加，防止重名
    serial_number = 0
    while(1):
        # 文件名合成
        file_name = ("log_%s_%d.txt") % (time_str, serial_number)
        # 防止重名
        if file_name in dir_ls:
            print("file exist")
            serial_number = serial_number+1
        else:
            print("file no exist")
            break
    print(file_name)
    return file_name


# 创建文件
log_file_name = creat_time_file_name()
myfile1 = open(log_file_name, 'a+')
myfile1.write("enter the first txt\n")
myfile1.close()
