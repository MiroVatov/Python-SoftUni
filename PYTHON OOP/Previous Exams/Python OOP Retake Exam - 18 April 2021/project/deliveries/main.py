from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository
from project.deliveries.food import Food
from project.deliveries.drink import Drink
from project.shop import Shop

# prod_repository = ProductRepository()
# cust_rep = CustomerRepository()
# food = Food("Salam")
# drink = Drink("Bira")
# customer1 = Customer("Billa")
# customer2 = Customer("Lidl")
# print(prod_repository.add(food))
# # prod_repository.add(food)
# print(prod_repository.add(drink))
# print(prod_repository.decrease(food, 5))
# print(prod_repository.decrease(food, 4))
# print(prod_repository.find("Salam"))
# print(cust_rep.add(customer1))
# print(cust_rep.add(customer2))
# print(cust_rep.remove("Billa"))
shop = Shop()
print(shop.deliver("Drink", "Airan"))
print(shop.deliver("Drink", "Whiskey"))
print(shop.deliver("Food", "Burger"))
# print(shop.deliver("Drink", "Salmon"))
print(shop.sell("Aiko", **{"Airan": 5, "Burger": 2}))

print(shop.sell("Amo", **{"Airan": 12, "Burger": 23}))
print(shop.sell("Jumbo", **{"Airan": 6, "Burger": 13}))
