# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
import pymysql
import sys
from mpl_finance import candlestick2_ochl
from matplotlib.ticker import MultipleLocator
# 第一個參數是資料，第二個參數是周期
def calEMA(df, term): 
    for i in range(len(df)):
        if i==0:    # 第一天
            df.ix[i,'EMA']=df.ix[i,'close']
        if i>0:
            df.ix[i,'EMA']=(term-1)/(term+1)*df.ix[i-1,'EMA']+2/(term+1)*df.ix[i,'close']
    EMAList=list(df['EMA'])
    return EMAList
# 定義計算MACD的方法 
def calMACD(df, shortTerm=12, longTerm=26, DIFTerm=9):
    shortEMA = calEMA(df, shortTerm)
    longEMA = calEMA(df, longTerm)
    df['DIF'] = pd.Series(shortEMA) - pd.Series(longEMA)
    for i in range(len(df)):
        if i==0:    # 第一天
            df.ix[i,'DEA'] = df.ix[i,'DIF']     # ix可以透過標簽名和索引來取得資料
        if i>0:  
            df.ix[i,'DEA'] = (DIFTerm-1)/(DIFTerm+1)*df.ix[i-1,'DEA'] + 2/(DIFTerm+1)*df.ix[i,'DIF']  
    df['MACD'] = 2*(df['DIF'] - df['DEA'])
    return df
try:
    # 開啟資料庫連線
    db = pymysql.connect("localhost","root","123456","pythonStock" )
except:
    print('Error when Connecting to DB.')   
    sys.exit()  
cursor = db.cursor()
cursor.execute("select * from stock_600895")
cols = cursor.description   # 傳回列名
heads = []
# 依次把每個cols元素中的第一個值放入col陣列
for index in cols:
    heads.append(index[0])
result = cursor.fetchall()
df = pd.DataFrame(list(result))
df.columns=heads
# print(calMACD(df, 12, 26, 9))     # 輸出結果      
stockDataFrame = calMACD(df, 12, 26, 9)
# 開始繪圖，設定大小，共享x座標軸
figure,(axPrice, axMACD) = plt.subplots(2, sharex=True, figsize=(15,8))
# 呼叫方法繪制K線圖 
candlestick2_ochl(ax = axPrice, 
                  opens=stockDataFrame["open"].values, closes=stockDataFrame["close"].values,
                  highs=stockDataFrame["high"].values, lows=stockDataFrame["low"].values,
                  width=0.75, colorup='red', colordown='green')
axPrice.set_title("600895張江高科K線圖和均線圖")     # 設定子圖示題
stockDataFrame['close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均線')
stockDataFrame['close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均線')
stockDataFrame['close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均線')
axPrice.legend(loc='best')      # 繪制圖例
axPrice.set_ylabel("價格（單位：元）")
axPrice.grid(linestyle='-.')    # 帶網格線
# 開始繪制第二個子圖
stockDataFrame['DEA'].plot(ax=axMACD,color="red",label='DEA')
stockDataFrame['DIF'].plot(ax=axMACD,color="blue",label='DIF')
plt.legend(loc='best')          # 繪制圖例
# 設定第二個子圖中的MACD柱狀圖
for index, row in stockDataFrame.iterrows():
    if(row['MACD'] >0):         # 大於0則用紅色
        axMACD.bar(row['date'], row['MACD'],width=0.5, color='red')        
    else:                       # 小於等於0則用綠色 
        axMACD.bar(row['date'], row['MACD'],width=0.5, color='green')
axMACD.set_title("600895張江高科MACD")  # 設定子圖的標題
axMACD.grid(linestyle='-.')     # 帶網格線
# xmajorLocator = MultipleLocator(10)     # 將x軸的主刻度設定為10的倍數
# axMACD.xaxis.set_major_locator(xmajorLocator)
major_xtics=stockDataFrame['date'][stockDataFrame.index%10==0]
axMACD.set_xticks(major_xtics)
# 旋轉x軸顯示文字的角度
for xtick in axMACD.get_xticklabels():
    xtick.set_rotation(30)    
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
plt.show()