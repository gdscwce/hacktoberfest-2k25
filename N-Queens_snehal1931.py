from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()         # Columns used
        pos_diag = set()     # Positive diagonals (r + c) used
        neg_diag = set()     # Negative diagonals (r - c) used
        
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                # Found a valid solution
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    # Current position is not safe
                    continue

                # Place Queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Remove Queen (Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
