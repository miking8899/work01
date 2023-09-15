# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl
from matplotlib.ticker import MultipleLocator
# 根據指定程式碼和時間範圍，取得股票資料
df = pd.read_csv('D:/stockData/ch7/600895.csv',encoding='gbk')
# 設定大小，共享x座標軸
figure,(axPrice, axVol) = plt.subplots(2, sharex=True, figsize=(15,8))
# 呼叫方法繪制K線圖 
candlestick2_ochl(ax = axPrice, 
                  opens=df["Open"].values, closes=df["Close"].values,
                  highs=df["High"].values, lows=df["Low"].values,
                  width=0.75, colorup='red', colordown='green')
axPrice.set_title("600895張江高科K線圖和均線圖")  # 設定子圖示題
df['Close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均線')
df['Close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均線')
df['Close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均線')
axPrice.legend(loc='best')  # 繪制圖例
axPrice.set_ylabel("價格（單位：元）")
axPrice.grid(True)          # 帶網格線
# 如下繪製成交量子圖
# 直方圖表示成交量，用for循環處理不同的彩色
for index, row in df.iterrows():
    if(row['Close'] >= row['Open']):
        axVol.bar(row['Date'],row['Volume']/1000000,width = 0.5,color='red')
    else:    
        axVol.bar(row['Date'],row['Volume']/1000000,width = 0.5,color='green')        
axVol.set_ylabel("成交量（單位：萬手）")   # 設定y軸標題
axVol.set_title("600895張江高科成交量")    # 設定子圖的標題
axVol.set_ylim(0,df['Volume'].max()/1000000*1.2)    # 設定y軸範圍
xmajorLocator = MultipleLocator(5)                  # 將x軸主刻度設定為5的倍數
axVol.xaxis.set_major_locator(xmajorLocator)
axVol.grid(True)    # 帶網格線
# 旋轉x軸的展示文字角度
for xtick in axVol.get_xticklabels():
    xtick.set_rotation(15)
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()