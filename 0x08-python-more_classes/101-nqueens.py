#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
In this module, we will solve this puzzle using Backtracing
"""
import sys


class Nqueens:
    """class with necessary methods to solve the N-queens problem"""

    def __init__(self, n):
        """Initializing Nqueens class with an empty board"""

        self.n = n
        self.board = [["."] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, r, c):
        """Tell if a board cell is safe or not"""
        n = len(self.board)
        r -= 1
        c_right = c + 1
        c_left = c - 1

        while r >= 0:
            if self.board[r][c] == "Q":
                return False
            if c_right < n and self.board[r][c_right] == "Q":
                return False
            if c_left >= 0 and self.board[r][c_left] == "Q":
                return False

            r -= 1
            c_left -= 1
            c_right += 1

        return True

    def addSolution(self, board):
        config = []
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == "Q":
                    config.append([i, j])
                    break

        self.solutions.append(config)

    def solveNQueens(self, board, r):
        """Procedure to solve N-queens problem using Backtracing"""
        n = self.n

        if r == self.n:
            self.addSolution(board)
        else:
            for c in range(n):
                if self.is_safe(r, c):
                    board[r][c] = "Q"
                    self.solveNQueens(board, r + 1)
                    board[r][c] = "."


if __name__ == '__main__':

    list_args = sys.argv

    if len(list_args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(list_args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = Nqueens(n)
    nqueens.solveNQueens(nqueens.board, 0)
    for config in nqueens.solutions:
        print(config)
