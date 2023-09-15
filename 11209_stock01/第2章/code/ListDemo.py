# !/usr/bin/env python
# coding=utf-8

priceList = [10.58,25.47,100.58] # 浮點型清單
cityList = ["ShangHai", "HangZhou", "NanJing"] # 字串型態清單
mixList = [1, 3.14, "Company"] #混合型態的清單，謹慎使用
  
# 在主控台輸出
print(priceList)  #[10.58, 25.47, 100.58]
print(cityList)   #['ShangHai', 'HangZhou', 'NanJing']
print(mixList)    #[1, 3.14, 'Company']

del mixList[2]
print(mixList)    # 沒有了最後一個元素
#mixArr.remove(2) # 去掉沒有的元素，也會拋出例外
mixList.remove(1)
print(mixList)    # 也看不到1了

print(priceList[0])      # 獲得陣列指定位置的元素，這裡輸出的是10.58
priceList.append(200.74) # 加入元素
print(priceList)         # 能看到加入後的元素
print(cityList.index("ShangHai"));
#print(cityList.index("DaLian")); # 若果找不到元素，會拋出例外並終止程式


