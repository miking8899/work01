# !/usr/bin/env python
# coding=utf-8
# 定義降冪規則
def desc(x, y):
    if x < y:
        return 1    # 若果x小於y，則x排在y之前
    elif x > y:
        return -1   # 若果大於y，則x排在y之後
    else:
        return 0    # 否則並列
# 定義待排序的numbers清單  
numbers = [5, 58, 47 ,75 ,100]
numbers.sort(desc) # 在排序時用到desc方法 
print numbers      # 輸出[100, 75, 58, 47, 5]
numbers.sort()
print numbers      # 輸出[5, 47, 58, 75, 100]