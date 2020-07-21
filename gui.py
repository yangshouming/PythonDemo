'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-08-27 14:20:50
@LastEditTime: 2020-07-21 16:53:36
@LastEditors: Stream
'''
import tkinter
import tkinter.messagebox

main_windows = tkinter.Tk()  # 创建窗口
main_windows.title("Stream")  # 标题名字
main_windows.geometry('800x480')  # 宽x高

# list
li_msg = ['my', 'name', 'is', 'stream']
list_box = tkinter.Listbox(main_windows)

for i in li_msg:
    list_box.insert(0, i)
list_box.pack()


def add_messagebox():
    # 弹窗
    tkinter.messagebox.showinfo('showinfo', '123456789abc')
    tkinter.messagebox.askokcancel('askokcancel', '123456789abc')


# 按钮
my_button_cfg = {'text': '按钮-点击', 'bd': 8, }
my_button = tkinter.Button(main_windows, my_button_cfg,
                           command=add_messagebox)

my_button.pack()
my_button.flash()

my_button_cfg = {'text': '按钮-点击2', 'bd': 8, }
my_button2 = tkinter.Button(main_windows, my_button_cfg,
                            command=add_messagebox)

# my_button2.place(x=100, y=100, width=100, height=100)
my_button2.grid(row=1, column=1)

# 复选框
my_Checkbutton_cfg = {'text': '复选框', 'bd': 8, }
my_Checkbutton = tkinter.Checkbutton(main_windows, my_Checkbutton_cfg)
my_Checkbutton.flash()
my_Checkbutton.pack()

my_Entry_cfg = {'text': '输入框，请输入', 'bd': 8, 'show': '*'}
my_entry = tkinter.Entry(main_windows)
my_entry.pack()

# 进入消息循环
main_windows.mainloop()
