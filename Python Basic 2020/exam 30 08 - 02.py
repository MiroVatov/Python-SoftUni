tickets_qty = int(input())
budget = int(input())
ticket_price = int(input())

total_bill = tickets_qty * ticket_price


if budget < total_bill:
    print(f'The budget of {budget}$ is not enough. Your client can\'t buy {tickets_qty} tickets with this budget!')
else:
    diff = (budget - total_bill)
    print(f'You can sell your client {tickets_qty} tickets for the price of {total_bill}$!')
    print(f'Your client should become a change of {diff}$!')