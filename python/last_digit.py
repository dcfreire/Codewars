lpow = {
    0: [0],
    1: [1],
    2: [6, 2, 4, 8],
    3: [1, 3, 9, 7],
    4: [6, 4],
    5: [5],
    6: [6],
    7: [1, 7, 9, 3],
    8: [6, 8, 4, 2],
    9: [9, 1]
}


def last_digit(lst):

    if len(lst) == 0:
        return 1

    if len(lst) == 1:
        return lst[0]
    if all(0 == i for i in lst) and not len(lst) % 2:
        return 1
    if all(0 == i for i in lst):
        return 0
    while len(lst) > 3:
        if lst[-1] == 0:
            lst[-2] = 1
        del lst[-1]
    lst.append(1)
    exp = (lst[1] % 4) ** (lst[2] % 2)
    return (lst[0] ** exp)%10


last_digit([3, 4, 5])
