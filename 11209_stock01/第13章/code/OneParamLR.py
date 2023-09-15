# !/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
 
# 從檔案中讀資料，並轉換成DataFrame格式
dataset=datasets.load_boston()
data=pd.DataFrame(dataset.data)
data.columns=dataset.feature_names  # 特征值
data['HousePrice']=dataset.target   # 房價，即目的值
 
# 這裡單純計算離中心區域的距離和房價的關系
dis=data.loc[0:data['DIS'].size-1,'DIS'].as_matrix()
housePrice=data.loc[0:data['HousePrice'].size-1,'HousePrice'].as_matrix()
 
# 轉置一下，否則資料是豎排的
dis=np.array([dis]).T
housePrice=np.array([housePrice]).T
 
# 訓練線性模型
lrTool=LinearRegression()
lrTool.fit(dis,housePrice)
# 輸出系數和截距 
print(lrTool.coef_)
print(lrTool.intercept_)  
 
# 畫圖顯示
plt.scatter(dis,housePrice,label='Real Data')
plt.plot(dis,lrTool.predict(dis),c='R',linewidth='2',label='Predict')

print(lrTool.score(dis,housePrice))
print(r2_score(housePrice, lrTool.predict(dis)))

# 驗證資料
print(dis[0])
print(lrTool.predict(dis)[0])
print(dis[2])
print(lrTool.predict(dis)[2])

plt.legend(loc='best')      # 繪制圖例
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("DIS與房價的線性關系")
plt.xlabel("DIS")
plt.ylabel("HousePrice")
plt.show()