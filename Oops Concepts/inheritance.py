class Emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"{self.name} has id no {self.id}")


class Program(Emp):
    def __init__(self,name,id,job):
        self.name=name
        self.id=id
        self.job=job
    def showLang(self):
        print("default lang is python")

    def details(self):
        print(f"{self.name} having id {self.id} has a very inerest on {self.job} ")

a=Emp("sundar",100)
a.showDetails()
b=Program("elos",401,"je")
b.showDetails()   
b.showLang()
c=Program("bro",120,"intern")
c.details()