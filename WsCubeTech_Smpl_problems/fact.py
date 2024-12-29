n=int(input("enter the value for n:"))
fact=1
if(n<0):
    print("not possible")
elif(n==0) or (n==1):
    print("factorial of 0 | 1 is",1)
else:
    for i in range(1,n+1):
        fact=fact*i
        i+=1
        

print("factorial of the number is:",fact)