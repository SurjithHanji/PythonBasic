s={1,2,5,6}
s2={3,6,7}
print(s.union(s2))
print(s.update(s2))
print(s.intersection(s2))

cities1={"tokyo","madrid","Berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities2.union(cities1)
print(cities3)
cities1.intersection_update(cities2)
print(cities1)


print(cities1.symmetric_difference(cities2))

print(cities1.union(cities2))

print(cities1.intersection_update(cities2))

print(cities1.isdisjoint(cities2))
print(cities1.issuperset(cities2))
print(cities1.issubset(cities2))

print(cities1.add("bangalore"))
print(cities1)

print(cities1.remove("madrid"))
print(cities1.remove("tokyo"))

if "madrid" in cities1:
    print("hello")
else:
    print("no")