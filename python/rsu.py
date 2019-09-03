# %%
import re
import numpy as np
import math

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

        while c < len(tokens):
            if tokens[c] == '(':
                bracket += 1
            elif tokens[c][0] == ')':
                bracket -= 1
            if not re.search(r"p", ''.join(tokens)):
                break
            if tokens[c][0] == 'p':
                if bracket:
                    raise Exception('Function nested in brackets')
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
                        bn += 1
                    elif tokens[c][0] == 'q':
                        bn -= 1
                    c += 1
                if bracket:
                    raise Exception('Brackets not oppened/closed properly in function')
                if (scope, tokens[bc][1:]) in self.functions:
                    raise Exception('Function already defined in this scope')
                self.functions[(scope, tokens[bc][1:])] = tokens[bc+1:c-1]
                
                self.get_funs(tokens[bc+1:c-1], scope + "|" + tokens[bc][1:])
                del tokens[bc:c]
                c = bc - 1
            c += 1
    stacktrace = []

    def convert_to_raw(self, tokens, scope='-1', fn='-1'):
        ret = []
        self.get_funs(tokens)
        c = 0
        while c < len(tokens):
            if re.match(r"[RLF]\d+", tokens[c]):
                num = int(tokens[c][1:])
                ret.extend([tokens[c][0] for i in range(num)])
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
                self.stacktrace.append((saux, tokens[c][1:]))
                if len(set(self.stacktrace)) != len(self.stacktrace) and scope != '-1':
                    raise Exception('Infinite loop detected in patterns')
                self.expand_fun((saux, tokens[c][1:]))
                tokens[c:c+1] = self.functions[(saux, tokens[c][1:])]
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
                ap = self.convert_to_raw(inbr[1:-1])
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
        self.functions[key] = re.sub(r"p\d+.+q{1}", '', ''.join(self.functions[key]))
        a = RSUProgram(str(self.functions[key]))
        self.functions[key] = self.convert_to_raw(
            a.get_tokens(), key[0], key[1])

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
                cur_pos[0] += round(math.sin(cur_dir))
                cur_pos[1] += round(math.cos(cur_dir))
                if cur_pos[0] < 0:
                    grid = np.concatenate((np.zeros((1, grid.shape[1])), grid), axis=0)
                    cur_pos[0] = 0
                elif cur_pos[1] < 0:
                    grid = np.concatenate((np.zeros((grid.shape[0], 1)), grid), axis=1)
                    cur_pos[1] = 0
                if cur_pos[0] == grid.shape[0]:
                    grid = np.concatenate((grid, np.zeros((1, grid.shape[1]))), axis=0)
                elif cur_pos[1] == grid.shape[1]:
                    grid = np.concatenate((grid, np.zeros((grid.shape[0], 1))), axis=1)
                grid[cur_pos[0]][cur_pos[1]] = 1

            if c == 'R':
                cur_dir += math.pi/2
            if c == 'L':
                cur_dir -= math.pi/2
        grid = self.format_grid(grid)
        ret = []
        first = True
        for i in range(grid.shape[0]):
            if not first:
                ret.append("\r\n")
            ret.extend(grid[i])
            first = False
        self.functions.clear()
        return ''.join(ret)

    def execute(self):
        ret = self.execute_raw(self.convert_to_raw(self.get_tokens()))
        self.stacktrace.clear()
        self.functions.clear()
        return ret


RSUProgram("""
p0FFLFFR((FFFR)2(FFFFFL)3)4qp1FRqp2FP1qp3FP2qp4FP3qP0P1P2P3P4
FFLFFR((FFFR)2(FFFFFL)3)4""").execute()


# %%
