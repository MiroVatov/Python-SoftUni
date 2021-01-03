from collections import deque


def solve():
    water_in_dispenser = int(input())
    people_waiting = deque()
    while True:
        people = input()
        if people == "Start":
            break
        people_waiting.append(people)

    while True:
        command = input()
        if command == "End":
            print(f"{water_in_dispenser} liters left")
            break
        if command.isdigit():
            liters = int(command)

            if liters <= water_in_dispenser:
                water_in_dispenser -= liters
                person = people_waiting.popleft()
                print(f"{person} got water")

            else:
                person = people_waiting.popleft()
                print(f"{person} must wait")
        else:
            command = command.split()
            liters = int(command[1])
            water_in_dispenser += liters


solve()
