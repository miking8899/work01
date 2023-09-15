# ch20_6.py
def isRectangleOverlap(rec1, rec2):
    x1, y1, x2, y2 = rec1
    x3, y3, x4, y4 = rec2
    return not (x2 <= x3 or y2 <= y3 or x1 >= x4 or y1 >= y4)

print(isRectangleOverlap([0, 0, 2, 2], [1, 1, 4, 4]))
print(isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 2]))








      



    





        





