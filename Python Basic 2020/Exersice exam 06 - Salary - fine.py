open_tabs = int(input())
salary = int(input())

fine = 0
total_fine = 0

for i in range(1, open_tabs + 1):
    website = input()
    if website == 'Facebook':
        fine = 150
        total_fine += fine
    elif website == 'Instagram':
        fine = 100
        total_fine += fine
    elif website == 'Reddit':
        fine = 50
        total_fine += fine


salary -= total_fine
if salary <= 0:
        print('You have lost your salary.')
else:
    print(f'{salary}')

