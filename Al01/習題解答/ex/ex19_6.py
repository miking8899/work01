# ex19_6.py
def cr(head, foot):
    chicken = 0
    while True:
        rabbit = head - chicken                 # 頭的總數
        if 2 * chicken + 4 * rabbit == foot:    # 腳的總數
            break
        chicken += 1
        if chicken > head:
            return 'input', 'error!', False
    return chicken, rabbit, True

h = eval(input('請輸入頭的數量 : '))
f = eval(input('請輸入腳的數量 : '))
chicken, rabbit, flag = cr(h, f)
if flag:
    print(f'雞有 {chicken} 隻, 兔有 {rabbit} 隻')
else:
    print(chicken, rabbit)




