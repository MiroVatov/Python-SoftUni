budget = float(input())
actor_name = input()

while actor_name != 'ACTION':

    name_lenght = len(actor_name)

    if name_lenght > 15:
        actor_salary = budget * 0.20
    elif name_lenght <= 15:
        actor_salary = float(input())
        actor_salary = actor_salary
    budget -= actor_salary
    if budget <= 0:
        break
    actor_name = input()

if budget >= 0:
    print(f'We are left with {budget:.2f} leva.')
elif budget < 0:
    budget = abs(budget)
    print(f'We need {budget:.2f} leva for our actors.')