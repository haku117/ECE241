class Vehicle:

    def __init__(self, name, color):
        self.__name = name  # __name is private to Vehicle class
        self.__color = color

    def getColor(self):  # getColor() function is accessible to class Car
        return self.__color

    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color

    def getName(self):  # getName() is accessible outside the class
        return self.__name

    def __str__(self):
        return self.getName() + " in " + self.getColor() + " color"

class Sedan(Vehicle):

    def __init__(self, name, color, model):
        # call parent constructor to set name and color
        super().__init__(name, color)
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

    def __str__(self):
        return "Sedan:" + self.getName() + self.__model + " in " + self.getColor() + " color"

class SUV(Vehicle):
    def __init__(self, name, color, model=None):
        # call parent constructor to set name and color
        super().__init__(name, color)
        self.__model = model

    def setModel(self, model):
            self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

    def __str__(self):
        return "SUV: " + self.getName() + self.__model + " in " + self.getColor() + " color"


# in method getDescrition we are able to call getName(), getColor() because they are
# accessible to child class through inheritance

sedan = Sedan("BMW 533", "red", "xi")
suv = SUV("Toyota", "green", "Highlander")
suv2 = SUV("Toyota", "green")
suv2.setModel("4Runner")

print(sedan.getDescription())
print(sedan.getName())  # car has no method getName() but it is accessible through class Vehicle
print(sedan)

print(suv.getDescription())
print(suv.getName())  # car has no method getName() but it is accessible through class Vehicle
print(suv)

print(suv2)
