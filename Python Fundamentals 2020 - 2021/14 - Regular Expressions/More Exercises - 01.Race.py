participants_list = input().split(", ")
racers_dict = {}

while True:
    command = input()
    if command == "end of race":
        break

    racer = [r for r in command if r.isalpha()]
    racer = ''.join(racer)
    digits = [int(d) for d in command if d.isdigit()]
    digits = sum(digits)

    if racer in participants_list:
        if racer not in racers_dict:
            racers_dict[racer] = digits
        else:
            racers_dict[racer] += digits

sorted_racers_dict = dict(sorted(racers_dict.items(), key=lambda x: x[1], reverse=True))

counter = 0

for k, v in sorted_racers_dict.items():
    counter += 1
    if counter == 4:
        break
    if counter == 1:
        print(f"1st place: {k}")
    elif counter == 2:
        print(f"2nd place: {k}")
    elif counter == 3:
        print(f"3rd place: {k}")