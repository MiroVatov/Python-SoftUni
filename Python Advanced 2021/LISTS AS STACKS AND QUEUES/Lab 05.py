from collections import deque


def solve(people, toss_count):
    people = deque(people)
    index = 0

    while len(people) > 1:
        index += 1
        person = people.popleft()
        if toss_count == index:
            print(f"Removed {person}")
            index = 0
        else:
            people.append(person)

    print(f"Last is {''.join(people)}")


solve(input().split(" "), int(input()))
