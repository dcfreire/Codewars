def solution(args):
    c = 0
    b = []
    aux = []
    while c < len(args) - 1:
        if args[c + 1] - 1 == args[c]:
            aux.append(args[c])
        else:
            aux.append(args[c])
            aux = [str(i) for i in aux]

            if len(aux) > 2:
                b.append(aux[0] + "-" + aux[-1])
            elif len(aux) == 2:
                b.extend(aux)
            else:
                b.append(str(args[c]))
            aux.clear()
        c += 1
    aux.append(args[c])
    aux = [str(i) for i in aux]
    if len(aux) > 2:
        b.append(aux[0] + "-" + aux[-1])
    elif len(aux) == 2:
        b.extend(aux)
    else:
        b.append(str(args[c]))
    return ','.join(b)
