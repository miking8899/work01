# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl  
# 從檔案中讀取資料
df = pd.read_csv('D:/stockData/ch6/600895.csv',encoding='gbk',index_col=0)
# 設定圖的位置
fig = plt.figure()
ax = fig.add_subplot(111)
# 呼叫方法繪制K線圖 
candlestick2_ochl(ax = ax, 
                  opens=df["Open"].values, closes=df["Close"].values,
                  highs=df["High"].values, lows=df["Low"].values,
                  width=0.75, colorup='red', colordown='green')
df['Close'].rolling(window=3).mean().plot(color="red",label='3日均線')
df['Close'].rolling(window=5).mean().plot(color="blue",label='5日均線')
df['Close'].rolling(window=10).mean().plot(color="green",label='10日均線')
plt.legend(loc='best')  # 繪制圖例
# 設定x軸的標簽 
plt.xticks(range(len(df.index.values)),df.index.values,rotation=30 ) 
ax.grid(True)           # 帶網格線
plt.title("600895張江高科的K線圖")
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.show()