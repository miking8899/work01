# ch1_10.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 10, 10)                # 建立含10個元素的陣列
ypt1 = xpt / xpt                            # 時間複雜度是 O(1)
ypt2 = np.log2(xpt)                         # 時間複雜度是 O(logn)               
ypt3 = xpt                                  # 時間複雜度是 O(n)
plt.plot(xpt, ypt1, '-o', label="O(1)")                  
plt.plot(xpt, ypt2, '-o', label="O(logn)")                  
plt.plot(xpt, ypt3, '-o', label="O(n)")
plt.legend(loc="best")                      # 建立圖例
plt.show()




