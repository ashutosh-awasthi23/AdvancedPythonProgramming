class Car:
    #  Attributes of the class
    wheels = 4
    make = ""
    model = ""
    year = ""

    def __init__(self, make, model, year):
        self.make = make
        self.year = year
        self.model = model

    def display_info(self):
        print(f"Car Information:\nYear of manufacturing: {self.year}\nMake: {self.make}\nModel: {self.model}\n")


if __name__ == '__main__':

    # car1 = Car()
    # car1.nodel = "Toyota"
    # car1.make = "Corolla"
    # car1.year = 2020
    #
    # car2 = Car()
    # car2.nodel = "Honda"
    # car2.make = "Civic"
    # car2.year = 2022

    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Honda", "Civic", 2022)

    car1.display_info()
    car2.display_info()
