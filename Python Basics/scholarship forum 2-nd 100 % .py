import math

salary = float(input())
averageGrade = float(input())
minSalary = float(input())

socialScholarship = 0.35 * minSalary
scholarship = averageGrade * 25

if averageGrade <= 4.5:
    print('You cannot get a scholarship!')
elif averageGrade > 4.5 and averageGrade < 5.5:
    if salary > minSalary:
        print('You cannot get a scholarship!')
    elif salary <= minSalary:
        print(f'You get a Social scholarship {math.floor(socialScholarship)} BGN')
elif averageGrade >= 5.5:
    if salary > minSalary:
        print(f'You get a scholarship for excellent results {math.floor(scholarship)} BGN')
    elif salary <= minSalary:
        if socialScholarship > scholarship:
            print(f'You get a Social scholarship {math.floor(socialScholarship)} BGN')
        elif socialScholarship <= scholarship:
            print(f'You get a scholarship for excellent results {math.floor(scholarship)} BGN')