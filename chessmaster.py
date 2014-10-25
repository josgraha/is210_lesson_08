#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08 Chess Master."""
import sys
import traceback
import time


class ChessPiece(object):
    """A round rubber thing.

    Args:
        position (string): The chess notation of the current position (eg,  'a8').

    Attributes:
       position (string): The position in chess notation.
       moves (tuple): Move history of this piece.
    """
    cols = 'abcdefgh'
    prefix = ''

    def __init__(self, position):
        if not self.is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.position = position
        self.moves = []
        self.prefix = ChessPiece.prefix

    def algebraic_to_numeric(self, tile=None):
        #print 'tile: {}'.format(tile)
        if tile is None:
            return None
        try:
            y = int(tile[1]) - 1
            x = ChessPiece.cols.find(tile[0])
            #print 'x: {}, y: {}'.format(x, y)
            if y > 7 or y < 0 or x < 0:
                return None
            return x, y
        except:
            traceback.print_exc(file=sys.stdout)
            return None
        return None

    def is_legal_move(self, position):
        return True if self.algebraic_to_numeric(position) is not None else False

    def move(self, position):
        if not self.is_legal_move(position):
            return False
        move = ('{}{}'.format(self.prefix,self.position), '{}{}'.format(self.prefix, position), time.time())
        self.moves.append(move)
        self.position = position
        return move
