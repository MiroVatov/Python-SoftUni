pool_volume = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
absent_hours = float(input())

first_pipe_debit = absent_hours * first_pipe_debit
second_pipe_debit = absent_hours * second_pipe_debit
total_pool_debit = first_pipe_debit + second_pipe_debit
total_pool_debit_perc = (total_pool_debit / pool_volume) * 100
total_pool_debit_left = abs(pool_volume - total_pool_debit)
first_pipe_debit = (first_pipe_debit / total_pool_debit) * 100
second_pipe_debit = (second_pipe_debit / total_pool_debit) * 100


if total_pool_debit <= pool_volume:
    print(f'The pool is {total_pool_debit_perc:.2f}% full. Pipe 1: {first_pipe_debit:.2f}%. Pipe 2: {second_pipe_debit:.2f}%.')
elif total_pool_debit > pool_volume:
    print(f'For {absent_hours:.2f} hours the pool overflows with {total_pool_debit_left:.2f} liters.')