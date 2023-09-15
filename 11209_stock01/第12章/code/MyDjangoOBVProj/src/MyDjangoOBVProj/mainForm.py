# !/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
import pandas_datareader
import matplotlib.pyplot as plt
import pandas as pd
from mpl_finance import candlestick2_ochl
import sys
from io import BytesIO
import base64
import imp
from . import models
imp.reload(sys)
import logging
from django.db import connection
# 參考django日志案例
logger = logging.getLogger(__name__)
# logger = logging.getLogger('loggers')
def display(request):
    logger.info("start to display main.html")
    return render(request, 'main.html')

# 計算OBV的方法 
def calOBV(df):
    logger.info("start calOBV")
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

def insertData(stockCode,startDate,endDate):
    logger.info("start insertData")
    # 先移除
    models.stockInfo.objects.filter(stockCode=stockCode).delete()
    stock = pandas_datareader.get_data_yahoo(stockCode+'.ss',startDate,endDate)
    # 移除最後一天多餘的股票交易資料
    stock.drop(stock.index[len(stock)-1],inplace=True)
    filename='D:\\stockData\ch12\\'+stockCode+startDate+endDate+'.csv'
    stock.to_csv(filename)
    stock = pd.read_csv(filename,encoding='gbk')
    cnt=0
    # 存入資料庫
    stockInfoList=[]
    while cnt<=len(stock)-1:
        date=stock.iloc[cnt]['Date']
        open=float(stock.iloc[cnt]['Open'])
        close=float(stock.iloc[cnt]['Close'])
        high=float(stock.iloc[cnt]['High'])
        low=float(stock.iloc[cnt]['Low'])
        vol=int(stock.iloc[cnt]['Volume'])        
        stockOne = models.stockInfo(date=date,open=open,close=close,high=high,low=low,vol=vol,stockCode=stockCode)
        stockInfoList.append(stockOne)
        cnt=cnt+1
    models.stockInfo.objects.bulk_create(stockInfoList)
    return stock

def loadStock(stockCode,startDate,endDate):
    logger.info("start loadStock")
    # 先從資料表中取得資料
    cursor = connection.cursor()
    try:
        cursor.execute("select date,high,low,open,close,vol from stockInfo where stockCode='"+stockCode+"' and date>='"+startDate+"' and date<='"+endDate+"'")
        heads = ['Date','High','Low','Open','Close','Volume']
        # 依次把每個cols元素中的第一個值放入col陣列
        result = cursor.fetchall()
        df = pd.DataFrame(list(result))    
    except:
        logger.error("in loadStock,error during visiting stockInfo table")           
    finally:
        cursor.close()
    # 資料表中存在資料，則從資料表中讀取     
    if(len(df)>0):        
        df.columns=heads
        return df;
    # 若果沒有讀取到，則從網站爬取，並插入資料表中
    else:
        logger.info("No data in DB, get from Web")
        df = insertData(stockCode,startDate,endDate)
        return df      

def calBuyPoints(df):
    cnt=0    
    buyDate=''
    while cnt<=len(df)-1:
        if(cnt>=5): # 前幾天有誤差，從第5天算起
            # 買點規則：股價連續兩天下跌，而OBV連續兩天上漲
            if df.iloc[cnt-1]['Close']>df.iloc[cnt]['Close'] and df.iloc[cnt-2]['Close']>df.iloc[cnt-1]['Close']:
                logger.debug("calBuyPoints, decrease for 2 days." + df.iloc[cnt]['Date'])
                logger.debug("obv on first day is:" + str(df.iloc[cnt-2]['OBV']))
                logger.debug("obv on second day is:" + str(df.iloc[cnt-1]['OBV']))
                logger.debug("obv on third day is:" + str(df.iloc[cnt]['OBV']))
                if(df.iloc[cnt-1]['OBV']<df.iloc[cnt]['OBV'] and df.iloc[cnt-2]['OBV']<df.iloc[cnt-1]['OBV']):
                    buyDate = buyDate+df.iloc[cnt]['Date'] + ','
        cnt=cnt+1
    return buyDate 

def calSellPoints(df):
    cnt=0    
    sellDate=''
    while cnt<=len(df)-1:
        if(cnt>=5): # 前幾天有誤差，從第5天算起
            # 賣點規則：股價連續兩天上漲，而OBV連續兩天下跌
            if df.iloc[cnt-1]['Close']<df.iloc[cnt]['Close'] and df.iloc[cnt-2]['Close']<df.iloc[cnt-1]['Close']:
                logger.debug("calSellPoints, increase for 2 days." + df.iloc[cnt]['Date'])
                logger.debug("obv on first day is:" + str(df.iloc[cnt-2]['OBV']))
                logger.debug("obv on second day is:" + str(df.iloc[cnt-1]['OBV']))
                logger.debug("obv on third day is:" + str(df.iloc[cnt]['OBV']))
                if(df.iloc[cnt-1]['OBV']>df.iloc[cnt]['OBV'] and df.iloc[cnt-2]['OBV']>df.iloc[cnt-1]['OBV']):
                    sellDate = sellDate+df.iloc[cnt]['Date'] + ','
        cnt=cnt+1
    return sellDate 

def draw(request):
    logger.info("start draw")
    # 取得頁面參數    
    stockCode = request.POST.get('stockCode')
    logger.info("stockCode is:" + stockCode)    
    startDate = request.POST.get('startDate')
    logger.info("startDate is:" + startDate)
    endDate = request.POST.get('endDate')   
    logger.info("endDate is:" + endDate) 
    # 取得股票資料
    df = loadStock(stockCode,startDate,endDate)
    # 計算OBV值  
    df = calOBV(df)
    
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
    plt.legend(loc='best') #繪制圖例
    plt.rcParams['font.sans-serif']=['SimHei']
    # 在OBV子圖上加上負值效果
    plt.rcParams['axes.unicode_minus'] = False
    axOBV.set_ylabel("單位：萬手")
    axOBV.set_title("OBV指標圖")       # 設定子圖的標題
    axOBV.grid(linestyle='-.')         # 帶網格線
    # 設定x軸座標的標簽和旋轉角度
    major_index=df.index[df.index%5==0]
    major_xtics=df['Date'][df.index%5==0]
    plt.xticks(major_index,major_xtics)
    plt.setp(plt.gca().get_xticklabels(), rotation=30) 
    logger.debug("convert plt to buffer")  
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.close()     
    base64img = base64.b64encode(buffer.getvalue())    
    img = "data:image/png;base64,"+base64img.decode()
    logger.debug("start to Render in stock.html")
    
    buyDate = calBuyPoints(df)
    sellDate = calSellPoints(df)  
    
    return render(request, 'stock.html', {
            'img': img,'stockCode':stockCode,
            'buyDate':buyDate,'sellDate':sellDate})