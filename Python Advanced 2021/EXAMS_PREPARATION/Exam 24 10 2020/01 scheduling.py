jobs = [int(i) for i in input().split(', ')]
searched_job_index = int(input())

searched_index_value = jobs[searched_job_index]
cycles_num = 0
current_job_index = jobs[0]

while True:

    current_job = min(jobs)
    current_job_index = jobs.index(current_job)

    if current_job == searched_index_value and current_job_index == searched_job_index:
        cycles_num += current_job
        break

    elif current_job == searched_index_value and current_job_index != searched_job_index:
        jobs[current_job_index] = 1_000_000
        cycles_num += current_job
    else:
        jobs[current_job_index] = 1_000_000
        cycles_num += current_job

print(cycles_num)





