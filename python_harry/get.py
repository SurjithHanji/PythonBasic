class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"the name of employee:{self.name} is {self.id}")


class programmer(employee):
    def showlanguage(self):
        print("the default language is python")

class developer(programmer):
    def dev(self):
        print("default is front end web developer")

e=employee("rohan",420)
e.showdetails()

e1=programmer("gagan",3100)
# e1.showdetails()
e1.showlanguage()

e2=developer("alex",300)
e2.dev()