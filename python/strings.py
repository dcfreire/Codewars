from collections import defaultdict
from operator import itemgetter
import re


def mix(s1, s2):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    s1 = re.sub(r'[ -Z]', '', s1)
    s2 = re.sub(r'[ -Z]', '', s2)

    l = list()
    str = ""
    for i in s1:
        d1[i] += 1
    for i in s2:
        d2[i] += 1
    for i in d1:
        if(d1[i] > d2[i]):
            l.append([i, d1[i], "1:"])
        if(d1[i] == d2[i]):
            l.append([i, d1[i], "=:"])
    for i in d2:
        if(d2[i] > d1[i]):
            l.append([i, d2[i], "2:"])
    l = sorted(l, key=itemgetter(1))
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if l[i][1] == l[j][1]:
                if l[i][2] > l[j][2]:
                    aux = l[i]
                    l[i] = l[j]
                    l[j] = aux
                else:
                    if l[i][2] == l[j][2] and ord(l[i][0]) > ord(l[j][0]):
                        aux = l[i]
                        l[i] = l[j]
                        l[j] = aux

    for i in reversed(l):
        if i[1] > 1:
            str += i[2]
            str += i[0] * i[1]
            str += "/"
    str = str[0: len(str) - 1]
    return str
