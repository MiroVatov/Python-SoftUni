base_camp = 5364
summit = 8848

days_count = 1
night_yes_no = input()

success = False

while night_yes_no!= 'END':
    meters = int(input())

    if night_yes_no == 'Yes':
        days_count += 1
    elif night_yes_no == 'No':
        days_count = days_count
    base_camp += meters
    if base_camp >= summit or days_count >= 5:

        break

    night_yes_no = input()

if base_camp >= summit:
    print(f'Goal reached for {days_count} days!')
else:
    print(f'Failed!')
    print(f'{base_camp}')
