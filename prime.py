def priFunction(command, b):
    
    function = ""
    f = ""
    h = 0
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
    function = "pri"
    command = command.strip(b)
    if function == "pri":
        for f in command:
            command = command.strip(f)
            break
        try:
            for g in command:
                if g == ")":
                    command = command.strip(g)
                    break
                else:
                    h = h + int(g)
            command = command.strip(i)
            result = True
            for y in range (2, h):
                if (h % y)==0:
                    print(str(h) + " is not a prime as it is divisible by " + str(y))
                    result = False
                    break
            if result == True:
                print(str(h), "is a prime number.")
        except:
            print("Invalid Command")