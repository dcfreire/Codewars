
cache = {}


def fib(n):
    if n in cache.keys():
        return cache[n]

    if n == -2:
        return -1
    if n == 1 or n == 2 or n == -1:
        return 1
    if n == 0:
        return 0
    if n % 2:
        cache[n] = fib(((n - 1) / 2) + 1)**2 + fib((n - 1) / 2)**2
    else:
        cache[n] = fib(n / 2) * (2 * fib(((n) / 2) + 1) - fib(n / 2))

    return cache[n]
