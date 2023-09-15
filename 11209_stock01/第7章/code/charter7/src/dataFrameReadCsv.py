# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
# 從檔案中讀取資料
df = pd.read_csv('D:/stockData/ch6/600895.csv',encoding='gbk',index_col='Date')
print(df.head(1))   # 列印第1行資料
print(df.tail(2))   # 列印最後2行的資料
print(df.index.values)      # 列印索引列（Date）資料
print(df['Close'].values)   # 列印索引列（Date）資料
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)       # 帶網格線
df['Open'].plot(color="red",label='Open')#繪制開碟價 
df['Close'].plot(color="blue",label='Close')#繪制收碟價
plt.legend(loc='best')      # 繪制圖例
# 設定x軸的標簽
plt.xticks(range(len(df.index.values)),df.index.values,rotation=30 ) 
plt.show()