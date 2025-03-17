stack=[]

def push():
    if(len(stack)==n):
        print("stack is full!")
    else:
        element=input("enter the element:")
        stack.append(element)
        print(stack)

def pop_ele():
    if(len(stack)==0):
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element is:",e)
        print(stack)

n=int(input("enter the limit of stack:"))
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input("enter your choice:"))
    if(choice==1):
        push()
    elif(choice==2):
        pop_ele()
    else:
        break