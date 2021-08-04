
def get_pins(observed):
    str = [[char] for char in observed]
    for c in str:
        if c[0] == '1':
            c.extend(['2', '4'])
        if c[0] == '2':
            c.extend(['1', '5', '3'])
        if c[0] == '3':
            c.extend(['2', '6'])
        if c[0] == '4':
            c.extend(['1', '5', '7'])
        if c[0] == '5':
            c.extend(['2', '4', '6', '8'])
        if c[0] == '6':
            c.extend(['3', '5', '9'])
        if c[0] == '7':
            c.extend(['4', '8'])
        if c[0] == '8':
            c.extend(['7', '5', '9', '0'])
        if c[0] == '9':
            c.extend(['8', '6'])
        if c[0] == '0':
            c.extend(['8'])
    perm = [len(str[i]) - 1 for i in range(len(str))]
    print(perm)
    ret = []
    comb = []
    print(str)
    while(sum(perm) > 0):
        for i in range(len(perm)):
            comb.append(str[i][perm[i]])
        ret.append(''.join(comb))
        comb.clear()
        set = True
        for i in range(len(perm) - 1, -1, -1):
            if set:
                perm[i] -= 1
                if perm[i] < 0:
                    perm[i] = len(str[i]) - 1
                    set = True
                else:
                    set = False
    for i in range(len(perm)):
        comb.append(str[i][perm[i]])
    ret.append(''.join(comb))
    return ret
