target = int(input())
starting_height = target - 30

total_jumps = 0
fail_jumps = 0
failed = False

while not failed:
    attempt = int(input())
    total_jumps += 1

    if attempt <= starting_height:
        fail_jumps += 1
        if fail_jumps == 3:
            failed = True
    else:
        if starting_height >= target:
            break
        fail_jumps = 0
        starting_height += 5

if failed:
    print(f'Tihomir failed at {starting_height}cm after {total_jumps} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {starting_height}cm after {total_jumps} jumps.')