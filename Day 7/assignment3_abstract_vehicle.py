from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
class car(vehicle):
    name = "Car"
    def start(self):
        print("The car has started ")
    def stop(self):
        print("The car has stopped")

class bike(vehicle):
    name = "Bike"
    def start(self):
        print("The bike has started ")
    def stop(self):
        print("The bike has stopped")


class bus(vehicle):
    name = "Bus"
    def start(self):
        print("The bus has started ")
    def stop(self):
        print("The bus has stopped")

class garage:
    li = []
    def add_vehicle(self,*args):
        for i in args:
            self.li.append(i)
        print("Vehicle list are as follows")
        for i in self.li:
            print( i.name)
        # pass
    def starter_stopper(self,obj):
        obj.start()
        obj.stop()



obj1=bus()
g=garage()
g.starter_stopper((obj1))

obj2=car()
# g1=garage()
g.starter_stopper((obj2))

obj3=bike()
# g2=garage()
g.starter_stopper((obj3))


g.add_vehicle(obj1,obj2,obj3)
# g.add_vehicle(obj2)
# g.add_vehicle(obj3)


