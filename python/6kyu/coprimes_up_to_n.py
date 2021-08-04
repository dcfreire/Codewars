import math

def coprimes(n):
    coprimes = []
    for i in range(n):
        if math.gcd(n, i) == 1:
            coprimes.append(i)
    return coprimes