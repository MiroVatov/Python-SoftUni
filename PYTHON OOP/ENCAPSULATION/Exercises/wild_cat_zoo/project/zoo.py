
class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
        self.prices = []
        self.animals_dict = {}
        self.workers_dict = {}

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.prices.append(price)
            self.__budget -= price
            if type(animal).__name__ not in self.animals_dict:
                self.animals_dict[type(animal).__name__] = []
            self.animals_dict[type(animal).__name__].append(animal)

            return f"{animal.name} the {type(animal).__name__} added to the zoo"

            # TODO check if the animal class should be added with its methods(name, gender, age)
        elif self.__budget < price and len(self.animals) < self.__animal_capacity:
            return f"Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            if type(worker).__name__ not in self.workers_dict:
                self.workers_dict[type(worker).__name__] = []
            self.workers_dict[type(worker).__name__].append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.workers_dict[type(worker).__name__].remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries_sum = 0
        for worker in self.workers:
            total_salaries_sum += worker.salary
        if self.__budget >= total_salaries_sum:
            self.__budget -= total_salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        # TODO check how to get the money for every animal (list with prices)
        total_money_needed_to_tend_the_animals = 0
        for animal in self.animals:
            total_money_needed_to_tend_the_animals += animal.get_needs()
        if self.__budget >= total_money_needed_to_tend_the_animals:
            self.__budget -= total_money_needed_to_tend_the_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        data = f"You have {len(self.animals)} animals" + '\n'

        # Djambazov's Way

        # amount_of_lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        # amount_of_cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        # amount_of_tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]

        # data += f"----- {len(amount_of_lions)} Lions:" + '\n'
        # for lion in amount_of_lions:
        #     data += f"{lion.__repr__()}" + '\n'
        # data += f"----- {len(amount_of_tigers)} Tigers:" + '\n'
        # for tiger in amount_of_tigers:
        #     data += f"{tiger.__repr__()}" + '\n'
        # data += f"----- {len(amount_of_cheetahs)} Cheetahs:" + '\n'
        # for cheetah in amount_of_cheetahs:
        #     data += f"{cheetah.__repr__()}" + '\n'

        for animal_class, animal_data in self.animals_dict.items():
            data += f"----- {len(animal_data)} {animal_class}s:" + '\n'

            for an_data in animal_data:
                data += f"{an_data.__repr__()}" + '\n'
        return data.rstrip()

    def workers_status(self):

        data = f"You have {len(self.workers)} workers" + '\n'
        amount_of_keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        amount_of_caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        amount_of_vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        data += f"----- {len(amount_of_keepers)} Keepers:" + '\n'
        for keeper in amount_of_keepers:
            data += f"{keeper.__repr__()}" + '\n'
        data += f"----- {len(amount_of_caretakers)} Caretakers:" + '\n'
        for caretaker in amount_of_caretakers:
            data += f"{caretaker.__repr__()}" + '\n'
        data += f"----- {len(amount_of_vets)} Vets:" + '\n'
        for vet in amount_of_vets:
            data += f"{vet.__repr__()}" + '\n'

        return data.rstrip()

        # data = f"You have {len(self.workers)} workers" + '\n'
        # sorted_workers_dict = dict(sorted(self.workers_dict.items(), key=lambda x: x[0]))
        # for worker_class, worker_data in sorted_workers_dict.items():
        #     data += f"----- {len(worker_data)} {worker_class}s:" + '\n'
        #
        #     for w_data in worker_data:
        #         data += f"{w_data.__repr__()}" + '\n'
        # return data.rstrip()
