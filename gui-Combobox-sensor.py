import binascii
import tkinter
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
import time
import _thread

import serial
import serial.tools.list_ports

name_list = [
    "传感器1 ",
    "传感器2 ",
    "传感器3 ",
    "传感器4 ",
    "传感器5 ",
    "传感器6 ",
    "传感器7 ",
    "传感器8 ",
    "传感器9 ",
    "传感器10",
    "传感器11",
    "传感器12",
    "传感器13",
    "传感器14",
    "传感器15",
    "传感器16",
    "传感器17",
    "传感器18",
    "传感器19",
    "传感器20",
    "传感器21",
    "传感器22",
    "传感器23",
    "传感器24",
    "传感器25",
    "传感器26",
    "传感器27",
    "传感器28",
    "传感器29",
    "传感器30",
]


root = tkinter.Tk()
root.geometry("800x400+1000+100")
root.title("Steam")

Combobox_list = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

for j in range(3):
    for i in range(10):
        numberChosen = ttk.Combobox(root, width=12, state='readonly')
        numberChosen['values'] = ("无", "湖北新普惠", "河北欧速", "邯郸研盛",
                                  "和而泰", "预留品牌1", "预留品牌2", "预留品牌3", "预留品牌4",)  # 设置下拉列表的值
        numberChosen.current(0)  # 设置下拉菜单的默认值
        numberChosen.grid(row=i, column=1+3*j)  # 布局
        Combobox_list[i+10*j] = numberChosen  # 保存列表到全局变量

        tkinter.Label(root, text=name_list[i+10*j]
                      ).grid(row=i, column=0+3*j)  # 标签名字


def Button_reset_callbakc(Button_number):
    print("Button_reset_callbakc", Button_number)
    for i in range(30):
        Combobox_list[i].current(Button_number)
        print("text number", i, Combobox_list[i].current())


# command=lambda: Button_reset_callbakc(i)
# 我们使用Button传递数值时，需要用：lambda: 功能函数(var1, var2, ……)

i = 0

ttk.Button(root, text="复位全部", command=lambda: Button_reset_callbakc(0)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="湖北新普惠", command=lambda: Button_reset_callbakc(1)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="河北欧速", command=lambda: Button_reset_callbakc(2)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="邯郸研盛", command=lambda: Button_reset_callbakc(3)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="和而泰", command=lambda: Button_reset_callbakc(4)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="预留品牌1", command=lambda: Button_reset_callbakc(5)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="预留品牌2", command=lambda: Button_reset_callbakc(6)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="预留品牌3", command=lambda: Button_reset_callbakc(7)).grid(
    row=i, column=10)
i = i+1

ttk.Button(root, text="预留品牌4", command=lambda: Button_reset_callbakc(8)).grid(
    row=i, column=10)
i = i+1


def Button_debug_callbakc():
    print("Button_debug_callbakc")
    for i in range(30):
        print("Combobox index", i, Combobox_list[i].current())


ttk.Button(root, text="测试", command=Button_debug_callbakc).grid(
    row=i, column=10)
i = i+1

# 串口UI------------------------------------------------------------------
column_port_lable = 11
column_port_menu = 12
Canvas_size = 20
ser = 0


def GetCom():
    """获取并存储串口号到数组"""
    port_list = list(serial.tools.list_ports.comports())
    print(len(port_list))
    portcnt = len(port_list)
    serial_com = []
    for m in range(portcnt):
        port_list_1 = list(port_list[m])
        serial_com.append(port_list_1[0])
    return serial_com


def Com_Ctrl(com, bps):
    '''串口开关'''
    global Button_open_textvariable
    global Canvas_open
    global Canvas_size
    global ser
    if Button_open_textvariable.get() == "打开串口":
        Button_open_textvariable.set("关闭串口")
        Canvas_open.create_rectangle(
            0, 0, Canvas_size, Canvas_size, fill="green")
        ser = serial.Serial(
            port=com,
            baudrate=int(bps),
            timeout=1,
        )
        if ser.is_open:
            print('打开串口')
            pass
        else:
            ser.open()
            print('打开串口')
        # recv_data = threading.Thread(target=thread_recv)
        # recv_data.start()
    else:
        Button_open_textvariable.set("打开串口")
        Canvas_open.create_rectangle(
            0, 0, Canvas_size, Canvas_size, fill="gray")
        if ser.is_open:
            ser.close()
            print('关闭串口')
        else:
            pass


# COM
Combobox_COM = ttk.Combobox(root, width=12, state='readonly')
Combobox_COM['values'] = GetCom()  # 设置下拉列表的值
Combobox_COM.current(0)  # 设置下拉菜单的默认值
Combobox_COM.grid(row=0, column=column_port_menu)  # 布局
tkinter.Label(root, text='端口号').grid(row=0, column=column_port_lable)  # 标签名字

# 波特率
Combobox_baute = ttk.Combobox(root, width=12, state='readonly')
Combobox_baute['values'] = ("4800", "9600", "19200",
                            "38400", "115200")  # 设置下拉列表的值
Combobox_baute.current(1)  # 设置下拉菜单的默认值
Combobox_baute.grid(row=1, column=column_port_menu)  # 布局
tkinter.Label(root, text='波特率').grid(row=1, column=column_port_lable)  # 标签名字

# 打开串口

Button_open_textvariable = tkinter.StringVar()
Button_open_textvariable.set("打开串口")

# 状态图标
Canvas_open = tkinter.Canvas(root, width=Canvas_size, height=Canvas_size)
Canvas_open.grid(row=2, column=column_port_lable)
Canvas_open.create_rectangle(0, 0, Canvas_size, Canvas_size, fill="gray")


def Button_open_COM_callbakc():
    Com_Ctrl(Combobox_COM.get(), Combobox_baute.get())


Button_open = ttk.Button(
    root, textvariable=Button_open_textvariable, command=Button_open_COM_callbakc)
Button_open.grid(row=2, column=column_port_menu)

# 某品牌传感器应答指令
xinpuhui_cmd_list = [
    '01 11 12 34 3f',  # 01
    '02 11 12 34 3f',  # 02
    '03 11 12 34 3f',  # 03
    '04 11 12 34 3f',  # 04
    '05 11 12 34 3f',  # 05
    '06 11 12 34 3f',  # 06
    '07 11 12 34 3f',  # 07
    '08 11 12 34 3f',  # 08
    '09 11 12 34 3f',  # 09
    '0A 11 12 34 3f',  # 10
    '0B 11 12 34 3f',  # 11
    '0C 11 12 34 3f',  # 12
    '0D 11 12 34 3f',  # 13
    '0E 11 12 34 3f',  # 14
    '0F 11 12 34 3f',  # 15
    '10 11 12 34 3f',  # 16
    '11 11 12 34 3f',  # 17
    '12 11 12 34 3f',  # 18
    '13 11 12 34 3f',  # 19
    '14 11 12 34 3f',  # 20
    '15 11 12 34 3f',  # 21
    '16 11 12 34 3f',  # 22
    '17 11 12 34 3f',  # 23
    '18 11 12 34 3f',  # 24
    '19 11 12 34 3f',  # 25
    '1A 11 12 34 3f',  # 26
    '1B 11 12 34 3f',  # 27
    '1C 11 12 34 3f',  # 28
    '1D 11 12 34 3f',  # 29
    '1E 11 12 34 3f',  # 30
]


ousu_cmd_list = [
    '01 11 12 34 3f',  # 01
    '02 11 12 34 3f',  # 02
    '03 11 12 34 3f',  # 03
    '04 11 12 34 3f',  # 04
    '05 11 12 34 3f',  # 05
    '06 11 12 34 3f',  # 06
    '07 11 12 34 3f',  # 07
    '08 11 12 34 3f',  # 08
    '09 11 12 34 3f',  # 09
    '0A 11 12 34 3f',  # 10
    '0B 11 12 34 3f',  # 11
    '0C 11 12 34 3f',  # 12
    '0D 11 12 34 3f',  # 13
    '0E 11 12 34 3f',  # 14
    '0F 11 12 34 3f',  # 15
    '10 11 12 34 3f',  # 16
    '11 11 12 34 3f',  # 17
    '12 11 12 34 3f',  # 18
    '13 11 12 34 3f',  # 19
    '14 11 12 34 3f',  # 20
    '15 11 12 34 3f',  # 21
    '16 11 12 34 3f',  # 22
    '17 11 12 34 3f',  # 23
    '18 11 12 34 3f',  # 24
    '19 11 12 34 3f',  # 25
    '1A 11 12 34 3f',  # 26
    '1B 11 12 34 3f',  # 27
    '1C 11 12 34 3f',  # 28
    '1D 11 12 34 3f',  # 29
    '1E 11 12 34 3f',  # 30
]

sensor_cmd_list = [
    xinpuhui_cmd_list,
    ousu_cmd_list,
]

# print(sensor_cmd_list)
# print(sensor_cmd_list[0])


def Button_send_COM_callbakc():
    if ser.is_open:
        # 字符转16进制
        tx_data = bytes.fromhex(xinpuhui_cmd_list[1])
        ser.write(tx_data)
    else:
        print("请打开串口")


Button_send = ttk.Button(
    root, text='发送', command=Button_send_COM_callbakc)
Button_send.grid(row=3, column=column_port_menu)


# def com_recv(threadName, delay):

#     global ser
#     while 1:
#         print("com_recv")
#         # n = ser.inwaiting()
#         # if n:
#         #     data = str(binascii.b2a_hex(ser.read(n)))[2:-1]
#         #     print(data)
#         time.sleep(1)


def com_recv(threadName, delay):
    global ser
    while 1:
        if(ser):
            n = ser.in_waiting()
            if n:
                data = str(binascii.b2a_hex(ser.read(n)))[2:-1]
                print(data)

        print("%s: %s" % (threadName, time.ctime(time.time())))
        time.sleep(delay)


_thread.start_new_thread(com_recv, ("Thread-COM-RECV", 4, ))
_thread.start_new_thread(root.mainloop(), ("Thread-GUI", 2, ))
