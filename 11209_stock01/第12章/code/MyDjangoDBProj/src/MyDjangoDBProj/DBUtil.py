# !/usr/bin/env python
# coding=utf-8
from django.http import HttpResponse
from . import models
 
def insertStock(request):
    stockInfo = models.stockInfo(date='20190101',open=10.0,close=10.5,high=10.7,low=10.3,vol=10,stockCode='DemoCode')
    stockInfo.save()    
    return HttpResponse("OK!")

def insertMoreStock(request):
    stockInfoList=[]
    stock1 = models.stockInfo(date='20190101',open=10.0,close=10.5,high=10.7,low=10.3,vol=10,stockCode='DemoCode')
    stockInfoList.append(stock1)
    stock2 = models.stockInfo(date='20190102',open=10.5,close=11,high=11.2,low=10.8,vol=12,stockCode='DemoCode')
    stockInfoList.append(stock2)
    models.stockInfo.objects.bulk_create(stockInfoList)
    return HttpResponse("OK!")

def deleteStock(request):
    # 移除所有資料記錄
    # models.stockInfo.objects.all().delete()
    # 移除指定資料記錄
    models.stockInfo.objects.filter(date='20190101',stockCode='DemoCode').delete()
    return HttpResponse("OK!")

def updateStock(request):
    # 找到資料記錄並更新
    models.stockInfo.objects.filter(date='20190101',stockCode='DemoCode').update(open=12,close=13)
    return HttpResponse("OK!")

def getAllStock(request):
    stockInfoList = models.stockInfo.objects.all()
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def getStockWithFilter(request):
    stockInfoList = models.stockInfo.objects.filter(date='20190101')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoLike(request):
    # 傳回包括2019的股票資料
    stockInfoList = models.stockInfo.objects.filter(date__contains='2019')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoStartswith(request):
    # 傳回以2019開頭的股票資料
    stockInfoList = models.stockInfo.objects.filter(date__startswith='2019')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoEndswith(request):
    # 傳回以2019結束的股票資料
    stockInfoList = models.stockInfo.objects.filter(date__endswith='2019')
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

def demoRange(request):
    # 大於8，小於12
    # stockInfoList = models.stockInfo.objects.filter(open__gt=8,open__lt=12)
    # 大於等於8，小於等於12
    stockInfoList = models.stockInfo.objects.filter(open__gte=8,open__lte=12)
    response = ""
    for stock in stockInfoList:
        response += 'stockCode is:' + stock.stockCode + ',date is:' + stock.date +',open is:' +str(stock.open)+',close is:'+str(stock.close)+'<br>'
    return HttpResponse(response)

from django.db import connection
def demoSQL(request):
    cursor = connection.cursor()
    try:
        cursor.execute('select * from stockInfo')
        result=cursor.fetchall()
    finally:
        cursor.close()    
    return HttpResponse(result)