people_waiting = int(input())

current_state = [int(p) for p in input().split(" ")]
MAXIMUM_STATE = 4
max_size = len(current_state) * 4
sum_current_people = 0

for people in range(len(current_state)):
    current_people = 0
    if current_state[people] < MAXIMUM_STATE:
        available_places = MAXIMUM_STATE - current_state[people]
        if people_waiting >= available_places:
            current_people = available_places

        elif people_waiting < available_places:
            current_people = people_waiting

        current_state[people] += current_people
        people_waiting -= current_people
    else:
        continue

    sum_current_people = sum(current_state)

    if sum_current_people == max_size or people_waiting == 0:
        break

if people_waiting == 0 and sum_current_people < max_size:
    print(f"The lift has empty spots!")
    print(f"{' '.join(map(str, current_state))}")
elif people_waiting > 0 and sum_current_people == max_size:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(f"{' '.join(map(str, current_state))}")
else:
    print(f"{' '.join(map(str, current_state))}")