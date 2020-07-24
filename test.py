import serial
import serial.tools.list_ports
import tkinter

root = tkinter.Tk()
root.geometry("800x400")
root.title("Steam")

port_list = list(serial.tools.list_ports.comports())
if len(port_list) == 0:
    print('找不到串口')
else:
    for i in range(0, len(port_list)):
        print('序号%d :' % (i+1), port_list[i])


tuple_list = tuple(serial.tools.list_ports.comports())
index = 0
print(tuple_list[index][0])

variable = tkinter.StringVar()
variable.set(port_list[0])
tkinter.OptionMenu(
    root, variable, *port_list).grid(row=0, column=0)


# str_com = list(port_list[0])
# sPort = str_com[0]  # 获取串口号 字符形式
# print(sPort)


root.mainloop()
