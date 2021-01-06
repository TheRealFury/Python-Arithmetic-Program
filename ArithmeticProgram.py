# import stuff #
from extract3Letters import First3Letters
from add import addFunction
from multiply import mulFunction
from divide import divFunction
from subtract import subFunction
from power import powFunction
from nroot import nrtFunction
from factorise import facFunction
from prime import priFunction
from prime_inRange import cprFunction
from Help import Help

# Put the entire thing into a forever loop. #
while True:
    
    # Creating and clearing some variables #
    b = ""
    command = ""
    
    # Command-prompt-like input line #
    command = input(" -> ")
    
    # Extract first 3 letters #
    b = First3Letters(command)
        
    # If first 3 letters are "add", do this stuff... #
    if b == "add":
        addFunction(command, b)
            
    # If first 3 letters are "mul", do this stuff... #
    elif b == "mul":
        mulFunction(command, b)
            
    # If first 3 letters are "div", do this stuff... #
    elif b == "div":
        divFunction(command, b)
            
    # If first 3 letters are "sub", do this stuff... #
    elif b == "sub":
        subFunction(command, b)
            
    # If first 3 letters are "pow", do this stuff... #
    elif b == "pow":
        powFunction(command, b)
            
    # If first 3 letters are "nrt", do this stuff... #
    elif b == "nrt":
        nrtFunction(command, b)
    
    # If first 3 letters are "fac", do this stuff... #    
    elif b == "fac":
        facFunction(command, b)
    
    # If first 3 letters are "pri", do this stuff... #
    elif b == "pri":
        priFunction(command, b)
    
    # If first 3 letters are "cpr", do this stuff... #
    elif b == "cpr":
        cprFunction(command, b)
        
    elif command == "help":
        Help()
        
    elif command == 'credits':
        print("All credits go to the creator!")
        
    elif command == " ":
        print("Knock-knock. Anyone at home?")
                            
    else:
        print("Invalid Command")