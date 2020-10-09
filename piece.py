#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Piece:
    def __init__(self, symbol):
        self.symbol = symbol
        self.has_moved = False


def is_piece(c, turn):
    if turn == "White":
        return c == "R" or c == "N" or c == "B" or c == "Q" or c == "K"
    else:
        return c == "r" or c == "n" or c == "b" or c == "q" or c == "k"
