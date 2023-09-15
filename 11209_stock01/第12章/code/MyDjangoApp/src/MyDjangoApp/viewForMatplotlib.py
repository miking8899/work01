#!/usr/bin/env python
#coding=utf-8
from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
import sys
from io import BytesIO
import base64
import imp
imp.reload(sys)

def createMatplotlibImg(request):    
    figure = plt.figure()  
    ax = figure.add_subplot(111)
    ax.set_title('django整合matplotlib')
    x = np.array([1,2,3,4,5])
    ax.plot(x, x*x)
    plt.rcParams['font.sans-serif']=['SimHei']
    # 把圖形儲存為bytes格式，方便傳輸
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.close()     # 關閉plt物件，否則下次呼叫可能出錯    
    base64img = base64.b64encode(buffer.getvalue())    
    img = "data:image/png;base64,"+base64img.decode()
        
    return render(request, 'data.html', {
            'img': img
        })
    