def powFunction(command, b):
    function = ""
    f = ""
    d = ""
    e = ""
    h = ""
    g = ""
    i = ""
    function = "pow"
    command = command.strip(b)
    if function == "pow":
        for f in command:
            command = command.strip(f)
            break
        for d in command:
            if d == ",":
                command = command.strip(d)
                break
            else:
                e = e + d
                command = command.strip(e)
        for g in command:
            if g == ")":
                command = command.strip(g)
                break
            else:
                h = h + g
        command = command.strip(i)
        try:
            i = int(e) ** int(h)
            print(" >>> The result after powering ", e, "by", h, "is - ", float(i))
        except:
            print(" >>> Invalid Command")