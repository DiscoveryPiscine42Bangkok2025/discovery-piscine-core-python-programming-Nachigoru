def checkmate(board):
    #handle non-string input
    if not isinstance(board, str):
        return

    #Split into rows, strip whitespace, remove empty lines
    rows = [row.strip() for row in board.strip().split("\n") if row.strip()]

    if not rows:
        return

    size = len(rows)

    #must be square board
    for row in rows:
        if len(row) != size:
            return

    #find king on board
    king_pos = None
    king_count = 0

    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                king_pos = (r, c)
                king_count += 1

    #there can only be one king
    if king_count != 1:
        return

    #Direction scanner
    def scan(dr, dc, threats):     
        r, c = king_pos             
        r += dr                     
        c += dc                    
        while 0 <= r < size and 0 <= c < size:  
            piece = rows[r][c]     
            if piece != ".":        
                return piece in threats 
            r += dr                 
            c += dc                 
        return False                

    #Pawn checker
    def pawn_check():              
        kr, kc = king_pos           
        for dc in [-1, 1]:          
            r, c = kr + 1, kc + dc 
            if 0 <= r < size and 0 <= c < size:  
                if rows[r][c] == "P":            
                    return True                  
        return False                

    #Check detection
    straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]   
    diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

    in_check = any(scan(dr, dc, {"R", "Q"}) for dr, dc in straight)          
    in_check = in_check or any(scan(dr, dc, {"B", "Q"}) for dr, dc in diagonal)  
    in_check = in_check or pawn_check()   

    print("Success" if in_check else "Fail")  
