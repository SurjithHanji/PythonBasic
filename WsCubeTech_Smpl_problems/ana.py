nterms=int(input("enter the number of terms:"))
result=list(map(lambda x :2 ** x, range(nterms+1)))
print(result)

for i in range(nterms+1):
    print("the value of 2 raised to power ",i,"is",result[i])