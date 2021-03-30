from project.animals.animal import Bird


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food_type):
        if food_type.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {type(food_type).__name__}!"
        self.weight += (0.25 * food_type.quantity)
        self.food_eaten += food_type.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food_type):
        if food_type.__class__.__name__ not in ["Meat", "Vegetable", "Fruit", "Seed"]:
            return f"{self.__class__.__name__} does not eat {type(food_type).__name__}!"
        self.weight += (0.35 * food_type.quantity)
        self.food_eaten += food_type.quantity


