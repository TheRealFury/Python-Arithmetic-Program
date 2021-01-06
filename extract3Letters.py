def First3Letters(command):
    b = ""
    c = 0
    for a in command:
        b = b + a
        c = c + 1
        if c == 3:
            break
    return b