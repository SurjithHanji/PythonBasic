# # fact=1
# n=int(input("entr the n value:"))
def fact(n):
    if n==0:
        return 1
    else:
        return (n*fact(n-1))
n=int(input("entr the n vlue:"))
res=fact(n)

print("factorial of a ",n,"is ",res)

