"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

rows = 20
columns = 20

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

lattice = int(fact(rows + columns) / (fact(rows) * fact(columns)))

print(lattice)
