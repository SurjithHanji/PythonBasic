import numpy as np
def extract_even_number(arr):
    return arr[arr%2==0]

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
even_numbers=extract_even_number(arr)
print(even_numbers)