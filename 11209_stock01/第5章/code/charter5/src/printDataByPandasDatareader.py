# coding=utf-8
import pandas_datareader
stockCodeList = []
stockCodeList.append('600007.ss')  # 滬股“中國國貿” 
stockCodeList.append('000001.sz')  # 深股“平安銀行”
stockCodeList.append('2318.hk')    # 港股“中國平安”
stockCodeList.append('IBM')        # 美股，IBM，直接輸入股票程式碼不帶副檔名

for code in stockCodeList:
    # 為了示範，只取一天的交易資料
    stock = pandas_datareader.get_data_yahoo(code,'2019-01-02','2019-01-02')
    print(stock)