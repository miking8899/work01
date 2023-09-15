# !/usr/bin/env python
# coding=utf-8
import os,shutil    # 透過import匯入兩個庫
def moveFile(src,dest):
    if not os.path.isfile(src):
        print("File not exist!" + src)
    else:
        fpath=os.path.split(dest)[0]   # 取得路徑
        if not os.path.exists(fpath):
            os.makedirs(fpath)         # 若果路徑不存在，則建立
        shutil.move(src,dest)          # 搬移檔案
        print('Finished Moving')
def copyFile(src,dest):
    if not os.path.isfile(src):
        print("File not exist!" + src)
    else:
        fpath=os.path.split(dest)[0]    # 取得路徑
        if not os.path.exists(fpath):
            os.makedirs(fpath)          # 建立路徑
        shutil.copyfile(src,dest)       # 複製檔案
        print('Finished Copying')
# 呼叫方法
srcForCopy='c:\\1\\python.txt'
destForCopy='c:\\1\\python1.txt'
copyFile (srcForCopy,destForCopy)
srcForMove='c:\\1\\python.txt'
destForMove='c:\\1\\python2.txt'
moveFile (srcForMove,destForMove)

