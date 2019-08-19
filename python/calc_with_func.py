import operator


def zero(args=[]):
    if len(args):
        return args[0](0, args[1])
    return 0


def one(args=[]):
    if len(args):
        return args[0](1, args[1])
    return 1


def two(args=[]):
    if len(args):
        return args[0](2, args[1])
    return 2


def three(args=[]):
    if len(args):
        return args[0](3, args[1])
    return 3


def four(args=[]):
    if len(args):
        return args[0](4, args[1])
    return 4


def five(args=[]):
    if len(args):
        return args[0](5, args[1])
    return 5


def six(args=[]):
    if len(args):
        return args[0](6, args[1])
    return 6


def seven(args=[]):
    if len(args):
        return args[0](7, args[1])
    return 7


def eight(args=[]):
    if len(args):
        return args[0](8, args[1])
    return 8


def nine(args=[]):
    if len(args):
        return args[0](9, args[1])
    return 9


def plus(num):
    return operator.add, num


def minus(num):
    return operator.add, operator.neg(num)


def times(num):
    return operator.mul, num


def divided_by(num):
    return operator.floordiv, num
