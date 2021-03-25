class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        data = ''
        subscription = [subscription for subscription in self.subscriptions if subscription.id == subscription_id]
        customer = [customer for customer in self.customers if customer.id == subscription_id]
        trainer = [trainer for trainer in self.trainers if trainer.id == subscription_id]
        plan = [plan for plan in self.plans if plan.id == trainer[0].id]
        equipment = [equipment for equipment in self.equipment if equipment.id == plan[0].id]

        data = f"{subscription[0].__repr__()}" + '\n' + f"{customer[0].__repr__()}" + '\n' + f"{trainer[0].__repr__()}" + '\n' + f"{equipment[0].__repr__()}" + '\n' + f"{plan[0].__repr__()}"
        return data

