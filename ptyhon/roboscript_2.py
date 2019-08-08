import numpy as np


def expand(code):
    char = ''
    num = []
    ret = []
    c = 0
    while c < len(code):
        if code[c].isdecimal() :
            while code[c].isdecimal():
                num.append(code[c])
                c += 1
                if(c == len(code)):
                    break

            for i in range(int(''.join(num), 10)-1):
                ret.append(char)
            num.clear()
        else:
            ret.append(code[c])
            char = code[c]
            c += 1
    return ''.join(ret)
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
            print(cur_dir)
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
