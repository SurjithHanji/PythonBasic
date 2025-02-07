dic={
    "harry":"human being",
    "spoon":"object"
}
print(dic["harry"])

info={"name":"karan","age":20,"eligible":True}
print(info)
print(info['name'])
print(info.get('name'))
print(info.keys())

for key in info.keys():
    print(info[key])

print(info.values())

print(info.items())

for key,value in info.items():
   print(f"The value corresponding to the key {key} is {info[key]}")
   print(f"The value corresponding to the key {key} is {value }")