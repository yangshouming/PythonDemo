import math

import serial

print(" =========================== enter python learn =========================== ")


print(" =========================== for  range =========================== ")  # 当前学习内容

for i in range(1, 3, 1):
    print(i)
for i in range(3):
    print(i*10)

print(" =========================== while  =========================== ")  # 当前学习内容

i = 0
while i < 3:
    print(i)
    i = i + 1
    if (i % 2 == 0):
        break

L = ['Bart', 'Lisa', 'Adam']
for l_index in L:
    print("hello,", l_index)

print(" =========================== dict  =========================== ")  # 当前学习内容

d_test = {"name": "tom", "age": 6}
for i in d_test:
    print(i, d_test[i])


key_value = d_test.get("name", 'not exist')
if (key_value != 'not exist'):
    print("exist", key_value)
else:
    print(key_value)

print(" =========================== 三引号 多行 打印  =========================== ")  # 当前学习内容
print(
    """hello world!
hello world!
hello world!
hello world!""")

print(" =========================== 数据类型转换 字符串 整数 浮点数 =========================== ")  # 当前学习内容
str1 = "123456789"
str2 = "3.14"
str1num = int(str1)
str2num = float(str2)

print(str1num)
print(str2num)

print(" =========================== 格式化打印 =========================== ")  # 当前学习内容

int_num = 123456
float_num = 3.1314

print("int_num %d float_num %02.1f str1 %s int_num_hex %#X" %
      (int_num, float_num, str1, int_num))

print(" =========================== 列表 =========================== ")  # 当前学习内容
ls_test = ["ls_str", 123456, 3.14]
for i in ls_test:
    print(i)
ls_test.append("aaaa")
for i in ls_test:
    print(i)


print(" =========================== if  =========================== ")  # 当前学习内容
if ((int_num > 100) & (float_num > 4)):
    print("true")
else:
    print("false")

"""
print(" =========================== 键盘输入  =========================== ")  # 当前学习内容
print("BMI TEST")
input_str = input("请输入身高(米)，回车结束:\n")
hight = float(input_str)
input_str = input("请输入体重(KG)，回车结束:\n")
weight = float(input_str)
bmi = weight/(hight**2)
print("你的BMI系数是%d" % bmi)
if(bmi < 18.5):
    print("低于18.5：过轻")
elif (bmi < 25):
    print("18.5-25：正常")
elif (bmi < 28):
    print("25-28：过重")
elif (bmi < 32):
    print("28-32：肥胖")
else:
    print("高于32：严重肥胖")
print("测试结束")
"""
print(" =========================== list  =========================== ")  # 当前学习内容
l1 = [123, 3.14, '456']
for i in l1:
    print(i)
print(l1)
print(" =========================== dict  =========================== ")  # 当前学习内容
d1 = {"k1": 1, 'k2': 2, '3': 3}
for i in d1:
    print(i)
print(d1)
print(" =========================== set  =========================== ")  # 当前学习内容
s1 = {1, 2, 3, 4, 5, 6, 6, 6, 7, 7}  # set 集合是用大括号{} 或者用set函数
for i in s1:
    print(i)
print(s1)
print(" =========================== tuple  =========================== ")  # 当前学习内容
t1 = (1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 77, 7, 7)  # tuple 元组 是用小括号
for i in t1:
    print(i)
print(t1)

print(" =========================== function  =========================== ")  # 当前学习内容
n1 = 255
n2 = 1000

n1_h = hex(n1)
print(n1_h)
n2_h = hex(n2)
print(n2_h)


def add_func(a, b):
    print("add_func:%d+%d=%d" % (a, b, (a+b)))


def abs_func(a):
    # this a func note doc
    # 必选参数
    # 传入参数检测
    if not isinstance(a, (float, int)):
        raise TypeError("input type error")
    if(a < 0):
        print("negative", -a)
        return -a
    else:
        print('positive', a)
        return a


add_func(1, 5)
abs_func(5)
abs_func(-5)
# abs_func('a')


def default_func(a, b=5):
    # 默认参数
    print(a+b)


default_func(3)
default_func(3, 6)


def variable_func(*a):
    # 可变参数
    for i in a:
        print(i)
    print(a)


variable_func(l1)  # 传入一个list,函数内部会处理成以list为元素的tuple
variable_func(*l1)  # 传入list的元素，,函数内部会处理成以list元素为元素的tuple，即元组的内容与列表相同

print(" =========================== 关键字参数  =========================== ")  # 当前学习内容


def key_func(a, **b):
    print(a)
    print(b)


extra = {'city': 'Beijing', '1': 'Engineer'}
key_func(1, key1='123')
key_func(2, **extra)

print(" =========================== 全部参数  =========================== ")  # 当前学习内容


def all_func(a, *b, c='c', **d):
    # 参数 a-必选 b-可选 c-命名关键字+默认 d-关键字
    print(a)
    print(b)
    print(c)
    print(d)


# all_func(1, "b", c='c value', **extra)
# all_func(1, "b", c='3 value', d='4 vvv')

all_func(111)
all_func(222, *l1)
all_func(222, *l1, c='new c')
all_func(222, *l1, c='new c', **d1)


def string_del_space(str3):
    print(str3)
    if(str3[0] == ' '):
        print("del head")
        str_temp1 = str3[1:]
    if(str3[-1] == ' '):
        print('del end')
        str_temp1 = str_temp1[0:-1]
        print(str_temp1.replace('2', 'a', 2))
    print(str_temp1)


string_del1 = ' 123'
string_del_space(string_del1)
