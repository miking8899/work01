# ch7_5.py
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("最大 3 個  : ", heapq.nlargest(3, h))
print("最小 3 個  : ", heapq.nsmallest(3, h))
print("原先資料集 : ",h)




















