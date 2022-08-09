"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def main():
    limit = 28123
    abundant_numbers = [number for number in range(12, limit + 1) if not is_prime(number) and is_abundant(number)]

    sum_of_two_abundant_numbers = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sum_of_two_abundant_numbers.add(abundant_numbers[i] + abundant_numbers[j])

    numbers = sum((number for number in range(limit + 1) if number not in sum_of_two_abundant_numbers))

    print("Answer:", numbers)

    
def is_abundant(number):
    if sum(get_proper_divisors(number)) > number:
        return True

    return False


def get_proper_divisors(number):
    return [n for n in range(1, int(number // 2) + 1) if number % n == 0]


def is_prime(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False

    return True

main()
