# !/usr/bin/env python
# coding=utf-8
import pymysql
import sys
import pandas as pd
try:
    # 開啟資料庫連線
    db = pymysql.connect("localhost","root","123456","pythonStock" )
except:
    print('Error when Connecting to DB.')   
    sys.exit()  
cursor = db.cursor()
cursor.execute("select * from stockinfo")
# 取得所有的資料，但不包括清單名
result=cursor.fetchall()
cols = cursor.description       # 傳回清單標頭資訊
print(cols)
col = []
# 依次把每個cols元素中的第一個值放入col陣列
for index in cols:
    col.append(index[0])   
result = list(result)   # 轉成清單，方便存入DataFrame
result = pd.DataFrame(result,columns=col)
print(result)           # 輸出結果
# 關閉游標和連線物件，否則會造成資源無法釋放
cursor.close()
db.close()