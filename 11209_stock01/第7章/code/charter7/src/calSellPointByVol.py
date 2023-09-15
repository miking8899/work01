# !/usr/bin/env python
# coding=utf-8
import pandas_datareader
import pandas as pd
import numpy as np
# 漲幅是否大於指定比率
def isMoreThanPer(lessVal,highVal,per):
    if np.abs(highVal-lessVal)/lessVal>per/100:
        return True
    else:
        return False        
# 漲幅是否小於指定比率
def isLessThanPer(lessVal,highVal,per):
    if np.abs(highVal-lessVal)/lessVal<per/100:
        return True
    else:
        return False
# 本次直接從檔案中讀取資料
df = pd.read_csv('D:/stockData/ch7/60089520181231.csv',encoding='gbk')
cnt=0    
while cnt<=len(df)-1:
    try:
        # 規則1：連續三天收碟價變動不超過3%
        if isLessThanPer(df.iloc[cnt]['Close'],df.iloc[cnt+1]['Close'],3) and isLessThanPer(df.iloc[cnt]['Close'],df.iloc[cnt+2]['Close'],3) :
            #規則2：連續三天成交量跌幅超過75%
            if isMoreThanPer(df.iloc[cnt+1]['Volume'],df.iloc[cnt]['Volume'],75) and isMoreThanPer(df.iloc[cnt+2]['Volume'],df.iloc[cnt]['Volume'],75) :
                print("Sell Point on:" + df.iloc[cnt]['Date'])
    except: 
        pass                
    cnt=cnt+1