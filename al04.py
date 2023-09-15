def fact(n):
    if n <= 1:
        return 1
    else:
        return (n*fact(n-1))


number = int(input("請輸入整數,算階數: "))

print(f"{number} 階的結果 = {fact(number)}")
3