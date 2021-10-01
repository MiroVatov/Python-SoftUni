from abc import ABC, abstractmethod


class Table(ABC):

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []  # containing every food order made from the table.
        self.drink_orders = []  # containing every drink order made from the table.
        self.number_of_people = 0  # the count of people who sit at the table. 0 by default.
        self.is_reserved = False  # Returns True if the table is reserved.

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        if number_of_people <= self.capacity:
            self.number_of_people += number_of_people
            self.is_reserved = True

    def order_food(self, baked_food):  # BakedFood -> object
        self.food_orders.append(baked_food)

    def order_drink(self, drink):  # Drink -> object
        self.drink_orders.append(drink)

    def get_bill(self):
        total_amount_ordered = 0
        if self.food_orders:
            for food in self.food_orders:
                total_amount_ordered += food.price

        if self.drink_orders:
            for drink in self.drink_orders:
                total_amount_ordered += drink.price
        return total_amount_ordered

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            data = f"Table: {self.table_number}"
            data += f"Type: {self.__class__.__name__}"  # TODO Check if this shows the type of the table -> Inside table or Outside table
            data += f"Capacity: {self.capacity}"
            return data

