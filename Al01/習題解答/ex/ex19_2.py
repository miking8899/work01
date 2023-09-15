# ex19_2.py
def convert(n, base):
    r = ''
    while n > 0:
        r = str(n % base) + r
        n //= base
    return r

n = eval(input('輸入整數 n = '))
base = eval(input('輸入底數 base = '))
print(f"{n} base {base} = {convert(n, base)}")



