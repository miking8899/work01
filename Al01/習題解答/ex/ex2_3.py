# ex2_3.py
from array import *      

x = array('l', [1, 11, 22, 33, 44, 55])
print('陣列內容如下: ')
for data in x:
    print(data)
index = eval(input('請輸入欲插入的索引 : '))
num = eval(input('請輸入欲插入的數值 : '))
if index > 5 and index < 0:
    print("輸入錯誤")
else:
    x.insert(index, num)
    for data in x:
        print(data)







