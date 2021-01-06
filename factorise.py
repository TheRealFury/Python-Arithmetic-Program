def facFunction(command, b):
    function = ""
    f = ""
    h = ""
    g = ""
    i = ""
    c = ""
    b = ""
    d = 0
    a = command
    for c in a:
        b = b + c
        d = d + 1
        if d == 3:
            break
    function = "fac"
    command = command.strip(b)
    if function == "fac":
        for f in command:
            command = command.strip(f)
            break
        try:
            for g in command:
                if g == ")":
                    command = command.strip(g)
                    break
                else:
                    h = h + str(g)
            command = command.strip(i)
            numlist = []
            for i in range(1, int(h) + 1):
                if h % i == 0:
                    numlist.append(i)
            print("The factors of", h, "are -", numlist)
        except:
            print("Invalid Command")