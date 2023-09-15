# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
# 從檔案中讀取資料
df = pd.read_excel('D:/stockData/ch5/600895.ss.xlsx')
for index,row in df.iterrows():
    df.at[index, 'NewDate'] = df.at[index, 'Date'].strftime('%Y-%m-%d')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)           # 帶網格線
df['High'].plot(color="red",label='High')   # 繪制最高價 
df['Low'].plot(color="blue",label='Low')    # 繪制最低價
plt.legend(loc='best')  # 繪制圖例
# 設定x軸的標簽
plt.xticks(range(len(df['NewDate'])),df['NewDate'].values,rotation=30 ) 
plt.show()