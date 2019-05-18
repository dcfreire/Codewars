import numpy as np

def set_states(mat):
    newState = np.zeros(mat.shape)
    def look_around(ix, iy, mat):
        a = np.sum(mat[ix-1:ix+2, iy-1:iy+2])
        b = mat[ix][iy]
        count = a - b
        return count
    def switch(arg, what):
        if arg == 3 and not what:
            return 1
        switcher = {
            0:0,
            1:0,
            2:1,
            3:1,
            4:0,
        }
        return switcher.get(arg, 0) * what
    for ix in range(0, mat.shape[0]):
        for iy in range(0, mat.shape[1]):
            newState[ix][iy] = switch(look_around(ix, iy, mat), mat[ix][iy])
    return newState

def remove_dead(mat):
    arr = np.sum(mat,axis=1).tolist()
    begin = 0
    while arr[begin] == 0 or arr[len(arr) - 1] == 0:
        if arr[begin] == 0:
            del arr[begin]
            mat = np.delete(mat, begin, 0)
        if arr[len(arr) - 1] == 0:
            del arr[len(arr) - 1]
            mat = np.delete(mat, mat.shape[0] - 1, 0)

    arr = np.sum(mat,axis=0).tolist()
    while  arr[begin] == 0 or arr[len(arr) - 1] == 0:
        if not arr[begin]:
            del arr[begin]
            mat = np.delete(mat, begin, 1)
        if not arr[len(arr) - 1]:
            mat = np.delete(mat, mat.shape[1] - 1, 1)
            del arr[len(arr) - 1]
    return mat

def get_generation(cells, generations):
    cells = np.asarray(cells)
    print(cells)
    if not generations:
        return cells.tolist()
    newStep = np.zeros((len(cells) + 4, len(cells[0]) + 4))
    newStep[2:cells.shape[0]+2, 2:cells.shape[1]+2] = cells
    newStep = set_states(newStep)
    newStep = remove_dead(newStep)
    return get_generation(newStep, generations-1)
