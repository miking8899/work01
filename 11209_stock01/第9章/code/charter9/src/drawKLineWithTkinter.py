# !/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from mpl_finance import candlestick2_ochl
import tkinter
win = tkinter.Tk()
df = pd.read_csv('D:/stockData/ch6/600895.csv',encoding='gbk',index_col=0)
win.title("tkinter整合matplotlib")
figure = plt.figure()
canvas = FigureCanvasTkAgg(figure, win)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=2)  
# 把用matplotlib繪制的動作定義在方法中，方便呼叫
def drawKLineOnCancas():   
    plt.clf() #先清理所有在plt上的圖形   
    ax = figure.add_subplot(111)
    ax.set_title('600895張江高科的K線圖')
    ax = figure.add_subplot(111)
    # 呼叫方法繪制K線圖 
    candlestick2_ochl(ax = ax, 
                  opens=df["Open"].values, closes=df["Close"].values,
                  highs=df["High"].values, lows=df["Low"].values,
                  width=0.75, colorup='red', colordown='green')
    df['Close'].rolling(window=3).mean().plot(color="red",label='3日均線')
    df['Close'].rolling(window=5).mean().plot(color="blue",label='5日均線')
    df['Close'].rolling(window=10).mean().plot(color="green",label='10日均線')
    plt.legend(loc='best')  # 繪制圖例
    plt.xticks(range(len(df.index.values)),df.index.values,rotation=30 ) 
    ax.grid(True)           # 帶網格
    plt.rcParams['font.sans-serif']=['SimHei']
    canvas.draw() 

button =tkinter.Button(win, text='開始繪制', width=10,command=drawKLineOnCancas).grid(row=1,column=0,columnspan=3)
def clearCanvas():
    plt.clf()  
    canvas.draw() 
button =tkinter.Button(win, text='清理', width=10,command=clearCanvas).grid(row=1,column=1,columnspan=3)
win.mainloop()