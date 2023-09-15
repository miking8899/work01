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
try:
    # 插入2條記錄
    insertSql1="insert into stockinfo (date,open,close,high,low,vol,stockCode ) values ('20190103',16.65,15.31,15.78,16.24,94733382,'600895')"
    cursor.execute(insertSql1)
    raise Exception 
    insertSql2="insert into stockinfo (date,open,close,high,low,vol,stockCode ) values ('20190104',16.58,15.60,15.70,16.30,68985635,'600895')"
    cursor.execute(insertSql2)
    db.commit()     # 沒問題就傳送
except:
    print("Error happens, rollback.")
    db.rollback()
finally:        
    cursor.close()
    db.close()

