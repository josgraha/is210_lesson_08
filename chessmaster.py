#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08 Chess Master."""
import time


class ChessPiece(object):
    """A round rubber thing.

    Args:
        position (string): The chess notation of the current position (eg,  'a8').

    Attributes:
       position (string): The position in chess notation.
       moves (tuple): Move history of this piece.
    """
    prefix = ''
    cols = 'abcdefgh'
    # noinspection PyBroadException
    @staticmethod
    def algebraic_to_numeric(tile):
        if tile is None:
            return None
        try:
            x = ChessPiece.cols.find(tile[0])
            y = tile[1] - 1
            return x, y
        except Exception:
            return None
        return None

    def is_legal_move(position):
        return True if algebraic_to_numeric(position) is not None else False

    def __init__(self, position=None):
        if not ChessPiece.is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.position = position
