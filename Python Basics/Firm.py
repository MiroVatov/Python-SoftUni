import math
hours_needed = int(input()) # hours needed for the firm to complete the project
days_in_hand = int(input()) # days the firm have to complete the project / 1 day = 8 hours
overtime_employees = int(input()) # number of employees, who are working overtime - 2 hours per day

hours_in_hand = (days_in_hand * 0.90) * 8 # total days in hand after - 10%  * 8 hours to convert to total hours available
overtime_employees = (overtime_employees * days_in_hand) * 2
total_hours = math.floor(hours_in_hand + overtime_employees)

hours_left = abs(hours_needed - total_hours)

if total_hours >= hours_needed:
    print(f'Yes!{hours_left} hours left.')
else:
    print(f'Not enough time!{hours_left} hours needed.')
