def find_nb(m):
    c = 0
    p = 1
    while c < m:
        c += p ** 3
        p += 1
    if c > m:
        return -1
    else:
        return p - 1
