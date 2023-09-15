import re   # 匯入庫
numStr = '1c'
numPattern = '^[0-9]+$'         # 比對數字的正規表示法
if re.match(numPattern,numStr):
    print('All Numbers')
lowCaseStr = 'abc'
strPattern = '^[a-z]+$'         # 比對小寫字母的正規表示法
if re.match(strPattern,lowCaseStr):
    print('All Low Case')
stockPattern='^[6|3|0][0-9]{5}$'    # 比對滬深A股主板和創業板股票
stockCode='300000'     
if re.match(stockPattern,stockCode):
    print('Is Stock Code')   

myStr = '13785214563'
myPattern = '^1[3|4|5|7|8][0-9]{9}$'
if re.match(myPattern,myStr):
    print('Match')