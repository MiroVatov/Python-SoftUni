from collections import deque

success = False

food_qty = int(input())

food_demand = [int(i) for i in input().split()]
food_demand = deque(food_demand)

max_order = max(food_demand)

for elem in range(len(food_demand)):
    order = food_demand[0]
    if order <= food_qty:
        food_demand.popleft()
        food_qty -= order
        if len(food_demand) == 0 and food_qty >= 0:
            success = True
            break

print(max_order)
if success:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, food_demand))}")