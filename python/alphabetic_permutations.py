
from collections import Counter
import math
from functools import reduce


def listPosition(word):

    n = 1
    srted = sorted(list(word))
    for i, char in enumerate(list(word)):

        while srted[i] != char:
            frequencies = Counter(srted[i + 1:])
            fac = math.factorial(
                reduce(lambda acc, x: acc + x, frequencies.values(), 0))
            div = reduce(lambda acc,
                         x: math.factorial(x) * acc, frequencies.values(), 1)
            try:
                elem = next((x for x in srted[i:] if srted[i] < x), None)
                index = srted[i:].index(elem) + i
                po = srted.pop(index)
                srted.insert(i, po)
            except ValueError:
                break
            n += fac // div
        srted[i+1:] = sorted(srted[i+1:])
    return n


print(listPosition("BOOKKEEPER"))
#frequencies[char] -= 1
# if frequencies[char] == 0:
#    del frequencies[char]
#bgr = list(filter(lambda x, ch=char: ch > x, frequencies.keys()))
# nchar = reduce(lambda acc, x: acc + x,
#               [frequencies[x] for x in bgr], 0)
# fac = math.factorial(
#    reduce(lambda acc, x: acc + x, frequencies.values(), 0))
# div = reduce(lambda acc, x: acc + x, frequencies.values(), 0) * reduce(lambda acc,
#                                                                       x: math.factorial(x) * acc, [frequencies[x] for x in bgr], 1)
#n += nchar * fac // div if bgr else 0
