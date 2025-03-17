d={}
print(type(d))

a={1:"hlo",2:"hey",3:"houddo"}
print(a)

print(a[1])
print(a.get(1))

# d["1"]=1
# d["2"]=2
# print(d.get(1))


## set

s=set()
print(type(s))

s1=set("hello")
print(s1)

s1.add("y")
print(s1)

print("h" in s1)