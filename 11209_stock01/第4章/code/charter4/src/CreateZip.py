# !/usr/bin/env python
# coding=utf-8
import zipfile,os   # 匯入兩個庫
zip=zipfile.ZipFile('c:\\1.zip', 'w')   # 指定壓縮後的檔名
try:
    for curPath, subFolders, files in os.walk('c:\\1'):
        for file in files:              # 壓縮所有的檔案
            print(os.path.join(curPath, file))        
            zip.write(os.path.join(curPath, file))
except:
    print("Error When Creating Zip File")
finally:                
    zip.close()