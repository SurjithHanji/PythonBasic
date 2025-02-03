def sumofN(n):
    if n<=1:
        return n
    else:
        return n+sumofN(n-1)
    
n=int(input("value for n:"))

if n<=0:
    print("enter a positive number")
else:
    print("the sum of natural numbers is:",sumofN(n))