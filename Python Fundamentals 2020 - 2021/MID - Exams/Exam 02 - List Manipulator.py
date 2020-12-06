def blacklist(fr_list, fr_name, bl_listed):
    if fr_name in fr_list:
        idx = fr_list.index(fr_name)
        print(f"{fr_name} was blacklisted.")
        bl_listed.append(fr_name)
        fr_list[idx] = "Blacklisted"
        return fr_list, bl_listed
    else:
        print(f"{fr_name} was not found.")


def error(fr_list, idx, lost):
    if fr_list[idx] != "Blacklisted" and fr_list[idx] != "Lost":
        print(f"{fr_list[idx]} was lost due to an error.")
        lost.append(fr_list[idx])
        fr_list[idx] = "Lost"
        return fr_list, lost


def change(fr_list, idx, fr_name):
    if 0 <= idx < len(fr_list):
        print(f"{fr_list[idx]} changed his username to {fr_name}.")
        fr_list[idx] = fr_name
        return fr_list


friends_list = input().split(", ")
blacklisted = []
lost_names = []

while True:
    command = input()
    if command == "Report":
        break
    token = command.split()
    action = token[0]
    if action == "Blacklist":
        name = token[1]
        blacklist(friends_list, name, blacklisted)

    elif action == "Error":
        index = int(token[1])
        error(friends_list, index, lost_names)

    elif action == "Change":
        index = int(token[1])
        username = token[2]
        if 0 <= index <= len(friends_list):
            change(friends_list, index, username)

print(f"Blacklisted names: {len(blacklisted)}")
print(f"Lost names: {len(lost_names)}")
print(f"{' '.join(friends_list)}")
