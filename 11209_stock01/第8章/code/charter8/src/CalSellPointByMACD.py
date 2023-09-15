# !/usr/bin/env python
# coding=utf-8
import pandas as pd
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
    return df    
def getMACDByCode(code):
    try:
        # 開啟資料庫連線
        db = pymysql.connect("localhost","root","123456","pythonStock" )
    except:
        print('Error when Connecting to DB.')   
        sys.exit()  
    cursor = db.cursor()
    cursor.execute('select * from stock_'+code)
    cols = cursor.description   # 傳回列名
    heads = []
    # 依次把每個cols元素中的第一個值放入col陣列
    for index in cols:
        heads.append(index[0])
    result = cursor.fetchall()
    df = pd.DataFrame(list(result))
    df.columns=heads
    stockDataFrame = calMACD(df, 12, 26, 9)
    return stockDataFrame
stockDf = getMACDByCode('600460')
cnt=0    
while cnt<=len(stockDf)-1:
    if(cnt>=30):    # 前幾天有誤差，從第30天算起
        try:        
            # 規則1：這天DIF值下穿DEA
            if stockDf.iloc[cnt]['DIF']<stockDf.iloc[cnt]['DEA'] and stockDf.iloc[cnt-1]['DIF']>stockDf.iloc[cnt-1]['DEA']:
                # 規則2：Bar柱是否向下運動
                if stockDf.iloc[cnt]['MACD']<stockDf.iloc[cnt-1]['MACD']:
                    print("Sell Point by MACD on:" + stockDf.iloc[cnt]['date'])
        except:
            pass                
    cnt=cnt+1