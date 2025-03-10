class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def action(self):
        print(f"{self.name} is barking")

dog1=dog("rocky",2)
dog2=dog("joe",1.7)

print(f"{dog1.name} is {dog1.age} years old")

dog1.action()