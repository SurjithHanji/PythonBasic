class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self,name,id,lang):
        # self.name=name
        # self.id=id
        super().__init__(name,id)
        self.lang=lang

rohan=employee("rohan", '420')
harry=programmer("harry","231","pyhton")

print(rohan.name) 

print(harry.name)
print(harry.id)
print(harry.lang)