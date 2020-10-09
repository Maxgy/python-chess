#!/usr/bin/env python
# -*- coding: utf-8 -*-

from piece import Piece, is_piece
from pawn import pawn_move, pawn_kill


class Move:
    def __init__(self, col, row, piece=None, x=False):
        self.piece = piece
        self.x = x
        self.col = col
        self.row = row


def select_move(board, move):
    if move.piece == None:
        pawn_move(board, move.row, move.col)
    elif not move.x:
        if move.piece == "R":
            print("move R")
        elif move.piece == "N":
            print("move N")
        elif move.piece == "B":
            print("move B")
        elif move.piece == "Q":
            print("move Q")
        elif move.piece == "K":
            print("move K")
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
            pawn_kill(board, file_to_col(move[0]), rank_to_row(move[3]),
                      file_to_col(move[2]))


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


def check_move(move, turn):
    if len(move) == 2:
        return file_to_col(move[0]) != None and rank_to_row(move[1]) != None
    elif len(move) == 3:
        return is_piece(move[0], turn) and file_to_col(
            move[1]) != None and rank_to_row(move[2]) != None
    elif len(move) == 4:
        return is_piece(move[0], turn) and move[1] == "x" and file_to_col(
            move[2]) != None and rank_to_row(move[3]) != None
    else:
        return False


def string_to_move(move):
    if len(move) == 2:
        return Move(file_to_col(move[0]), rank_to_row(move[1]))
    elif len(move) == 3:
        return Move(file_to_col(move[0]), rank_to_row(move[1]), Piece(move[0]))
    elif len(move) == 4:
        return Move(file_to_col(move[0]), rank_to_row(move[1]), Piece(move[0]),
                    True)
