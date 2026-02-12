from checkmate import checkmate

def main():
    # ตัวอย่างกระดานสี่เหลี่ยมจัตุรัส 
   board = """\
..P.
.K..
....
....\
    """
   checkmate(board)

if __name__ == "__main__":
    main()