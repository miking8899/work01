# coding=utf-8
import pandas_datareader
code='600895.ss'
stock = pandas_datareader.get_data_yahoo(code,'2019-01-01','2019-01-30')
print(stock)    # 輸出內容
# 儲存為excel和csv文件
stock.to_excel('D:\\stockData\\ch5\\'+code+'.xlsx')
stock.to_csv('D:\\stockData\ch5\\'+code+'.csv')