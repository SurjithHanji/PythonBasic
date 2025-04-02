from abc import ABC
class car(ABC):
    def show(self):
        print("every car has 4 wheels")
    #@abstractmethod
    def speed(self):
        pass

class maruthi(car):
    def speed(self):
        print("speed is 100km/hr")

class suzuki(car):
    def speed(self):
        print("speed is 200km/hr")

m1=maruthi()
m1.show()
m1.speed()

s1=suzuki()
s1.show()
s1.speed()