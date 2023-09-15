# ex9_4.py
def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length-1):
        print(f"第 {i+1} 次外圈排序")
        for j in range(length-1-i):
            if nLst[j] < nLst[j+1]:
                nLst[j],nLst[j+1] = nLst[j+1],nLst[j]
            print(f"第 {j+1} 次內圈排序 : {nLst}")
    return nLst

data = []
while True:
    val = input("請輸入數值(Q或q代表輸入結束) : ")
    if val == "Q" or val == "q":
        break
    data.append(int(val))
print("原始串列 : ", data)
print("排序結果 : ", bubble_sort(data))











