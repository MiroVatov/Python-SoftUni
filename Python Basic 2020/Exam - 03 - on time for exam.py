exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = (exam_hour * 60) + exam_minutes
arrival_time = (arrival_hour * 60) + arrival_minutes

if arrival_time > exam_time:
    diff = arrival_time - exam_time
    print('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    elif diff >= 60:
        h = diff // 60
        m = diff % 60
        if m < 10:
            print(f'{h}:0{m} hours after the start')
        else:
            print(f'{h}:{m} hours after the start')

elif arrival_time < exam_time:
    diff = exam_time - arrival_time
    if diff > 30:
        print('Early')
        if diff < 60:
            print(f'{diff} minutes before the start')
        elif diff >= 60:
            h = diff // 60
            m = diff % 60
            if m < 10:
                print(f'{h}:0{m} hours before the start')
            else:
                print(f'{h}:{m} hours before the start')
diff = exam_time - arrival_time
if diff == 0 or diff <= 30:
    if diff == 0:
        print('On time')
    else:
        print(f'On time')
        print(f'{diff} minutes before the start')


