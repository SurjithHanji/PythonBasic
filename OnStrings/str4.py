def if_prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
n=int(input("enter a number:"))
if if_prime(n):
    print("prime")
else:
    print("not prime")