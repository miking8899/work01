# !/usr/bin/env python
# coding=utf-8
from pandas import DataFrame
data = {'Date':['20190102','20190103','20190104'],'Open':[10,10.5,10.2],'Close':[10.5,10.2,10.3]}
df = DataFrame(data, columns=['Date','Open','Close'], index=['1','2','3'])
# 輸出Index(['1', '2', '3'], dtype='object')
print(df.index)     # 檢視索引
# 輸出Index(['Date', 'Open', 'Close'], dtype='object')
print(df.columns)   # 檢視列名
'''
[['20190102' 10.0 10.5]
 ['20190103' 10.5 10.2]
 ['20190104' 10.2 10.3]]
'''
print(df.values)    # 檢視數值
# 輸出[10.  10.5 10.2]
print(df['Open'].values)    # 檢視指定列的數值
'''
Date     20190102
Open           10
Close        10.5
Name: 1, dtype: object
'''
print(df.loc['1'])          # 檢視指定索引行的數值
# 檢視指定行的數值，結果等同print(df.loc['1']) 
print(df.iloc[0])