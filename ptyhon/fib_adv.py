import math




def rootaprox(val):
    if (val < 11):
        return val

    return 10**math.floor(math.log10(val)/2)


def karatsu_mult(x, y):
    if not x:
        return 0
    m = rootaprox(x)
    x_low = x % m
    x_high = math.floor(x/m)
    y_low = y % m
    y_high = math.floor(y/m)
    a = x_high * y_high
    b = (x_high + x_low)*(y_high + y_low)
    c = y_low * x_low
    return a*(m**2) + (b - a - c)*m +c

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
        cache[n] = fib(((n-1)/2)+1)**2 + fib((n-1)/2)**2
    else:
        cache[n] = fib(n/2)*(2*fib(((n)/2)+1) - fib(n/2))

    return cache[n]

fib(-5)
