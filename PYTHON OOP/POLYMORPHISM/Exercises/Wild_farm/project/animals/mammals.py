from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food_type):
        if food_type.__class__.__name__ not in ["Vegetable", "Fruit"]:
            return f"{self.__class__.__name__} does not eat {type(food_type).__name__}!"
        self.gain_weight(0.10, food_type)


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food_type):
        if food_type.__class__.__name__ not in ["Meat"]:
            return f"{self.__class__.__name__} does not eat {type(food_type).__name__}!"
        self.gain_weight(0.40, food_type)


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food_type):
        if food_type.__class__.__name__ not in ["Meat", "Vegetable"]:
            return f"{self.__class__.__name__} does not eat {type(food_type).__name__}!"
        self.gain_weight(0.30, food_type)


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food_type):
        if food_type.__class__.__name__ not in ["Meat"]:
            return f"{self.__class__.__name__} does not eat {type(food_type).__name__}!"

        self.gain_weight(1.00, food_type)

