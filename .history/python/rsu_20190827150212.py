# %%
import re
import numpy as np


class RSUProgram:
    source = ""
    functions = {}

    def __init__(self, source):
        self.source = source

    def get_tokens(self):
        self.source = re.sub(
            r"((\/\/.*\n?)|((\/\*)((\*\/){0}[^\6])*?(\*\/){1}))", " ", self.source)
        if re.findall(r"[a-zA-Z)]\s\d", self.source):
            raise Exception('Invalid indentation/spacing')
        if re.findall(r"[^FRL()Ppq0-9\s]", self.source):
            raise Exception('Operation not defined')
        if re.findall(r"[^FRL)Pp\d]\d+", self.source):
            raise Exception('Invalid integer location')
        self.source = re.sub(r"\s", "", self.source)
        if re.findall(r"(p|P)([^0-9]|$)", self.source):
            raise Exception('Function without an indentifier')
        if re.findall(r"\D0\d+", self.source):
            raise Exception('Leading zeroes')

        if re.findall(r"(p|P)[^\d]+", self.source):
            raise Exception('Function without an identifier')
        return re.findall(r"([FRL)]\d*|\(|[pP]\d+|q)", self.source)

    def get_funs(self, tokens, scope="-1"):
        fun = re.findall(r"(^p\d+|.*q{1})", ''.join(tokens))
        if (scope, fun[0][1:]) in self.functions:
            raise Exception('Function already defined in this scope')
        self.functions[(scope, fun[0][1:])] = fun[1][:-1]
        # Inherits parents scope
        c = ''.join(fun[1:]).find("p")
        if c != -1:
            self.get_funs(re.findall(
                r"([FRL)]\d*|\(|[pP]\d+|q)", fun[1][c:]), scope + "|" + fun[0][1:-1])

    def convert_to_raw(self, tokens, scope='-1', fn='-1'):
        ret = []
        c = 0
        if scope == '-1' and fn == '-1':
            while c < len(tokens):
                if re.search(r"p\d+", tokens[c]):
                    bn = 1
                    bc = c
                    c += 1
                    while bn:
                        if c == len(tokens):
                            raise Exception('Expected function end')
                        if tokens[c][0] == 'p':
                            bn += 1
                        elif tokens[c][0] == 'q':
                            bn -= 1
                        c += 1
                    self.get_funs(tokens[bc:c])
                    del tokens[bc:c]
                    c = bc - 1
                c += 1
            self.expand_funs()

        c = 0
        while c < len(tokens):
            if re.match(r"[RLF]\d+", tokens[c]):
                num = int(re.findall(r"\d+", tokens[c])[0])
                ret.append(''.join([tokens[c][0] for i in range(num)]))
            elif re.match(r"[RLF]", tokens[c]):
                ret.append(tokens[c])
            elif re.match(r"P\d+", tokens[c]):
                saux = scope
                while saux != "-1" and (saux, tokens[c][1:]) not in self.functions.keys():
                    saux = re.sub(r"\|[^|]*$", "", saux)
                if (saux, tokens[c][1:]) not in self.functions.keys():
                    raise Exception('Function not defined P' + fn)
                ret.append(self.functions[(saux, tokens[c][1:])])
            elif re.match(r"\(", tokens[c]):
                bn = 1
                bc = c
                c += 1
                inbr = []
                inbr.append(tokens[c])
                while bn:
                    if tokens[c] == '(':
                        bn += 1
                    if tokens[c][0] == ')':
                        bn -= 1
                    inbr.append(tokens[c])
                    c += 1
                num = re.findall(r"\d+", inbr[-1])

                del tokens[bc:c]
                c = bc - 1
                if not num:
                    for _ in range(int(num[0])):
                        tokens[bc:bc] = inbr[1:-1]
                else:
                    tokens[bc:bc] = inbr[1:-1]
            c += 1
        return [item for sublist in ret for item in sublist]

    def expand_funs(self):
        for k in sorted(self.functions.keys(), key=lambda tup: len(tup[0]), reverse=True):
            self.functions[k] = re.sub(r"p\d+.+q{1}", '', self.functions[k])
            self.functions[k] = self.convert_to_raw(
                RSUProgram(self.functions[k]).get_tokens(), k[0], k[1])

    def format_grid(self, grid):
        ret = np.full(grid.shape, ' ')
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j]:
                    ret[i][j] = '*'
        return ret

    def remove_dead(self, mat):
        arr = np.sum(mat, axis=1).tolist()
        begin = 0
        while arr[begin] == 0 or arr[len(arr) - 1] == 0:
            if arr[begin] == 0:
                del arr[begin]
                mat = np.delete(mat, begin, 0)
            if arr[len(arr) - 1] == 0:
                del arr[len(arr) - 1]
                mat = np.delete(mat, mat.shape[0] - 1, 0)

        arr = np.sum(mat, axis=0).tolist()
        while arr[begin] == 0 or arr[len(arr) - 1] == 0:
            if not arr[begin]:
                del arr[begin]
                mat = np.delete(mat, begin, 1)
            if not arr[len(arr) - 1]:
                mat = np.delete(mat, mat.shape[1] - 1, 1)
                del arr[len(arr) - 1]
        return mat

    def ex_grid(self, grid):
        ret = np.zeros((len(grid) + 2, len(grid[0]) + 2))
        ret[1:grid.shape[0] + 1, 1:grid.shape[1] + 1] = grid
        return ret

    def execute_raw(self, cmds):
        grid = np.zeros((3, 3))
        grid[1][1] = '1'
        cur_dir = 0
        cur_pos = [1, 1]
        for c in cmds:
            if c == 'F':
                if cur_dir == 0:
                    grid[cur_pos[0]][cur_pos[1] + 1] = 1
                    cur_pos[1] += 1
                if cur_dir == 1:
                    grid[cur_pos[0] - 1][cur_pos[1]] = 1
                    cur_pos[0] -= 1
                if cur_dir == 2:
                    grid[cur_pos[0]][cur_pos[1] - 1] = 1
                    cur_pos[1] -= 1
                if cur_dir == 3:
                    grid[cur_pos[0] + 1][cur_pos[1]] = 1
                    cur_pos[0] += 1

            if c == 'R':
                cur_dir -= 1
                if cur_dir < 0:
                    cur_dir = 3
            if c == 'L':
                cur_dir += 1
                if cur_dir > 3:
                    cur_dir = 0
            if cur_pos[0] == grid.shape[0] - 1 or cur_pos[1] == grid.shape[1] - 1 or 0 in cur_pos:
                grid = self.ex_grid(grid)
                cur_pos[0] += 1
                cur_pos[1] += 1
        grid = self.remove_dead(grid)
        grid = self.format_grid(grid)
        ret = []
        first = True
        for i in range(grid.shape[0]):
            if not first:
                ret.append("\r\n")
            ret.append(''.join(grid[i]))
            first = False
        self.functions.clear()
        return ''.join(ret)

    def execute(self):
        return self.execute_raw(''.join(self.convert_to_raw(self.get_tokens())))


a = RSUProgram(
    """P0P1P2P3P4p0FFLFFR((FFFR)2(FFFFFL)3)4qp1FRqp2FP1qp3FP2qp4FP3q""")
a = a.convert_to_raw(a.get_tokens())
a
