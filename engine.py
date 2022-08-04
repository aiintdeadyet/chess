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

    def show_move(self, x, y):
        '''shows possible moves for piece at x, y'''
        # get piece at x, y
        piece = self.board[x][y]
        # get possible moves
        moves = self.get_moves(piece, x, y)
        # show moves
        for move in moves:
            print(move)

    def get_moves(self, piece, x, y):
        '''returns possible moves for piece at x, y'''
        # get possible moves
        moves = []
        match piece:
            case 'p':
                moves = self.get_Bpawn_moves(x, y)
            case 'r':
                moves = self.get_rook_moves(x, y)
            case 'n':
                moves = self.get_knight_moves(x, y)
            case 'b':
                moves = self.get_bishop_moves(x, y)
            case 'q':
                moves = self.get_queen_moves(x, y)
            case 'k':
                moves = self.get_king_moves(x, y)
            case 'K':
                moves = self.get_king_moves(x, y)
            case 'P':
                moves = self.get_Wpawn_moves(x, y)
            case 'R':
                moves = self.get_rook_moves(x, y)
            case 'N':
                moves = self.get_knight_moves(x, y)
            case 'B':
                moves = self.get_bishop_moves(x, y)
            case 'Q':
                moves = self.get_queen_moves(x, y)
        return moves

    
            