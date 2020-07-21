import tkinter

OptionMenuList = [
    "无",
    "Beijing",
    "Shanghai",
    "Tianjin",
    "Aomen",
    "Xianggang",
    "Hankou"
]

list1 = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
print(list1)

root = tkinter.Tk()
root.geometry("800x400")
root.title("Steam")

for i in range(30):
    variable = tkinter.StringVar()
    variable.set("无")
    list1[i] = variable

# variable1 = tkinter.StringVar()
# variable1.set("无")
# list1[1] = variable1


for i in range(30):

    tkinter.OptionMenu(root, list1[i], *OptionMenuList).grid(row=i, column=1)
    tkinter.Label(root, text="用户名：").grid(row=i, column=0)

root.mainloop()
