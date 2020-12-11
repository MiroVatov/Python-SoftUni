imune_system_initial_health = int(input())
system_health = imune_system_initial_health
viruses_dict = {}
system_defeated = False

while True:
    virus_name = input()
    if virus_name == 'end':
        break

    virus_strength = sum([ord(i) for i in virus_name])// 3
    time_to_defeat = virus_strength * len(virus_name)
    if virus_name not in viruses_dict:
        viruses_dict[virus_name] = {'strength': virus_strength, 'time_to_defeat': time_to_defeat}
    else:
        time_to_defeat = time_to_defeat // 3
        viruses_dict[virus_name]['time_to_defeat'] = time_to_defeat
    if system_health > virus_strength:
        print(f'Virus {virus_name}: {virus_strength} => {time_to_defeat} seconds')
        minutes = time_to_defeat // 60
        seconds = time_to_defeat % 60
        system_health -= time_to_defeat
        if system_health < 0:
            print('Immune System Defeated.')
            system_defeated = True
            break
        print(f'{virus_name} defeated in {minutes}m {seconds}s.')
        print(f"Remaining health: {int(system_health)}")
        if system_health + (system_health * 0.20) > imune_system_initial_health:
            system_health = imune_system_initial_health
        else:
            system_health = int(system_health + (system_health * 0.2))
    else:
        print('Immune System Defeated.')
        system_defeated = True
        break
if not system_defeated:
    print(f'Final Health: {int(system_health)}')

