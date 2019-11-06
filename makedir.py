'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-23 09:50:00
@LastEditTime: 2019-10-29 09:15:47
@LastEditors: Please set LastEditors
'''
# -*- coding: UTF-8 -*-

import sys
import os

import shutil

# 在文件夹的后面添加序号，01 02 ...

# 创建文件夹的的路径，在该路径下创建子文件夹
# 'D:\\04MyFile\\Python\\Code\\demo\\PythonDemo\\Location_01'
# 'D:\\04MyFile\\Python\\Code\\demo\\PythonDemo\\Location_01\\Scene__01'
dir_path = r'./OutPut'  # 当前工作目录  ./OutPut
# 主要的文件名，包括需要的下划线等
dir_name_1 = 'Location_'  # Location_     Scene_     T_
dir_name_2 = 'Scene_'  # Location_     Scene_     T_
dir_name_3 = 'T_'  # Location_     Scene_     T_

# 创建的数量
creart_dir_numbers = 100
# 序号的宽度
dir_name_width = 2


def num2sequence(num, dir_name_width=2):
    dir_sequence = ('%02d') % (num)
    dir_sequence = dir_sequence.zfill(dir_name_width)
    return dir_sequence


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

        # dir_sequence = ('%02d') % (i)
        # dir_sequence = dir_sequence.zfill(dir_name_width)
        dir_sequence = num2sequence(i)

        dir_name_new = (dir_path+'\\'+dir_name_main+dir_sequence)

        path_exist = os.path.exists(dir_name_new)
        if path_exist:
            print("目标文件夹存在")
        else:
            print("目标文件夹不存在")
            os.makedirs(dir_name_new)
        print(dir_name_new)


# batch_make_dir(dir_path, dir_name_3, creart_dir_numbers, dir_name_width)

cnt = 0
for l in range(1, 4):
    for s in range(1, 6):

        l_sequence = num2sequence(l)
        s_sequence = num2sequence(s)

        dir_path_new = 'enmpty'
        dir_path_new = (dir_path +
                        '\\'+dir_name_1 + l_sequence +
                        '\\'+dir_name_2+s_sequence)
        print(dir_path_new)
        cnt += 1
        batch_make_dir(dir_path_new, dir_name_3,
                       creart_dir_numbers+1, dir_name_width)
print('cnt', cnt)


if POSE == 1:
    POSE = 56
elif POSE >= 2:
    POSE = POSE-1
