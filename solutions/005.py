"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def get_lcm_up_to(limit):
    """Least commom multiple"""
    
    num = limit
    increment = limit
    up_to = 2
    
    while True:
        found = True
        for i in range(1, up_to + 1):
            if num % i != 0:
                found = False

        if found:
            increment = num
            up_to += 1
            if up_to == limit:
                break
        else:
            num += increment

    return num

print(get_lcm_up_to(20))