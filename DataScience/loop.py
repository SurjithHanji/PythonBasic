# if else and elif

n=int(input("enter the number"))
if(n>0):
    print("positive")
elif(n==0):
    print("its zero")
else:
    print("negative")


# if else and elif

n=int(input("enter the number"))
if(n>0):
    print("positive")
elif(n==0):
    print("its zero")
else:
    print("negative")

#to eligible to became voter
age=int(input())
if(age>18):
    print("eligible to vote")
else:
    print("not eligible")



#facotial of a number

n=5
fact=1
while(n>0):
    fact*=n
    n-=1
print(f"factorial of a n is{fact}")


#skip negative numbers

l=[1,-23,43,64,-46,456,254,-2452,2133]
for num in l:
    if(num<0):
        continue
    print(num)


#continue 
#odd numbers from 1 to 5


n=int(input("enter the n :"))
for i in range(1,n+1):
    if(i%2==0):
        continue
    print(i)
        