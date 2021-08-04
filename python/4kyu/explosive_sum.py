mem = {}


def exp_sum(n):
    s = 0
    aux = 1
    k = 1

    if n == 0:
        return 1

    if n < 0:
        return 0

    if mem.get(n) != None:
        return mem[n]

    while aux:
        aux = exp_sum(n - (k * (3 * k - 1) / 2))
        s += (-1) ** (k + 1) * aux

        if k > 0:
            k = k * (-1)
        else:
            k = (k * (-1)) + 1

    mem[n] = s
    return s
