def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_n_queens_util(board, col, N, result):
    if col >= N:
        result.append([row[:] for row in board])
        return
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, N, result)
            board[i][col] = 0
def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)
    return result
N = 8
solutions = solve_n_queens(N)
for solution in solutions:
    for row in solution:
        print(" ".join(map(str, row)))
    print()
