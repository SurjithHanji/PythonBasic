arr=[24,41,33,42,17]

def selection(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i,n):
            if arr[j]<arr[mini]:
                mini=j
                arr[i],arr[mini]=arr[mini],arr[i]

selection(arr)
print(arr)