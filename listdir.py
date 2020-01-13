'''
@Description: 获取目标目录下的文件名
@Author: Stream
@Date: 2019-10-22 15:11:30
@LastEditTime: 2019-10-31 16:19:41
@LastEditors: Please set LastEditors
'''
import os
import sys

target_path = r'F:\SVN_RD\525-C19214A IntelligentWardrobSystem\2-Document\1-软件\10-临时文件\首次整机调试'  # windows下的路径


def my_listdir(dir_path):

    dir_ls = os.listdir(dir_path)  # 获取目标目录下的文件名
    print('files numbers is', len(dir_ls))  # 打印该目录下的文件数量
    file_dir_path = dir_path.replace('\\', '/')  # 将windows的路径分隔符转换成python的分隔符

    myfile1 = open(file_dir_path+r'\文件说明.txt', 'w+')  # 将文件名写入txt
    for i in dir_ls:
        print(i)
        myfile1.writelines(str(i)+'\n')


my_listdir(target_path)
