import tkinter
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
import time


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


OptionMenuList = (
    "无        ",
    "湖北新普惠 ",
    "河北欧速   ",
    "邯郸研盛   ",
    "和而泰     ",
    "预留品牌1  ",
    "预留品牌2  ",
    "预留品牌3  ",
    "预留品牌4	",
)

variable_list = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

root = tkinter.Tk()
root.geometry("800x400+1000+100")
root.title("Steam")


# for i in range(30):
#     variable = tkinter.StringVar()
#     variable.set(OptionMenuList[0])
#     variable_list[i] = variable
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

        tkinter.Label(root, text=name_list[i+10*j]).grid(row=i, column=0+3*j)

for i in range(9):
    Combobox_list[i].current(i)


def Button_reset_callbakc(Button_number):
    print("Button_reset_callbakc", Button_number)
    for i in range(30):
        Combobox_list[i].current(Button_number)
        print("text number", i, Combobox_list[i].get())


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


# for i in range(10):
#     numberChosen = ttk.Combobox(root)
#     numberChosen['values'] = ("无", "湖北新普惠", "河北欧速", "邯郸研盛",
#                               "和而泰", "预留品牌1", "预留品牌2", "预留品牌3", "预留品牌4",)  # 设置下拉列表的值
#     numberChosen.current(0)  # 设置下拉菜单的默认值
#     numberChosen.grid(row=i, column=10)
#     Combobox_list[i] = numberChosen

root.mainloop()
