from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
employees = list(map(int, input().split(', ')))

total_pizzas_made = 0

while pizza_orders and employees:

    ordered_pizzas = pizza_orders.popleft()
    if ordered_pizzas > 10 or ordered_pizzas <= 0:
        continue

    employee_capacity = employees.pop()

    if ordered_pizzas <= employee_capacity:
        total_pizzas_made += ordered_pizzas

    elif ordered_pizzas > employee_capacity:
        pizzas_left = ordered_pizzas - employee_capacity
        pizza_orders.appendleft(pizzas_left)
        total_pizzas_made += employee_capacity


if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas_made}')
    print(f"Employees: {', '.join(map(str, employees))}")

elif not employees and pizza_orders:
    print('Not all orders are completed.')
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")

