def perf_num(num):
    divisor = 0
    for n in range(1, num):
        if num % n == 0:
            divisor += n

    if num == divisor and num > 0:
        return f"We have a perfect number!"

    else:
        return f"It's not so perfect."

num = int(input())

print(perf_num(num))