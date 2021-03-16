from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = deque(map(int, input().split(', ')))

total_time = 0

while True:

    if not customers:
        print(f'All customers were driven to their destinations')
        print(f'Total time: {total_time} minutes')
        break

    if not taxis and customers:
        print(f'Not all customers were driven to their destinations')
        print(f"Customers left: {', '.join(map(str, customers))}")
        break

    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer

    else:
        customers.appendleft(current_customer)

