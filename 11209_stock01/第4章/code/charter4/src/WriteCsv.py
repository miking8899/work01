# !/usr/bin/env python
# coding=utf-8
import csv  # 匯入csv模組
head=['code','price','Date']
stock1=['600001',26,'20181212']
stock2=['600002',32,'20181212']
stock3=['600003',32,'20181212']
# 以'a'追加寫模式開啟檔案
file = open('c:\\1\\stock.csv','a',newline='')
# 設定寫入的物件
write = csv.writer(file)
# 寫入實際的內容
write.writerow(head)
write.writerow(stock1)
write.writerow(stock2)
write.writerow(stock3)
print("Finishe Writing CSV File.")