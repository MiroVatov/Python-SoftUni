games_sold = int(input())
heartstone_count = 0
fortnite_count = 0
overwatch_count = 0
others_count = 0
total_count = 0
for i in range(1, games_sold + 1):
    game_name = input()

    if game_name == 'Hearthstone':
        heartstone_count += 1
    elif game_name == 'Fornite':
        fortnite_count += 1
    elif game_name == 'Overwatch':
        overwatch_count += 1
    else:
        others_count += 1
    total_count += 1

print(f'Hearthstone - {(heartstone_count / games_sold) * 100:.2f}%')
print(f'Fornite - {(fortnite_count / games_sold) * 100:.2f}%')
print(f'Overwatch - {(overwatch_count / games_sold) * 100:.2f}%')
print(f'Others - {(others_count / games_sold) * 100:.2f}%')