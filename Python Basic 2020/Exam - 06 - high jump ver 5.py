wanted_height = int(input())
starting_attempt = wanted_height - 30
succeed = True
total_attempts = 0
while wanted_height >= starting_attempt and succeed:

    failed_attempt_number = 0
    for i in range(1, 3 + 1):

        attempt = int(input())
        if attempt > starting_attempt:
            total_attempts += 1
            starting_attempt += 5
            break
        else:
            failed_attempt_number += 1
            total_attempts += 1
            if failed_attempt_number == 3:
                succeed = False
                break

if not succeed:
    print(f'Tihomir failed at {starting_attempt}cm after {total_attempts} jumps.')
else:
    starting_attempt -= 5
    print(f'Tihomir succeeded, he jumped over {starting_attempt}cm after {total_attempts} jumps.')