def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)


degree = 10
print(f"{degree } 階!= {fact(degree)}")
