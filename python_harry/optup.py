tupl=("spain","italy","india","Russia")
temp=list(tupl)
temp.append("colombia")
temp.pop(1)
print(tupl)
tupl=tuple(temp)
print(tupl)



t=(1,2,3,4,5,5,6,7,8)
res=t.count(5)
print(res)

print(t.index(5))

print(t.index(3,1,6))