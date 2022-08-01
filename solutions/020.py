"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def main():
    fact_100 = str(factorial(100))
    sum = 0

    for digit in fact_100:
        sum += int(digit)

    print("Answer:", sum)


def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)

main()