from MODULES.Labs.Lab04 import mathops

n = input()

res = mathops.exec(*mathops.math_ops(n))
print(f"{res:.2f}")