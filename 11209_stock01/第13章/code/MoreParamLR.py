#!/usr/bin/env python
#coding=utf-8
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score 
# 載入資料
dataset = datasets.load_boston()
# 特征值集合，不內含目的值房價
featureData = dataset.data
housePrice = dataset.target
 
lrTool = LinearRegression()
lrTool.fit(featureData, housePrice)
# 輸出系數和截距 
print(lrTool.coef_)
print(lrTool.intercept_ )  
 
# 畫圖顯示
plt.scatter(housePrice,housePrice,label='Real Data')
plt.scatter(housePrice,lrTool.predict(featureData),c='R',label='Predicted Data')

print(r2_score(housePrice, lrTool.predict(featureData)))

plt.legend(loc='best')      # 繪制圖例
plt.rcParams['font.sans-serif']=['SimHei']
plt.xlabel("House Price")
plt.ylabel("Predicted Price")
plt.show()