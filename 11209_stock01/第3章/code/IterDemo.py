# !/usr/bin/env python
# coding=utf-8
class createEven:           # 有“可檢查需求”的類別
    def __init__(self, min, max):
        self.value = min
        self.min = min
        self.max = max
    def __iter__(self):     # 輸出全部
        print("in iter")     
        return self
    def __next__(self):     # 產生下一個偶數
        print("in next")
        self.value += 2
        return self.value
myEvenList = createEven(0,6)
for i in myEvenList:        # 輸出myEventList清單中不大於10的偶數
    print(i)
    if(i>=10):
        break        