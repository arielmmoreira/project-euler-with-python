"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97 and 7.
Similarly, we can work from right to left: 3797, 379, 37 and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5 and 7 are not considered to be truncatable primes.
"""

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_truncatable(n):

    digits = 0
    # from right to left
    number = n

    while number != 0:
        number = number // 10
        if not is_prime(number):
            return False

        digits += 1

    # from left to right
    number = n
    while number != 0:
        number = number % pow(10, digits - 1)
        digits -= 1
        if not is_prime(number):
            return False

    return True


limit = 11
truncatable = 0
total = 0
i = 10
while True:

    if is_prime(i):
        if is_truncatable(i):
            total += i
            truncatable += 1

    i += 1

    if truncatable == limit:
        break

print('Answer:', total)
