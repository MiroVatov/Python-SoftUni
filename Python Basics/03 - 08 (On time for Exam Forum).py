exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

if exam_hour == 0:
    exam_hour == 24
if arrival_minutes == 0:
    arrival_minutes == 24

exam_total_minutes = (exam_hour * 60) + exam_minutes
arrival_total_minutes = (arrival_hour * 60) + arrival_minutes

print(exam_total_minutes - 30)
print(arrival_total_minutes)
print(exam_total_minutes)

if exam_total_minutes - 30 <= arrival_total_minutes <= exam_total_minutes:
    print('On Time')
    if arrival_total_minutes != exam_total_minutes:
        diff = exam_total_minutes - arrival_total_minutes
        print(f'{diff} minutes before the start')
elif arrival_total_minutes > exam_total_minutes:
    late_time = arrival_total_minutes - exam_total_minutes
    print('Late')
    if late_time < 60:
        print(f'{late_time} minutes after the start')
    else:
        minutes = late_time % 60
        hours_in_minutes = late_time - minutes
        hours = hours_in_minutes // 60
        print(f'{hours}:{minutes:02d} hours after the start')
else:
    print('Early')
    early_minutes = exam_total_minutes - arrival_total_minutes
    if early_minutes < 60:
        print(f'{early_minutes} minutes before the start')
    else:
        minutes = early_minutes % 60
        hours_in_minutes = early_minutes - minutes
        hours = hours_in_minutes // 60
        print(f'{hours}: {minutes:02d} hours before the start')