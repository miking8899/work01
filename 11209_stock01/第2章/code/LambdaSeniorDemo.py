# !/usr/bin/env python
# coding=utf-8
# 第3個參數是lambda表達式
def add(x,y,func):
    return func(x) + func(y)
print(add(2,4,lambda a:a*a)) # 2的平方加4的平方等於20

print("My Stock List".find("stock")) # 輸出-1，表示沒找到
def existKey(key,words,func):
    return func(words).find(key)
# 輸出3，表示找到了
print(existKey("stock","My Stock List" ,lambda words:words.lower()))