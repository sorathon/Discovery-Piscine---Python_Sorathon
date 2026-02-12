from checkmate import checkmate

def main():
    # ตัวอย่างกระดานสี่เหลี่ยมจัตุรัส 
   board = """\
....
.K..
..P..
....\
    """
   checkmate(board)

if __name__ == "__main__":
    main()