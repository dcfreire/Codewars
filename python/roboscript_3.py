import numpy as np
func = {}


def is_decimal(code, c):
    num =[]
    while code[c].isdecimal():
        num.append(code[c])
        c += 1
        if(c == len(code)):
            break
    return ''.join(num), c

def search_funcs(code):
    bl = []
    code_list = list(code)
    while True:
        bl.clear()
        code = ''.join(code_list)

        ind = code.find("p")

        print(ind)
        if ind == -1:
            break;
        del code_list[ind]
        num = is_decimal(code_list, ind)
        del code_list[ind:num[1]]
        while code_list[ind] != 'q':
            bl.append(code_list[ind])
            del code_list[ind]
        del code_list[ind]
        func[num[0]] = ''.join(bl)
        if not len(code_list):
            break;
    return code

def expand(code):
    char = ''
    code = search_funcs(code)
    code = list(code)
    bl = []
    ret = []
    c = 0
    bn = 0
    while c < len(code):
        if code[c].isdecimal():
            num = is_decimal(code, c)
            del code[c:num[1]]
            if int(num[0], 10) == 0:
                del code[c-1]
                c -=1
            for i in range(int(''.join(num[0]), 10)-1):
                ret.append(char)
            code[c:c] = ''.join(ret)
            ret.clear()


        else:
            if code[c] == 'P':
                del code[c]
                num = is_decimal(code, c)
                del code[c:num[1]]
                code[c:c] = func[num[0]]
            if code[c] == '(':
                bl.clear()
                bn += 1
                b = c + 1
                while bn:
                    if code[b] == '(':
                        bn += 1
                    if code[b] == ')':
                        bn -= 1
                    if not bn:
                        break;
                    bl.append(code[b])
                    b += 1
                char = ''.join(bl)
                if b+1 < len(code):
                    if code[b+1].isdecimal():
                        num = is_decimal(code, b+1)
                        del code[c:num[1]]
                        for i in range(int(''.join(num[0]), 10)):
                            code[c:c] = list(char)
                        c -= 1
            elif code[c] == ')':
                c+=1
                continue
            else:
                char = code[c]


            c += 1
    return ''.join(code)
def ex_grid(grid):
    ret = np.zeros((len(grid)+2, len(grid[0])+2))
    ret[1:grid.shape[0]+1, 1:grid.shape[1]+1] = grid
    return ret


def remove_dead(mat):
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

def format_grid(grid):
    ret = np.full(grid.shape, ' ')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j]:
                ret[i][j] = '*'
    return ret

def execute(code):
    ex_code = expand(code)
    grid = np.zeros((3, 3))
    grid[1][1] = '1'
    cur_dir = 0
    cur_pos = [1, 1]
    for c in ex_code:
        if c == 'F':
            if cur_dir == 0:
                grid[cur_pos[0]][cur_pos[1]+1] = 1
                cur_pos[1] += 1
            if cur_dir == 1:
                grid[cur_pos[0]-1][cur_pos[1]] = 1
                cur_pos[0] -= 1
            if cur_dir == 2:
                grid[cur_pos[0]][cur_pos[1]-1] = 1
                cur_pos[1] -= 1
            if cur_dir == 3:
                grid[cur_pos[0]+1][cur_pos[1]] = 1
                cur_pos[0] += 1

        if c == 'R':
            cur_dir -= 1
            if cur_dir < 0:
                cur_dir = 3
        if c == 'L':
            cur_dir += 1
            if cur_dir > 3:
                cur_dir = 0
        if cur_pos[0] == grid.shape[0]-1 or cur_pos[1] == grid.shape[1]-1 or 0 in cur_pos:
            grid = ex_grid(grid)
            cur_pos[0] += 1
            cur_pos[1] += 1
    grid = remove_dead(grid)
    grid = format_grid(grid)
    ret = []
    first = True
    for i in range(grid.shape[0]):
        if not first:
            ret.append("\r\n")
        ret.append(''.join(grid[i]))
        first = False
    return ''.join(ret)

expand("p13A1B2C3q2A7B1P13")
func
