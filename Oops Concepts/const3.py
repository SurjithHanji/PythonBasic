class Person:

    ##Parameterized constructor


    def __init__(self,name,occ):
        self.name=name
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("harry","hr")
b=Person("shraddah","manager")
c=Person(1,2)
a.info()
b.info()
a.info()