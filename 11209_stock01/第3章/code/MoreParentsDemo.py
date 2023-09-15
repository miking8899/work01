# !/usr/bin/env python
# coding=utf-8
class FileHandle(object):   # 處理檔案的類別
    def read(self,path):
        print("Reading File")
        # 讀檔案                 
    def write(self,path,value):
        __path = path
        print("Writing File")
        # 寫檔案        
class DBHandle(object):     # 處理資料庫的類別
    def read(self,path):
        print("Reading DB")
        # 讀資料庫         
    def write(self,path,value):
        __path = path
        print("Writing DB")
        # 寫資料庫        
# Tool同時繼承了兩個類別          
class Tool(FileHandle,DBHandle):
#class Tool(DBHandle,FileHandle):
    def businessLogic(self):
        print("In Tool")
tool = Tool()
tool.read("c:\\1.txt")