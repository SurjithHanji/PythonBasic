class person:
    name="harry"
    occupation="software engineer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")


b=person()
b.name="ritika"
b.occupation="hr"
a=person()
a.name="shubham"
print(a.name)
print(a.occupation)
a.occupation="soldier"
print(a.occupation)
a.info()
b.info()