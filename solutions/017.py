"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

digit = {'0':'', '1': 'one', '2': 'two', '3':'three', '4':'four', '5':'five', 
        '6':'six', '7':'seven', '8':'eight', '9':'nine'}

decimal = {'0':'', '10': 'ten', '11': 'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', 
            '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}

tens = {'0':'', '2': 'twenty', '3':'thirty', '4':'forty', '5':'fifty', 
        '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

def main():
    limit = 1001
    sum = 0
    for number in range(1, limit):
        sum += len(parse_number(number))

    print(sum)


def parse_number(number):
    length = len(str(number))
    
    if length == 1:
        return digit[str(number)]

    elif length == 2:
        return parse_ten(number)

    elif length == 3:
        return parse_hundred(number)

    return "onethousand"


def parse_hundred(number):
    number = str(number)

    first_digit = digit[number[0]] + "hundred"
    remaining_digits = parse_ten(number[1:])
    
    if not remaining_digits:
        return first_digit
        
    return first_digit + "and" + remaining_digits

    
def parse_ten(number):
    number = str(number)

    first_digit = number[0]
    if first_digit == '1':
        return decimal[number]

    second_digit = number[1]
    ten = tens[first_digit]
    unit = digit[second_digit]

    return ten + unit


main()