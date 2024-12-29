a=0
b=1
n=int(input("entr the number until we need to do fibo:"))
if(n==1):
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,n+1):
       c=a+b
       a=b
       b=c
       print(c)