# !/usr/bin/env python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
# 計算RSI的方法，輸導入參數數periodList傳入周期清單 
def calRSI(df,periodList):
    # 計算和上一個交易日收碟價的差值
    df['diff'] = df["Close"]-df["Close"].shift(1) 
    df['diff'].fillna(0, inplace = True)    
    df['up'] = df['diff']
    # 過濾掉小於0的值
    df['up'][df['up']<0] = 0
    df['down'] = df['diff']
    # 過濾掉大於0的值
    df['down'][df['down']>0] = 0
    # 透過for循環，依次計算periodList中不同周期的RSI相等
    for period in periodList:
        df['upAvg'+str(period)] = df['up'].rolling(period).sum()/period
        df['upAvg'+str(period)].fillna(0, inplace = True)
        df['downAvg'+str(period)] = abs(df['down'].rolling(period).sum()/period)
        df['downAvg'+str(period)].fillna(0, inplace = True)
        df['RSI'+str(period)] = 100 - 100/((df['upAvg'+str(period)]/df['downAvg'+str(period)]+1))
    return df
filename='D:\\stockData\ch10\\6005842018-09-012019-05-31.csv'
df = pd.read_csv(filename,encoding='gbk')
list = [6,12,24]    # 周期清單
# 呼叫方法計算RSI
stockDataFrame = calRSI(df,list) 
print(stockDataFrame)
# 開始繪圖
plt.figure()
stockDataFrame['RSI6'].plot(color="blue",label='RSI6')
stockDataFrame['RSI12'].plot(color="green",label='RSI12')
stockDataFrame['RSI24'].plot(color="purple",label='RSI24')
plt.legend(loc='best')  # 繪制圖例       
# 設定x軸座標的標簽和旋轉角度
major_index=stockDataFrame.index[stockDataFrame.index%10==0]
major_xtics=stockDataFrame['Date'][stockDataFrame.index%10==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
# 帶網格線，且設定了網格型態
plt.grid(linestyle='-.') 
plt.title("RSI效果圖")
plt.rcParams['font.sans-serif']=['SimHei']
plt.savefig('D:\\stockData\ch10\\6005842018-09-012019-05-31.png')
plt.show()

