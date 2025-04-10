from collections import Counter

l=[1,2,3,4,5,3,4,2,6,8,8,6,9]
print(Counter(l))

f=dict()
for i in range(0,len(l)):
    if l[i] in f:
        f[l[i]]+=1
    else:
        f[l[i]]=1
print(f[1])


