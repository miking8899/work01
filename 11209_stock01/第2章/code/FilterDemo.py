# !/usr/bin/env python
# coding=utf-8
# 判斷輸導入參數數是否是小寫字母的函數
def isLowCase(str):
    return str.lower() == str
strlist = filter(isLowCase, ["Hello","world"])
print(strlist)  # ['world']
# 判斷輸導入參數數是否為空的函數
def filterNull(empNo):
    return empNo.strip() !=''
dataFromFile=['101','102','103','']
empList = filter(filterNull,dataFromFile)
print(empList) # ['101', '102', '103']