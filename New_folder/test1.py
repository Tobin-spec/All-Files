#variable to store the input
the_code = input()
#i wanna reverse the input
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

stack = Stack()
for c in the_code:
    stack.push(c)


reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

#i wanna remove characters other than letters and spaces
alphabets = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def function(x):
    for char in x:
        if char not in alphabets:
            x = x.replace(char,'')
    return x
#i wanna print the decoded input
print(function(reverse))

