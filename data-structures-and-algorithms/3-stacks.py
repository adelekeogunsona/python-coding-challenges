"""An implementation of the Stack data structure in Python"""

class Stack:

    def __init__(self):
        self.stack = list()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def peak(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
    
    def __str__(self):
        return str(self.stack)


my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
# print(my_stack)
assert my_stack.pop() == 3
assert my_stack.peak() == 1
assert my_stack.pop() == 1
assert my_stack.pop() == None
