num=int(input("enter a number:"))
if(num<0):
    print("its negative number")
elif(num>0):
    if(num<10):
        print("its range is 10")
    elif(num<50 and num>10):
        print("its range is 50")
    else:
        print("its range is 100")
else:
    print("its anumber and thank u")
