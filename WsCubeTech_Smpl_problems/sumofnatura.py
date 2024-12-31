def naturalSum(n):
    if n<=1:
        return n
    else:
        return n+naturalSum(n-1)
    
n=int(input("enter the n value:"))
if n<=0:
    print("enter positive number")
else:
    print("the sum of natural numbers is:",naturalSum(n))