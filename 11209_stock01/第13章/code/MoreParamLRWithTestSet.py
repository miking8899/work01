# !/usr/bin/env python
# coding=utf-8
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

 
dataset = datasets.load_boston()
# 特征值集合，不內含目的值房價
featureData = dataset.data
housePrice = dataset.target
# 劃分訓練集和測試集，測試集的比例是10% 
featureTrain, featureTrainTest, housePriceTrain, housePriceTest = train_test_split(featureData, housePrice, test_size=0.1)
# 建構線性回歸物件 
lrTool = LinearRegression()
# 用訓練集來擬合參數
lrTool.fit(featureTrain, housePriceTrain)
# 用訓練集繪圖
plt.scatter(housePriceTrain,lrTool.predict(featureTrain),c='R',label='Predicted Data')
plt.scatter(housePriceTrain,housePriceTrain,label='Real Data')
# 用測試集來計算方差
predictByTest = lrTool.predict(featureTrainTest)
# 用測試集計算方差
testResult = np.sum(((predictByTest - housePriceTest) ** 2) / len(housePriceTest))
print(testResult)
plt.show()