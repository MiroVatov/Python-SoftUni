initial_energy = 100
initial_coins = 100

working_days_event = input().split("|")
day_sucessfull = True

for e in working_days_event:
    if not day_sucessfull:
        break
    token = e.split("-")
    event = token[0]
    energy = int(token[1])

    

if day_sucessfull:

    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")