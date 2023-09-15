# ch20_9.py
def findContentChildren(greedy, size):
    greedy.sort()                                   # 排序greedy串列
    size.sort()                                     # 排序size串列
    index = 0                                       # size的索引
    ptr = 0                                         # greedy指標
    for g in greedy:                                # 遍歷greedy
        while len(size) > index and g > size[index]: # 如果不滿足g
            index += 1                              # 索引往後移
        if index < len(size) and size[index] >= g:  # 如果滿足
            ptr += 1                                # greedy指標往右移
            index += 1                              # 索引往後移    
    return ptr

print(findContentChildren([1, 2, 3], [1, 1]))
print(findContentChildren([1, 2], [1, 2, 3]))
print(findContentChildren([2, 2], [1, 2, 3]))
print(findContentChildren([2, 4], [1, 2, 3]))








      



    





        





