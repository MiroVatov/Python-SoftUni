followers_dict = {}

while True:

    command = input().split(": ")

    if command[0] == "Log out":
        break
    username = command[1].strip()

    if command[0] == "New follower":
        if username not in followers_dict:
            followers_dict[username] = [0], [0]
        else:
            continue
    elif command[0] == "Like":
        likes_count = int(command[2])
        if username not in followers_dict:
            followers_dict[username] = [likes_count], [0]
        else:
            followers_dict[username][0][0] += likes_count

    elif command[0] == "Comment":

        if username not in followers_dict:
            followers_dict[username] = [0], [1]
        else:
            followers_dict[username][1][0] += 1

    elif command[0] == "Blocked":
        if username in followers_dict:
            del followers_dict[username]

        else:
            print(f"{username} doesn't exist.")

for k, v in followers_dict.items():
    followers_dict[k] = [inner for item in v for inner in item]

sorted_followers_dict = dict(sorted(followers_dict.items(), key=lambda x: (-x[1][0], x[0])))

print(f"{len(followers_dict)} followers")
for key, val in sorted_followers_dict.items():
    print(f"{key}: {sum(val)}")
