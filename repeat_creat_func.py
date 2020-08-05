'''
@Description: 根据模板批量生成函数，需要替代的部分用AAAAA/BBBBB/CCCCC表示，每次支持三个字符同时替换
@Author: Stream
@Version: V0.0.1
@Date: 2020-07-27 10:57:50
@LastEditors: Stream
@LastEditTime: 2020-07-27 14:16:57
@FilePath: \repeat_creat_func.py
@ChangeLog: ChangeLog
'''


import sys
import os

template_func = r"""
/*
* 函数名称 : Xinpuhui_AAAAA_BBBBB_CCCCC_data_parse_func
* 功能描述 : 数据解析
* 参    数 : @pdata 数据指针
			 @length 数据长度
* 返回值   : 0-正确 1-错误
* 示    例 : Xinpuhui_AAAAA_data_parse_func(pdata,length);
*/
/******************************************************************************/
int Xinpuhui_AAAAA_data_parse_func( uint8_t *pdata, uint16_t length )
{

    printf( "%s\r\n", __func__ );
    return 0;
}

"""

replace_str_list_AAAAA = [
    'ENV_AAAAA',
    'soil_AAAAA',
]

replace_str_list_BBBBB = [
    'ENV_BBBBB',
]

replace_str_list_CCCCC = [
    'ENV_CCCCC',
    'soil_CCCCC',
]

output_func = 0

myfile1 = open("repeat_creat_func_out.c", 'w+')

for i in range(len(replace_str_list_AAAAA)):
    output_func = template_func.replace('AAAAA', replace_str_list_AAAAA[i])

    if (i < (len(replace_str_list_BBBBB))):
        output_func = output_func.replace('BBBBB', replace_str_list_BBBBB[i])
    else:
        print("no BBBBB need to replace", i)
    if (i < (len(replace_str_list_CCCCC))):
        output_func = output_func.replace('CCCCC', replace_str_list_CCCCC[i])
    else:
        print("no CCCCC need to replace", i)

    myfile1.write(output_func)
    myfile1.write("\n")

myfile1.close()
