#!/usr/bin/python3
"""Solves the N-Queens backtracking problem
"""
import sys


def nqueens(N):
    """N Queens Module
    """
    def backtrack(queens, xy_dif, xy_sum):
        """Backtracking function"""
        p = len(queens)
        if p == N:
            result.append(queens)
            return None
        for q in range(N):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                backtrack(queens+[q], xy_dif+[p-q], xy_sum+[p+q])

    result = []
    backtrack([], [], [])
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = nqueens(N)
    output = []
    for sol in solutions:
        output.append([[i, j] for i, j in enumerate(sol)])
    for sol in output:
        print(sol)
