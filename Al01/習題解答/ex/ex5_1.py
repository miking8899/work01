# ex5_1.py
class Stack():
    def __init__(self):
        self.my_stack = []

    def my_push(self, data):
        self.my_stack.append(data)

    def my_pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)

    def isEmpty(self):
        return self.my_stack == []

    def get(self):
        return self.my_stack[-1]

stack = Stack()
fruits = ['Grape', 'Mango', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print(f'將 {fruit} 水果堆入堆疊')

print(f'堆疊有 {stack.size()} 種水果')
print(f'堆疊取出 {stack.get()} 水果, 同時不刪除')
print(f'堆疊取出 {stack.get()} 水果, 同時不刪除')
print(f'堆疊取出 {stack.get()} 水果, 同時不刪除')
while not stack.isEmpty():
    print(stack.my_pop())

















