# ch20_8.py
def uniquePaths(m, n):
    map = [[0] * n] * m
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:            # 行或列為0
                map[i][j] = 1               # 紀錄只有1種走法
            else:
                # 左邊 +上方走法的和
                map[i][j] = map[i - 1][j] + map[i][j - 1]   
    return map[m - 1][n - 1]                # 傳回走法的和
                          
print(uniquePaths(3, 2))
print(uniquePaths(7, 3))







      



    





        





