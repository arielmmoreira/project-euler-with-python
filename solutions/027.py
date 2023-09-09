"""
Euler discovered the remarkable quadratic formula:
    n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) = 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values 0 <= n <= 79.
The product of the coefficients, -79 and 1601, is -126479

Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| <= 1000,
    where |n| is the modulus/absolute value of n,
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0
"""

def is_prime(number):
    if number % 2 == 0:
        return False

    for num in range(3, int(number ** 0.5) + 1):
        if number % num == 0:
            return False

    return True


n = 0
results = []
for a in range(-999, 999):
    for b in range(-1000, 1000):
        primes = 0
        while True:
            quadratic = (n ** 2) + (a * n) + b
            if not is_prime(abs(quadratic)):
                results.append({'a': a, 'b': b, 'n': n, 'primes': primes})
                n = 0
                break

            primes += 1
            n += 1

primes = 0
value_for_a = 0
value_for_b = 0
for result in results:
    if result['primes'] > primes:
        primes = result['primes']
        value_for_a = result['a']
        value_for_b = result['b']

print(value_for_a * value_for_b)