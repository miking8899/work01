# coding=utf-8
import requests
import re
# 定義爬取列印和儲存資料的方法
def printAndSaveStock(code):
    url = 'http://hq.sinajs.cn/list=' + code
    response = requests.get(url).text    
    rule = r'"(.*?)"'       # 設定截取字串的規則
    result = re.findall(rule, response)    
    print(result[0])
    filename = 'D:\\stockData\\ch5\\'+code+".csv"
    f = open(filename,'w')
    # findall方法傳回的是清單，這裡第0號索引存放所需的內容
    f.write(result[0])  # 寫檔案
    f.close()           # 關閉檔案
# 爬取張江高科和中國國貿這兩只股票的交易資料
codes = ['sh600895', 'sh600007']
for code in codes:
    printAndSaveStock(code)