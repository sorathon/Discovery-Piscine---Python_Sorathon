import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    count_z = text.count("z")
    
    if count_z > 0:
        print("z" * count_z)
    else:
        print("none")
