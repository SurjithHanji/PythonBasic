l=[1,223,3,2,1,5,4,5,7]

m=l
m[0]=0
print(l)

m1=l.copy()
m1[0]=2
print(l)
print(m1)

l.insert(0,899)
print(l)

m3=[900,800,700]
l.extend(m3)
print(l)