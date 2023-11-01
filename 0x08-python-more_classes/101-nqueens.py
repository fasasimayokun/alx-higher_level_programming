#!/usr/bin/python3
"""a n queens puzzle"""

import sys


def init_board(n):
    """the board constructor of a chessboard"""
    board = []
    [board.append([]) for nm in range(n)]
    [row.append(' ') for nm in range(n) for row in board]
    return board


def board_deepcopy(board):
    """returns a deepcopy of the chessboard"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_res(board):
    """return the list of lists representation of a solved chessboard"""
    solu = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solu.append([row, col])
                break
    return (solu)


def xout(board, row, col):
    """x out spots on the chessboard all spots
    where non-attacking queens can no longer be played are x out
    Args:
        board (list): the current working chessboard.
        row (int): the row where queen was last played
        col (int): the column where a queen was last played
    """
    # x out all forwar spots
    for cl in range(col + 1, len(board)):
        board[row][cl] = 'x'
    # x out all backward spots
    for bk in range(col - 1, -1, -1):
        board[row][bk] = 'x'
    # x out all spots below
    for rw in range(row + 1, len(board)):
        board[rw][col] = 'x'
    # x out al spots top
    for tp in range(row - 1, -1, -1):
        board[tp][col] = 'x'
    # x out all spots diagonally bottom ot the right
    cl = col + 1
    for rw in range(row + 1, len(board)):
        if cl >= len(board):
            break
        board[rw][cl] = 'x'
        cl += 1
    # x out all spots diagonally top left
    cl = col - 1
    for rw in range(row - 1, -1, -1):
        if cl < 0:
            break
        board[rw][cl]
        cl -= 1
    # x out all spots diagonally top right
    cl = col + 1
    for rw in range(row - 1, -1, -1):
        if cl >= len(board):
            break
        board[rw][cl] = 'x'
        cl += 1
    # x out all spots diagonally bottom left
    cl = col - 1
    for rw in range(row + 1, len(board)):
        if cl < 0:
            break
        board[rw][cl] = 'x'
        cl -= 1


def recursive_sol(board, row, queens, res):
    """the recursively solve an N-queens puzzle
    Args:
        board (list): the current working chessboard
        row (int): the current working row
        queens (int): the current number of placed queens
        res (list): a list of lists of solutions
    Return:
        res
    """
    if queens == len(board):
        res.append(get_res(board))
        return res

    for col in range(len(board)):
        if board[row][col] == ' ':
            temp_board = board_deepcopy(board)
            temp_board[row][col] = 'Q'
            xout(temp_board, row, col)
            res = recursive_sol(temp_board, row + 1,
                                queens + 1, res)
    return res


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.ext(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    res = recursive_sol(board, 0, 0, [])
    for ans in res:
        print(ans)
