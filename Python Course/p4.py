def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    # Check left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    # Check right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i] == j:
            return False
    return True

def solve_nqueens_backtracking(n):
    solutions = []
    board = [-1] * n  # board[i] = column of queen in row i

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

# Example usage:
n = 4
solutions = solve_nqueens_backtracking(n)
print(f"Backtracking: Total solutions for {n}-Queens:", len(solutions))
for sol in solutions:
    print(sol)


def solve_nqueens_branch_bound(n):
    solutions = []

    def backtrack(row, cols, diag1, diag2, board):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if col not in cols and (row + col) not in diag1 and (row - col) not in diag2:
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                board.append(col)
                backtrack(row + 1, cols, diag1, diag2, board)
                board.pop()
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

    backtrack(0, set(), set(), set(), [])
    return solutions

# Example usage:
solutions_bb = solve_nqueens_branch_bound(n)
print(f"Branch & Bound: Total solutions for {n}-Queens:", len(solutions_bb))
for sol in solutions_bb:
    print(sol)
