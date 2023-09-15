# coding=utf-8
from pandas import Series
import pandas as pd
s1 = Series(range(3),index = ["one","two","three"])
'''
print(s1)輸出如下
one      0
two      1
three    2
dtype: int32
'''
print(s1)
s2 = {'one': 1, 'two': 2, 'three': 3}
print(s2)           # {'two': 2, 'one': 1, 'three': 3}
print(s1[0])        # 輸出0
print(s1['one'])    # 輸出0
# 拋出例外，找不到索引 print(s2['four']) 
arr = range(3)
# 陣列轉Series
s3 = pd.Series(arr)
'''
print(s3)輸出
0    0
1    1
2    2
dtype: int32
'''
print(s3) 
print(s3[0])        # 輸出0