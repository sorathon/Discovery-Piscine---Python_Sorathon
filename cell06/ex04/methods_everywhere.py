import sys

def shrink(word):
    return word[:8]

def enlarge(word):
    return word + "Z" * (8 - len(word))

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)
