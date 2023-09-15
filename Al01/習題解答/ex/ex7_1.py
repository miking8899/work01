# ex7_1.py
import heapq

h_list = [10, 21, 5, 9, 13, 28, 3]
h = []
for i in range(len(h_list)):
    heapq.heappush(h, h_list[i])
    print(f"插入 {h_list[i]:2d} 後的二元堆積樹 h = {h}")


