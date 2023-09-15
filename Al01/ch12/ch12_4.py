# ch12_4.py
def hanoi(n, src, aux, dst):
    ''' src是來源木樁, aux是輔助木樁, dst是目的木樁 '''
    if n == 1:                          # 河內塔終止條件
        print(f'移動圓盤 {n} 從 {src} 到 {dst}')
    else:
        hanoi(n - 1, src, dst, aux)     # 將當下 n-1 木樁從 src 移到 aux
        print(f'移動圓盤 {n} 從 {src} 到 {dst}')
        hanoi(n - 1, aux, src, dst)     # 將當下 n-1 木樁從 aux 移到 dst
             
n = eval(input('請輸入圓盤數量 : '))
hanoi(n, 'A', 'B', 'C')







      



    
