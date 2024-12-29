n=int(input("enter the n value fo add :"))
if(n<0):
    print("plz enter a positive number")
else:
    sum=0
    while(n>0):
        sum+=n
        n-=1
    print(sum)