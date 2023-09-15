# !/usr/bin/env python
# coding=utf-8
stockInfoList = ['600001','600002']
try:
    print(stockInfoList[4]) # 索引出錯時會觸發
    # 1/0
except IndexError: 
    print('Index Error')    
try:
    # 參數的值正確，但傳回值不符合預期時會觸發 
    print(stockInfoList.index('600003'))    
except ValueError: 
    print('Value Error')
try:
    2+'error'   # 函數參數型態不正確時會觸發
except TypeError: 
    print('Type Error')
try:
    1/0 # 除零例外
except ZeroDivisionError: 
    print('ZeroDivision Error')
class Car:       
    def __init__(self,owner):
        self.owner = owner      
myCar = Car("Peter")
try:
    print(myCar.price)  # 參考屬性錯誤時觸發
except AttributeError: 
    print('Attribute Error')