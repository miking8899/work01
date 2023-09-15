# ch9_4.py    
def cocktail_sort(nLst):
    ''' 雞尾酒排序 '''
    n = len(nLst) 
    is_sorted = True
    start = 0                                       # 前端索引
    end = n-1                                       # 末端索引
    while is_sorted: 
        is_sorted = False                           # 重置是否排序完成
        for i in range (start, end):                # 往右比較
            if (nLst[i] > nLst[i + 1]) : 
                nLst[i], nLst[i + 1]= nLst[i + 1], nLst[i] 
                is_sorted = True
        print("往後排序過程 : ", nLst)
        if not is_sorted:                           # 如果沒有交換就結束
            break

        end = end-1                                 # 末端索引左移一個索引
        for i in range(end-1, start-1, -1):         # 往左比較
            if (nLst[i] > nLst[i + 1]): 
                nLst[i], nLst[i + 1] = nLst[i + 1], nLst[i] 
                is_sorted = True
        start = start + 1                           # 前端索引右移一個索引
        print("往前排序過程 : ", nLst)
    return nLst
         
data = [6, 1, 5, 7, 3] 
print("原始串列 : ", data)
print("排序結果 : ", cocktail_sort(data))

