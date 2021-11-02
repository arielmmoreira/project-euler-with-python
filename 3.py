"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def is_prime(number):
    if number % 2 == 0:
        return False

    for num in range(3, int(number ** 0.5) + 1):
        if number % num == 0:
            return False

    return True

def largest_prime_factor(number):
    for num in range(int(number ** 0.5) + 1, 2, -1):
        if is_prime(num) and number % num == 0:
            return num

print(largest_prime_factor(600851475143))
