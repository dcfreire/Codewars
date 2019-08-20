import re
upsidedown = {
    '0': '0',
    '1': '1',
    '2': 'a',
    '3': 'a',
    '4': 'a',
    '5': 'a',
    '6': '9',
    '7': 'a',
    '8': '8',
    '9': '6'
}


def upd(x, y):
    l = list(map(lambda x: ''.join(reversed([i for i in list(map(lambda k: upsidedown.get(k), x))])), [str(char) for char in range(x, y + 1)]))
    ret = []
    for a in range(x, y):
        if str(a) == l[a - x]:
            ret.append(l[a - x])
    return ret
filter(lambda a: not re.findall("a", a),)
list(upd(10, 100))
[char for char in str(range(1, 5 + 1))]

str(reversed('abc'))
