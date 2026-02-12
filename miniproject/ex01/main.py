import sys
from checkmainex00 import checkmate

def main():
    if len(sys.argv) < 2:
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, "r") as f:
                board = f.read()
            checkmate(board)
        except:
            print("Error")

if __name__ == "__main__":
    main()
