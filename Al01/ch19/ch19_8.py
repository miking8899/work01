# ch19_8.py
import math
def isPrime(num):
    """ 測試num是否質數 """
    for n in range(2, int(math.sqrt(num))+1):
        if num % n == 0:
            return False
    return True

print("以下是 1 - 100 間所有質數")
for i in range(2,101):
    if isPrime(i):                   
        print(i, end="\t")



