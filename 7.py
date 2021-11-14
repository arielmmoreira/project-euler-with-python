"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def is_prime(number):
    if number % 2 == 0:
        return False

    for num in range(3, int(number ** 0.5) + 1):
        if number % num == 0:
            return False

    return True


def get_prime_by_position(target):
    number = 0
    position = 0

    while True:
        if is_prime(number):
            position += 1

        if position == target:
            break

        number += 1

    return number

print(get_prime_by_position(10001))
