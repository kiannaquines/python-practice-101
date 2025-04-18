class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        return self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        
        return self.items[-1]

    def reverse(self):
        self.items = self.items[::-1]

        return self.items

    def clear(self):
        return self.items.clear()

    def __str__(self):
        return f"Stack {self.items}"

if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)

    print(stack)

    size = stack.size()

    print(size)

    stack.pop()

    print(stack)

    print(stack.reverse())

    stack.clear()

    print(stack)
