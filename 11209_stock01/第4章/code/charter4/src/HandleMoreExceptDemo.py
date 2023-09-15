# !/usr/bin/env python
# coding=utf-8
def divide(x,y):
    try:
        return x/y
    except(ZeroDivisionError, TypeError, Exception) as e:
        print(e) 
# 如下是各種錯誤的呼叫       
print(divide(1,'1'))    # 觸發TypeError例外
print(divide(1,0))      # 觸發ZeroDivisionError