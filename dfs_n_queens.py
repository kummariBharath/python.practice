def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    # The stack stores the state of the board as a list of column positions.
    # For example, [1, 3] means a queen at row 0 col 1, and row 1 col 3.
    stack = [[]]
    
    while stack:
        board = stack.pop()
        row = len(board)
        
        if row == n:
            solutions.append(board)
            continue
            
        # Iterate in reverse so the smallest column index is processed first (LIFO behavior)
        for col in range(n - 1, -1, -1):
            # Check if placing a queen at (row, col) is valid
            if all(board[i] != col and abs(board[i] - col) != row - i for i in range(row)):
                stack.append(board + [col])
                
    return solutions