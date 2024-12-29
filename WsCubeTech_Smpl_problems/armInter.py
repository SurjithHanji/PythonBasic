

ll=int(input("entr lowerlimit:"))
ul=int(input("enter the upperlimit:"))
for n in range(ll,ul+1):
    order=len(str(n))
    sum=0
    tmp=n
    while tmp>0:
       digit=tmp%10
       cube=digit**3
       sum+=cube
       tmp//=10
       
    if n==sum:
        print(n)