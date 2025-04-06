n=int(input())
rs=[]
while n>0:
    rem=n%10
    n=n//10
    rs.append(rem)
print(rs) 
print(len(rs))
print(type(rs))
     