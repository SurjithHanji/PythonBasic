#public access modifier
class employee:
    def __init__(self):
        self.name="harry"

a=employee()
print(a.name)

#private access modifier
class payment:
    def __init__(self):
        self.__pay="no"
p=payment()
print(p._payment__pay)#to access private modifier


#protected access modifier

class student:
    def __init__(self):
        self._name="sooraj"
    
    def funname(self):
        return "koli"

class subject(student):
    pass

obj=student()
obj1=subject()

print(obj._name)
print(obj.funname())

print(obj1._name)
print(obj1.funname())

