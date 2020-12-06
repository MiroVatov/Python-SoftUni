import sys
player_name = input()
max_points = -sys.maxsize
winner = ''
while player_name != 'Stop':
    player_points = 0
    for i in player_name:
       number = int(input())
       i = ord(i)
       if i == number:
           player_points += 10
       else:
           player_points += 2
    if player_points >= max_points:
        max_points = player_points
        winner = player_name

    player_name = input()

print(f'The winner is {winner} with {max_points} points!')
