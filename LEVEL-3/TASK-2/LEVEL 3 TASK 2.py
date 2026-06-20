def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):

    # Check left side of current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):

    if col >= n:
        return True

    for row in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 'Q'

            if solve_n_queens(board, col + 1, n):
                return True

            board[row][col] = '.'

    return False


n = int(input("Enter value of N: "))

board = [['.' for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):
    print("\nSolution Found:\n")
    print_board(board)
else:
    print("No solution exists.")