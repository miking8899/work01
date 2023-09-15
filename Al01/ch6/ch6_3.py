# ch6_3.py
class Node():
    def __init__(self, data):
        ''' 建立二元樹的節點 '''
        self.data = data
        self.left = None
        self.right = None

    def print_root(self):
        print(self.data)

root = Node(20)
root.print_root()
















