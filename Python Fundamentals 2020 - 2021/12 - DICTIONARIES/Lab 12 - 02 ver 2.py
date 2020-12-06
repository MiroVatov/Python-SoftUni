
data = input()
elements = data.split(" ")

products = {}

for index in range(0, len(elements), 2):
    products[elements[index]] = int(elements[index + 1])

search_products = input().split(" ")

for search_prod in search_products:
    quantity = products.get(search_prod)
    if quantity:
        print(f"We have {quantity} of {search_prod} left")

    else:
        print(f"Sorry, we don't have {search_prod}")