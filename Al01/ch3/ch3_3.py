# ch3_3.py
class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data            # 資料
        self.next = None            # 指標

class Linked_list():
    ''' 鏈結串列 '''
    def __init__(self): 
        self.head = None            # 鏈結串列第 1 個節點

    def print_list(self):
        ''' 列印鏈結串列 '''   
        ptr = self.head             # 指標指向鏈結串列第 1 個節點
        while ptr:
            print(ptr.data)         # 列印節點
            ptr = ptr.next          # 移動指標到下一個節點

    def begining(self, newdata):
        ''' 在第 1 個節點前插入新節點 '''
        new_node = Node(newdata)    # 建立新節點
        new_node.next = self.head   # 新節點指標指向舊的第1個節點
        self.head = new_node        # 更新鏈結串列的第一個節點

link = Linked_list()
link.head = Node(5)
n2 = Node(15)                       # 節點 2
n3 = Node(25)                       # 節點 3
link.head.next = n2                 # 節點 1 指向節點 2
n2.next = n3                        # 節點 2 指向節點 3
link.print_list()                   # 列印鏈結串列 link
print("新的鏈結串列")
link.begining(100)                  # 在第 1 個節點前插入新的節點
link.print_list()                   # 列印新的鏈結串列 link










