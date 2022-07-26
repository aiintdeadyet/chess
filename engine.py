# Class to store information about the current game


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
