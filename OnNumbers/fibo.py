def fibo(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return [0,1]

    sequence=[0,1]
    for i in range(n):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence

n=int(input("enter a value for n"))
print(fibo(n))
