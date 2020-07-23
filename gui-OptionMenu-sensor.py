import tkinter


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


OptionMenuList = [
    "无        ",
    "湖北新普惠 ",
    "河北欧速   ",
    "邯郸研盛   ",
    "和而泰     ",
    "预留品牌1  ",
    "预留品牌2  ",
    "预留品牌3  ",
    "预留品牌4	",
]

variable_list = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
print(variable_list)

root = tkinter.Tk()
root.geometry("800x400")
root.title("Steam")

for i in range(30):
    variable = tkinter.StringVar()
    variable.set(OptionMenuList[0])
    variable_list[i] = variable


for j in range(3):
    for i in range(10):
        tkinter.OptionMenu(
            root, variable_list[i+10*j], *OptionMenuList).grid(row=i, column=1+2*j)
        tkinter.Label(root, text=name_list[i+10*j]).grid(row=i, column=0+2*j)


# for i in range(30):

#     tkinter.OptionMenu(
#         root, variable_list[i], *OptionMenuList).grid(row=i, column=1)
#     tkinter.Label(root, text=name_list[i]).grid(row=i, column=0)

root.mainloop()
