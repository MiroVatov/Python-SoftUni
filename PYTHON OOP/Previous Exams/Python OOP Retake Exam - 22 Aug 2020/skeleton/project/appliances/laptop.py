from project.appliances.appliance import Appliance


class Laptop(Appliance):

    def __init__(self):
        super().__init__(1)
        self.cost = 1  # per day

