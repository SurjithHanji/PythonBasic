a=13
b=12
tmp=a
print(tmp)
a=b
print("the value of a:",a)
b=tmp
print("the value of b:",b)

a,b=b,a
print("value of a is:",a)
print("value of b is:",b)