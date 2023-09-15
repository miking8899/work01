# !/usr/bin/env python
# coding=utf-8

priceList = [10.58,25.47,100.58,500.47] 
cityList = ["ShangHai", "HangZhou", "NanJing"] 

# 進行排序
priceList.sort()
print(priceList);
# print(priceList.sort()); # 錯誤的用法

print(sum(priceList))   # 求和
print(max(priceList))   # 求最大值，輸出500.47
print(min(cityList))    # 求最小值，輸出HangZhou

subList = priceList[1:3] #截取陣列中元素
print(subList) # 輸出[25.47, 100.58]
