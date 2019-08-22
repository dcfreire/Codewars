from math import log


def log_fac(m, n):
    sum = 0
    for i in range(m, n + 1):
        sum += log(i)
    return sum


def log_binomial(n, k):
    if k > (n - k):
        return (log_fac(n - k + 1, n) - log_fac(2, k))
    else:
        return (log_fac(k + 1, n) - log_fac(2, n - k))
def pow_binomial(n, k):
    def eratosthenes_simple_numbers(N):
        yield 2
        nonsimp = set()
        for i in range(3, N + 1, 2):
            if i not in nonsimp:
                nonsimp |= {j for j in range(i * i, N + 1, 2 * i)}
                yield i
    def calc_pow_in_factorial(a, p):
        res = 0
        while a:
            a //= p
            res += a
        return res
    ans = 1
    for p in eratosthenes_simple_numbers(n):
        ans *= p ** (calc_pow_in_factorial(n, p) - calc_pow_in_factorial(k, p) - calc_pow_in_factorial(n - k, p))
    return ans

def height(n, m):
    ret = 0
    for i in range(1, n + 1):
        ret += pow_binomial(m, i)
    return ret


height(9477, 100000)
