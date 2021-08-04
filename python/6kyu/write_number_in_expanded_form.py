def expanded_form(num):
    li = []
    pow = 1
    last = num % 10
    num = int(num / 10)
    while num:
        if (num % 10) * int(10)**int(pow):
            li.insert(0, (num % 10) * int(10)**int(pow))
        pow += 1
        num = int(num / 10)
    if not last:
        last = li.pop(len(li) - 1)
    ret = ''.join(str(e) + ' + ' for e in li) + str(last)
    return ret
