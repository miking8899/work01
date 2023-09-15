# ex9_3.py
def selection_sort(nLst):
    ''' 選擇排序 '''
    for i in range(len(nLst)-1):        
        index = i                           # 最小值的索引
        for j in range(i+1, len(nLst)):     # 找最小值的索引
            if nLst[index][1] > nLst[j][1]:
                index = j
        if i == index:                      # 如果目前索引是最小值索引
            pass                            # 不更動
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]   # 資料對調
    return nLst

hotel = [('君悅酒店  ', 5560),
         ('東方酒店  ', 3450),
         ('北京大飯店', 4200),
         ('喜來登酒店', 5000),
         ('文華酒店  ', 5200),
         ]
         
print("北京酒店定價排行")
selection_sort(hotel)
for i in range(len(hotel)):
    print(f"{hotel[i][0]} -- {hotel[i][1]}")




    
