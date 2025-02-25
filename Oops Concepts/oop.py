class person:

    def __init__(self,n,o):
        print("hey i am a person")
        self.name=n
        self.occ=o
    # name="harry"
    # occ="developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("harry","developer")
b=person("Divya","HR")
a.info()
b.info()
# print(a.name)
# print(a.occ)
# a.info()