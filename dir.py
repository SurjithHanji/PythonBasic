x=[1,2,3]
print(dir(x))
print(x.__add__)
print(x.__reduce__)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("joun",34)
print(p.__dict__)

print(help(str))