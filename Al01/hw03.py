#請輸入購買金額-POST 機

import pyinputplus as pyip
money=0.0

while True:
    money=pyip.inputInt("請輸入購買金額(元):",min=0)
    discount=1.0
    if money>=100000 :
        discount=0.8
    elif money>=50000:
        discount=0.85
    elif money>=30000:
        discount=0.9
    elif money>=10000:
        discount=0.95
    print("")
    print("打",discount*10,"折")
    print("應收金額: ",round(money*discount,1),"元")

