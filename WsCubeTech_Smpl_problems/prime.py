n=int(input("entr the number:"))
if n==1 or n==0:
    print("its not prime and not coprime")
if(n>1):

    for i in range(2,n):
        if(n%i==0):
            print(n,"its not prime")
            break
        else:
            print(n,"its prime")
            break
