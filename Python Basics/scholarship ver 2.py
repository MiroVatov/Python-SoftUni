import math
income = float(input())
average_grades = float(input())
min_salary = float(input())
social_scholarship = math.floor(0.35 * min_salary)
scholarship = math.floor(average_grades * 25)

is_eligible_for_social_scholarship = 0
is_eligible_for_sucess_scholarship = 0

if income < min_salary:
    if average_grades < 4.50:
        is_eligible_for_social_scholarship = 'No'
    elif average_grades >= 4.50:
        is_eligible_for_social_scholarship = 'Yes'
    if average_grades >= 5.50:
        is_eligible_for_sucess_scholarship = 'Yes'

if income > min_salary:
    if average_grades >= 5.50:
        is_eligible_for_sucess_scholarship = 'Yes'
    elif average_grades >= 4.50:
        is_eligible_for_social_scholarship = 'No'

if is_eligible_for_social_scholarship == 'Yes':
        print(f'You get a Social scholarship {social_scholarship} BGN')
elif is_eligible_for_sucess_scholarship == 'Yes':
        print(f'You get a scholarship for excellent results {scholarship} BGN')
elif is_eligible_for_social_scholarship == 'No':
        print('You cannot get a scholarship!')
if is_eligible_for_sucess_scholarship == 'Yes' and is_eligible_for_social_scholarship == 'Yes' :
    if social_scholarship > scholarship:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    elif scholarship > social_scholarship:
        print(f'You get a scholarship for excellent results {scholarship} BGN')