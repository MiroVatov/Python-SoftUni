from collections import deque


def get_primes(primes):
    primes = deque(primes)

    while primes:
        element = primes.popleft()
        delitel = 0
        if element > 1:
            for i in range(1, element + 1):
                if element % i == 0:
                    delitel += 1
            if delitel == 2:
                yield element


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([2, 4, 3, 5, 6, 7, 9, 1, 0])))