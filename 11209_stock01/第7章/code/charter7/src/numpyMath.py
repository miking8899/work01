# !/usr/bin/env python
# coding=utf-8
import numpy as np
print(np.abs(-10))      # 求絕對值，該表達式傳回10
print(np.around(1.2))   # 去掉小數位數，該表達式傳回1
print(np.round_(1.7))   # 四捨五入，該表達式傳回2
print(np.ceil(1.1))     # 求大於或等於該數的整數，該表達式傳回2
print(np.floor(1.1))    # 求小於或等於該數的整數，該表達式傳回1
print(np.sqrt(16))      # 求平方根值，該表達式傳回4
print(np.square(6))     # 求平方，該表達式傳回36
print(np.sign(6))       # 符號函數，若果大於0則傳回1，該表達式傳回1
print(np.sign(-6))      # 符號函數，若果小0則傳回-1，該表達式傳回-1
print(np.sign(0))       # 符號函數，若果等於0則傳回0，該表達式傳回0
print(np.log10(100))    # 求以10為底的對數，該表達式傳回2
print(np.log2(4))       # 求以2為底的對數，該表達式傳回2
print(np.exp(1))        # 求以e為底的冪次方，該表達式傳回e
print(np.power(2,3))    # 求2的3次方，該表達式傳回8