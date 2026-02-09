import sys

if len(sys.argv) == 1:
    print("none")
else :
    para = sys.argv[1:]
    print("parameters: ",len(para))
    for p in para :
        print(p, len(p))