class Appliance:

    cost: float

    def __init__(self, cost: float):
        self.cost = cost  # cost per day

    def get_monthly_expense(self):
        return self.cost * 30


