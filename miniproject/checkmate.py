def find_king(grid, size):
    """ทำหน้าที่หาตำแหน่ง K และเช็คว่าต้องมีแค่ตัวเดียว"""
    king_pos = None
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                if king_pos is not None: return None # กรณีเจอ King มากกว่า 1 ตัว
                king_pos = (r, c)
    return king_pos

def check_rook_and_queen(grid, size, kr, kc):
    """เช็คแนวตรง (บน ล่าง ซ้าย ขวา) สำหรับ Rook และ Queen"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            if grid[r][c] != '.':
                if grid[r][c] in ('R', 'Q'): # ถ้าเจอเรือหรือควีน
                    return True
                break # เจอหมากอื่นบังทาง
            r, c = r + dr, c + dc
    return False

def check_bishop_and_queen(grid, size, kr, kc):
    """เช็คแนวทแยง 4 ทิศ สำหรับ Bishop และ Queen"""
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            if grid[r][c] != '.':
                if grid[r][c] in ('B', 'Q'): # ถ้าเจอบิชอปหรือควีน
                    return True
                break # เจอหมากอื่นบังทาง
            r, c = r + dr, c + dc
    return False

def check_pawn(grid, size, kr, kc):
    """เช็คเบี้ยศัตรูที่อยู่ทแยงมุมล่าง (เพราะเบี้ยเดินขึ้นข้างบนมากิน King)"""
    for dr, dc in [(1, -1), (1, 1)]:
        r, c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < size:
            if grid[r][c] == 'P':
                return True
    return False

def checkmate(board_str):
    # เตรียมบอร์ดและเช็ค Error
    rows = board_str.strip().split('\n')
    size = len(rows)
    grid = [list(r) for r in rows]
    
    if any(len(r) != size for r in grid): # เช็คว่าบอร์ดเบี้ยวไหม
        print("Error")
        return

    # หาตำแหน่ง King
    king = find_king(grid, size)
    if king is None:
        print("Error")
        return

    kr, kc = king
    # ตรวจสอบทีละด่าน
    if check_rook_and_queen(grid, size, kr, kc) or \
       check_bishop_and_queen(grid, size, kr, kc) or \
       check_pawn(grid, size, kr, kc):
        print("Success")
    else:
        print("Fail")