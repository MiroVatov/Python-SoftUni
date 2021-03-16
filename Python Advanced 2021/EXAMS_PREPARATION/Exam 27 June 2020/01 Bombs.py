from collections import deque

DATURA_BOMBS = [40, 0]
CHERRY_BOMBS = [60, 0]
SMOKE_DECOY_BOMBS = [120, 0]

datura = False
cherry = False
smoke = False

bomb_effects = deque(map(int, input().split(', ')))
bomb_castings = deque(map(int, input().split(', ')))

while (len(bomb_effects) > 0 and len(bomb_castings) > 0) and (not datura or not cherry or not smoke):

    bomb_eff = bomb_effects.popleft()
    bomb_cast = bomb_castings.pop()
    current_bomb_effect = bomb_eff + bomb_cast
    if current_bomb_effect == DATURA_BOMBS[0]:
        DATURA_BOMBS[1] += 1
        if DATURA_BOMBS[1] >= 3:
            datura = True
    elif current_bomb_effect == CHERRY_BOMBS[0]:
        CHERRY_BOMBS[1] += 1
        if CHERRY_BOMBS[1] >= 3:
            cherry = True
    elif current_bomb_effect == SMOKE_DECOY_BOMBS[0]:
        SMOKE_DECOY_BOMBS[1] += 1
        if SMOKE_DECOY_BOMBS[1] >= 3:
            smoke = True
    else:
        bomb_cast -= 5
        bomb_castings.append(bomb_cast)
        bomb_effects.appendleft(bomb_eff)

if datura and cherry and smoke:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print(f"Bomb Effects: empty")

if bomb_castings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_castings))}")
else:
    print(f"Bomb Casings: empty")

bombs_dict = {'Datura Bombs': DATURA_BOMBS[1], 'Cherry Bombs': CHERRY_BOMBS[1],
              'Smoke Decoy Bombs': SMOKE_DECOY_BOMBS[1]}

for bomb, count in sorted(bombs_dict.items()):
    print(f"{bomb}: {count}")
