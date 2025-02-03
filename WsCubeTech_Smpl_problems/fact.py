def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    
n=int(input("value for n:"))
if(n<=0):
    print("factorial is not exist for n<=0")
else:
    print("factorial of number is:",fact(n))