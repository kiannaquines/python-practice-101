class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        return self.items.append(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Cannot pop when stack is empty.')
        
        return self.items.pop()
    
    def reverse(self):
        if self.is_empty():
            raise IndexError('Cannot reverse when stack is empty')

        return self.items[::-1]
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty, you cannot peek it out.')
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == 0

    def clear(self):
        return self.items.clear()
    
    def __str__(self):
        return f"Stack Items: {self.items}"


if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.push(3)
    stack.push(2)
    stack.push(4)
    stack.push(7)
    stack.push(3)
    stack.push(10)

    stack.pop()
    print(stack)
    print(stack.reverse())
    print(stack.peek())
    print(stack.size())

    stack.clear()

    print(stack)
