from collections import deque


def best_list_pureness(*args):
    nums_list = deque(args[0])
    k = args[1]
    max_pureness = -1_000_000
    rotations = 0

    for rotation in range(k + 1):
        best_pureness = 0
        for ind, val in enumerate(nums_list):
            best_pureness += (ind * val)
        if best_pureness > max_pureness:
            max_pureness = best_pureness
            rotations = rotation
        last_element = nums_list.pop()
        nums_list.appendleft(last_element)
    return f"Best pureness {max_pureness} after {rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)





