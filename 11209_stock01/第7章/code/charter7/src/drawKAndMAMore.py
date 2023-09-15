# !/usr/bin/env python
# coding=utf-8
import pandas_datareader
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl
from matplotlib.ticker import MultipleLocator 
# 根據指定程式碼和時間範圍取得股票資料
code='600895.ss'
stock = pandas_datareader.get_data_yahoo(code,'2019-01-01','2019-03-31')
# 移除最後一行，因為get_data_yahoo會多取一天的資料
stock.drop(stock.index[len(stock)-1],inplace=True)
# 儲存在本機
stock.to_csv('D:\\stockData\ch7\\600895.csv')
df = pd.read_csv('D:/stockData/ch7/600895.csv',encoding='gbk',index_col=0)
# 設定視窗大小
fig, ax = plt.subplots(figsize=(10, 8))
xmajorLocator   = MultipleLocator(5)    # 將x軸主刻度設定為5的倍數
ax.xaxis.set_major_locator(xmajorLocator)
# 呼叫方法繪制K線圖 
candlestick2_ochl(ax = ax, 
                  opens=df["Open"].values, closes=df["Close"].values,
                  highs=df["High"].values, lows=df["Low"].values,
                  width=0.75, colorup='red', colordown='green')

df['Close'].rolling(window=3).mean().plot(color="red",label='3日均線')
df['Close'].rolling(window=5).mean().plot(color="blue",label='5日均線')
df['Close'].rolling(window=10).mean().plot(color="green",label='10日均線')
plt.legend(loc='best')  # 繪制圖例

ax.grid(True)           # 帶網格線
plt.title("600895張江高科的K線圖")
plt.rcParams['font.sans-serif']=['SimHei']
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.show()