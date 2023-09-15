# !/usr/bin/env python
# coding=utf-8
import pymysql
import sys
try:
    # 開啟資料庫連線
    db = pymysql.connect("localhost","root","123456","pythonStock" )
except:
    print('Error when Connecting to DB.')   
    sys.exit()  
cursor = db.cursor()
# 插入一條記錄
insertSql="insert into stockinfo (date,open,close,high,low,vol,stockCode ) values ('20190103',16.65,15.31,15.78,16.24,94733382,'600895')"
cursor.execute(insertSql)
db.commit()     # 需要呼叫commit方法才能把動作傳送到資料表中使之生效
# 移除一條記錄
deleteSql="delete from stockinfo where stockCode = '600895' and date='20190103'"
cursor.execute(deleteSql) 
db.commit() 
# 更新資料
insertErrorSql="insert into stockinfo (date,open,close,high,low,vol,stockCode ) values ('201901030000',16.65,15.31,15.78,16.24,94733382,'600895')"
cursor.execute(insertErrorSql)  # 插入了一條錯誤的記錄，date不對
db.commit() 
updateSql="update stockinfo set date='20190103' where date='201901030000' and stockCode = '600895'"
cursor.execute(updateSql)
db.commit()
cursor.close()
db.close()