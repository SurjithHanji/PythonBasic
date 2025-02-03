tup=(1,5,6,"green")
print(type(tup),tup)

tup1=(1)
print(type(tup1))

tup2=(1,)
print(type(tup2))


print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
print(len(tup))


if "green" in tup:
    print("yes gren is in tup")
else:
    print("no way") 

tup4=tup[1:4]
print(tup4)