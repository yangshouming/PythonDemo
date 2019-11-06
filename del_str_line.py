'''
@Author: your name
@Date: 2019-11-04 10:19:13
@LastEditTime: 2019-11-05 15:40:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \PythonDemo\del_str_line.py
'''

import sys
import os

cnt = 0
num = 0
with open("1101 st主控.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # print(lines)
with open("1101 st主控-t.txt", "w", encoding="utf-8") as f_w:
    for line in lines:
        num = num+1
        # if "ADC" in line:
        #     continue
        # f_w.write(line)
        line_temp = line[:-1]  # 去除\n换行符

        if line_temp.isnumeric():
            f_w.write(line)
        else:
            cnt = cnt+1
            print('del line num=', num, '   cnt=', cnt)
            continue
