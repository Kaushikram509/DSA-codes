class Stack:
    def __init__(self):
        self.stack=[]


        #push
    def push(self, data):
        self.stack.append(data)

        #pop
    def pop(self):
        if(self.is_Empty()):
            return "Stack is Empty"
        return self.stack.pop()
    
        #peek
    def peek(self):
        if(self.is_Empty()):
            return "Stack is empty"
        return self.stack[-1]
    
        #is Empty
    def is_Empty(self):
        return len(self.stack) == 0
    

        #Size
    def Size(self):
        return len(self.stack)
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top:", s.peek())
print("Popped:",s.Size())
print("Is Empty:",s.is_Empty())
