import itertools

x = ["1", "2", "3", "4", "5"]
perm = itertools.permutations(x)

for i in perm:
    print(i)
