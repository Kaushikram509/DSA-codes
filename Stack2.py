#using built-in function
class Stack:
    
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
    
Stack = []
#push
Stack.append(10)
Stack.append(20)
Stack.append(30)
print("Stack after push:",Stack)
#pop
removed = Stack.pop()
print("Popped Element:",removed)
print("Stack after pop:",Stack)
#peek
top = Stack[-1]
print("Top element:",top)
#isempty
print("Is stack empty?",len(Stack) == 0)
#size
print("Stack size:",len(Stack))
