def bouncingBall(h, bounce, window):
    c = 1
    p = 1
    if h <= 0 or bounce < 0 or bounce >= 1 or window >= h:
        return -1
    while bounce ** p > window/h:
        p += 1
        c += 2
    return c
