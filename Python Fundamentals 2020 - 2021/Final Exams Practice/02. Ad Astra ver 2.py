import re

initial_text = input()

pattern = r'(?P<separator>#|\|)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<exp_date>\d{2}\/\d{2}\/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)'
calories_per_day = 2000

match = re.finditer(pattern, initial_text)
total_calories = 0

for m in match:
    total_calories += int(m.group('calories'))

days_to_last_in_space = total_calories // calories_per_day

print(f"You have food to last you for: {days_to_last_in_space} days!")

match = re.finditer(pattern, initial_text)

for mat in match:
    print(f"Item: {mat.group('item')}, Best before: {mat.group('exp_date')}, Nutrition: {mat.group('calories')}")