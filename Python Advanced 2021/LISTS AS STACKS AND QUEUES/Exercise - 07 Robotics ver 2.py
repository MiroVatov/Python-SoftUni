from datetime import datetime, timedelta
from collections import deque

robots = input().split(';')  # ROB-15;SS2-10;NX8000-3

for i in range(len(robots)):
    robot = robots[i].split('-')  # ['ROB', '15']
    robots[i] = {
        'name': robot[0],
        'processing_time': int(robot[1]),
        'available_at': 0  # at the start all the robots are available -> time -> 0
    }

# 8:00:00 -> start time -> we can change the time format during the time calculation
start_time = datetime.strptime(input(), '%H:%M:%S')  # from string format this func method makes it to data format

items = deque()

next_item = input()

while next_item != "End":
    items.append(next_item)
    next_item = input()

current_time = 0

while items:
    current_time += 1

    next_item = items.popleft()

    for robot in robots:
        # check first available robot ?
        if robot['available_at'] <= current_time:  # check if the available time of robot is less then the current time -> means that the robots is available for work
            robot['available_at'] = current_time + int(robot['processing_time'])  # we update the the availabe time of the robot -> means that the robot is not free any more
            robot_name = robot['name']
            time_str = (start_time + timedelta(seconds=current_time)).strftime('%H:%M:%S')  #-> stringformat makes the data into string, so we can print it
            print(f"{robot_name} - {next_item} [{time_str}]")
            break
            # take available robot

        # print -> ROB - detail [08:00:01]

         # only when found available robot
    # this else is for the for cycle -> enter only if we went through all the conditions in the for cycle and we didn't reach the break condition.
    # !!! if we went through all the robots and didn't found available robot, we enter into the else condition. We put the product into the end of the products list and continue.
    else:
        items.append(next_item)