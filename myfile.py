'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-21 17:57:11
@LastEditTime: 2019-08-23 09:50:24
@LastEditors: Please set LastEditors
'''


# -*- coding: UTF-8 -*-

import sys
import os
sys.stdout.write('stdout write 测试\n')

print('file test=====================================')
myfile1 = open("myfile1_2019-8-22.txt", 'a+')
myfile1.write("enter the first text\n")


myfile1 = open("myfile1_2019-8-22.txt", 'a+')
file_read_string = myfile1.read()
print(file_read_string)
