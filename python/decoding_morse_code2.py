import re
from fractions import gcd
from functools import reduce


def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip("0")
    pvec = re.findall(r"0+|1+", bits)
    lenvec = []
    for i in pvec:
        lenvec.append(len(i))
    p = reduce(gcd, lenvec)

    return bits.replace('111'*p, '-').replace('0000000'*p, '|').replace('1'*p, '.').replace('0'*p, ' ')


def decodeMorse(morseCode):
    morseCode = re.split(r"\|", re.sub(r" (?=\S)", '', morseCode))
    ret = []
    for s in morseCode:
        chars = re.findall("[.-]+", s)
        for c in chars:
            ret.append(MORSE_CODE[c])
        ret.append(' ')

    return ''.join(ret).strip(' ')


print(decodeMorse(decodeBits("111")))
