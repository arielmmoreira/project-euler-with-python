"""
If p s the perimeter of a right angle triangle with integral length sides, {a, b, c},  there are exactly three solutions for p = 120.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p <= 1000, is the number of solutions maximised?
"""

limit = 1000

def are_valid_sizes(a, b, c):
    if a == b or a == c or b == c:
        return False

    sides = {a, b, c}
    longest = max(a, b, c)
    sides.remove(longest)
    if longest ** 2 == sides.pop() ** 2 + sides.pop() ** 2:
        return True

    return False


max_solutions = 0
p_of_max_solutions = 0
results = dict()
for p in range(limit + 1):
    results = []
    for i in range(p):
        for j in range(i + 1, p // 2):
            k = p - (i + j)
            if are_valid_sizes(i, j, k):
                results.append([i, j, k])

    if len(results) > max_solutions:
        max_solutions = len(results)
        p_of_max_solutions = p


print('Answer:', p_of_max_solutions)
