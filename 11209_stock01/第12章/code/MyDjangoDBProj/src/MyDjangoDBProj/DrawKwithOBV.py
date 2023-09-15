# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl
# 計算OBV的方法 
def calOBV(df):
    # 把成交量換算成萬手
    df['VolByHand'] = df['Volume']/1000000
    # 建立OBV列，先全填充為0
    df['OBV'] =0  
    cnt=1   # 索引從1開始，即從第2天算起
    while cnt<=len(df)-1:
        if(df.iloc[cnt]['Close']>df.iloc[cnt-1]['Close']):
            df.ix[cnt,'OBV'] = df.ix[cnt-1,'OBV'] + df.ix[cnt,'VolByHand']
        if(df.iloc[cnt]['Close']<df.iloc[cnt-1]['Close']):            
            df.ix[cnt,'OBV'] = df.ix[cnt-1,'OBV'] - df.ix[cnt,'VolByHand']   
        cnt=cnt+1   
    return df
filename='D:\\stockData\ch12\\6004602019-01-012019-05-31.csv'
df = pd.read_csv(filename,encoding='gbk')
# 呼叫方法計算OBV
df = calOBV(df) 
# print(df) # 可以去除這個注解以檢視結果
figure = plt.figure()
# 建立子圖     
(axPrice, axOBV) = figure.subplots(2, sharex=True)
# 呼叫方法，在axPrice子圖中繪制K線圖 
candlestick2_ochl(ax = axPrice, 
              opens=df["Open"].values, closes=df["Close"].values,
              highs=df["High"].values, lows=df["Low"].values,
              width=0.75, colorup='red', colordown='green')
axPrice.set_title("K線圖和均線圖")    # 設定子圖示題
df['Close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均線')
df['Close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均線')
df['Close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均線')
axPrice.legend(loc='best')      # 繪制圖例
axPrice.set_ylabel("價格（單位：元）")
axPrice.grid(linestyle='-.')    # 帶網格線        
# 在axOBV子圖中繪制OBV圖形
df['OBV'].plot(ax=axOBV,color="blue",label='OBV')
plt.legend(loc='best')          # 繪制圖例
plt.rcParams['font.sans-serif']=['SimHei']
# 在OBV子圖上加上負值效果
plt.rcParams['axes.unicode_minus'] = False
axOBV.set_ylabel("單位：萬手")
axOBV.set_title("OBV指標圖")    # 設定子圖的標題
axOBV.grid(linestyle='-.')      # 帶網格線
# 設定x軸座標的標簽和旋轉角度
major_index=df.index[df.index%5==0]
major_xtics=df['Date'][df.index%5==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.show()