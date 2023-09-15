# !/usr/bin/env python
# coding=utf-8
def square(x):     # 計算平方數
    return x ** 2
print map(square, [1,3,5])   # 輸出[1, 9, 25]

def strToLowCase(str):
    return str.lower()
strList=["Company","OFFICE"]
strList = map(strToLowCase,strList)
print(strList)      # ['company', 'office']

def tagCustomer(num):
    if num>5000:
        return "VIP"
    else:
        return "Normal"
print map(tagCustomer,[1000])   # ['Normal']   
#print map(tagCustomer,1000)    # 會顯示出錯