def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("enter the number:"))
if n<=0:
    print("entr positive number")
else:
    print("fibonacci sequesnce is:")
    for i in range(n):
        print(fibo(i))