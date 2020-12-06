import math
income = float(input())
average_grades = float(input())
min_salary = float(input())
social_scholarship = math.floor(0.35 * min_salary)
scholarship = math.floor(average_grades * 25)

if income < min_salary:
    if  4.5 >= average_grades > 5.50:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    elif average_grades < 4.5:
        print('You cannot get a scholarship!')

if income > min_salary:
    if average_grades <= 5.5:
        print('You cannot get a scholarship!')
    elif average_grades >= 5.5:
        print(f'You get a scholarship for excellent results {scholarship} BGN')

if income < min_salary:
    if average_grades >= 5.5:
        if social_scholarship > scholarship:
            print (f'You get a Social scholarship {social_scholarship} BGN')
        elif scholarship > social_scholarship:
            print(f'You get a scholarship for excellent results {scholarship} BGN')




