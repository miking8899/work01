# !/usr/bin/env python
# coding=utf-8
# 定義沒傳回的函數
def printMsg(x,y):
    print "x is %d" %x
    print "y is %d" %y
# 透過return傳回
def add(x,y):
    return x + y
1
# 呼叫函數
printMsg(1,2)
# printMsg("1",2) 	# 顯示出錯，這就是不注意參數型態的後果
print add(100,50)

