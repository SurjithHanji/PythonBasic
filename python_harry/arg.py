def avg(a,b):
    print("the average is:",(a+b)/2)
avg(4,6)


#passing arguments

## 1) Default Argument Passing

def avg(a=1,b=9):
    print("the average is:",(a+b)/2)

avg()
avg(5,1)

## 2) Keyword argument passing

def avg2(a=9,b=21):
    print("the average is:",(a+b)/2)

avg2(b=9)
avg2(b=9,a=21)


## 3) Required argument passing

def avg3(fname,lname):
    print("hello",fname,lname)

avg3("surjith","hanji")


## 4) variable length argument passing

def avg4(*num):
    sum=0
    for i in num:
        sum+=i
    print("avg is :",sum/len(num))

avg4(4,5,7)