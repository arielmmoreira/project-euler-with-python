"""
The number 197 is called a circular prime because all rotations of the digits: 197, 971 and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97;

How many circular primes are there below one million?
"""


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

count = 0
for i in range(2, pow(10, 6)):
    if is_prime(i):
        number = list(map(int, str(i)))
        all_primes = True
        for j in range(len(number) - 1):
            number.append(number.pop(0))
            if not is_prime(int(''.join(map(str, number)))):
                all_primes = False
                break

        if all_primes:
            count += 1

print('Answer:', count)