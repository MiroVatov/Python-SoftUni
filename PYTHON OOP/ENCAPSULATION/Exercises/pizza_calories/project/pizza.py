
class Pizza:

    def __init__(self, name: str, dough, toppings_capacity: int):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}  # the topping type as a key and the topping's weight as a value
        self.__toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings(self):
        return self.__toppings

    @property
    def topping_capacity(self):
        return self.__toppings_capacity

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @dough.setter
    def dough(self, val):
        self.__dough = val

    @toppings.setter
    def toppings(self, val):
        self.__toppings = val

    @topping_capacity.setter
    def topping_capacity(self, value):
        self.__toppings_capacity = value

    def add_topping(self, topping):

        if len(self.__toppings) >= self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.__toppings[topping.topping_type] = topping.weight
        else:
            self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total_toppings_weight = sum(self.__toppings.values())
        res = self.__dough.weight
        return total_toppings_weight + res




