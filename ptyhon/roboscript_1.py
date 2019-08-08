


def switch(arg):
        switcher = {
            'F': "<span style=\"color: pink\">",
            'L': "<span style=\"color: red\">",
            'R': "<span style=\"color: green\">",
            '0': "<span style=\"color: orange\">",
            '1': "<span style=\"color: orange\">",
            '2': "<span style=\"color: orange\">",
            '3': "<span style=\"color: orange\">",
            '4': "<span style=\"color: orange\">",
            '5': "<span style=\"color: orange\">",
            '6': "<span style=\"color: orange\">",
            '7': "<span style=\"color: orange\">",
            '8': "<span style=\"color: orange\">",
            '9': "<span style=\"color: orange\">"
        }
        return switcher.get(arg, '')


def highlight(code):
    ret = []
    cur = ''
    c = 0
    for i in range(len(code)):
            if i < c:
                continue
            if code[c].isdecimal():
                aux = 'k'
                cur = aux
            else:
                aux = code[c]
                cur = aux
            ret.append(switch(code[c]))
            while aux == cur:
                ret.append(code[c])
                c += 1
                if c == len(code):
                    break;
                if code[c].isdecimal():
                    cur = 'k'
                else:
                    cur = code[c]
            if aux != '(' and aux != ')':
                ret.append("</span>")

    return ''.join(ret)
