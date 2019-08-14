def next_bigger(n):
    digs = [int(d) for d in str(n)]
    digs.reverse()
    c = 0
    index_min = 0
    for i in range(len(digs)-1):
        if digs[i] > digs[i+1]:
            index_min = i
            while c <= i:
                if digs[index_min] > digs[c] and digs[c] > digs[i+1]:
                    index_min = c
                c += 1
            digs[index_min], digs[i+1] = digs[i+1], digs[index_min]
            digs[0:i+1] = sorted(digs[0:i+1], reverse=True)
            break;
    digs.reverse()
    digs = int(''.join([str(i) for i in digs]), 10)
    if digs == n:
        return -1
    return digs
