#using Deque(Double Ended Queue)
from collections import deque
stack = deque()

#push
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)
#pop
stack.pop()
print(stack)
#peek
print(stack[-1])
