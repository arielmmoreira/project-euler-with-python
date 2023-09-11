"""
The decimal number 585 (1001001001 in binary) is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(number):
    return number == number[::-1]


summatory = 0
for number in range(1, pow(10, 6)):
    base_10 = [int(n) for n in str(number)]
    base_2 = [int(n) for n in str(bin(number))[2:]]
    if is_palindrome(base_10) and is_palindrome(base_2):
        summatory += number

print('Answer:', summatory)