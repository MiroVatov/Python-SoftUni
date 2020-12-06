battles_won = 0
initial_energy = int(input())

while True:

    distance = input()

    if distance == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
        break
    energy = int(distance)
    if initial_energy < energy:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        break
    else:
        battles_won += 1
        initial_energy -= energy

    if battles_won % 3 == 0:
       initial_energy += battles_won


