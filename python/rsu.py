# %%
import re
import numpy as np


class RSUProgram:
    source = ""

    def __init__(self, source):
        self.source = source
        self.functions = {}



    def get_tokens(self):
        # Remove comments, sub them with " " so that stray integers may be checked correctly
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
        # If the tokens are valid, return all tokens
        return re.findall(r"([FRL)]\d*|\(|[pP]\d+|q)", self.source)

    def get_funs(self, tokens, scope="-1"):
        fn = re.findall(r"\d+", ''.join(tokens))[0]
        if (scope, fn) in self.functions:
            raise Exception('Function already defined in this scope')
        self.functions[(scope, fn)] = re.sub(r"p\d+[^q]+q", "",''.join(tokens[1:-1]))
        # Get the first function from the tokens provided
        fun = re.findall(r"(p\d+[^q]+q)", ''.join(tokens[1:]))
        for f in fun:
            # Inherits parents scope
            c = ''.join(f).find("p")
            if c != -1:
                self.get_funs(re.findall(
                    r"([FRL)]\d*|\(|[pP]\d+|q)", 
                    f), scope + "|" + fn)

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
        stacktrace = []
        c = 0
        while tokens:
            if re.match(r"[RLF]\d+", tokens[0]):
                num = int(re.findall(r"\d+", tokens[0])[0])
                ret.append(''.join([tokens[0][0] for i in range(num)]))
                del tokens[0]
            elif re.match(r"[RLF]", tokens[0]):
                ret.append(tokens[0])
                del tokens[0]
            elif re.match(r"P\d+", tokens[0]):
                saux = scope + "|" + fn
                while saux != "-1" and (saux, tokens[0][1:]) not in self.functions.keys():
                    saux = re.sub(r"\|[^|]*$", "", saux)
                if (saux, tokens[0][1:]) not in self.functions.keys():
                    raise Exception('Function not defined P' + fn)
                stacktrace.append((saux, tokens[0][1:]))
                if len(set(stacktrace)) != len(stacktrace) and fn != '-1':
                    raise Exception('Infinite loop detected in patterns')
                self.expand_fun((saux, tokens[0][1:]))
                tokens.extend(re.findall(r"([FRL)]\d*|\(|[pP]\d+|q)", ''.join(self.functions[(saux, tokens[0][1:])])))
                del tokens[0]
            elif re.match(r"\(", tokens[0]):
                bn = 1
                bc = 1
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
                num = re.findall(r"\d+", inbr[-1])

                del tokens[0:bc]
                if num:
                    for _ in range(int(num[0])):
                        tokens[0:0] = inbr[1:-1]
                else:
                    tokens[0:0] = inbr[1:-1]
            elif tokens[0][0] == ')':
                raise Exception('Unmatched bracket')
        return [item for sublist in ret for item in sublist]

    def expand_fun(self, key):
        self.functions[key] = re.sub(r"p\d+.+q{1}", '', ''.join(self.functions[key]))
        a = RSUProgram(str(''.join(self.functions[key])))
        self.functions[key] = self.convert_to_raw(
            a.get_tokens(), key[0], key[1])

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


a = RSUProgram("""
p1
  p2
    // empty!
  q
q
p3
  (
    P2
  )2
q

P3 // should still throw an error
""")
a.convert_to_raw(a.get_tokens())
# %%
