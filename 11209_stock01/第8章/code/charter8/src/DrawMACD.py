# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt 
import pymysql
import sys
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
    return df[['date','DIF','DEA','MACD']]
    # return df
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
print(calMACD(df, 12, 26, 9))   # 輸出結果      
stockDataFrame = calMACD(df, 12, 26, 9)
# 開始繪圖
plt.figure()
stockDataFrame['DEA'].plot(color="red",label='DEA')
stockDataFrame['DIF'].plot(color="blue",label='DIF')
plt.legend(loc='best')      # 繪制圖例
# 設定MACD柱狀圖
for index, row in stockDataFrame.iterrows():
    if(row['MACD'] >0):     # 大於0則用紅色
        plt.bar(row['date'], row['MACD'],width=0.5, color='red')        
    else:                   # 小於等於0則用綠色 
        plt.bar(row['date'], row['MACD'],width=0.5, color='green')
# 設定x軸座標的標簽和旋轉角度
major_index=stockDataFrame.index[stockDataFrame.index%10==0]
major_xtics=stockDataFrame['date'][stockDataFrame.index%10==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
# 帶網格線，且設定了網格型態
plt.grid(linestyle='-.') 
plt.title("600895張江高科的MACD圖")
plt.rcParams['axes.unicode_minus'] = False 
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()