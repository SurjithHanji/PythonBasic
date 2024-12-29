n=int(input("enter the n value:"))
tmp=n
sum=0
while(tmp>0):
    digit=tmp%10
    cube=digit**3
    sum+=cube
    tmp=tmp//10

if(sum==n):
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")

