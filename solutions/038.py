"""
Take the number 192 and multiply it by each of 1, 2 and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4 and 5, giving the pandigital 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).

What is the largest 1 to 0 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?
"""


def is_pandigit(n):
    numbers = list()
    while n != 0:
        digit = n % 10
        if digit in numbers:
            return False

        numbers.append(digit)
        n = n // 10

    for i in range(1, 10):
        if i not in numbers:
            return False

    return True

largest = 0
limit = 999999999
number = 1
multiplier = 1
concatenated_product = ''
while True:
    product = number * multiplier
    if product > limit:
        break

    concatenated_product += str(product)
    if len(concatenated_product) > 9:
        number += 1
        multiplier = 1
        concatenated_product = ''
        continue

    if is_pandigit(int(concatenated_product)) and multiplier > 1:
        largest = max(largest, int(concatenated_product))

    multiplier += 1

print('Answer:', largest)

