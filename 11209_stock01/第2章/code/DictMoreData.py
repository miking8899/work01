# !/usr/bin/env python
# coding=utf-8
# 以清單模式定義Mike和Tom兩個人的賬戶
accountsInfoList = [{'name': 'Mike', 'balance': 100,'stockList':['600123','600158']}, {'name': 'Tom', 'balance': 200,'stockList':['600243','600558']} ]
# 透過for循環，依次輸出清單中的元素
for item in accountsInfoList:
    print item['name'],
    print item['balance'],
    print item['stockList']
# 以字典的模式定義
accountInfoDict={ 'Peter':{'balance': 100,'stockList':['600123','600158'] }, 'Tom': { 'balance': 200,'stockList':['600243','600558']} }
# 輸出{'balance': 100, 'stockList': ['600123', '600158']}
print(accountInfoDict.get('Peter'))
PeterAccount={ 'Peter':{'balance': 200,'stockList':['600223','600158',600458] }}
accountInfoDict.update(PeterAccount)
print(accountInfoDict.get('Peter')) # 能看到更新後的內容
JohnAccount={ 'John':{'balance': 200,'stockList':[] }}
accountInfoDict.update(JohnAccount)
# 利用雙層循環列印
for name,account in accountInfoDict.items():
    print ("name is %s:"%(name)),   # 輸出name後不換行
    for key,value in account.items():
        print value,
    print # 輸完一個人的訊息後換行