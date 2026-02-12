def checkmate(board_str):
    # 1. เตรียมกระดานและเช็คความถูกต้อง (Validation)
    rows = board_str.strip().split('\n')
    size = len(rows)
    grid = [list(r) for r in rows]

    # เช็คว่าเป็นสี่เหลี่ยมจัตุรัสไหม
    for r in grid:
        if len(r) != size:
            print("Error")
            return

    # 2. หาตำแหน่ง King และเช็คว่ามีตัวเดียวไหม
    king_pos = []
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                king_pos.append((r, c))
    
    if len(king_pos) != 1:
        print("Error")
        return
    
    kr, kc = king_pos[0]

    # 3. ตรวจสอบการรุก (The Logic)
    # [ทิศทางแนวตั้ง-นอน, ทิศทางแนวทแยง]
    directions = [
        ( (-1,0), (1,0), (0,-1), (0,1) ),    # แนวตรง (Rook, Queen)
        ( (-1,-1), (-1,1), (1,-1), (1,1) )   # แนวทแยง (Bishop, Queen)
    ]

    # ตรวจสอบแนวตรงและแนวทแยง (Sliding Pieces)
    for i, group in enumerate(directions):
        for dr, dc in group:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                piece = grid[r][c]
                if piece != '.':
                    # ถ้าเจอหมากตัวแรก...
                    if i == 0 and piece in ('R', 'Q'): # แนวตรงเจอ R หรือ Q
                        print("Success")
                        return
                    if i == 1 and piece in ('B', 'Q'): # แนวทแยงเจอ B หรือ Q
                        print("Success")
                        return
                    break # เจอหมากตัวอื่นขวางทาง ให้หยุดดูทิศนี้
                r, c = r + dr, c + dc

    # ตรวจสอบเบี้ย (Pawn)
    # เช็คแค่ 2 จุดทแยงมุม "ด้านล่าง" ของ King (เพราะ Pawn เดินขึ้นข้างบนเพื่อกิน King)
    for dr, dc in [(1, -1), (1, 1)]:
        r, c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < size and grid[r][c] == 'P':
            print("Success")
            return

    print("Fail")