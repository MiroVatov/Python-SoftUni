shops_to_visit = input().split()
number_of_visits = int(input())

for _ in range(number_of_visits):
    command = input().split()

    if command[0] == "Include":
        shop = command[1]
        shops_to_visit.append(shop)

    elif command[0] == "Visit":
        if command[1] == "first":
            power = int(command[2])
            if power <= len(shops_to_visit):
                del shops_to_visit[:power]
        elif command[1] == "last":
            power = int(command[2])
            if power <= len(shops_to_visit):
                del shops_to_visit[-power:]
    elif command[0] == "Prefer":
        ind_1 = int(command[1])
        ind_2 = int(command[2])
        if ind_1 in range(len(shops_to_visit)) and ind_2 in range(len(shops_to_visit)):
            shops_to_visit[ind_1], shops_to_visit[ind_2] = shops_to_visit[ind_2], shops_to_visit[ind_1]
    elif command[0] == "Place":
        shop = command[1]
        index = int(command[2])
        if index + 1 in range(len(shops_to_visit)):
            shops_to_visit.insert(index + 1, shop)

print(f"Shops left:")
print(f"{' '.join(shops_to_visit)}")