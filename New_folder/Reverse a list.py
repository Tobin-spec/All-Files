class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

num_list = [1,2,3,4,5]

stack = Stack()
for i in num_list:
    stack.push(i)

reverse_list = []

for c in range(len(stack.items)):
    reverse_list.append(stack.pop())

print(reverse_list)
