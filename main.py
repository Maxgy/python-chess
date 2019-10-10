class Piece:
    def __init__(self, symbol):
        self.symbol = symbol
        self.has_moved = False


board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]
board = [list(map(Piece, row)) for row in board]


def show_board():
    for row in board:
        for piece in row:
            print(piece.symbol, end=" ")
        print()
    print()


def file_to_col(n):
    if n == "a":
        return 0
    elif n == "b":
        return 1
    elif n == "c":
        return 2
    elif n == "d":
        return 3
    elif n == "e":
        return 4
    elif n == "f":
        return 5
    elif n == "g":
        return 6
    elif n == "h":
        return 7


def rank_to_row(n):
    if n == "1":
        return 7
    elif n == "2":
        return 6
    elif n == "3":
        return 5
    elif n == "4":
        return 4
    elif n == "5":
        return 3
    elif n == "6":
        return 2
    elif n == "7":
        return 1
    elif n == "8":
        return 0


def select_move(move):
    if len(move) == 2:
        pawn_move(rank_to_row(move[1]), file_to_col(move[0]))
    elif len(move) == 4 and move[1] == "x":
        if move[0] == "R":
            pass
        elif move[0] == "N":
            pass
        elif move[0] == "B":
            pass
        elif move[0] == "Q":
            pass
        elif move[0] == "K":
            pass
        else:
            pawn_kill(file_to_col(move[0]),
                      rank_to_row(move[3]),
                      file_to_col(move[2]))


def pawn_move(row, col):
    if board[row + 1][col].symbol == "P" and board[row][col].symbol == ".":
        board[row + 1][col].symbol = "."
        board[row][col].symbol = "P"
    elif board[row + 2][col].symbol == "P" and board[row][col].symbol == ".":
        board[row + 2][col], board[row][col] = board[row][col], board[row + 2][col]


def pawn_kill(pawn_col, row, col):
    if board[row + 1][pawn_col].symbol == "P" and board[row][col].symbol != ".":
        board[row + 1][pawn_col].symbol = "."
        board[row][col].symbol = "P"


turn = "White"

while True:
    show_board()

    user_move = ""
    while user_move == "":
        user_move = input("Move : ")

    print("Your move: " + user_move)
    select_move(user_move)
