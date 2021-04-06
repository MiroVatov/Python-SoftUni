from project.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        # super().__init__(cost=1.2)
        super().__init__(1.2)
        self.cost = 1.2  # per day



