def nrtFunction(command, b):
    function = ""
    f = ""
    d = ""
    e = ""
    h = ""
    g = ""
    i = ""
    function = "nrt"
    command = command.strip(b)
    if function == "nrt":
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
        if float(h) == 0:
            print("You have no power. The answer will thus always be 1.")
        else:
            if float(h) == 1:
                print("The 1st root of", e, "is -", e)
            else:
                try:
                    i = float(e) ** (1 / float(h))
                except:
                    print(" >>> Invalid Command")
                if float(h) == 2:
                    print("The 2nd root of ", e, "is  - ", i)
                else:
                    if float(h) == 3:
                        print("The 3rd root of", e, "is -", i)
                    else:
                        print("The ", h, "th root of", e, "is - ", i)