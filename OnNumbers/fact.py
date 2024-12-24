n=int(input("enter a value to find factorial:"))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print("factorial is ",fact(n))