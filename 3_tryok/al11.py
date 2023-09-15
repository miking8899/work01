class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def inser_list(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node


link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()
print(" 新的連結 ")
link.inser_list(1000)
link.print_list()

num = 134

while num >= 0:
    num = int(input("請輸入要插入的連結資料: "))
    link.inser_list(num)
link.print_list()

# exercise 3_3.py link list insert OK 3Q
