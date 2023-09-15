# ex1_6.py
import itertools

x = ['a', 'b', 'c', 'd', 'e', 'f']
perm = itertools.permutations(x)
n = 0
for i in perm:
    n += 1
    print(i)
print(f"總共有 {n} 組合方式")




















