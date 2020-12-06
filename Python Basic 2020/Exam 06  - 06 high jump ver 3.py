height_target = int(input())

letva_height = height_target - 30
jump_counter = 0
fail_counter = 0

while letva_height <= height_target:
    fail_counter = 0
    for i in range(1, 4):
        jump_height = int(input())
        jump_counter += 1
        if jump_height > letva_height:
            letva_height += 5
            break
        else:
            fail_counter += 1
    if fail_counter == 3:
        print(f'Tihomir failed at {letva_height}cm after {jump_counter} jumps.')
        break
if jump_height > height_target:
    print(f'Tihomir succeeded, he jumped over {height_target}cm after {jump_counter} jumps.')

