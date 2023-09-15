# ch19_5.py

n = '10001'
r = 0
for i in range(len(n)):
    r += int(n[i]) * (2 ** (len(n) - i - 1))
print(f"{n} = {r}")


