def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
n=7 
print(fact(7))

import math
print(math.factorial(n))
n=7
print("factorial of",n,"is",fact(n))