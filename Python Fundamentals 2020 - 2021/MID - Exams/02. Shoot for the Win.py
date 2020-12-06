shot_targets = list(map(int, input().split()))

targets_shotted = 0
target_index = 0

while True:

    target = input()
    power = 0
    if target == "End":
        break
    target = int(target)

    if 0 <= target < len(shot_targets):
        target_index = shot_targets[target]
        if target_index != -1:
            shot_targets[target] = -1
            power = target_index
            targets_shotted += 1
            for i in range(len(shot_targets)):
                if shot_targets[i] > power and shot_targets[i] != -1:
                    shot_targets[i] -= power
                elif shot_targets[i] <= power and shot_targets[i] != -1:
                    shot_targets[i] += power

if target == "End":
    print(f"Shot targets: {targets_shotted} -> {' '.join(map(str,shot_targets))}")
