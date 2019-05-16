import numpy as np

def set_states(mat):
    newState = np.zeros(mat.shape)
    def look_around(ix, iy):
        count = np.sum(mat[ix-1:ix+1, iy-1:iy+1]) - mat[ix][iy]
        return count
    def switch(arg, what):
        switcher = {
            0:0,
            1:0,
            2:1,
            3:1,
            4:0,
        }
        if arg == 3 and not what:
            return 1
        return switcher.get(arg, 0) * what
    for ix, iy in np.ndindex(mat[1:len(mat)-1, 1:len(mat[0])-1].shape):
        newState[ix][iy] = switch(look_around(ix, iy), mat[ix][iy])
    return newState

def remove_dead(mat):
    for i in mat:
        if not all(i):
            np.delete(mat, 0, 0)
        else:
            break
    for i in range(len(mat)-1, 0):
        if not all(mat[i]):
            np.delete(mat, i, 0)
        else:
            break
    mat = np.transpose(mat)
    for i in mat:
        if not all(i):
            np.delete(mat, 0, 0)
        else:
            break
    for i in range(len(mat)-1, 0):
        if not all(mat[i]):
            np.delete(mat, i, 0)
        else:
            break
    mat = np.transpose(mat)
    return mat

def get_generation(cells, generations):
    cells = np.asarray(cells)
    if not generations:
        return cells
    newStep = np.zeros((len(cells) + 2, len(cells[0]) + 2))
    ns = newStep.shape[0]
    nc = cells.shape[0]
    lower = (ns) // 2 - (nc // 2)
    upper = (ns // 2) + (nc // 2)
    newStep[lower:upper, lower:upper] = cells
    newStep = set_states(newStep)
    remove_dead(cells)
    get_generation(cells, generations-1)
    return cells
