# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader
from mpl_finance import candlestick2_ochl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
import tkinter.messagebox
# 計算KDJ
def calKDJ(df):
    df['MinLow'] = df['Low'].rolling(9, min_periods=9).min()
    # 填充NaN資料
    df['MinLow'].fillna(value = df['Low'].expanding().min(), inplace = True) 
    df['MaxHigh'] = df['High'].rolling(9, min_periods=9).max()
    df['MaxHigh'].fillna(value = df['High'].expanding().max(), inplace = True)    
    df['RSV'] = (df['Close'] - df['MinLow']) / (df['MaxHigh'] - df['MinLow']) * 100
    for i in range(len(df)):
        if i==0:    # 第一天
            df.ix[i,'K']=50
            df.ix[i,'D']=50
        if i>0:
            df.ix[i,'K']=df.ix[i-1,'K']*2/3 + 1/3*df.ix[i,'RSV']
            df.ix[i,'D']=df.ix[i-1,'D']*2/3 + 1/3*df.ix[i,'K']            
        df.ix[i,'J']=3*df.ix[i,'K']-2*df.ix[i,'D']  
    return df
# 繪制KDJ線
def drawKDJAndKLine(stockCode,startDate,endDate):
    filename='D:\\stockData\ch9\\'+stockCode+startDate+endDate+'.csv'
    getStockDataFromAPI(stockCode,startDate,endDate)
    df = pd.read_csv(filename,encoding='gbk')
    stockDataFrame = calKDJ(df)
    # 建立子圖     
    (axPrice, axKDJ) = figure.subplots(2, sharex=True)
    # 呼叫方法，在第axPrice子圖中繪制K線圖 
    candlestick2_ochl(ax = axPrice, 
                  opens=stockDataFrame["Open"].values, closes=stockDataFrame["Close"].values,
                  highs=stockDataFrame["High"].values, lows=stockDataFrame["Low"].values,
                  width=0.75, colorup='red', colordown='green')
    axPrice.set_title("K線圖和均線圖")    # 設定子圖示題
    stockDataFrame['Close'].rolling(window=3).mean().plot(ax=axPrice,color="red",label='3日均線')
    stockDataFrame['Close'].rolling(window=5).mean().plot(ax=axPrice,color="blue",label='5日均線')
    stockDataFrame['Close'].rolling(window=10).mean().plot(ax=axPrice,color="green",label='10日均線')
    axPrice.legend(loc='best')      # 繪制圖例
    axPrice.set_ylabel("價格（單位：元）")
    axPrice.grid(linestyle='-.')    # 帶網格線        
    # 在axKDJ子圖中繪制KDJ
    stockDataFrame['K'].plot(ax=axKDJ,color="blue",label='K')
    stockDataFrame['D'].plot(ax=axKDJ,color="green",label='D')
    stockDataFrame['J'].plot(ax=axKDJ,color="purple",label='J')
    plt.legend(loc='best')          # 繪制圖例
    plt.rcParams['font.sans-serif']=['SimHei']       
    axKDJ.set_title("KDJ圖")        # 設定子圖的標題
    axKDJ.grid(linestyle='-.')      # 帶網格線
    # 設定x軸座標的標簽和旋轉角度
    major_index=stockDataFrame.index[stockDataFrame.index%5==0]
    major_xtics=stockDataFrame['Date'][stockDataFrame.index%5==0]
    plt.xticks(major_index,major_xtics)
    plt.setp(plt.gca().get_xticklabels(), rotation=30) 
# 從API中取得股票資料
def getStockDataFromAPI(stockCode,startDate,endDate):
    try:
        # 給股票程式碼加ss前綴來取得上證股票的資料
        stock = pandas_datareader.get_data_yahoo(stockCode+'.ss',startDate,endDate)
        if(len(stock)<1):
            # 若果沒取到資料，則拋出例外 
            raise Exception()
        # 移除最後一行，因為get_data_yahoo會多取一天的股票交易資料
        stock.drop(stock.index[len(stock)-1],inplace=True)  # 在本機留份csv
        filename='D:\\stockData\ch9\\'+stockCode+startDate+endDate+'.csv'
        stock.to_csv(filename)                
    except Exception as e:
        print('Error when getting the data of:' + stockCode)
        print(repr(e))
# 設定tkinter視窗
win = tkinter.Tk()
win.geometry('625x600')     # 設定大小
win.title("K線均線整合KDJ")
# 放置控制項
tkinter.Label(win,text='股票程式碼：').place(x=10,y=20)
tkinter.Label(win,text='開始時間：').place(x=10,y=50)
tkinter.Label(win,text='結束時間：').place(x=10,y=80)
stockCodeVal = tkinter.StringVar()
startDateVal = tkinter.StringVar()
endDateVal = tkinter.StringVar()
stockCodeEntry = tkinter.Entry(win,textvariable=stockCodeVal)
stockCodeEntry.place(x=70,y=20)
stockCodeEntry.insert(0,'600640')
startDateEntry = tkinter.Entry(win,textvariable=startDateVal)
startDateEntry.place(x=70,y=50)
startDateEntry.insert(0,'2019-01-01')
endDateEntry = tkinter.Entry(win,textvariable=endDateVal)
endDateEntry.place(x=70,y=80)
endDateEntry.insert(0,'2019-05-31')
def draw():     # 繪制按鈕的處理函數
    plt.clf()   # 先清理所有在plt上的圖形   
    stockCode=stockCodeVal.get()
    startDate=startDateVal.get()    
    endDate=endDateVal.get()
    drawKDJAndKLine(stockCode,startDate,endDate)
    canvas.draw()  
tkinter.Button(win,text='繪制',width=12,command=draw).place(x=200,y=50)
def reset():
    stockCodeEntry.delete(0,tkinter.END)
    stockCodeEntry.insert(0,'600640')
    startDateEntry.delete(0,tkinter.END)
    startDateEntry.insert(0,'2019-01-01')
    endDateEntry.delete(0,tkinter.END)
    endDateEntry.insert(0,'2019-05-31')
    plt.clf()
    canvas.draw() 
tkinter.Button(win,text='重設',width=12,command=reset).place(x=200,y=80)
# 以交談視窗的形式輸出買點
def printBuyPoints():
    stockCode=stockCodeVal.get()
    startDate=startDateVal.get()    
    endDate=endDateVal.get()    
    filename='D:\\stockData\ch9\\'+stockCode+startDate+endDate+'.csv'
    getStockDataFromAPI(stockCode,startDate,endDate)
    df = pd.read_csv(filename,encoding='gbk')
    stockDf = calKDJ(df)
    cnt=0
    buyDate=''
    while cnt<=len(stockDf)-1:
        if(cnt>=5): # 略過前幾天的誤差
            #規則1：前一天J值大於10，當天J值小於10，是買點、        
            if stockDf.iloc[cnt]['J']<10 and stockDf.iloc[cnt-1]['J']>10:
                buyDate = buyDate+stockDf.iloc[cnt]['Date'] + ','
                cnt=cnt+1
                continue 
            # 規則2：K,D均在20之下，出現K線上穿D線的金叉現象
            # 規則1和規則2是“或”的關系，所以當滿足規則1時直接continue
            if stockDf.iloc[cnt]['K']>stockDf.iloc[cnt]['D'] and stockDf.iloc[cnt-1]['D']>stockDf.iloc[cnt-1]['K']:
                # 滿足上穿條件後再判斷K和D均小於20                
                if stockDf.iloc[cnt]['K']< 20 and stockDf.iloc[cnt]['D']<20:
                    buyDate = buyDate + stockDf.iloc[cnt]['Date'] + ','
        cnt=cnt+1            
    # 完成後，透過交談視窗的形式顯示買入日期
    tkinter.messagebox.showinfo('提示買點',buyDate)
tkinter.Button(win,text='計算買點',width=12,command=printBuyPoints).place(x=300,y=50)
# 以交談視窗的形式輸出賣點
def printSellPoints():
    stockCode=stockCodeVal.get()
    startDate=startDateVal.get()    
    endDate=endDateVal.get()    
    filename='D:\\stockData\ch9\\'+stockCode+startDate+endDate+'.csv'
    getStockDataFromAPI(stockCode,startDate,endDate)
    df = pd.read_csv(filename,encoding='gbk')
    stockDf = calKDJ(df)
    cnt=0
    sellDate=''
    while cnt<=len(stockDf)-1:
        if(cnt>=5): # 略過前幾天的誤差
            # 規則1：前一天J值小於100，當天J值大於100，是賣點、        
            if stockDf.iloc[cnt]['J']>100 and stockDf.iloc[cnt-1]['J']<100:
                sellDate = sellDate+stockDf.iloc[cnt]['Date'] + ','
                cnt=cnt+1
                continue 
            # 規則2：K,D均在80之上，出現K線下穿D線的死叉現象            
            if stockDf.iloc[cnt]['K']<stockDf.iloc[cnt]['D'] and stockDf.iloc[cnt-1]['D']<stockDf.iloc[cnt-1]['K']:
                # 滿足上穿條件後再判斷K和D均大於80                
                if stockDf.iloc[cnt]['K']> 80 and stockDf.iloc[cnt]['D']>80:
                    sellDate = sellDate + stockDf.iloc[cnt]['Date'] + ','
        cnt=cnt+1            
    # 完成後，透過交談視窗的形式顯示買入日期
    tkinter.messagebox.showinfo('提示賣點',sellDate)
tkinter.Button(win,text='計算賣點',width=12,command=printSellPoints).place(x=300,y=80)

# 開始整合figure和win
figure = plt.figure()
canvas = FigureCanvasTkAgg(figure, win)
canvas.get_tk_widget().config(width=575,height=500)
canvas.get_tk_widget().place(x=0,y=100)
win.mainloop()