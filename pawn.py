#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pawn_move(board, row, col):
    if board[row + 1][col].symbol == "P" and board[row][col].symbol == ".":
        board[row + 1][col].symbol = "."
        board[row][col].symbol = "P"
    elif board[row + 2][col].symbol == "P" and board[row][col].symbol == ".":
        board[row + 2][col], board[row][col] = board[row][col], board[row +
                                                                      2][col]


def pawn_kill(board, pawn_col, row, col):
    if board[row +
             1][pawn_col].symbol == "P" and board[row][col].symbol != ".":
        board[row + 1][pawn_col].symbol = "."
        board[row][col].symbol = "P"
