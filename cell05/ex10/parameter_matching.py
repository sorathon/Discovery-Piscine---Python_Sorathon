import sys

if len(sys.argv) != 2 :
    print("none")
else :
    para = sys.argv[1]
    user_input = input("What was the parameter? ")
    
    if user_input == para :
        print("Good job!")
    else :
        print("Nope, sorry...")