from collections import deque


def solve():
    people = deque()

    while True:
        command = input()
        if command == "End":
            print(f"{len(people)} people remaining.")
            break
        elif command == "Paid":
            while len(people) > 0:
                print(people.popleft())

        else:
            people.append(command)


solve()