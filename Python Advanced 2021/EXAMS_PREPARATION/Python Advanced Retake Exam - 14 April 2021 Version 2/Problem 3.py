from collections import deque


def stock_availability(*params):
    params = deque(params)
    inventory_list = params.popleft()
    action = params.popleft()

    if action == "delivery":
        inventory_list.extend(list(params))

    elif action == "sell":
        if len(params) == 0:
            del inventory_list[0]

        elif isinstance(params[0], int):
            number_of_elements_to_delete = params[0]
            del inventory_list[0:number_of_elements_to_delete]

        elif isinstance(params[0], str):
            if len(params) == 1 and params[0] in inventory_list:
                inventory_list = [value for value in inventory_list if value != params[0]]

            elif len(params) > 1:
                for item in params:
                    if item in inventory_list:
                        inventory_list = [val for val in inventory_list if item != val]

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana", "cabbage", "avocado", "choco", "avocado"], "sell", "caramel", "berry", "choco"))
print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["choco", "vanilla", "banana"], "sell", 2))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
