# !/usr/bin/env python
# coding=utf-8
# 定義一個加法的函數add
def add(x, y):
    return x + y
print(reduce(add, [1,2,3,4,5]))     # 輸出15
print(reduce(add, [1,2,3,4,5],100)) # 輸出115
# 定義乘法的函數
def multiply(x,y):
    return x*y
print(reduce(multiply, [1,2,3,4,5]))  # 輸出120
# 定義拼接數字的函數
def combineNumber(x, y):
    return x * 10 + y
print(reduce(combineNumber, [1,2,3,4,5])) # 輸出12345