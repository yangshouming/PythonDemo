'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-26 11:42:04
@LastEditTime: 2019-08-26 14:57:40
@LastEditors: Please set LastEditors
'''
# -*- coding: UTF-8 -*-


class my_class:
    '''
    class doc
    '''
    number1 = 123  # 类变量 对象之间是独立的，外部可以直接访问
    str1 = 'str1'

    def __init__(self):
        self.i = 0

    def add(self, num1, num2):
        sum = 0  # 局部变量，仅函数内有效
        sum = num1+num2
        number1 = sum
        print(number1)
        return sum

    def dec(self, num1, num2):
        temp = 0
        temp = num1-num2
        number1 = temp
        print(number1)
        return temp

    def add2(self, num1, num2):
        temp = 0
        temp = num1+num2
        self.number1 = temp
        print(self.number1)
        return temp

    def prt(self):
        print(self)
        print(self.__class__)


isinstance1 = my_class()
isinstance2 = my_class()

isinstance1.add(10, 12)
print(isinstance1.number1)
print(isinstance2.number1)

isinstance1.number1 = 111
isinstance2.number1 = 222
isinstance2.add(20, 22)

isinstance1.add2(10, 12)
isinstance2.add2(20, 22)

print(isinstance1.number1)
print(isinstance2.number1)


isinstance1.prt()
isinstance2.prt()


class my_class2(my_class):
    '''
    类 继承
    '''

    def add(self, num1, num2):
        sum = 0  # 局部变量，仅函数内有效
        sum = num1+num2+100
        number1 = sum
        print(number1)
        return sum


isinstance3 = my_class2()
isinstance3.add(10, 12)
isinstance3.add2(10, 12)


def acc(num):
    sum = 0
    for i in num:
        sum += num[i]
    print(sum)


num_list = range(10)
acc(num_list)
