import array as arr

arr1=arr.array('i',[1,2,3])
print(arr1.typecode)

arr2=arr.array('d',[1.0,3.0,4.0])
print(arr2.typecode)

print(len(arr1))
print(len(arr2))

for i in range(len(arr1)):
    print(arr1[i],end=" ")


x=list(range(0,100,2))
narr=arr.array('i',x)

for i in range(len(narr)):
    print(narr[i],end=" ")
print("\n")
print(narr[20])


arr1.insert(0,7)
arr1.append(10)
for i in range(len(arr1)):
    print(arr1[i],end="  ")


arr1[0]=78
arr1[-1]=90
for i in range(len(arr1)):
    print(arr1[i],end="  ")

arr1.pop()
for i in range(len(arr1)):
    print(arr1[i],end="  ")

arr1.pop(0)
for i in range(len(arr1)):
    print(arr1[i],end="  ")


x1=list(range(0,100,3))
arr3=arr.array('i',x1)

arr0=arr3[10:20]
for i in range(len(arr0)):
    print(arr0[i],end="  ")

arr4=arr3[::-1]
print("\n")
for i in range(len(arr4)):
    print(arr4[i],end="  ")



arr1.remove(3)
for i in range(len(arr1)):
    print(arr1[i],end="  ")

sarr=arr4.index(96)
res=arr4[sarr]
print(sarr,res)


import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)

z=np.zeros((2,2))
print(z)

o=np.ones((3,3))
print(o)

print(np.full((3,3),10))
print(np.eye(4))


print(np.array([[1,2,3,4,5],[5,6,7,8,9]]))