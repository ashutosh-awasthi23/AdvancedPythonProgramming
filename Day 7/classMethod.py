class Car:
    # Class Variable
    number_of_cars = 0

    def __init__(self, brand, model):
        # Instance variable
        self.brand = brand
        self.model = model

        Car.number_of_cars += 1

    @classmethod
    def get_number_of_cars(cls):
        return f"Total number of cars: {cls.number_of_cars}"

    def display_info(self):
        print(f"Car Information:\nMake: {self.brand}\nModel: {self.model}\n")


if __name__ == '__main__':
    car1 = Car("Toyota", "Corolla")
    car2 = Car("Honda", "Civic")

    car1.display_info()
    car2.display_info()

    print(Car.get_number_of_cars())
