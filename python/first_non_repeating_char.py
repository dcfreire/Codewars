def first_non_repeating_letter(string):
    c = 0
    while c < len(string):
        if(string.upper().count(string[c].upper()) == 1):
            return string[c]
        c += 1
    return ""
