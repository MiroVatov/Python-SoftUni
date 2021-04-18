
class CustomerRepository:

    def __init__(self):
        self.customers = []

    def add(self, customer):
        customer_name = customer.name
        if customer in self.customers:
            raise ValueError(f"Customer {customer_name} already exists.")
        self.customers.append(customer)

    def remove(self, customer_name: str):
        customer_exists = [cust for cust in self.customers if cust.name == customer_name]
        if len(customer_exists) == 0:
            raise ValueError(f"Customer {customer_name} does not exist.")
        customer = customer_exists[0]
        self.customers.remove(customer)
        return f"Removed customer: {customer_name}"

    def find(self, customer_name: str):
        customer_found = [cust for cust in self.customers if cust.name == customer_name]
        if not customer_found:
            return "None"
        customer = customer_found[0]
        return customer
