#!/usr/bin/env python3
import sys
"""N-Queens"""


def IsSafe(board, row, col, N):
    '''Check the Queen if it could be in the board'''
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True


def SolveNqueensUtil(board, row, N, solutions):
    '''Use backtracking to solve the problem'''
    if row == N:
        solutions.append([[i, col] for i, col in enumerate(board[row - 1])])
        return

    for col in range(N):
        if IsSafe(board, row, col, N):
            board[row][col] = 1
            SolveNqueensUtil(board, row + 1, N, solutions)
            board[row][col] = 0


def SolveNqueens(N):
    '''Get the solution of N-Queen'''
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    SolveNqueens(board, 0, N, solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    SolveNqueens(sys.argv[1])
