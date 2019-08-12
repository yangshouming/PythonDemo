print(" =========================== enter python learn =========================== ")


print(" =========================== for  =========================== ")  # 当前学习内容

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
