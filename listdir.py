'''
@Description: 获取目标目录下的文件名
@Author: Stream
@Date: 2019-10-22 15:11:30
@LastEditTime: 2019-10-31 16:19:41
@LastEditors: Please set LastEditors
'''
import os
import sys

target_path = r'F:\SVN_RD\525-B18194A IntelligentLamp\2-Document\项目输出文档V01\受控版本v01-2019-10-28'  # windows下的路径


def my_listdir(dir_path):

    dir_ls = os.listdir(dir_path)  # 获取目标目录下的文件名
    print('files numbers is', len(dir_ls))  # 打印该目录下的文件数量
    file_dir_path = dir_path.replace('\\', '/')  # 将windows的路径分隔符转换成python的分隔符

    myfile1 = open(file_dir_path+r'\listdir.txt', 'w+')  # 将文件名写入txt
    for i in dir_ls:
        print(i)
        myfile1.writelines(str(i)+'\n')


my_listdir(target_path)
