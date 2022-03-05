"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

primes = [2]

def is_prime(number):
    if number % 2 == 0:
        return False

    for num in range(3, int(number ** 0.5) + 1):
        if number % num == 0:
            return False

    return True


for i in range(3, 2000000):
    if is_prime(i):
        primes.append(i)


print(sum(primes))
