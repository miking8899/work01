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
# 改寫後的Tool類別          
class Tool(object):    
    def __init__(self,fileHandle):
        self.fileHandle = fileHandle
        self.dbHandle = DBHandle()
    def calDataInFile(self,path):
        self.fileHandle.read(path)        
        # 統計檔案中的資料
    def calDataInDB(self,path):
        self.dbHandle.read(path)        
        # 統計檔案中的資料
# 使用類別        
fileHandle =  FileHandle()       
tool = Tool(fileHandle)
tool.calDataInFile("c:\\1.txt")         # 輸出Reading File
tool.calDataInDB("localhost:3309/myDB") # 輸出Reading DB