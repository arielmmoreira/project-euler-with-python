"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(inside 13.txt)
"""
with open("13.txt", "r") as file:
    numbers = file.read().splitlines()

numbers = [int(number) for number in numbers]
sum_numbers = sum(numbers)
first_ten_digits = str(sum_numbers)[:10]
print(first_ten_digits)