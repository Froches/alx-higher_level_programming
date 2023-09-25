#!/usr/bin/python3
"""Nqueens puzzle"""
import sys


def is_safe(board, row, col, N):
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

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

        board = [[0] * N for _ in range(N)]
        solutions = []

        def backtrack(row):
            if row == N:
                solutions.append(["".join("Q" if col == 1 else "." for col in row) for row in board])
                return

            for col in range(N):
                if is_safe(board, row, col, N):
                    board[row][col] = 1
                    backtrack(row + 1)
                    board[row][col] = 0

        backtrack(0)

        for solution in solutions:
            for row in solution:
                print(row)
            print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
    print(N)
