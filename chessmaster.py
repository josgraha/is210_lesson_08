#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08 Chess Master."""
import sys
import traceback
import time
from enum import Enum

class PieceMoveHelper(object):
    """Chess Piece Move Helper

    """
    cols = 'abcdefgh'
    MOVE_TYPE = Enum('DIAGONAL', 'LINEAR')
    DIAGONAL_MOVES = Enum('NE', 'NW', 'SE', 'SW')
    LINEAR_MOVES = Enum('ASC', 'DESC')
    @staticmethod
    def numeric_position(tile=None):
        print 'numeric_position: tile: {}'.format(tile)
        if tile is None:
            return None
        try:
            y = int(tile[1]) - 1
            x = ChessPiece.cols.find(tile[0])
            print 'numeric_position: (x: {}, y: {})'.format(x, y)
            if y > 7 or y < 0 or x < 0:
                return None
            return x, y
        except:
            traceback.print_exc(file=sys.stdout)
            return None
        return None

    @staticmethod
    def is_position_valid(position):
        return True if PieceMoveHelper.numeric_position(position) is not None else False

    @staticmethod
    def algebraic_to_numeric(tile=None):
        print 'PieceMoveHelper.algebraic_to_numeric: tile: {}'.format(tile)
        if tile is None:
            return None
        try:
            y = int(tile[1]) - 1
            x = PieceMoveHelper.cols.find(tile[0])
            print 'x: {}, y: {}'.format(x, y)
            if y > 7 or y < 0 or x < 0:
                return None
            return x, y
        except:
            traceback.print_exc(file=sys.stdout)
            return None
        return None

    @staticmethod
    def numeric_to_algebraic(coord):
        print 'PieceMoveHelper.numeric_to_algebraic: tile: {}'.format(tile)
        if coord is None:
            return None
        try:
            x, y = coord
            if y > 7 or y < 0 or x < 0:
                return None
            row = int(y) + 1
            col = PieceMoveHelper.cols.index(x)
            position = '{}{}'.format(col, row)
            print 'position: {}'.format(position)
            return position
        except:
            traceback.print_exc(file=sys.stdout)
            return None
        return None

    @staticmethod
    def vertical_moves(position, distance=None):
        return None

    @staticmethod
    def horizontal_moves(position, distance=None):
        return None

    @staticmethod
    def get_next_moves(position, moveType):
        return None

    @staticmethod
    def get_linear_moves(x, y, distance, is_vertical=False):
        start = x if not is_vertical else y
        lower = 0 if distance is None or (start - distance) < 0 else (start - distance)
        upper = 7 if distance is None or (start + distance) > 7 else (start + distance)
        lower_moves = (start - lower)
        upper_moves = (upper - start)
        moves = []
        if left_moves > 0:
            for i in range(1, down_moves):
                print 'left: down: i: {}, moves: {}'.format(i, left_moves)
                move = PieceMoveHelper.numeric_to_algebraic(x, (left + i))
                moves.append(move)
        if right_moves > 0:
            for i in range(1, up_moves):
                print 'right: up: i: {}, moves: {}'.format(i, right_moves)
                move = PieceMoveHelper.numeric_to_algebraic(x, (right + i))
                moves.append(move)
        print 'moves: {}'.format(moves)
        return moves


class ChessPiece(object):
    """A piece on a chessboard.

    Args:
        position (string): The chess notation of the current position (eg,  'a8').

    Attributes:
       position (string): The position in chess notation.
       moves (tuple): Move history of this piece.
    """
    prefix = ''

    def __init__(self, position):
        if not self.is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.position = position
        self.moves = []
        self.prefix = ChessPiece.prefix

    def algebraic_to_numeric(self, tile=None):
        return PieceMoveHelper.algebraic_to_numeric(tile)

    def is_legal_move(self, position):
        return True if PieceMoveHelper.is_position_valid(position) is not None else False

    def move(self, position):
        if not self.is_legal_move(position):
            return False
        move = ('{}{}'.format(self.prefix, self.position), '{}{}'.format(self.prefix, position), time.time())
        self.moves.append(move)
        self.position = position
        return move
