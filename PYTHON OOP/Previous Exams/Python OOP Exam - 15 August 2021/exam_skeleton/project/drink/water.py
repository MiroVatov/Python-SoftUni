from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: int, brand: str):
        super(Water, self).__init__(name=name, portion=portion, price=1.50, brand=brand)
