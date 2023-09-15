# ex12_1.py
def mycount(nLst):
    if nLst == []:
        return 0
    return 1 + mycount(nLst[1:])

data = [1, 5, 9, 2, 8, 100, 81]
print('data         = ', data)
print('data元素個數 = ', mycount(data))






        





