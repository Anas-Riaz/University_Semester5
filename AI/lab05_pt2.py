def is_under_attack(board, row, col, n):
    # Check if there is any queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return True

    # Check if there is any queen in the same upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return True

    # Check if there is any queen in the same lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return True

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    return solve_n_queens_helper(board, 0, n)

def solve_n_queens_helper(board, col, n):
    # Base case: all queens are placed successfully
    if col >= n:
        return board

    # Try placing the queen in each row of the current column
    for row in range(n):
        if not is_under_attack(board, row, col, n):
            board[row][col] = 1

            # Recursively try placing the queen in the next column
            if solve_n_queens_helper(board, col + 1, n):
                return board

            # Backtrack if the queen cannot be placed in this row
            board[row][col] = 0

    # Return None if the queen cannot be placed in any row of this column
    return None

