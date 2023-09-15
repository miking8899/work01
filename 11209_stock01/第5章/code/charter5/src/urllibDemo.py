# coding=utf-8
import urllib.request   # 匯入庫
stockCode = '600895'    # 待爬取的股票“張江高科”所對應的股票程式碼
url = 'http://quotes.money.163.com/service/chddata.html?code=0'+stockCode+\'&start=20190102&end=20190102&fields=TCLOSE;HIGH;LOW;TOPEN;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER'
print(url)              # 列印出要爬取的url
# 呼叫urlopen方法爬取資料
response = urllib.request.urlopen(url)
# 由於傳回結果中有中文，因此要用gbk解碼
print(response.read().decode("gbk"))
response.close();       # 關閉物件