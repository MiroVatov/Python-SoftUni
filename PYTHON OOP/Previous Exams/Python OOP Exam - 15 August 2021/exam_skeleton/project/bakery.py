from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []  # will contain every type of food in the bakery's menu
        self.drinks_menu = []  # will contain every type of drink in the bakery's menu
        self.tables_repository = []  # containing every table at the bakery
        self.total_income = 0  # the total income from all the completed bills

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def is_food_already_in_the_menu(self, food_name):
        for food in self.food_menu:
            if food_name == food.name:
                return food
        return None

    def is_drink_already_in_the_menu(self, drink_name):
        for drink in self.drinks_menu:
            if drink_name == drink.name:
                return drink
        return None

    def is_table_in_the_repository(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def add_food(self, food_type: str, name: str, price: float):
        food_found = self.is_food_already_in_the_menu(name)

        if food_found is not None:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = ""
        if food_type == "Bread":
            food = Bread(name, price)

        elif food_type == "Cake":
            food = Cake(name, price)
        self.food_menu.append(food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        drink_found = self.is_drink_already_in_the_menu(name)

        if drink_found is not None:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = ""
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)

        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        self.drinks_menu.append(drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table_found = self.is_table_in_the_repository(table_number)

        if table_found is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = ""
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)

        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        self.tables_repository.append(table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and number_of_people <= table.capacity:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        food_ordered = []
        food_not_in_menu = []
        table_found = self.is_table_in_the_repository(table_number)

        if table_found is None:
            return f"Could not find table {table_number}"

        for food_name in food_names:
            food_found = self.is_food_already_in_the_menu(food_name)
            if food_found is not None:
                table_found.order_food(food_found)
                food_ordered.append(food_found)
                self.total_income += food_found.price
            else:
                food_not_in_menu.append(food_name)

        data = ''
        if food_ordered:
            data += f"Table {table_number} ordered:" + '\n'
            for food in food_ordered:
                data += food.repr() + '\n'

        if food_not_in_menu:
            data += f"{self.name} does not have in the menu:" + '\n'
            for name in food_not_in_menu:
                data += name + '\n'
        return data.rstrip()

    def order_drink(self, table_number: int, *drinks_names):
        drinks_ordered = []
        drinks_not_in_menu = []
        table_found = self.is_table_in_the_repository(table_number)

        if table_found is None:
            return f"Could not find table {table_number}"

        for drink_name in drinks_names:
            drink_found = self.is_drink_already_in_the_menu(drink_name)
            if drink_found is not None:
                table_found.order_drink(drink_found)
                drinks_ordered.append(drink_found)
                self.total_income += drink_found.price
            else:
                drinks_not_in_menu.append(drink_name)

        data = ''
        if drinks_ordered:
            data += f"Table {table_number} ordered:" + '\n'
            for drink in drinks_ordered:
                data += drink.repr() + '\n'

        if drinks_not_in_menu:
            data += f"{self.name} does not have in the menu:" + '\n'
            for name in drinks_not_in_menu:
                data += name + '\n'
        return data.rstrip()

    def leave_table(self, table_number: int):
        table_found = self.is_table_in_the_repository(table_number)
        data = ""
        if table_found is not None:
            data += f"Table: {table_number}" + '\n'
            data += f"Bill: {table_found.get_bill():.2f}"

        table_found.clear()
        return data

    def get_free_tables_info(self):
        if self.tables_repository:
            for table in self.tables_repository:
                if not table.is_reserved:
                    table.free_table_info() + '\n'

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
