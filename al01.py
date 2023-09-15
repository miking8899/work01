import time


def rsum(i):
    #print(i, end='\t')
    if (i < 1):
        return 0
    else:
        return rsum(i-1)
    
    print(i, end="t")


rsum(10)
