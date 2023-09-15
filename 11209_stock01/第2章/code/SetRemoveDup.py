# !/usr/bin/env python
# coding=utf-8
# 呼叫集合的方法把清單轉換成集合
set1 = set(["a", "a", "b", "b", "c"])
print(set1) # 輸出set(['a', 'c', 'b'])
# 加入元素
set1.add("d")
set1.add("c")   # 由於重復，因此無法加入
print(set1)     # set(['a', 'c', 'b', 'd'])

set2 = set1.copy()
set1.clear()
print(set1)     # 由於已清理，因此輸出set([])
print(set2)     # set(['a', 'c', 'b', 'd'])

set2.discard("f") # 移除元素，哪怕沒找到也不會拋出例外

list=[1,1,2,2,3,3,4,4,5] # 含重復元素的清單
setFromList=set(list)    # 透過集合去掉重復的元素
print(setFromList)       # 輸出為set([1, 2, 3, 4, 5])