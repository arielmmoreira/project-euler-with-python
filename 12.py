
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

def main():
    num_divisors = 500
    factors = {}
    i = 1

    while True:
        number = int((i * (i + 1)) / 2)
        
        if len(get_factors(number, factors)) >= num_divisors:
            print(number)
            break

        i += 1


def get_factors(number, factors):
    factors[number] = {1, number}

    for i in range(2, int(number ** 0.5) + 1):
        quocient = number // i
        is_factor = True if number % i == 0 else False

        if is_factor:
            if quocient in factors.keys():
                factors[number] = factors[number].union(factors[quocient])

            else:            
                factors[number].add(quocient)
                factors[number].add(i)

    return factors[number]
  
main()



