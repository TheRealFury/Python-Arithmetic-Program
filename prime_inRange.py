def checkprime(x):
    result=True
    for y in range (2, x):
        if (x %y)==0:
            result=False
            print(str(x) + " is divisible by " + str(y))
            break
    return result

def cprFunction(command, b):
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
    function = "cpr"
    command = command.strip(b)
    if function == "cpr":
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
            z = 0
            for h in range (2, int(h) + 1):
                if ((checkprime(h)==False)):
                    pass
                else:
                    print(str(h) + " is a prime number.")
                    z=z+1
            print("The number of Prime Numbers found are : " + str(z))
        except:
            print("Invalid Command")