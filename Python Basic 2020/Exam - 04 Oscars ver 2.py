actor_name = input()
points_from_academy = float(input())
gudges_number = int(input())
points_to_beat = 1250.5
total_points = 0
#total_points = total_points + points_from_academy

for i in range(1, gudges_number + 1):
    gudge_name  = input()
    gudge_points = float(input())

    current_points = (gudge_points * len(gudge_name)) / 2
    total_points += current_points
    total_points = current_points + points_from_academy
    if total_points >= points_to_beat:
        break

if total_points >= points_to_beat:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = points_to_beat - total_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')

print(total_points)