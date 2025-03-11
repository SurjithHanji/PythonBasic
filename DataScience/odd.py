import numpy as np

def even(arr):
    return arr[arr%2==0]

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
even_numbers=even(arr)
print(even_numbers)


#addition of 10
import numpy as np
def add(arr):
    return arr+10
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
addi=add(arr)
print(addi)


#multiplication
import numpy as np
def mul(arr1,arr2):
    return arr1*arr2
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
result=mul(arr1,arr2)
print(result)

#square
import numpy as np
def square(arr):
    result=np.where(arr>5,arr**2,0)
    return result

arr=np.array([1,56,76,5])
result=square(arr)
print(result)
    