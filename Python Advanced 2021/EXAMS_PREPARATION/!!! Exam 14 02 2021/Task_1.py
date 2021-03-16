from collections import deque

firework_effects = deque(map(int, input().split(', ')))
explosive_power = list(map(int, input().split(', ')))

palm_firework = 0
willow_firework = 0
crosette_firework = 0

while firework_effects and explosive_power:

    if palm_firework >= 3 and willow_firework >= 3 and crosette_firework >= 3:
        break

    current_firework = firework_effects.popleft()
    current_power = explosive_power.pop()

    if current_firework <= 0:
        explosive_power.append(current_power)
        continue
    if current_power <= 0:
        firework_effects.appendleft(current_firework)
        continue
    if current_firework <= 0 and current_power <= 0:
        continue

    product = current_firework + current_power

    if product % 3 == 0 and not product % 5 == 0:
        palm_firework += 1
        continue
    if product % 5 == 0 and not product % 3 == 0:
        willow_firework += 1
        continue
    if product % 5 == 0 and product % 3 == 0:
        crosette_firework += 1
        continue
    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_power)

if palm_firework >= 3 and willow_firework >= 3 and crosette_firework >= 3:
    print(f"Congrats! You made the perfect firework show!")

else:
    print(f"Sorry. You can’t make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crosette_firework}")
