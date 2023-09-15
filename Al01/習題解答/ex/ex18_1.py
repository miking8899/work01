# ex18_1.py
import math

film = [5, 7, 8, 10, 2, 8]          # 玩命關頭特徵值
film_titles = [                     # 比較影片片名
    '復仇者聯盟',
    '決戰中途島',
    '冰雪奇緣',
    '雙子殺手',
]
film_features = [                   # 比較影片特徵值
    [2, 8, 8, 5, 6, 10],
    [5, 6, 9, 2, 5, 6],
    [8, 2, 0, 0, 10, 2],
    [5, 8, 8, 8, 3, 8],
]

dist = []                           # 儲存影片相似度值
for f in film_features:
    distances = 0
    for i in range(len(f)):
        distances += (film[i] - f[i]) ** 2
    dist.append(math.sqrt(distances))
    
min = min(dist)                     # 求最小值
min_index = dist.index(min)         # 最小值的索引

print("與玩命關頭最相似的電影 : ", film_titles[min_index])
print("相似度值 : ", dist[min_index])
for i in range(len(dist)):
    print(f"影片 : {film_titles[i]}, 相似度 : {dist[i]:6.2f}")

