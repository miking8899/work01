# !/usr/bin/env python
# coding=utf-8
import pandas as pd 
from sklearn import svm,preprocessing
import matplotlib.pyplot as plt 

origDf=pd.read_csv('D:/stockData/ch13/6035052018-09-012019-05-31.csv',encoding='gbk')
df=origDf[['Close', 'High', 'Low','Open' ,'Volume','Date']]
# diff清單示本日和上日收碟價的差
df['diff'] = df["Close"]-df["Close"].shift(1)
df['diff'].fillna(0, inplace = True)
# up清單示本日是否上漲，1表示漲，0表示跌
df['up'] = df['diff']   
df['up'][df['diff']>0] = 1
df['up'][df['diff']<=0] = 0
# 預測值暫且起始化為0
df['predictForUp'] = 0

# 目的值是真實的漲跌情況
target = df['up']

length=len(df)
trainNum=int(length*0.8)
predictNum=length-trainNum
# 選取指定列作為特征列
feature=df[['Close', 'High', 'Low','Open' ,'Volume']]
# 標准化處理特征值
feature=preprocessing.scale(feature)

# 訓練集的特征值和目的值
featureTrain=feature[0:trainNum]
targetTrain=target[0:trainNum]
svmTool = svm.SVC(kernel='linear')
svmTool.fit(featureTrain,targetTrain)

print(svmTool.score(featureTrain,targetTrain))

predictedIndex=trainNum
# 逐行預測測試集
while predictedIndex<length:
    testFeature=feature[predictedIndex:predictedIndex+1]            
    predictForUp=svmTool.predict(testFeature)    
    df.ix[predictedIndex,'predictForUp']=predictForUp    
    predictedIndex = predictedIndex+1    

# 該物件只包括預測資料，即只包括測試集
dfWithPredicted = df[trainNum:length]

# 開始繪圖，建立兩個子圖
figure = plt.figure()
# 建立子圖     
(axClose, axUpOrDown) = figure.subplots(2, sharex=True)
dfWithPredicted['Close'].plot(ax=axClose)
dfWithPredicted['predictForUp'].plot(ax=axUpOrDown,color="red", label='Predicted Data')
dfWithPredicted['up'].plot(ax=axUpOrDown,color="blue",label='Real Data')
plt.legend(loc='best')      # 繪制圖例

# 設定x軸座標的標簽和旋轉角度
major_index=dfWithPredicted.index[dfWithPredicted.index%2==0]
major_xtics=dfWithPredicted['Date'][dfWithPredicted.index%2==0]
plt.xticks(major_index,major_xtics)
plt.setp(plt.gca().get_xticklabels(), rotation=30) 
plt.title("透過SVM預測603505的漲跌情況")
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()