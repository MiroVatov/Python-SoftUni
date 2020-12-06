experience_needed = int(input())

battles_count = int(input())

gained_experience = 0
battle_count = 0
success = False

for battle in range(1, battles_count + 1):

    experience = int(input())

    if battle % 3 == 0:
        experience *= 1.15
    elif battle % 5 == 0:
        experience *= 0.90

    gained_experience += experience
    battle_count += 1

    if gained_experience >= experience_needed:
        success = True
        break

if success:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")

else:
    diff = experience_needed - gained_experience
    print(f"Player was not able to collect the needed experience, {diff:.2f} more needed.")