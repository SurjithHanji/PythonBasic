class Person:
    name="surjith"
    occupation="cloud engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
a.info()
print(a.name)