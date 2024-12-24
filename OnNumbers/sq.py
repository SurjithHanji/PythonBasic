def is_square(n):
    return int(n**0.5)**2==n
n=int(input("enter a value for n:"))
if is_square(n):
    print("it is perfect square")
else:
    print("it is not")