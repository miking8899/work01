# ch9_6.py
def selection_sort(nLst):
    ''' 選擇排序 '''
    for i in range(len(nLst)-1):        
        index = i                           # 最小值的索引
        for j in range(i+1, len(nLst)):     # 找最小值的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:                      # 如果目前索引是最小值索引
            pass                            # 不更動
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]   # 資料對調
    return nLst

cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用selection_sort( )由小排到大")
selection_sort(cars)           
print("排序串列結果 = ",cars)



    
