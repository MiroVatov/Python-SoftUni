numbers = input().split(" ")
jump = int(input())
iter = jump - 1
result = ""

while True:
    if len(numbers) == 0:
        break

    while iter >= len(numbers):
        iter = iter - len(numbers)

    result += f"{numbers[iter]},"
    numbers.pop(iter)

    iter += jump - 1

result = result[:-1]
print(f"[{result}]")
