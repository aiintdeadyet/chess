# Class to store information about the current game


from sympy import true


class game:
    '''makes new game objects'''
    def __init__(self):
        '''initializes game'''
        # board is 8x8 2D list of pieces
        self.board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                      ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        self.turn = 'white'
        self.castling = {'white': {'king': True, 'queen': True},
                         'black': {'king': True, 'queen': True}}
        self.history = []

    def move(self, start_pos, end_pos):
        '''moves piece from start_pos to end_pos'''
        if not self.check_move(start_pos, end_pos):
            return
        # get piece at start_pos
        piece = self.board[start_pos[0]][start_pos[1]]
        # get piece at end_pos
        end_piece = self.board[end_pos[0]][end_pos[1]]
        # move piece
        self.board[end_pos[0]][end_pos[1]] = piece
        self.board[start_pos[0]][start_pos[1]] = ' '
        # update castling
        match piece:
            case 'k':
                self.castling['white']['king'] = False
            case 'K':
                self.castling['black']['king'] = False
            case 'q':
                self.castling['white']['queen'] = False
            case 'Q':
                self.castling['black']['queen'] = False
        # update history
        self.history.append((start_pos, end_pos, piece, end_piece))
        # update turn
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

    def undo(self):
        '''undoes last move'''
        # get last move
        start_pos, end_pos, piece, end_piece = self.history.pop()
        # move piece
        self.board[start_pos[0]][start_pos[1]] = piece
        self.board[end_pos[0]][end_pos[1]] = end_piece
        # update castling
        if piece == 'k':
            self.castling['white']['king'] = True
        elif piece == 'K':
            self.castling['black']['king'] = True
        elif piece == 'q':
            self.castling['white']['queen'] = True
        elif piece == 'Q':
            self.castling['black']['queen'] = True
        # update turn
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

    def check_move(self, start_pos, end_pos):
        '''checks if move is valid'''
        # get piece at start_pos
        piece = self.board[start_pos[0]][start_pos[1]]
        # get piece at end_pos
        end_piece = self.board[end_pos[0]][end_pos[1]]
        # turn check
        if self.turn == 'white' and piece.islower():
                return False
        elif self.turn == 'black' and piece.isupper():
                return False
        # check if move is valid
        match (piece):
            case 'p': # black pawn
                if end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] + 2 and end_pos[1] == start_pos[1]:
                    return (end_piece == ' ' and start_pos[0] == 1)
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] + 1:
                    return end_piece.isupper()
                return False
            case 'P': # white pawn
                if end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 2 and end_pos[1] == start_pos[1]:
                    return end_piece == ' ' and start_pos[0] == 6
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.islower()
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] + 1:
                    return end_piece.islower()
                return False
            case 'r': # black rook
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                return False
            case 'R': # white rook
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                return False
            case 'n': # black knight
                if end_pos[0] == start_pos[0] + 2 and end_pos[1] == start_pos[1] + 1:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] + 2 and end_pos[1] == start_pos[1] - 1:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 2 and end_pos[1] == start_pos[1] + 1:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 2 and end_pos[1] == start_pos[1] - 1:
                    return end_piece == ' '
                return False
            case 'N': # white knight
                if end_pos[0] == start_pos[0] + 2 and end_pos[1] == start_pos[1] + 1:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] + 2 and end_pos[1] == start_pos[1] - 1:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 2 and end_pos[1] == start_pos[1] + 1:
                    return end_piece == ' '                    
                elif end_pos[0] == start_pos[0] - 2 and end_pos[1] == start_pos[1] - 1:
                    return end_piece == ' '
                return False
            case 'b': # black bishop
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                return False
            case 'B': # white bishop
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                return False
            case 'q': # black queen
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] + 1:
                    return end_piece.islower()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] + 1:
                    return end_piece.islower()
                return False
            case 'Q': # white queen
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] + 1:
                    return end_piece.islower()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] + 1:
                    return end_piece.islower()
                return False
            case 'k': # black king
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1]:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1]:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] and end_pos[1] == start_pos[1] - 1:
                    return end_piece.isupper()
                elif end_pos[0] == start_pos[0] and end_pos[1] == start_pos[1] + 1:
                    return end_piece.isupper()
                return False
            case 'K': # white king
                if end_pos[0] == start_pos[0] and end_pos[1] != start_pos[1]:
                    return end_piece == ' '
                elif end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1]:
                    return end_piece.islower()
                elif end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1]:
                    return end_piece.islower()
                elif end_pos[0] == start_pos[0] and end_pos[1] == start_pos[1] - 1:
                    return end_piece.islower()
                elif end_pos[0] == start_pos[0] and end_pos[1] == start_pos[1] + 1:
                    return end_piece.islower()
                return False

            