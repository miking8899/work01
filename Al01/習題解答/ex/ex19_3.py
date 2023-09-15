# ex19_3.py
def isPrime(num):
    """ 測試num是否質數 """
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

N = int(input("請輸入大於1的整數做質數測試 = "))
prime = []
for n in range(2, N+1):
    if isPrime(n):                   
        prime.append(n)
print('從 2 至 {} 的質數如下 : '.format(N))
print(prime)

