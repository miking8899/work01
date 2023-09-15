# coding=utf-8
# Print Hello World
from pandas import Series
import pandas as pd
s1 = Series(range(5),index = ["one","two","three","four","five"])
'''
s1.head(2) 輸出如下
one    0
two    1
dtype: int32
'''
print(s1.head(2))   # 若果不帶參數，預設傳回前5個
'''
s1.tail(2) 輸出如下
four    3
five    4
dtype: int32
'''
print(s1.tail(2))   # 若果不帶參數，預設傳回後5個
'''
s1.take([1,3]) 輸出如下
two     1
four    3
dtype: int32
'''
print(s1.take([1,3])) # 傳回指定位置的元素
'''
以切片的模式存取，如下兩句的輸出是一樣的
two      1
three    2
dtype: int32
'''
print(s1[1:3]) 
print(s1['two':'three'])