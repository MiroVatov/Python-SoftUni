n = int(input())
registered = {}
# unregistered = []

for i in range(n):
    command = input().split(" ")

    if command[0] == "register":

        username = command[1]
        license_nr = command[2]
        if username not in registered:
            registered[username] = license_nr
            print(f"{username} registered {license_nr} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_nr}")

    elif command[0] == "unregister":
        username = command[1]

        if username not in registered:
            print(f"ERROR: user {username} not found")

        else:
            registered.pop(username)
           # unregistered.append(username)
            print(f"{username} unregistered successfully")
# for k in unregistered:
#     del registered[k]

for user, val in registered.items():
    print(f"{user} => {val}")