

class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []
        self.customer_ids = {}
        self.dvd_ids = {}

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        customers_capacity = MovieWorld.customer_capacity
        if len(self.customers) < customers_capacity() and customer not in self.customers:
            self.customers.append(customer)
            self.customer_ids[customer.id] = customer

    def add_dvd(self, dvd):
        dvd_capacity = MovieWorld.dvd_capacity()
        if len(self.dvds) < dvd_capacity and dvd not in self.dvds:
            self.dvds.append(dvd)
            self.dvd_ids[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.dvd_ids[dvd_id]
        customer = self.customer_ids[customer_id]

        # TODO use the instances for the customer and the dvd in order to check for their properties, values and state

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        elif dvd.is_rented:
            return f"DVD is already rented"

        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = self.dvd_ids[dvd_id]
        customer = self.customer_ids[customer_id]

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers_data = ''
        count = 0
        for customer in self.customers:

            rented = ', '.join([dvd.name for dvd in customer.rented_dvds])
            if not rented:
                rented = ''
            customers_data += f"{customer.id}: {customer.name} of age {customer.age} has {len(customer.rented_dvds)} rented DVD's ({rented})" + '\n'

        dvd_data = ''
        for dvd in self.dvds:
            count += 1
            dvd_data += f"{dvd.id}: {dvd.name} ({dvd.creation_month} {dvd.creation_year}) has age restriction {dvd.age_restriction}. Status: {'rented' if dvd.is_rented else 'not rented'}" + '\n'

        return customers_data + dvd_data


