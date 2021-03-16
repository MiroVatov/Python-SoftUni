def stock_availability(*args):
    inventory_list = args[0]
    action = args[1]

    if action == 'delivery':
        boxes = list(args[2:])
        inventory_list.extend(boxes)

    elif action == 'sell':
        if len(args) > 2:
            parameter = list(args[2:])
            if str(parameter[0]).isdigit():
                number_or_string = int(args[2])
                inventory_list = inventory_list[number_or_string:]

            elif str(parameter[0].isalpha()):
                if len(parameter) == 1:
                    if parameter[0] in inventory_list:
                        inventory_list = [el for el in inventory_list if el != parameter[0]]
                elif len(parameter) > 1:
                    for el in parameter:
                        if el in inventory_list:
                            inventory_list = [par for par in inventory_list if par != el]

        else:
            inventory_list = inventory_list[1:]

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana", "banana", "cucumber", "avocado", "avocado", "Lichi"], "sell", "caramel", "banana", "avocado"))
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "cookie"))
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel"))