n=int(input("enter the number:"))
ll=int(input("entr the lowerlimit:"))
ul=int(input("entr the upper limit:"))
if(n==0) or (n==1):
    print("its not prime and its not coprime ")
elif(n>1):
    for i in range(ll,ul+1):
        if(n%i==0):
            print("its not prime")
            break
        else:
            print("its prime")
            break

else:
    print("its not a number in given range")