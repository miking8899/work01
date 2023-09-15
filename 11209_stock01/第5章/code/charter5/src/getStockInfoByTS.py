# coding=utf-8
import tushare as ts    # 匯入庫
# 指定儲存的檔名
fileName='D:\\stockData\\ch5\\stockListByTs.csv'
stockList=ts.get_stock_basics()     # 呼叫方法得到訊息
print(stockList)        # 在主控台列印
stockList.to_csv(fileName,encoding='gbk')   # 儲存到csv中