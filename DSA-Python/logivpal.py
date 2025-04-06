n=int(input())
num=n
res=0
while num>0:
    rem=num%10
    res=(res*10)+rem
    num=num//10
if n==res:
    print("palli")
else:
    print("not")



