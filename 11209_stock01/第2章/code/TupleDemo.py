# !/usr/bin/env python
# coding=utf-8
# 定義兩個元群組
cityTup = ("TianJin","WuHan","ChengDu")
#cityTup[0] = "HeFei" # 會拋出例外
#del cityTup[0] # 無法移除其中的元素，則會拋出例外
print(cityTup)  # 輸出結果是('TianJin', 'WuHan', 'ChengDu')
# 把清單轉為元群組
bookList = ["Python book","Java Book"]
bookTup = tuple(bookList) #把清單轉為元群組

# 查詢動作
print(cityTup[1])   # 輸出WuHan
print(cityTup[0:2]) # 輸出('TianJin', 'WuHan')

#統計元群組裡指定元素的個數
print(cityTup.count("TianJin"))  # 傳回1
#統計元群組的長度
print(len(cityTup))  # 傳回3

# 只能移除整個元群組物件
del cityTup
