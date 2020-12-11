import re

initial_text = input()

pattern = r'(?P<separator>#|\|)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<exp_date>\d{2}\/\d{2}\/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)'

calories_per_day = 2000

match = re.finditer(pattern, initial_text)
food_info_list = []
total_calories = 0

for m in match:
    result = m.groupdict()
    food_info_list.append(result)

    total_calories += int(m.group('calories'))

days_to_last_in_space = total_calories // calories_per_day

print(f"You have food to last you for: {days_to_last_in_space} days!")

for item in food_info_list:
    print(f"Item: {item['item']}, Best before: {item['exp_date']}, Nutrition: {item['calories']}")



