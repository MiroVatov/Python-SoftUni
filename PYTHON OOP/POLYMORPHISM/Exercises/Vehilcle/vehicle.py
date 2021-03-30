from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 0.9
        distance_to_travel = self.fuel_quantity / self.fuel_consumption

        if distance_to_travel >= distance:
            fuel_to_be_used = distance * self.fuel_consumption
            self.fuel_quantity -= fuel_to_be_used

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 1.6
        distance_to_travel = self.fuel_quantity / self.fuel_consumption

        if distance_to_travel >= distance:
            fuel_to_be_used = distance * self.fuel_consumption
            self.fuel_quantity -= fuel_to_be_used

    def refuel(self, fuel):
        fuel *= 0.95
        self.fuel_quantity += fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
