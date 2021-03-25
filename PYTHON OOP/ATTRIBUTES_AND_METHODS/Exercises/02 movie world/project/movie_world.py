

class MovieWorld:

    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []
        self.dvd_ids = {}
        self.customer_ids = {}

    @classmethod
    def dvd_capacity(cls):
        return cls._DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls._CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) >= self._CUSTOMER_CAPACITY and customer not in self.customers:  # TODO check if the customer condition is NOT correct !
            return
        self.customers.append(customer)
        self.customer_ids[customer.id] = customer

    def add_dvd(self, dvd):
        if len(self.dvds) >= self._DVD_CAPACITY:  # TODO check if the customer condition is NOT correct !
            return
        self.dvds.append(dvd)
        self.dvd_ids[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):

        customers_age = [cust.age for cust in self.customers if cust.id == customer_id]
        movie_allowed_age = [movie.age_restriction for movie in self.dvds if dvd_id == movie.id]
        dvd = self.dvd_ids.get(dvd_id)
        customer = self.customer_ids.get(customer_id)
        customer_name = [c.name for c in self.customers if c.id == customer_id]
        dvd_already_rented = [d.is_rented for d in self.dvds if d.id == dvd_id]

        if customer.has_dvd(dvd):
            return f"{customer.name} has already rented {dvd.name}"

        elif dvd_already_rented[0]:  # TODO check if the elif statement find the correct dvd ?!
            # if dvd.is_rented:

            return f"DVD is already rented"

        elif customers_age < movie_allowed_age:
            # customer.age < dvd.age_restriction:

            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        else:
            dvd_instance = [d for d in self.dvds if d.id == dvd_id]
            customer.rented_dvds.append(dvd_instance[0])
            dvd_name = [d.name for d in self.dvds if dvd_id == d.id]
            cust_name = [c.name for c in self.customers if c.id == customer_id]
            dvd.is_rented = True
            # customer.add_dvd(dvd)  # TODO check if dvd instance works, if not imply this method
            return f"{''.join(cust_name)} has successfully rented {''.join(dvd_name)}"

    def return_dvd(self, customer_id, dvd_id):

        customer = self.customer_ids.get(customer_id)
        dvd = self.dvd_ids.get(dvd_id)

        if not customer.has_dvd(dvd):
            return f"{customer.name} does not have that DVD"

        dvd_instance = [d for d in self.dvds if d.id == dvd_id]
        customer.rented_dvds.remove(dvd_instance[0])
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))
        return '\n'.join(customers + dvds)



