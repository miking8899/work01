# !/usr/bin/env python
# coding=utf-8
import csv,os
fileName="c:\\1\\stock.csv";
if not os.path.isfile(fileName):    # 判斷檔案是否存在
    print("File not exist!" + fileName)
else: 
    file = open(fileName,'r')       # 以讀的模式開啟檔案
    reader = csv.reader(file)
    for row in reader:              # 逐行讀取csv檔案
        try:
            print(row)
        except:
            print("Error when Reading Csv file.")
    file.close()                    # 讀完後關閉檔案      