def validation(license_pl):
    if len(license_pl) == 8:
        first_two = license_pl[:2]
        last_two = license_pl[-2:]
        is_valid = True
        for f in first_two:
            if ord(f) not in range(65, 91):
                is_valid = False
                break
        for la in last_two:
            if ord(la) not in range(65, 91):
                is_valid = False
                break
        if is_valid:
            middle = license_pl[2:-2:]
            if middle.isdigit():
                return True
    return False


users_dict = {}

num_of_inputs = int(input())

for i in range(num_of_inputs):
    command = input().split()
    action = command[0]

    if action == 'register':
        username = command[1]
        license_plate_number = command[2]

        if username in users_dict:
            print(f'ERROR: already registered with plate number {users_dict[username]}')
        else:
            if validation(license_plate_number):
                if license_plate_number not in users_dict.values():
                    users_dict[username] = license_plate_number
                    print(f"{username} registered {license_plate_number} successfully")
                else:
                    print(f"ERROR: license plate {license_plate_number} is busy")
            else:
                print(f"ERROR: invalid license plate {license_plate_number}")
    elif action == 'unregister':
        username = command[1]
        if username not in users_dict:
            print(f'ERROR: user {username} not found')
        else:
            print(f'user {username} unregistered successfully')
            del users_dict[username]

for user, number in users_dict.items():
    print(f"{user} => {number}")


