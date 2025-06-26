class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stopping(self):
        print("Vehicle is stopping")


class Car(Vehicle):
    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        number_of_doors: int,
        number_of_wheels: int,
    ):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


class Bike(Vehicle):
    def __init__(self, brand: str, model: str, year: int, number_of_wheels: int):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels


car = Car("Toyota", "Fortuner", 2020, 5, 4)
bike = Bike("Honda", "Scooty", 2000, 2)

print(car.__dict__)
print(bike.__dict__)

car.start()
bike.start()
