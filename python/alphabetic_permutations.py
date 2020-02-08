
from collections import Counter
import math


def to_factoradic(num):
    q = num
    c = 1
    ret = []
    while q:
        q_new = q // c
        r = q % c
        q = q_new
        ret.append(r)
        c += 1
    return ret


def listPosition(word):
    frequencies = Counter(word)
    mult = 1
    for m in frequencies.values():
        mult *= math.factorial(m)
    word = list(word).sort()

    return 1
