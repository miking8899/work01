# ex15_5.py
import math
def greedy(graph, cities, start):
    ''' 貪婪演算法計算業務員旅行 '''
    visited = []                                    # 儲存已拜訪城市
    visited.append(start)                           # 儲存起點城市
    start_i = cities.index(start)                   # 獲得起點城市的索引
    distance = 0                                    # 旅行距離
    for outer in range(len(cities) - 1):            # 尋找最近城市
        graph[start_i][start_i] = math.inf          # 將自己城市距離設為極大值
        min_dist = min(graph[start_i])              # 找出最短路徑
        distance += min_dist                        # 更新總路程距離
        end_i = graph[start_i].index(min_dist)      # 最短距離城市的索引
        visited.append(cities[end_i])               # 將最短距離城市列入已拜訪        
        for inner in range(len(graph)):             # 將已拜訪城市距離改為極大值
            graph[start_i][inner] = math.inf
            graph[inner][start_i] = math.inf
        start_i = end_i                             # 將下一個城市改為新的起點
    return distance, visited
        
cities = ['北京', '天津', '西安', '武漢', '上海', '廣州']
graph = [[0,       132,    1120,   1200,   1463,   1888],
         [132,     0,      1182,   1367,   957,    2100],
         [1120,    1182,     0,    1035,   1509,   1950],
         [1200,    1367,   1035,     0,    686,    1030],
         [1463,     957,   1509,   686,    0,      1705],
         [1888,    2100,   1950,   1030,   1705,   0   ]  
        ]
start = input('請輸入開始城市起點 : ')
dist, visited = greedy(graph, cities, start)
print('拜訪順序 : ', visited)
print('拜訪距離 : ', dist)


   















