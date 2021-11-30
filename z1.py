

class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self, ):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        last = self.stack[-1]
        self.stack.pop(-1)
        return last

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

