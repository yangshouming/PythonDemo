'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-23 09:50:00
@LastEditTime: 2019-08-23 11:41:35
@LastEditors: Please set LastEditors
'''
# -*- coding: UTF-8 -*-

import sys
import os

# 在文件夹的后面添加序号，01 02 ...

# 创建文件夹的的路径，在该路径下创建子文件夹 'D:\\04MyFile\\Python\\Code\\demo\\PythonDemo\\Location_01'
dir_path = 'D:\\04MyFile\\Python\\Code\\demo\\PythonDemo\\Location_01'
# 主要的文件名，包括需要的下划线等
dir_name_main = 'Scene_'
# 创建的数量
dir_numbers = 10
# 序号的宽度
dir_name_width = 2


def batch_make_dir(dir_path, dir_name_main, dir_numbers=10, dir_name_width=2):
    '''
    当前目录下，批量添加文件夹
    '''
    path_exist = os.path.exists(dir_path)
    if path_exist:
        print("父文件夹存在,则不需要创建")
    else:
        print("父文件夹不存在，需要创建")
        os.makedirs(dir_path)

    dir_name_new = 'enmpty'
    for i in range(1, dir_numbers):
        dir_sequence = ('%02d') % (i)
        dir_sequence = dir_sequence.zfill(dir_name_width)
        dir_name_new = (dir_path+'\\'+dir_name_main+dir_sequence)
        os.makedirs(dir_name_new)
        print(dir_name_new)


batch_make_dir(dir_path, dir_name_main, dir_numbers, 3)
