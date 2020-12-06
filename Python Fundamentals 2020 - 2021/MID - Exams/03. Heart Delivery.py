def is_jump_valid(jump, array):
    if 0 <= jump < len(array):
        return True


neighbourhood = list(map(int, input().split("@")))
index = 0

while True:

    command = input()
    if command == "Love!":
        break

    token = command.split()
    jump = int(token[1])
    jump_length = index + jump

    if not is_jump_valid(jump_length, neighbourhood):
        jump_length = 0
        if neighbourhood[jump_length] > 0:
            neighbourhood[jump_length] -= 2
            if neighbourhood[jump_length] == 0:
                print(f"Place {jump_length} has Valentine's day.")
        elif neighbourhood[jump_length] == 0:
            print(f"Place {jump_length} already had Valentine's day.")

    elif is_jump_valid(jump_length, neighbourhood):
        if neighbourhood[jump_length] == 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            neighbourhood[jump_length] -= 2
            if neighbourhood[jump_length] == 0:
                print(f"Place {jump_length} has Valentine's day.")
    index = jump_length

if command == "Love!":
    print(f"Cupid's last position was {index}.")
    successful = [i for i in neighbourhood if i != 0]

    if len(successful) == 0:
        print(f"Mission was successful.")
    else:
        print(f"Cupid has failed {len(successful)} places.")