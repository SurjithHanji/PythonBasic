class Person:
    name="harry"
    occupation="web dvlper"
    netwoeth="10"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()

a.name="suhbha"
a.occupation="ca"
print(a.name,a.occupation)
print(a.info())