"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def main():
    limit = 10 ** 6
    starting_number = 0
    biggest_sequence = 0
    collatz_sequences = {}

    for i in range(1, limit):
        gen_collatz_sequence(i, collatz_sequences)
        current = len(collatz_sequences[i])
        

        if current > biggest_sequence:
            biggest_sequence = current
            starting_number = i
        

    print(starting_number)


def gen_collatz_sequence(n, collatz_sequences):
    quotient = n
    collatz_sequences[n] = [n]

    while quotient != 1:
        if quotient % 2 == 0:
            quotient = quotient // 2
        else:
            quotient = 3 * quotient + 1

        if quotient in collatz_sequences.keys():
            collatz_sequences[n].extend(collatz_sequences[quotient])
            return
                   
        collatz_sequences[n].append(quotient)


main()