# sum recursive

def sum(n):
    if (n <= 1):
        return 1
    else:
        return n+sum(n-1)


print("SUM total =", sum(10))
