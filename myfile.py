'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-21 17:57:11
@LastEditTime: 2019-12-03 17:53:03
@LastEditors: Please set LastEditors
'''


# -*- coding: UTF-8 -*-

import sys
import os
import numpy

arr_data = [1, 2, 3, 4]


sys.stdout.write('stdout write \n')

print('file test=====================================')
myfile1 = open("myfile1_2019-8-22.txt", 'a+')
myfile1.write("enter the first text\n")
myfile1.write(str(arr_data))

myfile1 = open("myfile1_2019-8-22.txt", 'a+')
file_read_string = myfile1.read()
print(file_read_string)


fp = open('2019-12-3.txt', 'r')
ls = []
for line in fp:
    line = line.strip('\n')  # 将\n去掉
    ls.append(line.split(' '))  # 将空格作为分隔符将一个字符切割成一个字符数组

fp.close()
ls = numpy.array(ls, dtype=float)  # 将其转换成numpy的数组，并定义数据类型为float
print(ls)


# list_txt = list(file_read_string)
# print(list_txt)
