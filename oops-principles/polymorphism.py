class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, number_of_doors: int):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year)

    def start(self):
        print("Motorcycle is starting")

    def stop(self):
        print("Motorcycle is stopping")


class Plane(Vehicle):
    def __init__(self, brand: str, model: str, year: int, number_of_doors: int):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Plane is starting")

    def stop(self):
        print("Plane is stopping")


vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2022, 5),
    Motorcycle("Kawasaki", "Ninja", 2018),
    Motorcycle("Yamaha", "R15", 2003),
    Plane("Boeing", "747", 2015, 16),
]

# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()

#     elif isinstance(vehicle, Motorcycle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()

#     else:
#         raise Exception("Object is not a valid vehicle")

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
