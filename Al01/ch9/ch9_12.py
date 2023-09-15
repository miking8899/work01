# ch9_12.py    
def merge(left, right):
    ''' 兩數列合併 '''
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output

def merge_sort(nLst):
    ''' 合併排序 '''
    if len(nLst) <= 1:                      # 剩下一個或0個元素直接返回
        return nLst    
    mid = len(nLst) // 2                    # 取中間索引
    # 切割(divide)數列
    left = nLst[:mid]                       # 取左半段
    right = nLst[mid:]                      # 取右半段
    # 處理左序列和右邊序列
    left = merge_sort(left)                 # 左邊排序
    right = merge_sort(right)               # 右邊排序
    # 遞迴執行合併
    return merge(left, right)               # 傳回合併

data = [6, 1, 5, 7, 3, 9, 4] 
print("原始串列 : ", data)
print("排序結果 : ", merge_sort(data))

