#!/usr/bin/env python
# -*- coding: utf-8 -*-

from move import select_move, check_move, string_to_move
from piece import Piece

turn = "White"

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


while True:
    show_board()

    user_move = ""
    while not check_move(user_move, turn):
        user_move = input("Move : ").strip()
        if user_move == "quit" or user_move == "exit":
            quit()
        elif user_move == "show":
            show_board()

    print("Your move: " + user_move)
    select_move(board, string_to_move(user_move))
