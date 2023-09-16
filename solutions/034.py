"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


sum_of_numbers = 0
for number in range(100000):
    sum_of_factorial = 0
    for digit in str(number):
        sum_of_factorial += factorial(int(digit))

    if sum_of_factorial == number and number > 2:
        sum_of_numbers += number

print('Answer:', sum_of_numbers)
