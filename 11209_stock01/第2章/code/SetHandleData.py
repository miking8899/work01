# !/usr/bin/env python
# coding=utf-8
# 以大括號的模式定義集合
set1 = {'1', '3', '5', '7'}
set2 = {'2', '3', '6', '7'}
# 不能用中括號的模式定義集合，例如 set1 = ['1', '3', '5', '7']
# 交集 
set3 = set1 & set2
print(set3)             # 輸出 set(['3', '7'])
print(set1 & set2)      # 輸出 set(['3', '7'])   
print(set1.intersection(set2)) # 輸出 set(['3', '7'])
# 聯集
set4 = set1 | set2
print(set4)             # 輸出set(['1', '3', '2', '5', '7', '6'])
print(set1 | set2)      # set(['1', '3', '2', '5', '7', '6'])  
print(set1.union(set2)) # set(['1', '3', '2', '5', '7', '6']) 
# 差集
print(set1 - set2)              # 輸出set(['1', '5'])
print(set1.difference(set2))    # 輸出set(['1', '5'])
print(set2 - set1)              # 輸出set(['2', '6'])
print(set2.difference(set1))    # 輸出set(['2', '6'])
# 示範不可變集合的特性
unChangedSet = frozenset(3.14,9.8)
# unChangedSet.add(2.718)
# unChangedSet[0]=2.718
# unChangedSet.discard(3.14)