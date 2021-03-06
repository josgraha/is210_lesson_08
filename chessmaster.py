#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08 Chess Master."""
import sys
import traceback
import time


class MoveType(object):
    """Enum type for movement type.

    """
    diagonal, linear = range(2)


class DiagonalMoves(object):
    """Enum type.

    """
    ne, nw, se, sw = range(4)


class LinearMoves(object):
    """Enum type.

    """
    up, down, left, right = range(4)


class Helper(object):
    """Chess Piece Move Helper

    """
    cols = 'abcdefgh'
    move_type = MoveType
    diagonal_moves = DiagonalMoves
    linear_moves = LinearMoves

    # noinspection PyBroadException
    @staticmethod
    def numeric_position(tile=None):
        """Returns the numeric coordinate for the tile.

        :param tile:
        :return:
        """
        # print 'numeric_position: tile: {}'.format(tile)
        if tile is None:
            return None
        try:
            y = int(tile[1]) - 1
            x = Helper.cols.find(tile[0])
            # print 'numeric_position: (x: {}, y: {})'.format(x, y)
            if y > 7 or y < 0 or x < 0:
                return None
            return x, y
        except:
            traceback.print_exc(file=sys.stdout)
            return None

    @staticmethod
    def is_position_valid(position):
        """Returns true if position is valid.

        :param position:
        :return:
        """
        return True if Helper.numeric_position(position) is not None else False

    # noinspection PyBroadException
    @staticmethod
    def algebraic_to_numeric(tile=None):
        # print 'algebraic_to_numeric: tile: {}'.format(tile)
        if tile is None:
            return None
        try:
            y = int(tile[1]) - 1
            x = Helper.cols.find(tile[0])
            # print 'x: {}, y: {}'.format(x, y)
            if y > 7 or y < 0 or x < 0:
                return None
            return x, y
        except:
            traceback.print_exc(file=sys.stdout)
            return None

    @staticmethod
    def coord_to_algebraic(coord):
        """

        :rtype : string
        """
        # print 'coord_to_algebraic: coord: {}'.format(coord)
        if coord is None:
            return None
        x, y = coord
        return Helper.numeric_to_algebraic(x, y)

    @staticmethod
    def numeric_to_algebraic(x, y):
        """

        :param x:
        :param y:
        :return: string
        """
        # print 'numeric_to_algebraic: x: {}, y: {}'.format(x, y)
        if x is None or y is None:
            return None
        try:
            if y > 7 or y < 0 or x < 0 or x > 7:
                return None
            row = int(y) + 1
            col = Helper.cols[x]
            position = '{}{}'.format(col, row)
            # print 'position: {}'.format(position)
            return position
        except:
            traceback.print_exc(file=sys.stdout)
            return None

    @staticmethod
    def get_moves(position, move_type, move_dir, distance=None):
        """

        :param position:
        :param move_type:
        :param move_dir:
        :param distance:
        :return:
        """
        if not Helper.is_position_valid(position):
            return None
        x, y = Helper.algebraic_to_numeric(position)
        moves = []
        distance = 7 if distance is None else distance
        while distance > 0:
            x, y = Helper.get_coord_for_move(x, y, move_type, move_dir)
            # print 'get_moves: x: {}, y: {}'.format(x, y)
            next_pos = Helper.numeric_to_algebraic(x, y)
            if next_pos is not None and Helper.is_position_valid(next_pos):
                distance -= 1
                moves.append(next_pos)
            else:
                distance = 0
        if len(moves) >= 1:
            moves.sort()
            return moves
        return None

    @staticmethod
    def get_coord_for_move(x, y, move_type, move_dir):
        """

        :param x:
        :param y:
        :param move_type:
        :param move_dir:
        :return:
        """
        # print 'get_coord_for_move: x: {}, y: {}'.format(x, y)
        if x is None or y is None or move_type is None or move_dir is None:
            return None
        coord = None
        if move_type == Helper.move_type.diagonal:
            if move_dir == Helper.diagonal_moves.sw:
                coord = x - 1, y - 1
            elif move_dir == Helper.diagonal_moves.se:
                coord = x + 1, y - 1
            elif move_dir == Helper.diagonal_moves.ne:
                coord = x + 1, y + 1
            elif move_dir == Helper.diagonal_moves.nw:
                coord = x - 1, y + 1
        elif move_type == Helper.move_type.linear:
            if move_dir == Helper.linear_moves.down:
                coord = x, y - 1
            elif move_dir == Helper.linear_moves.up:
                coord = x, y + 1
            elif move_dir == Helper.linear_moves.left:
                coord = x - 1, y
            elif move_dir == Helper.linear_moves.right:
                coord = x + 1, y
        return coord

    @staticmethod
    def get_vertical_moves(pos, distance=None):
        """

        :param pos:
        :param distance:
        :return:
        """
        return Helper.get_linear_axis_moves(pos, distance, True)

    @staticmethod
    def get_horizontal_moves(pos, distance=None):
        """

        :param pos:
        :param distance:
        :return:
        """
        return Helper.get_linear_axis_moves(pos, distance, False)

    @staticmethod
    def get_linear_axis_moves(pos, distance=None, is_vertical=False):
        """

        :param pos:
        :param distance:
        :param is_vertical:
        :return:
        """
        if pos is None or not Helper.is_position_valid(pos):
            return None
        move_dirs = None
        if not is_vertical:
            move_dirs = [LinearMoves.left, LinearMoves.right]
        else:
            move_dirs = [LinearMoves.up, LinearMoves.down]
        return Helper.get_moves_for_dirs(pos, MoveType.linear, move_dirs, distance)

    @staticmethod
    def get_all_moves(pos, distance=None):
        """

        :param pos:
        :param distance:
        :return:
        """
        if pos is None or not Helper.is_position_valid(pos):
            return None
        moves = []
        linear = Helper.get_linear_moves(pos, distance)
        if linear is not None and len(linear) > 0:
            moves.extend(linear)
        diagonal = Helper.get_diagonal_moves(pos, distance)
        if diagonal is not None and len(diagonal) > 0:
            moves.extend(diagonal)
        if len(moves) > 0:
            return moves
        return None

    @staticmethod
    def get_linear_moves(pos, distance=None):
        """

        :param pos:
        :param distance:
        :return:
        """
        if pos is None or not Helper.is_position_valid(pos):
            return None
        move_dirs = [LinearMoves.up, LinearMoves.down, LinearMoves.left, LinearMoves.right]
        return Helper.get_moves_for_dirs(pos, MoveType.linear, move_dirs, distance)

    @staticmethod
    def get_diagonal_moves(pos, distance=None):
        """

        :param pos:
        :param distance:
        :return:
        """
        if pos is None or not Helper.is_position_valid(pos):
            return None
        move_dirs = [DiagonalMoves.ne, DiagonalMoves.nw, DiagonalMoves.se, DiagonalMoves.sw]
        return Helper.get_moves_for_dirs(pos, MoveType.diagonal, move_dirs, distance)

    @staticmethod
    def get_moves_for_dirs(pos, move_type, move_dirs, distance=None):
        """

        :param pos:
        :param move_type:
        :param move_dirs:
        :param distance:
        :return:
        """
        if move_type is None or move_dirs is None or len(move_dirs) <= 0:
            return None
        moves = []
        for move_dir in move_dirs:
            result = Helper.get_moves(pos, move_type, move_dir, distance)
            if result is not None and len(result) > 0:
                moves.extend(result)
        if moves is None or len(moves) <= 0:
            return None
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
        """

        :param position:
        :return:
        """
        if not Helper.is_position_valid(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.position = position
        self.moves = []
        self.prefix = ChessPiece.prefix

    def algebraic_to_numeric(self, tile=None):
        """

        :param tile:
        :return:
        """
        return Helper.algebraic_to_numeric(tile)

    def is_legal_move(self, position):
        """

        :param position:
        :return:
        """
        return Helper.is_position_valid(position)

    def move(self, position):
        """

        :param position:
        :return:
        """
        if not self.is_legal_move(position):
            return False
        move = ('{}{}'.format(self.prefix, self.position), '{}{}'.format(self.prefix, position), time.time())
        self.moves.append(move)
        self.position = position
        return move


class Rook(ChessPiece):
    """A Rook piece on a chessboard.

    Args:
        position (string): The chess notation of the current position (eg,  'a8').

    Attributes:
       position (string): The position in chess notation.
       moves (tuple): Move history of this piece.
    """
    prefix = 'R'

    def __init__(self, position):
        """

        :param position:
        :return:
        """
        ChessPiece.__init__(self, position)
        self.prefix = Rook.prefix

    def is_legal_move(self, position):
        """

        :param position:
        :return:
        """
        if not Helper.is_position_valid(position):
            return False
        legal_moves = Helper.get_linear_moves(self.position)
        if legal_moves is not None and position in legal_moves:
            return True
        return False


class Bishop(ChessPiece):
    """A Bishop piece on a chessboard.

    Args:
        position (string): The chess notation of the current position (eg,  'a8').

    Attributes:
       position (string): The position in chess notation.
       moves (tuple): Move history of this piece.
    """
    prefix = 'B'

    def __init__(self, position):
        """

        :param position:
        :return:
        """
        ChessPiece.__init__(self, position)
        self.prefix = Bishop.prefix

    def is_legal_move(self, position):
        """

        :param position:
        :return:
        """
        if not Helper.is_position_valid(position):
            return False
        legal_moves = Helper.get_diagonal_moves(self.position)
        if legal_moves is not None and position in legal_moves:
            return True
        return False


class King(ChessPiece):
    """A King piece on a chessboard.

    Args:
        position (string): The chess notation of the current position (eg,  'a8').

    Attributes:
       position (string): The position in chess notation.
       moves (tuple): Move history of this piece.
    """
    prefix = 'K'

    def __init__(self, position):
        """

        :param position:
        :return:
        """
        ChessPiece.__init__(self, position)
        self.prefix = King.prefix

    def is_legal_move(self, position):
        """

        :param position:
        :return:
        """
        if not Helper.is_position_valid(position):
            return False
        legal_moves = Helper.get_all_moves(self.position, 1)
        if legal_moves is not None and position in legal_moves:
            return True
        return False


class ChessMatch(object):
    """A Chess Match.

    Args:
        pieces (dict): The chess pieces keyed by full notation.

    Attributes:
       pieces (dict): The dict of pieces keyed by full notation.
       log (tuple): Move history of this match.
    """

    def __init__(self, pieces=None):
        """

        :param pieces:
        :return:
        """
        self.pieces = None
        self.log = []
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces

    def reset(self):
        """

        :return:
        """
        self.pieces = {
            'Ra1': Rook('a1'),
            'Rh1': Rook('h1'),
            'Ra8': Rook('a8'),
            'Rh8': Rook('h8'),
            'Bc1': Bishop('c1'),
            'Bf1': Bishop('f1'),
            'Bc8': Bishop('c8'),
            'Bf8': Bishop('f8'),
            'Ke1': King('e1'),
            'Ke8': King('e8')
        }
        self.log = []

    def move(self, piece_key, position):
        """

        :param piece_key:
        :param position:
        :return:
        """
        piece = self.pieces.pop(piece_key)
        if piece is None:
            return
        log_item = piece.move(position)
        if not log_item:
            return
        self.log.append(log_item)
        piece_key = '{}{}'.format(piece.prefix, piece.position)
        self.pieces[piece_key] = piece

    def __len__(self):
        """

        :return:
        """
        return len(self.log)