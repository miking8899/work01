# !/usr/bin/env python
# coding=utf-8

# 定義反昇排序的函數
def SortFunc(numArray):
    loopTimes = 0; # 記錄這個循環反昇排序的次數
    while loopTimes< len(numArray)-1: 
        # index為待比較元素的索引
        for index in range(len(numArray)-loopTimes-1):
            if numArray[index] > numArray[index+1]:
                tmp = numArray[index]
                numArray[index] = numArray[index+1]
                numArray[index+1] = tmp 
        loopTimes=loopTimes+1        
    return numArray

unSortedNums = [10,12,48,7,5,3]
print SortFunc(unSortedNums)