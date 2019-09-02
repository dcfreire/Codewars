# %%
import re
import numpy as np

class RSUProgram:
    source = ""
    functions = {}

    def __init__(self, source):
        self.source = source
        return

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
        fun = re.findall(r"(^p\d+|.*(?=q.+){1})", ''.join(tokens))
        if (scope, fun[0][1:]) in self.functions:
            raise Exception('Function already defined in this scope')
        self.functions[(scope, fun[0][1:])] = ''.join(fun[1])
        # Inherits parents scope
        c = ''.join(fun[1:]).find("p")
        if c != -1:
            self.get_funs(re.findall(
                r"([FRL)]\d*|\(|[pP]\d+|q)", fun[1][c:]), scope + "|" + fun[0][1:])

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
                while scope != "-1" and (scope, tokens[c][1:]) not in self.functions.keys():
                    scope = (re.sub(r"\|[^|]*$", "", scope)[0], tokens[c][1:])
                if (scope, tokens[c][1:]) not in self.functions.keys():
                    raise Exception('Function not defined P' + fn)
                ret.append(self.functions[(scope, tokens[c][1:])])
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
                if len(num) > 0:
                    for _ in range(int(num[0])):
                        tokens[bc:bc] = inbr[1:-1]
                else:
                    tokens[bc:bc] = inbr[1:-1]
            c += 1
        return [item for sublist in ret for item in sublist]

    def expand_funs(self):
        for k in sorted(self.functions.keys(), key=lambda tup: len(tup[0]), reverse=True):
            self.functions[k] = re.sub(r"p\d*.*q{1}", '', self.functions[k])
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
        return ''.join(ret)

    def execute(self):
        return self.execute_raw(''.join(self.convert_to_raw(self.get_tokens())))


RSUProgram("p781640\n  p532616\n    L R R1 R L R R17 F R F\n  q\n  p529569\n    R R F L8 R7 L17 R18 L17 F14 R10\n  q\n  p27885\n    R R10 R L F F F F F L\n  q\n  \n  P27885 L R14 F (\n    F L9 F2 R5 L4 F R F F F0\n  )12 L9 F P529569 L16 (\n    F R R6 F L11 R1 R4 F9 R8 R7\n  )11\nq\np513142\n  p49111\n    L16 R F14 R R L19 R L0 F F18\n  q\n  p925020\n    L9 L F2 R L R8 L R9 R F\n  q\n  p603183\n    F4 F R F1 R F16 F F L0 L\n  q\n  p976775\n    R L F F F19 F16 L L14 F4 F\n  q\n  \n  P976775 R6 F15 L R17 P925020 R R14 F F13\nq\n\nF15 L F8 (\n  R (\n    R F16 R10 L16 F L R14 F18 L L11\n  )18 F F12 F7 F0 F R7 L F\n)18 L7 L L (\n  (\n    L3 F L R19 F0 R2 F8 L19 R F7\n  )8 L14 L R F10 (\n    R12 R0 F R8 R L R3 R5 R9 L9\n  ) F15 F F R\n)8 L13 R19").execute()