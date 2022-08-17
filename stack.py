class Stack:
    stack = {}
    top = 0

    def stack_empty(self):
        if self.top == 0: 
            return True
        else: 
            return False
    
    def pop(self):
        if self.stack_empty():
            return "underflow error"
        else:
            self.top = self.top - 1
            return self.stack[self.top + 1]
    
    def push(self, element):
        self.top = self.top + 1
        self.stack[self.top] = element


stack = Stack()
print(f'inital top value: {stack.top}')

underflow_error = stack.pop() # empty pop, underflow error
print(f'underflow error: {underflow_error}')

stack.push(3)
print(f'get top element: {stack.stack[stack.top]}')

stack.pop()
print(f'stack should be empty again: {stack.top}')