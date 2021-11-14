"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a² + b² = c²
For example, 
    3² + 4² = 9 + 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def get_pythagorean(target):
    parts = target // 3

    for i in range(1, parts):
        for j in range(1, parts + 1):
            a = i
            b = a + j
            c = target - (b + a)
            if b >= c:
                break

            pythagorean = (a ** 2) + (b ** 2) == (c ** 2)
            if pythagorean and a + b + c == 1000:
                return a * b * c
                
print(get_pythagorean(1000))