from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
employees = list(map(int, input().split(', ')))

total_pizzas_made = 0
employee_capacity = 0
all_orders_completed = True

while pizza_orders:
    order = pizza_orders.popleft()

    if order <= 0 or order > 10:
        continue

    if not employees:
        all_orders_completed = False
        break

    employee_capacity = employees.pop()

    if order <= employee_capacity:
        total_pizzas_made += order

    elif order > employee_capacity:
        total_pizzas_made += employee_capacity
        order -= employee_capacity
        pizza_orders.appendleft(order)
        if not employees:
            all_orders_completed = False
            break


if not all_orders_completed:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")

else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(map(str, employees))}")

