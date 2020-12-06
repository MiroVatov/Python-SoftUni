first_player_eggs = int(input())
second_player_eggs = int(input())
winner = input()

while winner != 'End of battle':

    if winner == 'one':
        second_player_eggs -= 1
        if second_player_eggs == 0:
            print(f'Player two is out of eggs. Player one has {first_player_eggs} eggs left.')
            break
    elif winner == 'two':
        first_player_eggs -= 1
        if first_player_eggs == 0:
            print(f'Player one is out of eggs. Player two has {second_player_eggs} eggs left.')
            break
    winner = input()
if winner == 'End of battle':
    print(f'Player one has {first_player_eggs} eggs left.')
    print(f'Player two has {second_player_eggs} eggs left.')