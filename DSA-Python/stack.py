sk=[]
sk.append(10)
sk.append(20)
sk.append(30)
print(sk)

print(type(sk))

sk.pop()
sk.pop()
sk.pop()
print(sk)

if(len(sk))==0:
    print(True)

sk.append(20)
sk.append(30)
sk.append(50)

print(sk)
print(sk[-1])