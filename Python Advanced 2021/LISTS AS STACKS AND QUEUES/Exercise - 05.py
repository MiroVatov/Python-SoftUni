from collections import deque

n = int(input())

pumps_circle = deque()

for _ in range(n):
    pump = [int(x) for x in input().split()]
    pumps_circle.append(pump)

for i in range(n):
    # зануляваме горивото и булевата применлива в началото на всеки цикъл
    success = True
    tank_fuel = 0

    for nums in range(n):
        current_pump = pumps_circle.popleft()
        tank_fuel += (current_pump[0] - current_pump[1])
        if tank_fuel < 0:
            success = False
        # въртим фор цикъла независимо, че имаме неуспешна маневра между помпите и апендваме двойката елементи най-отзад, защото накрая преди проверката ->
        # , дали е success или НЕ, помпите трябва да са в първоначалната си последователност.
        pumps_circle.append(current_pump)
        # Успешен цикъл има толкова поворения, без да стане False,  колкото са елементите в дека
    if success:
        print(i)
        break
    else:
        # Преместваме първата помпа най-отзад, за да започне ->
        # -> вторият цикъл от втората помпа от първоначалният списък с помпи.
        pumps_circle.append(pumps_circle.popleft())




