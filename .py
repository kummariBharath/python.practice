class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
    
    def push(self, item):
        self.items.append(item)
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        return self.items.pop()
    
    def is_empty(self):
        return self.length == 0


# Test the Stack class
stack = Stack()
print(f"Is stack empty? {stack.is_empty()}")  # True

stack.push(10)
stack.push(20)
print(f"Is stack empty? {stack.is_empty()}")  # False
print(f"Stack length: {stack.length}")  # 2

stack.pop()
stack.pop()
print(f"Is stack empty? {stack.is_empty()}")  # True



