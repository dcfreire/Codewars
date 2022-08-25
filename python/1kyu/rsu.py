# Bad

import re
import numpy as np
cos = [1, 0, -1, 0]
sin = [0, 1, 0, -1]


class RSUProgram:
    source = ""

    def __init__(self, source):
        self.source = source
        self.functions = {}

    def get_tokens(self):
        # Remove comments, sub them with " " so that stray integers may be checked correctly
        self.source = re.sub(
            r"((\/\/.*\n?)|((\/\*)((\*\/){0}[^\6])*?(\*\/){1}))", " ", self.source)
        if re.search(r"[a-zA-Z)]\s\d", self.source):
            raise Exception('Invalid indentation/spacing')
        if re.search(r"[^FRL()Ppq0-9\s]", self.source):
            raise Exception('Operation not defined')
        if re.search(r"[^FRL)Pp\d]\d+", self.source):
            raise Exception('Invalid integer location')
        self.source = re.sub(r"\s", "", self.source)
        if re.search(r"(p|P)([^0-9]|$)", self.source):
            raise Exception('Function without an indentifier')
        if re.search(r"\D0\d+", self.source):
            raise Exception('Leading zeroes')
        if re.search(r"(p|P)[^\d]+", self.source):
            raise Exception('Function without an identifier')
        # If the tokens are valid, return all tokens
        return re.findall(r"([FRL)]\d*|\(|[pP]\d+|q)", self.source)

    def get_funs(self, tokens, scope="-1"):
        c = 0
        bracket = 0
        saux = ['-1']
        curp = '-1'
        while c < len(tokens):
            # if not re.search(r"p", ''.join(tokens[c:])):
            #    break
            if tokens[c] == '(':
                bracket += 1
            elif tokens[c][0] == ')':
                bracket -= 1
            elif tokens[c][0] == 'p':
                if bracket:
                    raise Exception()
                bn = 1
                bc = c
                c += 1
                while bn:
                    if tokens[c] == '(':
                        bracket += 1
                    elif tokens[c][0] == ')':
                        bracket -= 1
                    if c == len(tokens):
                        raise Exception('Expected function end')
                    if tokens[c][0] == 'p':
                        curp += '|' + tokens[c][1:]
                        saux.append(curp)
                        if len(saux) != len(set(saux)):
                            raise Exception()
                        if bracket:
                            raise Exception('Function nested in brackets')
                        bn += 1
                    elif tokens[c][0] == 'q':
                        curp = re.sub(r"\|[^|]*$", "", curp)
                        bn -= 1
                    c += 1

                if bracket:
                    raise Exception(
                        'Brackets not oppened/closed properly in function')
                if (scope, tokens[bc][1:]) in self.functions:
                    raise Exception('Function already defined in this scope')

                self.functions[(scope, tokens[bc][1:])] = tokens[bc+1:c-1]
                tokens[bc] = c
                c -= 1
            c += 1
        return tokens
    stacktrace = []

    def convert_to_raw(self, tokens, scope='-1', fn='-1'):
        ret = []
        if fn == '-1':
            self.get_funs(tokens)
        c = 0
        while c < len(tokens):
            if isinstance(tokens[c], int):
                c = tokens[c]
            elif re.match(r"[RLF]\d+", tokens[c]):
                num = int(tokens[c][1:])
                for _ in range(num):
                    ret.append(tokens[c][0])
                c += 1
            elif re.match(r"[RLF]", tokens[c]):
                ret.append(tokens[c])
                c += 1
            elif re.match(r"P\d+", tokens[c]):
                saux = scope + "|" + fn
                while saux != "-1" and (saux, tokens[c][1:]) not in self.functions.keys():
                    saux = re.sub(r"\|[^|]*$", "", saux)
                if (saux, tokens[c][1:]) not in self.functions.keys():
                    raise Exception('Function not defined ' + tokens[c])
                if fn != '-1':
                    self.stacktrace.append((saux, tokens[c][1:]))
                    if len(self.stacktrace) != len(set(self.stacktrace)):
                        raise Exception('Infinite loop detected in patterns')
                self.get_funs(
                    self.functions[(saux, tokens[c][1:])], saux + '|' + tokens[c][1:])
                self.expand_fun((saux, tokens[c][1:]))
                ret.extend(self.functions[(saux, tokens[c][1:])])
                c += 1
            elif tokens[c] == '(':
                bn = 1
                bc = c + 1
                inbr = []
                inbr.append(tokens[0])
                while bn:
                    if bc == len(tokens):
                        raise Exception('Bracket not opened/closed properly')
                    if tokens[bc] == '(':
                        bn += 1
                    if tokens[bc][0] == ')':
                        bn -= 1
                    inbr.append(tokens[bc])
                    bc += 1
                c = bc
                num = inbr[-1][1:]
                if num != '0':
                    ap = self.convert_to_raw(inbr[1:-1], scope, fn)
                if num:
                    for _ in range(int(num)):
                        ret.extend(ap)
                else:
                    ret.extend(ap)
            elif tokens[c][0] == ')':
                raise Exception('Unmatched bracket')
        self.stacktrace.clear()
        return ret

    def expand_fun(self, key):
        a = self.functions[key]
        self.functions[key] = self.convert_to_raw(
            a, key[0], key[1])

    def format_grid(self, grid):
        ret = np.full(grid.shape, ' ')
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j]:
                    ret[i][j] = '*'
        return ret

    def execute_raw(self, cmds):
        grid = np.zeros((1, 1))
        grid[0][0] = '1'
        cur_dir = 0
        cur_pos = [0, 0]
        for c in cmds:
            if c == 'F':
                cur_pos[0] += sin[cur_dir]
                cur_pos[1] += cos[cur_dir]
                if cur_pos[0] < 0:
                    grid = np.concatenate(
                        (np.zeros((1, grid.shape[1])), grid), axis=0)
                    cur_pos[0] = 0
                elif cur_pos[1] < 0:
                    grid = np.concatenate(
                        (np.zeros((grid.shape[0], 1)), grid), axis=1)
                    cur_pos[1] = 0
                if cur_pos[0] == grid.shape[0]:
                    grid = np.concatenate(
                        (grid, np.zeros((1, grid.shape[1]))), axis=0)
                elif cur_pos[1] == grid.shape[1]:
                    grid = np.concatenate(
                        (grid, np.zeros((grid.shape[0], 1))), axis=1)
                grid[cur_pos[0]][cur_pos[1]] = 1

            if c == 'R':
                cur_dir += 1
                if cur_dir == 4:
                    cur_dir = 0
            if c == 'L':
                cur_dir -= 1
                if cur_dir == -1:
                    cur_dir = 3
        grid = self.format_grid(grid)
        ret = []
        for i in range(grid.shape[0]):
            ret.append(''.join(grid[i]))

        return '\r\n'.join(ret)

    def execute(self):
        return self.execute_raw(self.convert_to_raw(self.get_tokens()))
