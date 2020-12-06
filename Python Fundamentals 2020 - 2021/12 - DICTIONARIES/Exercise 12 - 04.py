
product_information = input().split(" ")

prices_dict = {}
quantity_dict = {}

while product_information[0] != "buy":
    pr_name = product_information[0]
    if pr_name not in quantity_dict:
        pr_quantity = int(product_information[2])
        quantity_dict[pr_name] = pr_quantity
    else:
        pr_quantity = int(product_information[2])
        quantity_dict[pr_name] += pr_quantity
    pr_price = float(product_information[1])
    prices_dict[pr_name] = pr_price

    product_information = input().split(" ")

# for k in quantity_dict.keys():
#     print(f"{k} -> {prices_dict[k] * quantity_dict[k]:.2f}")

for k, value in quantity_dict.items():
    print(f"{k} -> {prices_dict[k] * quantity_dict[k]:.2f}")