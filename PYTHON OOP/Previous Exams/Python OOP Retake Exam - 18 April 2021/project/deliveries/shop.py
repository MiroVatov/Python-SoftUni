from project.deliveries.drink import Drink
from project.deliveries.food import Food
from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository


class Shop:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def deliver(self, product_type: str, name: str):
        if product_type in ["Drink", "Food"]:
            if product_type == "Drink":
                product = Drink(name)
                product_exists = [prod for prod in self.product_repository.products if prod.name == name]
                if product_exists:
                    raise ValueError(f"Product {product.name} already exists.")
                self.product_repository.products.append(product)
                return f"Product {name} successfully added to inventory."
            elif product_type == "Food":
                product = Food(name)
                product_exists = [prod for prod in self.product_repository.products if prod.name == name]
                if product_exists:
                    raise ValueError(f"Product {product.name} already exists.")
                self.product_repository.products.append(product)
                return f"Product {name} successfully added to inventory."
        # product_exists = [prod for prod in self.product_repository.products if prod.name == name]

    def sell(self, customer_name: str, **shopping_list):  #  shopping_list contains product name (str) as key argument and quantity (int) as value argument
        customer_exists = [cust for cust in self.customer_repository.customers if customer_name == cust.name]
        if not customer_exists:
            customer = Customer(customer_name)
            self.customer_repository.customers.append(customer)
            products_bought = {}
            shop_list = shopping_list
            for product_name, qty in shop_list.items():
                product_exist = [prod for prod in self.product_repository.products if product_name == prod.name]
                if product_exist:
                    product = product_exist[0]
                    if product.quantity < qty:
                        customer.products[product_name] = qty - product.quantity
                        self.product_repository.products.remove(product)
                        products_bought[product_name] = product.quantity
                    else:
                        products_bought[product_name] = product.quantity - qty
                        customer.products[product_name] = product.quantity - qty
                        self.product_repository.decrease(product, qty)

            data = ""
            for prod_name, quantity in products_bought.items():
                data += f"Left quantity of {prod_name}: {quantity}" + '\n'
            return data

