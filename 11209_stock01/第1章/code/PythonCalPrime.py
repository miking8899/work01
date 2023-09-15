# !/usr/bin/env python
# coding=utf-8

def printPrime(maxNum):
    num=[];
    currentNum=2
    for currentNum in range(2,maxNum+1):
       devidedNum=2
       for devidedNum in range(2,currentNum):
          if(currentNum%devidedNum==0):
              break
       if currentNum == devidedNum:   
           num.append(currentNum) # 把質數加入到清單裡
       #print(num)          
    print(num)
       
printPrime(101)