from collections import deque
stack=deque()
print(dir(stack))

stack.append("hey")
stack.append("how")
stack.append("are")
stack.append("you")
print(stack)

print(stack.pop())

print(stack)