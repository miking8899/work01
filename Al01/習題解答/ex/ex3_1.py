# ex3_1.py
class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data            # 資料
        self.next = None            # 指標

class Linked_list():
    ''' 鏈結串列 '''
    def __init__(self): 
        self.head = None            # 鏈結串列第 1 個節點

    def length(self):
        len = 0
        ptr = self.head
        while ptr:
            len += 1
            ptr = ptr.next
        return len

    def print_list(self):
        ''' 列印鏈結串列 '''   
        ptr = self.head             # 指標指向鏈結串列第 1 個節點
        while ptr:
            print(ptr.data)         # 列印節點
            ptr = ptr.next          # 移動指標到下一個節點

link = Linked_list()
link.head = Node(5)
n2 = Node(15)                       # 節點 2
n3 = Node(25)                       # 節點 3
link.head.next = n2                 # 節點 1 指向節點 2
n2.next = n3                        # 節點 2 指向節點 3
print("鏈結串列長度是 : ", link.length())
    








