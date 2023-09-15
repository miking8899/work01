# coding=utf-8
import urllib.request
stockCode = '600895'  # 張江高科
# 請注意，url後沒透過問號來傳各種參數
url = 'http://quotes.money.163.com/service/chddata.html'
# 參數是透過url.parse的模式來傳入的
param = bytes(urllib.parse.urlencode({'code': '0'+stockCode,'start':'20190102','end':'20190102','fields':'TCLOSE;HIGH;LOW;TOPEN;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER'}), encoding='utf8')
# 帶各種參數
response = urllib.request.urlopen(url,data=param,timeout=1)
print(response.read().decode("gbk"))
response.close();