class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e=Employee("Harru",12000)
print(e.name)
print(e.salary)

stri="harry-12000"
e1=Employee(stri.split("-")[0],stri.split("-")[1])
print(e1.name)
print(e1.salary)
