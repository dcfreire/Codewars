# %%
import random

mem = {1: [91, 480150779]}
f_mem = {0: 0, 1: 1, 2: 1, 3: 2, 4: 4}


def powers(n):
    aux = n-1
    r = 0
    while True:
        if not aux % 2:
            r += 1
            aux /= 2
        else:
            break
    return (r, int(aux))


def is_prime(n):
    if n in [2, 3]:
        return True
    if not n % 2:
        return False
    r, d = powers(n)
    for _ in range(2):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        try:
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    raise "continue outer"
        except:
            continue
        return False
    return True


def f(n):
    global f_mem
    if n in f_mem.keys():
        return f_mem[n]
    f_mem[n] = f(n-1) + f(n-2) - f(n-3) + f(n-4) - f(n-5)
    return f_mem[n]


def k_thlastDigPrime(k):
    global mem
    if k in mem.keys():
        return [mem[k][0] + 1, mem[k][1]]
    last = sorted(mem.keys())[-1]
    last_term = mem[last][0]
    while last != k:
        last_term += 1
        last_dig = str(f(last_term))[-9:]
        if is_prime(int(last_dig)):
            mem[last + 1] = [last_term, int(last_dig)]
            last += 1
    return [mem[k][0] + 1, mem[k][1]]


# %%
