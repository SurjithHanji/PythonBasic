class Person:
     def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()

a.name="varsha"
a.occupation="hr"
b.name="soori"
b.occupation="tl"
a.info()
b.info()