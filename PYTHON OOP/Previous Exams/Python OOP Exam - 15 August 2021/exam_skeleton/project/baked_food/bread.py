from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):

    def __init__(self, name: str, price: float):
        super(Bread, self).__init__(name=name, portion=200, price=price)


