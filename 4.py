"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True

    return False

def largest_palindrome():
    digits = 3
    limit = (10 ** digits) - 1
    products = set()

    for num1 in range(limit, 0, -1):
        for num2 in range(limit, 0, -1):
            product = num1 * num2
            if is_palindrome(product):
                products.add(product)

    return max(products)

print(largest_palindrome())