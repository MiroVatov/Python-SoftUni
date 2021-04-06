class Child:

    cost: float

    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost  # the money that the kid requires for a day
        self.toys_cost = toys_cost
        self.cost = food_cost + sum(toys_cost)   # TODO check if the yys cost is for a day or for a month  # Sum the food_cost with the cost of each toy and set the cost attribute to the result

    def get_monthly_expense(self):
        return self.cost * 30