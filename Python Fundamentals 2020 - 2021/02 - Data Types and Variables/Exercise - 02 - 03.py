number_of_people = int(input())
capacity = int(input())
courses = 0
while number_of_people > 0:
    number_of_people -= capacity
    if abs(number_of_people) >= 0:
        courses += 1

print(courses)