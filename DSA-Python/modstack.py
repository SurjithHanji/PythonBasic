import collections
stack=collections.deque()
print(stack)

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()

print(stack)

print(stack[-1])

## LIFO queue

import queue
stack1=queue.LifoQueue()
stack1.put(20)
stack1.put(30)
print(stack1)

print(stack1.get())