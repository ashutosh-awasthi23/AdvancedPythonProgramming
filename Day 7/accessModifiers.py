class Car:
    #  Attributes of the class
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self._model = model
        self.__year = year

    def display_info(self):
        print(f"Car Information:\nYear of manufacturing: {self.__year}\nBrand: {self.brand}\nModel: {self._model}\n")

    def set_year(self, year):
        self.__year = year


if __name__ == '__main__':
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Honda", "Civic", 2022)

    car1.set_year(2024)
    # car1.__year = 2024
    car1.display_info()
    car2.display_info()
