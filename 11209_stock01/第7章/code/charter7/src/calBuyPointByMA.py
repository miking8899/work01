# !/usr/bin/env python
# coding=utf-8
import pandas as pd
# 從檔案中讀取資料
df = pd.read_csv('D:/stockData/ch7/600895.csv',encoding='gbk')
maIntervalList = [3,5,10]
# 雖然在後文中只用到了5日均線，但這裡示範設定3種均線
for maInterval in maIntervalList:
    df['MA_' + str(maInterval)] = df['Close'].rolling(window=maInterval).mean()
cnt=0    
while cnt<=len(df)-1:
    try:
        # 規則1：收碟價連續三天上揚
        if df.iloc[cnt]['Close']<df.iloc[cnt+1]['Close'] and df.iloc[cnt+1]['Close']<df.iloc[cnt+2]['Close']:
            # 規則2：5日均線連續三天上揚
            if df.iloc[cnt]['MA_5']<df.iloc[cnt+1]['MA_5'] and df.iloc[cnt+1]['MA_5']<df.iloc[cnt+2]['MA_5']:
                # 規則3：第3天收碟價上穿5日均線
                if df.iloc[cnt+1]['MA_5']>df.iloc[cnt]['Close'] and df.iloc[cnt+2]['MA_5']<df.iloc[cnt+1]['Close']:     
                    print("Buy Point on:" + df.iloc[cnt]['Date'])
    except: # 有幾天是沒有5日均線的，所以用except處理例外
        pass                
    cnt=cnt+1