import numpy as np


def is_triangle(a, b, c):
    ar = [a, b, c]
    i = np.argmax(ar)
    k = ar[i]
    del ar[i]
    if ar[0] + ar[1] >= k:
        return True
    return False
