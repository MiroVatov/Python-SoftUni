time_for_scene = int(input())
scenes_number = int(input())
scene_time = int(input())

time_for_scene = time_for_scene * 0.85
time_for_shooting = scenes_number * scene_time

if time_for_scene >= time_for_shooting:
    diff = time_for_scene - time_for_shooting
    print(f'You managed to finish the movie on time! You have {round(diff)} minutes left!')
else:
    diff = time_for_shooting - time_for_scene
    print(f'Time is up! To complete the movie you need {round(diff)} minutes.')