"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def n_by_n_spiral(n):
    starting_max_number = n * n
    current_max_number = starting_max_number
    current_n = n
    result = starting_max_number

    while current_max_number > 1:
        for _ in range(4):
            current_max_number -= current_n - 1
            result += current_max_number

        current_n -= 2

    return result


print('Answer: ', n_by_n_spiral(1001))
