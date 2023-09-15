# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ochl
# 計算BIAS的方法，導入參數periodList傳入周期清單 
def calBIAS(df,periodList):
    # 檢查周期，計算6,12,24日BIAS
    for period in periodList:
        df['MA'+str(period)] = df['Close'].rolling(window=period).mean() 
        df['MA'+str(period)].fillna(value = df['Close'], inplace = True)
        df['BIAS'+str(period)] = (df['Close'] - df['MA'+str(period)])/df['MA'+str(period)]*100 
    return df
filename='D:\\stockData\ch11\\6006402019-01-012019-05-31.csv'
df = pd.read_csv(filename,encoding='gbk')
list = [6,12,24]    # 周期清單
# 呼叫方法計算BIAS
stockDataFrame = calBIAS(df,list) 
# print(stockDataFrame) # 可以去掉注解來檢視結果
figure = plt.figure()
# 建立子圖     
(axPrice, axBIAS) = figure.subplots(2, sharex=True)
# 呼叫方法，在axPrice子圖中繪制K線圖
candlestick2_ochl(ax = axPrice, 
              opens=df["Open"].values, closes=df["Close"].values,
              highs=df["High"].values, lows=df["Low"].values,
              width=0.75, colorup='red', colordown='green')
axPrice.set_title("K線圖和均線圖")    # 設定子圖示題
stockDataFrame['Close'].rolling(window=6).mean().plot(ax=axPrice,color="red",label='6日均線')
stockDataFrame['Close'].rolling(window=12).mean().plot(ax=axPrice,color="blue",label='12日均線')
stockDataFrame['Close'].rolling(window=24).mean().plot(ax=axPrice,color="green",label='24日均線')
axPrice.legend(loc='best')      # 繪制圖例
axPrice.set_ylabel("價格（單位：元）")
axPrice.grid(linestyle='-.')    # 帶網格線        
# 在axBIAS子圖中繪制BIAS圖形
stockDataFrame['BIAS6'].plot(ax=axBIAS,color="blue",label='BIAS6')
stockDataFrame['BIAS12'].plot(ax=axBIAS,color="green",label='BIAS12')
stockDataFrame['BIAS24'].plot(ax=axBIAS,color="purple",label='BIAS24')
plt.legend(loc='best')          # 繪制圖例
plt.rcParams['font.sans-serif']=['SimHei']       
axBIAS.set_title("BIAS指標圖")  # 設定子圖的標題
axBIAS.grid(linestyle='-.')     # 帶網格線
# 設定x軸座標的標簽和旋轉角度
major_index=stockDataFrame.index[stockDataFrame.index%5==0]
major_xtics=stockDataFrame['Date'][stockDataFrame.index%5==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.show()