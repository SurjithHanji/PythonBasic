# prefixing by __ indicates that it is private and 
# we cannot access directly it outside of the class

class Enp:
    def __init__(self):
        self.__name="harry"

a=Enp()
print(a._Enp__name)

#protected accessed by only class and its subclass


