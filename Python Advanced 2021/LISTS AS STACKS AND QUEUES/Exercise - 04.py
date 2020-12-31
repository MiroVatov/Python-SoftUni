rack = [int(i) for i in input().split()]
capacity = int(input())
current_rack = []

count_racks = 0
while rack:
    clothes_box = rack[-1]
    if sum(current_rack) + clothes_box < capacity:
        current_rack.append(clothes_box)
        rack.pop()
        if len(rack) == 0:
            count_racks += 1
    elif sum(current_rack) + clothes_box == capacity and len(rack) > 0:
        current_rack = []
        rack.pop()
        count_racks += 1
    elif sum(current_rack) + clothes_box > capacity:
        current_rack = []
        count_racks += 1

print(count_racks)