import numpy as np

letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
Colors = {"Red": 2, "Yellow": 1}


def who_is_winner(pieces_position_list):
    # Blank = 0, Yellow = 1, Red = 2
    a = np.zeros((7, 6))
    for s in pieces_position_list:
        a[letters.get(s[0])][np.where(a[letters.get(s[0])] == 0)
                             [0][0]] = Colors.get(s[2:])
        for i in range(4):
            for j in range(3):
                aux = a[i:i + 4, j:j + 4]
                if True in (aux == (1, 1, 1, 1)).all(axis=0) or True in (aux == (1, 1, 1, 1)).all(axis=1) or (np.diag(aux) == (1, 1, 1, 1)).all() or (np.diag(np.fliplr(aux)) == (1, 1, 1, 1)).all():
                    return "Yellow"
                if True in (aux == (2, 2, 2, 2)).all(axis=0) or True in (aux == (2, 2, 2, 2)).all(axis=1) or (np.diag(aux) == (2, 2, 2, 2)).all() or (np.diag(np.fliplr(aux)) == (2, 2, 2, 2)).all():
                    return "Red"
    return "Draw"


print(who_is_winner([
    "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
    "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
    "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
    "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
    "E_Yellow", "E_Red"
]))
