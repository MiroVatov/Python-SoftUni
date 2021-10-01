from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name: str, price: float):
        super(Cake, self).__init__(name=name, portion=245, price=price)

