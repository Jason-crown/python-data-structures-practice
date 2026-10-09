
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # 30
print(stack.pop())   # 30
print(stack.pop())   # 20
print(stack.size())  # 1
