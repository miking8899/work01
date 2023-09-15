# ex16_5.py
def gold(W, wt, val):
    ''' 動態規劃演算法 '''
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]   # 最初化表格
    items = [[[] for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格    
    for r in range(n + 1):                                  # 填入表格row
        for c in range(W + 1):                              # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r-1] <= c:
                cur = val[r-1] + table[r-1][c-wt[r-1]]
                cur_items = []
                cur_items.append(item[r-1])
                if items[r-1][c-wt[r-1]]:
                    cur_items += items[r-1][c-wt[r-1]]
                pre = table[r-1][c]
                pre_items = items[r-1][c]                
                if cur > pre:   
                    table[r][c] = cur
                    items[r][c] = cur_items
                else:
                    table[r][c] = pre
                    items[r][c] = pre_items
            else:
                table[r][c] = table[r-1][c]
                items[r][c] = items[r-1][c]
    return items, table[n][W]

item = ['礦山 A', '礦山 B', '礦山 C', '礦山 D', '礦山 E']
value = [10, 16, 20, 22, 25]                                # 金礦產值
weight = [3, 4, 3, 5, 5]                                    # 單項金礦所需人力
gold_weight = 10                                            # 總人力
items, total_value = gold(gold_weight, weight, value)
print('最大產值 = {} 公斤'.format(total_value))
print('礦山組合 : ', items[len(item)][gold_weight])







   















