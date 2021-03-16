from collections import deque

first_loot_box = deque(map(int, input().split()))
second_loot_box = list(map(int, input().split()))

claimed_items_sum = 0

while first_loot_box and second_loot_box:

    first_loot_item = first_loot_box.popleft()
    second_loot_item = second_loot_box.pop()

    if (first_loot_item + second_loot_item) % 2 == 0:
        claimed_items_sum += (first_loot_item + second_loot_item)

    else:
        first_loot_box.appendleft(first_loot_item)
        first_loot_box.append(second_loot_item)

if not first_loot_box:
    print(f"First lootbox is empty")

elif not second_loot_box:
    print(f"Second lootbox is empty")

if claimed_items_sum >= 100:
    print(f"Your loot was epic! Value: {claimed_items_sum}")

else:
    print(f"Your loot was poor... Value: {claimed_items_sum}")