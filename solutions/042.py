"""
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n + 1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Usgin source/042.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

def main():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    triangle_words = 0

    with open("../source/042.txt") as file:
        words = file.read().replace('"', '').split(',')

    for word in words:
        value = 0
        for letter in word:
            value += letters.index(letter) + 1

        if is_triangle_number(value):
            triangle_words += 1

    print('Answer:', triangle_words)


def generate_triangle_number(n):
    return int(1/2 * n * (n + 1))


def is_triangle_number(n):
    index = 1
    triangle_number = 0
    while triangle_number < n:
        triangle_number = generate_triangle_number(index)
        index += 1

    return triangle_number == n


main()
