def double(x):
    return x*2
print(double(5))

def appl(fx,value):
    return 6+fx(value)



avg=lambda x,y:(x+y)/2
double2=lambda x:x*2
cube=lambda x:x*3

print(avg(20,10))
print(double2(3))
print(cube(7))


print(appl(cube,2))