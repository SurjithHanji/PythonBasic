print("-----------Simple Calculator---------------")
n1=float(input("enter the n1 value: "))
n2=float(input("enter the n2 value: "))
print("List OF Operations")
print("press 1 for addition\n press 2 for subtraction\n press 3 for multiplication\n press 4 for divison\n")
choice=int(input('enter your choice 1-4: '))
if choice==1:
    print("the addition of two numbers is:",n1+n2)
elif choice==2:
    print("the subtraction of two numbers is:",n1-n2)
elif choice==3:
    print("the multiplication of two numbers is:",n1*n2)
elif choice==4:
    print("the division of two numbers is:",n1/n2)
else:
    print("invalid choice")
    
