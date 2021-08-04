def is_opposite(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return False
    for i in range(len(s1)):
        if ord(s1[i]) < 91:
            if ord(s2[i]) != ord(s1[i]) + 32:
                return False
        else:
            if ord(s2[i]) != ord(s1[i]) - 32:
                return False
    return True
