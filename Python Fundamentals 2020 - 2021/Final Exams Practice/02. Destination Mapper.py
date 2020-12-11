import re

initial_text = input()

pattern = re.compile(r'((?<=[=])[A-Z][A-Za-z]{2,}(?=[=]))|((?<=[\\/])[A-Z][A-Za-z]{2,}(?=[\\/]))')

destinations = []
travel_points = 0

for m in re.finditer(pattern, initial_text):
    destinations.append(m.group())

for points in destinations:
    travel_points += len(points)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")