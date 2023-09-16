"""
The fraction 49/98  is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

product = 1
denominator_of_product = 1
numerator_of_product = 1

for i in range(10, 99):
    for j in range(i + 1, 100):
        first_fraction = i / j
        numerator = str(i)
        denominator = str(j)

        simplified_numerator = ''
        simplified_denominator = ''

        if i % 10 == 0 and j % 10 == 0:
            continue

        if numerator[0] in denominator:
            simplified_numerator = numerator[1]
            simplified_denominator = denominator[(denominator.index(numerator[0]) + 1) % 2]

        if numerator[1] in denominator:
            simplified_numerator = numerator[0]
            simplified_denominator = denominator[(denominator.index(numerator[1]) + 1) % 2]

        if simplified_denominator != '' and simplified_denominator != '' and simplified_denominator != '0':
            second_fraction = int(simplified_numerator) / int(simplified_denominator)

            if first_fraction == second_fraction:
                product *= int(simplified_numerator) / int(simplified_denominator)
                denominator_of_product *= int(simplified_denominator)
                numerator_of_product *= int(simplified_numerator)


divider = 2
while True:
    if divider > numerator_of_product or divider > denominator_of_product:
        break

    if numerator_of_product % divider == 0 and denominator_of_product % 2 == 0:
        numerator_of_product /= divider
        denominator_of_product /= divider
        continue

    divider += 1

print('Answer:', int(denominator_of_product))
