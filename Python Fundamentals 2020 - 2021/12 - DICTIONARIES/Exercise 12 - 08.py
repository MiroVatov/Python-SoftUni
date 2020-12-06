token = input().split(" -> ")

employee_dict = {}

while token[0] != "End":

    company_name = token[0]
    emp_id = token[1]

    if company_name not in employee_dict:
        employee_dict[company_name] = [emp_id]
    else:
        if emp_id not in employee_dict[company_name]:
            employee_dict[company_name] += [emp_id]
        
    token = input().split(" -> ")
employees_sorted = sorted(employee_dict.items(), key=lambda x: x[0])

for k, v in employees_sorted:
    print(f"{k}")
    for c in v:
        print(f"-- {c}")