command = input()

users = {}
result = {}
while command != "Lumpawaroo":
    if len(command.split(" | ")) == 2:
        value, key = command.split(" | ")

        if key not in users:
            users[key] = value

    elif len(command.split(" -> ")) == 2:
        key, value = command.split(" -> ")

        users[key] = value

        print(f"{key} joins the {value} side!")

    command = input()

for key, value in users.items():
    if value not in result:
        result[value] = []
        result[value].append(key)

    else:
        result[value].append(key)

result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in result.items():
    print(f"Side: {key}, Members: {len(value)}")
    [print(f"! {name}") for name in sorted(value)]